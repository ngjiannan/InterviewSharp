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
        _connectionString = config.GetConnectionString("PracticeDb")
            ?? throw new InvalidOperationException("Missing ConnectionStrings:PracticeDb");
        _contentRoot = env.ContentRootPath;
    }

    [GeneratedRegex(@"\b(insert|update|delete|drop|alter|create|truncate|merge|exec|execute|grant|revoke|shutdown|backup|restore|into|use|openrowset|opendatasource|openquery|waitfor|dbcc)\b|\bxp_\w+|\bsp_\w+", RegexOptions.IgnoreCase)]
    private static partial Regex ForbiddenRegex();

    [GeneratedRegex(@"--[^\r\n]*|/\*.*?\*/", RegexOptions.Singleline)]
    private static partial Regex CommentRegex();

    // Light guard for a local single-user practice tool: read-only SELECT / WITH queries.
    public static string? Validate(string sql)
    {
        var cleaned = CommentRegex().Replace(sql ?? "", " ").Trim().TrimEnd(';').Trim();
        if (cleaned.Length == 0) return "Please enter a query.";
        if (!Regex.IsMatch(cleaned, @"^(select|with)\b", RegexOptions.IgnoreCase))
            return "Only SELECT or WITH (CTE) queries are allowed.";
        var noStrings = Regex.Replace(cleaned, @"'(?:[^']|'')*'", "''");
        if (noStrings.Contains(';')) return "Please run a single statement at a time.";
        var m = ForbiddenRegex().Match(noStrings);
        if (m.Success) return $"'{m.Value}' is not allowed in practice queries.";
        return null;
    }

    public async Task<QueryResult> RunAsync(string sql, bool skipValidation = false)
    {
        var result = new QueryResult();
        if (!skipValidation)
        {
            var problem = Validate(sql);
            if (problem is not null) { result.Error = problem; return result; }
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
        catch (Exception ex)
        {
            result.Error = ex.Message;
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
        var r = await RunAsync("SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS ORDER BY TABLE_NAME, ORDINAL_POSITION", skipValidation: true);
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
