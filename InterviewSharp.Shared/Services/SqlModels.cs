namespace InterviewSharp.Services;

public class QueryResult
{
    public List<string> Columns { get; set; } = new();
    public List<object?[]> Rows { get; set; } = new();
    public bool Truncated { get; set; }
    public string? Error { get; set; }
    public long ElapsedMs { get; set; }
}

public record CheckOutcome(bool Correct, string Message);

public class SchemaColumn
{
    public string Table { get; set; } = "";
    public string Column { get; set; } = "";
    public string Type { get; set; } = "";
}

public class SchemaInfo
{
    public List<SchemaColumn> Columns { get; set; } = new();
    public Dictionary<string, int> Counts { get; set; } = new();
}

// Runs practice queries: directly against SQL Server (server app) or through the HTTP API (PWA).
public interface ISqlService
{
    // False when no SQL backend is configured; the UI then falls back to study mode.
    bool IsConfigured { get; }
    bool CanReset { get; }
    Task<QueryResult> RunAsync(string sql);
    Task<CheckOutcome> CheckAsync(string sql, string questionKey);
    Task<SchemaInfo?> GetSchemaAsync();
    Task<string?> ResetAsync();
}
