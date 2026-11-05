using Microsoft.SqlServer.TransactSql.ScriptDom;

namespace InterviewSharp.Services;

// Parses user SQL with the real T-SQL grammar, so comments/strings/quoting cannot hide extra statements.
public static class SqlGuard
{
    // Returns (error, normalizedSql). The normalized text is regenerated from the parse tree and is what gets executed.
    public static (string? Error, string? Sql) Check(string? sql)
    {
        if (string.IsNullOrWhiteSpace(sql)) return ("Please enter a query.", null);

        var parser = new TSql160Parser(initialQuotedIdentifiers: true);
        using var reader = new StringReader(sql);
        var fragment = parser.Parse(reader, out var errors);
        if (errors.Count > 0) return ($"Syntax error near line {errors[0].Line}: {errors[0].Message}", null);

        if (fragment is not TSqlScript script || script.Batches.Count != 1 || script.Batches[0].Statements.Count != 1)
            return ("Please run a single statement at a time.", null);
        if (script.Batches[0].Statements[0] is not SelectStatement select)
            return ("Only SELECT or WITH (CTE) queries are allowed.", null);

        var visitor = new Visitor();
        select.Accept(visitor);
        if (visitor.Problem is not null) return (visitor.Problem, null);

        new Sql160ScriptGenerator(new SqlScriptGeneratorOptions { IncludeSemicolons = false }).GenerateScript(select, out var text);
        return (null, text);
    }

    private sealed class Visitor : TSqlFragmentVisitor
    {
        public string? Problem;

        public override void Visit(SelectStatement node)
        {
            if (node.Into is not null) Problem ??= "SELECT ... INTO is not allowed.";
            if (node.ComputeClauses?.Count > 0) Problem ??= "COMPUTE is not allowed.";
        }
        public override void Visit(OpenRowsetTableReference node) => Problem ??= "OPENROWSET is not allowed.";
        public override void Visit(OpenQueryTableReference node) => Problem ??= "OPENQUERY is not allowed.";
        public override void Visit(AdHocTableReference node) => Problem ??= "OPENDATASOURCE is not allowed.";
        public override void Visit(BulkOpenRowset node) => Problem ??= "OPENROWSET is not allowed.";
        public override void Visit(SchemaObjectFunctionTableReference node) => CheckName(node.SchemaObject);
        public override void Visit(FunctionCall node)
        {
            if (node.CallTarget is MultiPartIdentifierCallTarget t && t.MultiPartIdentifier.Count > 1)
                Problem ??= "Calling schema-qualified functions is not allowed.";
        }
        public override void Visit(SchemaObjectName node) => CheckName(node);
        public override void Visit(VariableReference node) => Problem ??= "Variables are not allowed.";
        public override void Visit(GlobalVariableExpression node) => Problem ??= "System variables are not allowed.";

        private void CheckName(SchemaObjectName? n)
        {
            if (n is null) return;
            if (n.ServerIdentifier is not null || (n.DatabaseIdentifier is not null))
                Problem ??= "Cross-database and linked-server references are not allowed.";
            var schema = n.SchemaIdentifier?.Value;
            var name = n.BaseIdentifier?.Value ?? "";
            if (schema is not null && schema.Equals("sys", StringComparison.OrdinalIgnoreCase) && !AllowedSys.Contains(name))
                Problem ??= $"sys.{name} is not available in practice queries.";
        }
    }

    // Harmless catalog views that only list objects the login can already read.
    private static readonly HashSet<string> AllowedSys = new(StringComparer.OrdinalIgnoreCase)
    {
        "tables", "columns", "partitions", "indexes", "index_columns", "objects", "schemas", "types", "foreign_keys", "foreign_key_columns", "key_constraints"
    };
}
