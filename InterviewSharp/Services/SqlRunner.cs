using System.Globalization;
using System.Text.RegularExpressions;
using Microsoft.Data.SqlClient;

namespace InterviewSharp.Services;

public partial class SqlRunner
{
    private const int MaxRows = 500;
    private readonly string _connectionString;
    private readonly string _contentRoot;

    public SqlRunner(IConfiguration config, IWebHostEnvironment env)
    {
        _connectionString = new SqlConnectionStringBuilder(config.GetConnectionString("PracticeDb")
            ?? throw new InvalidOperationException("Missing ConnectionStrings:PracticeDb"))
        {
            // Azure serverless SQL can be paused; allow time for it to resume
            ConnectTimeout = 60,
            ConnectRetryCount = 3,
            ConnectRetryInterval = 10
        }.ConnectionString;
        _contentRoot = env.ContentRootPath;
    }

    public async Task<QueryResult> RunAsync(string sql, bool skipValidation = false)
    {
        var result = new QueryResult();
        if (!skipValidation)
        {
            var (problem, normalized) = SqlGuard.Check(sql);
            if (problem is not null) { result.Error = problem; return result; }
            sql = normalized!;
        }

        var sw = System.Diagnostics.Stopwatch.StartNew();
        try
        {
            await using var conn = new SqlConnection(_connectionString);
            await conn.OpenAsync();
            await using var cmd = new SqlCommand(sql, conn) { CommandTimeout = 10 };
            await using var reader = await cmd.ExecuteReaderAsync();
            for (var i = 0; i < reader.FieldCount; i++)
                result.Columns.Add(string.IsNullOrEmpty(reader.GetName(i)) ? $"(column {i + 1})" : reader.GetName(i));
            while (await reader.ReadAsync())
            {
                if (result.Rows.Count >= MaxRows) { result.Truncated = true; break; }
                var row = new object?[reader.FieldCount];
                reader.GetValues(row);
                for (var i = 0; i < row.Length; i++) if (row[i] is DBNull) row[i] = null;
                result.Rows.Add(row);
            }
        }
        catch (SqlException ex) when (ex.Number is 102 or 105 or 156 or 207 or 208 or 245 or 8114 or 8115 or 8134 or 4104 or 209 or 8120 or 8121 or 325 or 319 or 321 or 1038)
        {
            result.Error = ex.Message;
        }
        catch (SqlException ex) when (ex.Number == -2)
        {
            result.Error = "The query took too long (10s limit).";
        }
        catch (Exception)
        {
            result.Error = "The query could not be run.";
        }
        result.ElapsedMs = sw.ElapsedMilliseconds;
        return result;
    }

    public async Task<CheckOutcome> CheckAsync(string userSql, string answerSql)
    {
        var user = await RunAsync(userSql);
        if (user.Error is not null) return new CheckOutcome(false, "Your query failed: " + user.Error);
        var expected = await RunAsync(answerSql, skipValidation: true);
        if (expected.Error is not null) return new CheckOutcome(false, "Could not run the model answer: " + expected.Error);

        if (user.Columns.Count != expected.Columns.Count)
            return new CheckOutcome(false, $"Expected {expected.Columns.Count} column(s) but your query returned {user.Columns.Count}. Check which columns the question asks for.");
        if (user.Rows.Count != expected.Rows.Count)
            return new CheckOutcome(false, $"Expected {expected.Rows.Count} row(s) but your query returned {user.Rows.Count}. Check your filters, joins (INNER vs LEFT) and grouping.");

        var u = user.Rows.Select(Key).OrderBy(x => x, StringComparer.Ordinal).ToList();
        var e = expected.Rows.Select(Key).OrderBy(x => x, StringComparer.Ordinal).ToList();
        for (var i = 0; i < u.Count; i++)
            if (u[i] != e[i])
                return new CheckOutcome(false, "The row count matches but some values differ. Check calculations, rounding and which rows are included.");

        return new CheckOutcome(true, "Correct! Your result matches the model answer (row order and column names are ignored).");
    }

    private static string Key(object?[] row) => string.Join("\u001f", row.Select(Normalize));

    private static string Normalize(object? v) => v switch
    {
        null => "NULL",
        DateTime d => d.ToString("yyyy-MM-dd HH:mm:ss", CultureInfo.InvariantCulture),
        string s => s.Trim(),
        bool b => b ? "1" : "0",
        byte or short or int or long or decimal or float or double =>
            Math.Round(Convert.ToDecimal(v, CultureInfo.InvariantCulture), 2).ToString("F2", CultureInfo.InvariantCulture),
        _ => Convert.ToString(v, CultureInfo.InvariantCulture)?.Trim() ?? "NULL"
    };

    public async Task<SchemaInfo> GetSchemaInfoAsync()
    {
        var info = new SchemaInfo();
        var r = await RunAsync("SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'dbo' ORDER BY TABLE_NAME, ORDINAL_POSITION", skipValidation: true);
        info.Columns = r.Rows.Select(x => new SchemaColumn { Table = (string)x[0]!, Column = (string)x[1]!, Type = (string)x[2]! }).ToList();
        if (info.Columns.Count > 0)
        {
            var c = await RunAsync("SELECT t.name, SUM(p.rows) FROM sys.tables t JOIN sys.partitions p ON p.object_id = t.object_id AND p.index_id IN (0,1) GROUP BY t.name", skipValidation: true);
            info.Counts = c.Rows.ToDictionary(x => (string)x[0]!, x => Convert.ToInt32(x[1]));
        }
        return info;
    }

    // Drops and recreates PracticeDB from the SQL scripts.
    public async Task<string?> ResetDatabaseAsync()
    {
        try
        {
            SqlConnection.ClearAllPools();
            var builder = new SqlConnectionStringBuilder(_connectionString) { InitialCatalog = "master" };
            await using var conn = new SqlConnection(builder.ConnectionString);
            await conn.OpenAsync();
            foreach (var file in new[] { "01_schema.sql", "02_seed.sql" })
            {
                var script = await File.ReadAllTextAsync(Path.Combine(_contentRoot, file));
                foreach (var batch in Regex.Split(script, @"^\s*GO\s*$", RegexOptions.Multiline | RegexOptions.IgnoreCase))
                {
                    if (string.IsNullOrWhiteSpace(batch)) continue;
                    await using var cmd = new SqlCommand(batch, conn) { CommandTimeout = 120 };
                    await cmd.ExecuteNonQueryAsync();
                }
            }
            return null;
        }
        catch (Exception ex)
        {
            return ex.Message;
        }
    }
}
