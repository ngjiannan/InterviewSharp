using System.Text.Json;

namespace InterviewSharp.Services;

public record Question(int Id, string Level, string Topic, string Text, List<string> Hints, string Answer, string Explanation, string Key, List<string> Tables, List<string> Returns, string Ordering);

public record McqQuestion(int Id, string Level, string Topic, string Text, List<string> Options, List<int> Correct,
    string Hint, string Explanation, string? Code, string Key);

public static class ContentJson
{
    public static readonly JsonSerializerOptions Options = new() { PropertyNameCaseInsensitive = true };
    public static List<T> Parse<T>(string json) => JsonSerializer.Deserialize<List<T>>(json, Options) ?? new();
}

public class QuestionService
{
    public IReadOnlyList<Question> Questions { get; }
    public QuestionService(IReadOnlyList<Question> questions) => Questions = questions;
    public Question? ByKey(string key) => Questions.FirstOrDefault(q => q.Key == key);
}

public class McqService
{
    private readonly IReadOnlyDictionary<string, IReadOnlyList<McqQuestion>> _tracks;
    public McqService(IReadOnlyDictionary<string, IReadOnlyList<McqQuestion>> tracks) => _tracks = tracks;
    public IReadOnlyList<McqQuestion> Get(string track) => _tracks.TryGetValue(track, out var q) ? q : Array.Empty<McqQuestion>();
}
