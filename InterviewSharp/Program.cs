using System.Threading.RateLimiting;
using InterviewSharp.Components;
using InterviewSharp.Services;
using Microsoft.AspNetCore.HttpOverrides;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorComponents()
    .AddInteractiveServerComponents();

var contentRoot = builder.Environment.ContentRootPath;
builder.Services.AddSingleton(new QuestionService(ContentJson.Parse<Question>(File.ReadAllText(Path.Combine(contentRoot, "questions.json")))));
builder.Services.AddSingleton(new McqService(new Dictionary<string, IReadOnlyList<McqQuestion>>
{
    ["angular"] = ContentJson.Parse<McqQuestion>(File.ReadAllText(Path.Combine(contentRoot, "mcq_angular.json"))),
    ["dotnet"] = ContentJson.Parse<McqQuestion>(File.ReadAllText(Path.Combine(contentRoot, "mcq_dotnet.json"))),
}));
builder.Services.AddSingleton<SqlRunner>();
builder.Services.AddSingleton<ISqlService, LocalSqlService>();

// CORS for the static PWA (set Cors:Origins to e.g. ["https://interviewsharp.pages.dev"]).
var origins = builder.Configuration.GetSection("Cors:Origins").Get<string[]>() ?? Array.Empty<string>();
builder.Services.AddCors(o => o.AddDefaultPolicy(p => p.WithOrigins(origins).WithMethods("GET", "POST").AllowAnyHeader()));

builder.Services.AddRateLimiter(o =>
{
    o.RejectionStatusCode = StatusCodes.Status429TooManyRequests;
    o.AddPolicy("sql", ctx => RateLimitPartition.GetFixedWindowLimiter(
        ctx.Connection.RemoteIpAddress?.ToString() ?? "anon",
        _ => new FixedWindowRateLimiterOptions { PermitLimit = builder.Configuration.GetValue("Api:RequestsPerMinute", 30), Window = TimeSpan.FromMinutes(1) }));
});

builder.Services.Configure<ForwardedHeadersOptions>(o =>
{
    o.ForwardedHeaders = ForwardedHeaders.XForwardedFor | ForwardedHeaders.XForwardedProto;
    o.KnownIPNetworks.Clear();
    o.KnownProxies.Clear();
});

var app = builder.Build();

app.UseForwardedHeaders();
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error", createScopeForErrors: true);
}
app.UseStatusCodePagesWithReExecute("/not-found", createScopeForStatusCodePages: true);
app.UseCors();
app.UseRateLimiter();
app.UseAntiforgery();

const int MaxSqlLength = 4000;
var api = app.MapGroup("/api").RequireRateLimiting("sql");
api.MapPost("/run", async (SqlRequest r, ISqlService sql) =>
    (r.Sql?.Length ?? 0) > MaxSqlLength
        ? Results.BadRequest("Query too long.")
        : Results.Ok(await sql.RunAsync(r.Sql ?? "")));
api.MapPost("/check", async (CheckRequest r, ISqlService sql) =>
    (r.Sql?.Length ?? 0) > MaxSqlLength || string.IsNullOrEmpty(r.Key)
        ? Results.BadRequest("Bad request.")
        : Results.Ok(await sql.CheckAsync(r.Sql ?? "", r.Key)));
api.MapGet("/schema", async (ISqlService sql) => Results.Ok(await sql.GetSchemaAsync()));
app.MapGet("/healthz", () => Results.Ok("ok"));

app.MapStaticAssets();
app.MapRazorComponents<App>()
    .AddInteractiveServerRenderMode()
    .AddAdditionalAssemblies(typeof(InterviewSharp.Shared.Pages.Marker).Assembly);

app.Run();

record SqlRequest(string? Sql);
record CheckRequest(string? Sql, string? Key);
