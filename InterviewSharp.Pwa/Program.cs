using Microsoft.AspNetCore.Components.Web;
using Microsoft.AspNetCore.Components.WebAssembly.Hosting;
using InterviewSharp.Pwa;
using InterviewSharp.Services;

var builder = WebAssemblyHostBuilder.CreateDefault(args);
builder.RootComponents.Add<App>("#app");
builder.RootComponents.Add<HeadOutlet>("head::after");

var http = new HttpClient { BaseAddress = new Uri(builder.HostEnvironment.BaseAddress) };
async Task<List<T>> Load<T>(string file) => ContentJson.Parse<T>(await http.GetStringAsync($"data/{file}"));

// Content is small static JSON, loaded once at startup (and cached offline by the service worker).
builder.Services.AddSingleton(new QuestionService(await Load<Question>("questions.json")));
builder.Services.AddSingleton(new McqService(new Dictionary<string, IReadOnlyList<McqQuestion>>
{
    ["angular"] = await Load<McqQuestion>("mcq_angular.json"),
    ["dotnet"] = await Load<McqQuestion>("mcq_dotnet.json"),
}));
var remote = new RemoteSqlService(new HttpClient { Timeout = TimeSpan.FromSeconds(75) }, builder.Configuration["ApiBaseUrl"]);
builder.Services.AddSingleton<ISqlService>(remote);
_ = remote.WarmUpAsync();

await builder.Build().RunAsync();
