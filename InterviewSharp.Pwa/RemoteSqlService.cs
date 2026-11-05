using System.Net.Http.Json;
using System.Text.Json;

namespace InterviewSharp.Services;

// ISqlService for the static PWA: talks to the hosted /api. With no ApiBaseUrl it stays in study mode.
public class RemoteSqlService : ISqlService
{
    private readonly HttpClient _http;
    private readonly string _baseUrl;

    public RemoteSqlService(HttpClient http, string? baseUrl)
    {
        _http = http;
        _baseUrl = (baseUrl ?? "").TrimEnd('/');
    }

    public bool IsConfigured => _baseUrl.Length > 0;
    public bool CanReset => false;

    private const string Unreachable =
        "Could not reach the SQL server. The free host sleeps when idle and can take 20-30 seconds to wake up - please try again.";

    public async Task<QueryResult> RunAsync(string sql)
    {
        try
        {
            var resp = await _http.PostAsJsonAsync($"{_baseUrl}/api/run", new { sql });
            if (resp.StatusCode == System.Net.HttpStatusCode.TooManyRequests)
                return new QueryResult { Error = "Too many requests - slow down and try again in a minute." };
            resp.EnsureSuccessStatusCode();
            var r = await resp.Content.ReadFromJsonAsync<QueryResult>(ContentJson.Options) ?? new QueryResult { Error = "Empty response." };
            foreach (var row in r.Rows)
                for (var i = 0; i < row.Length; i++) row[i] = Convert(row[i]);
            return r;
        }
        catch (Exception) { return new QueryResult { Error = Unreachable }; }
    }

    public async Task<CheckOutcome> CheckAsync(string sql, string questionKey)
    {
        try
        {
            var resp = await _http.PostAsJsonAsync($"{_baseUrl}/api/check", new { sql, key = questionKey });
            if (resp.StatusCode == System.Net.HttpStatusCode.TooManyRequests)
                return new CheckOutcome(false, "Too many requests - slow down and try again in a minute.");
            resp.EnsureSuccessStatusCode();
            return await resp.Content.ReadFromJsonAsync<CheckOutcome>(ContentJson.Options) ?? new CheckOutcome(false, "Empty response.");
        }
        catch (Exception) { return new CheckOutcome(false, Unreachable); }
    }

    public async Task<SchemaInfo?> GetSchemaAsync()
    {
        if (!IsConfigured) return null;
        try { return await _http.GetFromJsonAsync<SchemaInfo>($"{_baseUrl}/api/schema", ContentJson.Options); }
        catch (Exception) { return null; }
    }

    public Task<string?> ResetAsync() => Task.FromResult<string?>("Reset is only available when running locally.");

    // System.Text.Json yields JsonElement for object cells; turn them back into plain values for display.
    private static object? Convert(object? v)
    {
        if (v is not JsonElement e) return v;
        return e.ValueKind switch
        {
            JsonValueKind.Null or JsonValueKind.Undefined => null,
            JsonValueKind.String => e.TryGetDateTime(out var d) && e.GetString()!.Length >= 10 && e.GetString()![4] == '-' ? d : e.GetString(),
            JsonValueKind.Number => e.TryGetInt64(out var l) ? l : e.GetDecimal(),
            JsonValueKind.True => true,
            JsonValueKind.False => false,
            _ => e.ToString()
        };
    }
}
