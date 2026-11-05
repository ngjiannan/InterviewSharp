namespace InterviewSharp.Services;

// In-process ISqlService used by the server app (and exposed over HTTP via /api).
public class LocalSqlService : ISqlService
{
    private readonly SqlRunner _runner;
    private readonly QuestionService _questions;
    private readonly bool _allowReset;

    public LocalSqlService(SqlRunner runner, QuestionService questions, IConfiguration config)
    {
        _runner = runner;
        _questions = questions;
        _allowReset = config.GetValue("Hosted:AllowReset", true);
    }

    public bool IsConfigured => true;
    public bool CanReset => _allowReset;

    public Task<QueryResult> RunAsync(string sql) => _runner.RunAsync(sql);

    public async Task<CheckOutcome> CheckAsync(string sql, string questionKey)
    {
        var q = _questions.ByKey(questionKey);
        return q is null
            ? new CheckOutcome(false, "Unknown question.")
            : await _runner.CheckAsync(sql, q.Answer);
    }

    public async Task<SchemaInfo?> GetSchemaAsync() => await _runner.GetSchemaInfoAsync();

    public async Task<string?> ResetAsync() => _allowReset ? await _runner.ResetDatabaseAsync() : "Reset is disabled on this server.";
}
