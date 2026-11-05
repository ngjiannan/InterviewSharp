def add(m):
    E = "Expert"

    m(E, "GC / LOH",
      "Which statement about the Large Object Heap (LOH) in the .NET GC is correct?",
      ["Objects of 85,000 bytes or more are allocated on the LOH, which is collected only with gen 0 collections",
       "The LOH is always compacted on every gen 1 collection",
       "Objects of roughly 85,000 bytes or more are allocated on the LOH, which is logically collected together with gen 2",
       "Only arrays can ever be allocated on the LOH; strings never are"],
      [2],
      "Think about the size threshold and which generation the LOH is tied to.",
      "Large objects (about 85,000 bytes and up) go to the LOH, which is collected as part of gen 2 collections and is not compacted by default. Gen 0 and gen 1 collections do not touch it. Strings can also land on the LOH when large enough.")

    m(E, "GC / Server vs Workstation",
      "Which statements about server GC versus workstation GC are correct? (Select all that apply.)",
      ["Server GC creates a separate heap and dedicated GC thread per logical core",
       "Workstation GC cannot perform background (concurrent) gen 2 collections",
       "Server GC generally favors throughput at the cost of higher memory use",
       "Server GC never compacts the heap"],
      [0, 2],
      "Server GC trades memory for parallel throughput.",
      "Server GC uses per-core heaps and GC threads and is tuned for throughput, so it uses more memory. Workstation GC does support background GC, and both flavors can compact.")

    m(E, "Span<T> / ref structs",
      "Which statements about Span<T> are correct? (Select all that apply.)",
      ["It cannot be a field of a class or be boxed because it is a ref struct",
       "It cannot wrap an existing managed array, only stack memory",
       "Slicing it with Slice() copies the elements into a new buffer",
       "It can wrap memory obtained from stackalloc in safe code",
       "It cannot be captured by a lambda or stored in a closure"],
      [0, 3, 4],
      "Span<T> must live on the stack.",
      "As a ref struct, Span<T> is restricted to the stack: no boxing, no class fields, no closure capture. It can wrap arrays and stackalloc memory, and Slice returns a view over the same memory without copying.",
      code="""Span<int> buf = stackalloc int[4];
int[] arr = { 1, 2, 3, 4 };
Span<int> view = arr.AsSpan(1, 2); // view over arr, no copy
view[0] = 99;                      // arr[1] is now 99""")

    m(E, "ValueTask",
      "Which statements about consuming a ValueTask<T> are correct? (Select all that apply.)",
      ["A ValueTask<T> always avoids heap allocation",
       "It must not be awaited multiple times",
       "Call AsTask() if you need to await it more than once or store it for later use",
       "Task.WhenAll accepts ValueTask<T> instances directly without conversion"],
      [1, 2],
      "A ValueTask may wrap a pooled, reusable source.",
      "A ValueTask can wrap an IValueTaskSource that is reused, so it is single-consumption; AsTask gives a safely shareable Task. It only avoids allocation when it completes synchronously or is backed by a pooled source, and WhenAll requires Tasks.")

    m(E, "Async state machines",
      "In the snippet, what happens when F() is called without awaiting it?",
      ["The call returns a faulted Task and the exception is observed when the Task is awaited or inspected",
       "The exception is thrown synchronously from the call to F()",
       "The exception is swallowed permanently and can never be observed",
       "The process crashes immediately because the exception is unhandled"],
      [0],
      "The async state machine catches exceptions and stores them in the returned Task.",
      "The compiler-generated state machine wraps the body in try/catch and sets the exception on the AsyncTaskMethodBuilder's Task. The caller therefore gets a faulted Task, and the exception only surfaces on await, Wait or Result. It is not thrown synchronously.",
      code="""static async Task F()
{
    throw new InvalidOperationException("boom");
}

static void Main()
{
    Task t = F();            // line A
    Console.WriteLine(t.IsFaulted);
}""")

    m(E, "SynchronizationContext",
      "In an ASP.NET Core application, which statement about ConfigureAwait(false) and blocking calls is most accurate?",
      ["Omitting ConfigureAwait(false) will classically deadlock on .Result, exactly like in ASP.NET Framework",
       "ConfigureAwait(false) makes the awaited operation run on a new dedicated thread",
       "ConfigureAwait(false) prevents the state machine from being generated",
       "ASP.NET Core has no SynchronizationContext, so the classic context deadlock does not occur, but sync-over-async can still cause thread pool starvation"],
      [3],
      "Think about what ASP.NET Core removed compared to ASP.NET Framework.",
      "ASP.NET Core does not install a request SynchronizationContext, so the classic deadlock is gone. Blocking on async code still ties up thread pool threads and can starve the pool. ConfigureAwait(false) only controls context capture for continuations.")

    m(E, "ExecutionContext / AsyncLocal",
      "What does the following code print?",
      ["2",
       "1",
       "0",
       "It throws because AsyncLocal cannot be set inside an async method"],
      [1],
      "Changes made to an ambient value inside an async callee are not visible to the caller after it returns.",
      "ExecutionContext flows down into async calls, but modifications made inside the callee's async method apply to its own copy and are undone when control returns to the caller. The caller still sees 1. AsyncLocal can be set anywhere.",
      code="""static readonly AsyncLocal<int> V = new();

static async Task Child()
{
    V.Value = 2;
    await Task.Yield();
}

static async Task Main()
{
    V.Value = 1;
    await Child();
    Console.WriteLine(V.Value);
}""")

    m(E, "Channels",
      "Given a bounded channel created with FullMode = BoundedChannelFullMode.Wait that is currently full, which statements are correct? (Select all that apply.)",
      ["writer.TryWrite(item) returns false",
       "writer.WriteAsync(item) throws ChannelClosedException immediately",
       "The ValueTask returned by writer.WriteAsync(item) completes once space becomes available",
       "With BoundedChannelFullMode.DropWrite, WriteAsync completes successfully but the item is discarded"],
      [0, 2, 3],
      "Distinguish Wait mode from the drop modes.",
      "In Wait mode TryWrite fails and WriteAsync asynchronously waits for room. DropWrite silently discards the item being written. A ChannelClosedException is only thrown if the writer was completed.")

    m(E, "Channels",
      "When does ChannelReader<T>.Completion complete normally?",
      ["As soon as the writer calls Complete(), even if items are still buffered",
       "When the channel's buffer first becomes empty",
       "After the writer has called Complete() and all buffered items have been read",
       "Only when the reader's CancellationToken is cancelled"],
      [2],
      "Completion represents the end of data, not just the end of writing.",
      "Completion finishes only after the writer is marked complete and the buffer has been drained, which is what lets ReadAllAsync terminate cleanly. Completing the writer alone is not enough while items remain.")

    m(E, "lock / Monitor",
      "Why does C# forbid await inside a lock statement, and what is the usual alternative?",
      ["Monitor is owned by a thread, and the continuation may resume on a different thread; use SemaphoreSlim(1,1) with WaitAsync instead",
       "await is forbidden because the lock keyword compiles to a spin lock; use Thread.Sleep instead",
       "The compiler cannot generate a state machine inside try/finally; use a nested method",
       "It is allowed but only in static methods; use a static lock object"],
      [0],
      "Monitor ownership is tied to a managed thread id.",
      "Monitor.Exit must be called by the owning thread, but after an await the code may resume on another thread, so the compiler reports an error. SemaphoreSlim is not thread-affine and supports WaitAsync. Async methods can contain try/finally.",
      code="""private readonly SemaphoreSlim _gate = new(1, 1);

public async Task UpdateAsync()
{
    await _gate.WaitAsync();
    try { await DoWorkAsync(); }
    finally { _gate.Release(); }
}""")

    m(E, "SemaphoreSlim / cancellation",
      "In this method, what is the bug and the correct fix?",
      ["No bug: Release is always correct in finally",
       "WaitAsync must be called with ConfigureAwait(false) to avoid releasing twice",
       "SemaphoreSlim cannot be used with CancellationToken, so remove the token",
       "If WaitAsync(ct) throws OperationCanceledException, finally still calls Release and inflates the count; move WaitAsync before the try block"],
      [3],
      "Release should only happen if the wait succeeded.",
      "When WaitAsync is inside the try and is cancelled, the semaphore was never acquired, yet finally releases it, permanently increasing the available count and breaking mutual exclusion. Acquire before entering try so finally runs only after a successful acquire.",
      code="""async Task RunAsync(SemaphoreSlim sem, CancellationToken ct)
{
    try
    {
        await sem.WaitAsync(ct);
        await DoWorkAsync(ct);
    }
    finally
    {
        sem.Release();
    }
}""")

    m(E, "Interlocked",
      "Which statements about lock-free updates with Interlocked are correct? (Select all that apply.)",
      ["Interlocked.CompareExchange in a retry loop can implement arbitrary atomic read-modify-write updates",
       "Writing count = count + 1 on a volatile int is atomic",
       "Interlocked.Increment performs an atomic read-modify-write",
       "Interlocked.Read is required to read an int safely on 64-bit platforms"],
      [0, 2],
      "volatile gives ordering, not atomic read-modify-write.",
      "Interlocked.Increment is atomic, and a CompareExchange loop can build other atomic updates. A volatile read followed by a write is two separate operations, so increments can be lost. Interlocked.Read is only relevant for 64-bit values on 32-bit platforms.",
      code="""static int _max;

static void UpdateMax(int value)
{
    int cur;
    while (value > (cur = Volatile.Read(ref _max)))
    {
        if (Interlocked.CompareExchange(ref _max, value, cur) == cur) break;
    }
}""")

    m(E, "Memory model / volatile",
      "What does marking a field volatile guarantee in the .NET memory model?",
      ["It makes compound operations like i++ atomic",
       "Reads have acquire semantics and writes have release semantics, but compound operations are not atomic",
       "It forces the field to be allocated on the stack",
       "It gives a full fence around every access, equivalent to a lock"],
      [1],
      "Think acquire/release, not atomicity.",
      "Volatile reads are acquire and volatile writes are release, limiting reordering around them. It does not make read-modify-write atomic and is not a full fence or a lock.")

    m(E, "Expression trees",
      "Which statements about expression trees are correct? (Select all that apply.)",
      ["An Expression<Func<T,bool>> can be inspected by a provider such as EF Core and translated to SQL",
       "Calling Compile() repeatedly is cheap, so caching the delegate is unnecessary",
       "C# lets you convert a lambda with a statement body to Expression<Func<T>> without restriction",
       "Expression trees are immutable, so changes are made by rewriting with an ExpressionVisitor"],
      [0, 3],
      "Think data-as-code, and what the compiler allows in expression lambdas.",
      "Expression trees describe code as data and are immutable, so ExpressionVisitor builds modified copies. Compile() emits IL and is expensive, so delegates should be cached. The compiler rejects statement lambdas for expression trees.")

    m(E, "Expression trees",
      "For the lambda below, how is the captured local id represented in the expression tree?",
      ["As a ConstantExpression holding the int 5 evaluated at compile time",
       "As a ParameterExpression named id",
       "As a MemberExpression reading a field of a compiler-generated closure object held in a ConstantExpression",
       "As a MethodCallExpression to Convert.ToInt32"],
      [2],
      "Captured variables live in a closure class.",
      "The compiler hoists captured locals into a closure class instance, and the tree contains a field access on a constant of that closure type. That is why providers like EF Core can parameterize it and re-evaluate on each execution. It is not folded to a constant of 5.",
      code="""record Order(int Id);

int id = 5;
Expression<Func<Order, bool>> e = o => o.Id == id;
var right = ((BinaryExpression)e.Body).Right;
Console.WriteLine(right.NodeType);""")

    m(E, "Source generators",
      "Which statements about Roslyn source generators are correct? (Select all that apply.)",
      ["They can add new source files to a compilation but cannot modify existing user code",
       "They can rewrite the bodies of existing methods in user files",
       "IIncrementalGenerator is preferred over ISourceGenerator because it caches pipeline stages",
       "They can call into the compiled output of the project they are generating code for"],
      [0, 2],
      "Generators are additive and run inside the compiler.",
      "Generators only add code, and incremental generators cache stage results to keep the IDE responsive. They run before the target assembly exists, so they cannot call its compiled output or rewrite existing code.")

    m(E, "Source generators",
      "In an IIncrementalGenerator pipeline, what is the key practice for good caching and IDE performance?",
      ["Transform syntax early into small value-equatable models (such as records) and avoid carrying ISymbol or Compilation objects downstream",
       "Store the full Compilation in each pipeline step so results are always fresh",
       "Use static mutable dictionaries to cache models across runs",
       "Perform all work in the final RegisterSourceOutput step using SyntaxNode trees"],
      [0],
      "Incremental stages are skipped only when their inputs compare equal.",
      "The pipeline reuses cached outputs when a stage's input is equal to the previous one, so models need value equality, and symbols or compilations change on nearly every edit and defeat caching. Static mutable caches are unsafe and unnecessary.")

    m(E, "EF Core change tracker",
      "Which statements about EF Core tracking are correct? (Select all that apply.)",
      ["For tracked entities, DetectChanges compares current property values against a snapshot",
       "A no-tracking query returns the same instance for repeated rows with the same key",
       "AsNoTrackingWithIdentityResolution returns a single instance per key within the query results",
       "A context can track two different instances with the same primary key at the same time"],
      [0, 2],
      "Identity resolution is what the tracker normally provides.",
      "The default tracker uses snapshots and enforces one instance per key. Plain no-tracking queries may materialize separate instances for repeated rows, which AsNoTrackingWithIdentityResolution fixes within a query. Tracking two instances with the same key throws.")

    m(E, "EF Core concurrency",
      "How does EF Core optimistic concurrency with a configured concurrency token work? (Select all that apply.)",
      ["It takes a pessimistic lock on the row when the entity is loaded",
       "The UPDATE or DELETE includes the original token value in its WHERE clause",
       "A DbUpdateConcurrencyException is thrown when the affected row count is not the expected one",
       "The token value used is re-read from the database at SaveChanges time"],
      [1, 2],
      "The original values come from when the entity was loaded.",
      "EF adds the original token value to the WHERE clause and treats an unexpected affected-row count as a conflict. No row lock is taken, and the original value comes from load time, which is the point of the check.",
      code="""public class Product
{
    public int Id { get; set; }
    public string Name { get; set; } = "";
    [Timestamp] public byte[] RowVersion { get; set; } = null!;
}""")

    m(E, "EF Core split queries",
      "Which statements about AsSplitQuery in EF Core are correct? (Select all that apply.)",
      ["It avoids cartesian explosion when including multiple collection navigations",
       "It guarantees a consistent snapshot across all the generated SQL queries",
       "It uses multiple round trips, and data can change between them unless a suitable transaction isolation is used",
       "It requires AsNoTracking to work"],
      [0, 2],
      "Multiple queries means multiple points in time.",
      "Split queries issue separate SQL statements per collection to avoid duplicated parent rows. Without a snapshot or serializable transaction, results may be inconsistent between the statements. It works with tracking queries.",
      code="""var blogs = await db.Blogs
    .Include(b => b.Posts)
    .Include(b => b.Tags)
    .AsSplitQuery()
    .ToListAsync();""")

    m(E, "EF Core compiled queries",
      "What is the main benefit of EF.CompileAsyncQuery?",
      ["It caches the result rows in memory between calls",
       "It turns the query into a stored procedure on the database",
       "It disables parameterization to reuse database plans",
       "The query is translated once and reused through a delegate, skipping per-call query cache lookup and preprocessing"],
      [3],
      "It optimizes the client-side pipeline, not the database.",
      "A compiled query keeps the translated query in a delegate, removing repeated expression processing and cache-key computation. It does not cache data, create stored procedures, or change parameterization.",
      code="""static readonly Func<AppDb, int, Task<Customer?>> ById =
    EF.CompileAsyncQuery((AppDb db, int id) =>
        db.Customers.FirstOrDefault(c => c.Id == id));

var c = await ById(db, 42);""")

    m(E, "EF Core bulk operations",
      "What is true about ExecuteUpdateAsync in EF Core?",
      ["It loads the entities into the change tracker, modifies them, then calls SaveChanges",
       "It runs a set-based UPDATE directly in the database, and already tracked entities are not refreshed",
       "It only works inside a SaveChanges transaction",
       "It raises DbUpdateConcurrencyException automatically for rowversion columns"],
      [1],
      "It bypasses the change tracker entirely.",
      "ExecuteUpdate translates to a single UPDATE statement without materializing entities, so tracked instances can become stale. It does not use the tracker or concurrency token checks.")

    m(E, "ASP.NET Core middleware",
      "Which statements about the ASP.NET Core middleware pipeline are correct? (Select all that apply.)",
      ["A middleware that does not call next short-circuits the pipeline",
       "Response processing runs through middleware in the same order as request processing",
       "Exception handling middleware registered first can catch exceptions thrown by middleware registered after it",
       "app.Run adds a terminal middleware that has no next delegate"],
      [0, 2, 3],
      "Think of the pipeline as nested calls.",
      "Middleware are nested delegates: skipping next short-circuits, and an outer try/catch sees exceptions from inner components. Run is terminal. The response travels back through the middleware in reverse order.")

    m(E, "ASP.NET Core middleware",
      "An exception is thrown after the response body has already started streaming. What can an exception-handling middleware do?",
      ["Change the status code to 500 as usual",
       "Clear the already-sent headers with Response.Clear()",
       "Nothing useful to the status code; once HasStarted is true headers are sent, so it can only abort the connection or log",
       "Restart the request pipeline from the beginning"],
      [2],
      "Headers go out before the body.",
      "After the first body bytes are flushed, status and headers are already on the wire and cannot be modified. Handlers should check Response.HasStarted and typically log and abort. Clear fails or is ignored once the response has started.")

    m(E, "Rate limiting",
      "What is a known characteristic of the fixed window rate limiter compared to a sliding window?",
      ["Up to about twice the permit limit can pass in a short period that straddles a window boundary",
       "It never allows more than the limit in any time span",
       "It cannot be partitioned per user",
       "It queues requests by default with unlimited queue length"],
      [0],
      "Think of requests at the end of one window and the start of the next.",
      "A fixed window resets counts at boundaries, so bursts at the end of one window and the start of the next can approach twice the limit. Sliding windows smooth this. Fixed window limiters can be partitioned and do not queue unboundedly by default.")

    m(E, "Output caching",
      "Which statements about ASP.NET Core output caching are correct? (Select all that apply.)",
      ["Cache entries can be evicted by tag using IOutputCacheStore.EvictByTagAsync",
       "Responses are stored in the client browser cache",
       "By default it does not honor a client's Cache-Control: no-cache request header the way response caching does",
       "By default only 200 responses to GET or HEAD requests are cached"],
      [0, 2, 3],
      "Output caching is server-side and policy-driven.",
      "Output caching stores responses on the server, supports tag-based eviction, and is controlled by server policies rather than client headers. The default policy caches only 200 GET/HEAD responses. Browser storage is a different feature.")

    m(E, "Health checks",
      "What is the recommended design for liveness versus readiness health checks in an orchestrated environment?",
      ["Liveness should check all downstream dependencies so unhealthy pods restart",
       "Both probes should run the same checks to avoid confusion",
       "Readiness should return 200 always so traffic is never interrupted",
       "Liveness should be cheap and reflect only whether the process itself is healthy, while readiness checks dependencies and ability to serve traffic"],
      [3],
      "A restart should not be triggered by an external outage.",
      "A liveness probe that depends on a database can restart every instance during a database outage, making things worse. Readiness gates traffic and may check dependencies. Typically these are mapped as separate health check endpoints using tags.")

    m(E, "Minimal API filters",
      "In the snippet, how does an endpoint filter reject invalid input without invoking the handler?",
      ["Throw OperationCanceledException",
       "Return an IResult without calling next(context)",
       "Set context.HttpContext.Response.HasStarted to true",
       "Call next(context) twice"],
      [1],
      "A filter wraps the handler like middleware.",
      "An IEndpointFilter chooses whether to call next. Returning a result directly short-circuits the handler and later filters. Throwing cancellation would not produce a proper validation response.",
      code="""app.MapGet("/items/{id:int}", (int id) => Results.Ok(id))
   .AddEndpointFilter(async (ctx, next) =>
   {
       var id = ctx.GetArgument<int>(0);
       if (id <= 0) return Results.BadRequest("id must be positive");
       return await next(ctx);
   });""")

    m(E, "DI scoping",
      "Which statements about dependency injection lifetimes in Microsoft.Extensions.DependencyInjection are correct? (Select all that apply.)",
      ["A singleton that takes a scoped service in its constructor creates a captive dependency",
       "ServiceProviderOptions.ValidateScopes can detect resolving scoped services from the root provider",
       "Transient IDisposable services are never disposed by the container",
       "A singleton can create scopes on demand with IServiceScopeFactory to use scoped services safely"],
      [0, 1, 3],
      "The container tracks disposables it creates.",
      "Capturing a scoped service in a singleton keeps it alive for the app lifetime. ValidateScopes and scope factories address that. The container does track and dispose transient disposables it creates, at the end of their scope.")

    m(E, "Keyed services",
      "Given the registration below, what happens when you call provider.GetRequiredService<ICache>() with no key?",
      ["It returns the RedisCache because it is the only ICache registered",
       "It returns the first keyed registration alphabetically",
       "It returns null",
       "It throws InvalidOperationException because keyed registrations are not resolved by a non-keyed request"],
      [3],
      "Keyed and non-keyed registrations are looked up separately.",
      "A keyed registration only matches requests that supply a matching key, such as [FromKeyedServices(\"redis\")] or GetRequiredKeyedService. A non-keyed request finds no registration and GetRequiredService throws.",
      code="""builder.Services.AddKeyedSingleton<ICache, RedisCache>("redis");

public class Svc([FromKeyedServices("redis")] ICache cache) { }""")

    m(E, "DI disposal",
      "Which services does the built-in DI container dispose when the provider or scope is disposed?",
      ["Only instances it created itself via a type or factory registration; instances registered with AddSingleton(instance) are not disposed by it",
       "All services including pre-created instances registered with AddSingleton(instance)",
       "Only scoped services, never singletons",
       "None; services must always be disposed manually"],
      [0],
      "Ownership matters.",
      "The container owns and disposes instances it creates, but caller-provided instances remain the caller's responsibility. Singletons created by the container are disposed when the root provider is disposed.")

    m(E, "Outbox pattern",
      "Which statements about the transactional outbox pattern are correct? (Select all that apply.)",
      ["The outbox row is inserted in the same database transaction as the business change",
       "It gives exactly-once delivery to the broker without consumer cooperation",
       "Consumers should be idempotent because a relay can publish a message and crash before marking it sent",
       "Publishing to the broker inside the transaction before committing makes it equivalent",
       "A background relay reads unsent outbox rows and publishes them"],
      [0, 2, 4],
      "The pattern gives at-least-once delivery.",
      "The outbox atomically records intent with the state change, and a relay publishes later, which yields at-least-once delivery with possible duplicates. Publishing before commit can send messages for rolled-back changes, so it is not equivalent.")

    m(E, "Idempotency",
      "What is the most robust way to implement idempotency keys for a payment API?",
      ["Check a cache for the key, then process, with no locking",
       "Rely on clients never retrying",
       "Use the request timestamp as the key",
       "Insert the key under a unique constraint in the same transaction as the side effects, and return the stored response on replay"],
      [3],
      "A check-then-act race needs an atomic guard.",
      "A unique constraint makes the claim atomic, and committing it together with the side effects avoids processing twice or losing the record. A non-atomic check allows concurrent duplicates. Timestamps do not identify retries.")

    m(E, "Resilience",
      "Which statements about retry and circuit-breaker strategies are correct? (Select all that apply.)",
      ["Infinite immediate retries are safe because they maximize success",
       "Exponential backoff with jitter reduces synchronized retry storms",
       "An open circuit breaker fails calls fast, giving the dependency time to recover",
       "Retrying a non-idempotent POST is safe without idempotency keys"],
      [1, 2],
      "Retries amplify load on a failing dependency.",
      "Jitter spreads retries and breakers shed load. Unbounded immediate retries can overload a struggling service, and retrying non-idempotent operations risks duplicate effects.")

    m(E, "Resilience / timeouts",
      "How does a Polly (v8) timeout strategy behave if the guarded delegate ignores its CancellationToken?",
      ["It aborts the thread running the delegate",
       "It is cooperative: it signals cancellation through the token, so code that ignores the token keeps running",
       "It throws ThreadAbortException into the delegate",
       "It is guaranteed to terminate the underlying HTTP connection"],
      [1],
      "No thread is killed in modern .NET.",
      "Timeouts rely on cancellation tokens, and nothing can forcibly stop code that does not observe them. Thread abort is not supported in .NET Core and later, and connection termination is not automatic.")

    m(E, "Native AOT",
      "Which approach makes JSON serialization compatible with Native AOT and trimming?",
      ["Use the default reflection-based serializer, which works unchanged",
       "Disable the trimmer warnings",
       "Use a source-generated JsonSerializerContext with JsonSerializable attributes",
       "Use Type.GetType with strings to load converters"],
      [2],
      "Avoid runtime reflection over your types.",
      "The source generator emits serialization metadata at compile time, so the trimmer and AOT compiler can see what is needed. Reflection-based serialization may fail when members are trimmed, and suppressing warnings only hides the problem.",
      code="""[JsonSerializable(typeof(WeatherForecast))]
internal partial class AppJsonContext : JsonSerializerContext { }

string json = JsonSerializer.Serialize(
    forecast, AppJsonContext.Default.WeatherForecast);""")

    m(E, "Trimming",
      "Which statements about trimming and reflection are correct? (Select all that apply.)",
      ["The trimmer cannot statically see types accessed only by string name through reflection and may remove them",
       "Type.GetType(\"Namespace.Type\") is always safe with trimming",
       "[DynamicallyAccessedMembers] annotations tell the trimmer which members must be preserved",
       "PublishTrimmed removes only whole unused assemblies and never members"],
      [0, 2],
      "Static analysis cannot follow arbitrary strings.",
      "The linker works on static reachability, so annotations or explicit roots are needed for reflection targets. Trimming removes unused types and members as well, so string-based lookup can break.")

    m(E, "BenchmarkDotNet",
      "Which practices avoid common BenchmarkDotNet pitfalls? (Select all that apply.)",
      ["Running benchmarks from a Debug build is fine for relative comparisons",
       "Running in Release without a debugger attached",
       "Returning the computed result from the benchmark method so the JIT cannot eliminate the work as dead code",
       "Building the input data inside the benchmark method because setup cost is excluded automatically"],
      [1, 2],
      "Optimization and dead-code elimination affect measurements.",
      "Release builds are required for meaningful JIT optimization, and returning or consuming results prevents dead-code elimination. Setup inside the benchmark body is measured, so it should be in [GlobalSetup] or [IterationSetup].",
      code="""[Benchmark]
public int Sum() => _data.Sum();   // result returned, not discarded

[GlobalSetup]
public void Setup() => _data = Enumerable.Range(0, 1000).ToArray();""")

    m(E, "Cancellation",
      "On which thread do callbacks registered via CancellationToken.Register run when CancellationTokenSource.Cancel() is called?",
      ["Synchronously on the thread that calls Cancel(), by default",
       "Always on a new thread pool thread",
       "On the thread that created the token",
       "On the thread that registered the callback"],
      [0],
      "Cancel() does not queue the callbacks.",
      "Registered callbacks run inline on the thread that calls Cancel, so slow callbacks block the canceller. Use CancelAsync or move heavy work off the callback. They are not marshaled to the creating or registering thread.")

    m(E, "Concurrent collections",
      "Which statements about ConcurrentDictionary.GetOrAdd(key, valueFactory) are correct? (Select all that apply.)",
      ["The factory may be invoked more than once concurrently for the same key, but only one value is stored",
       "The factory always runs under the dictionary's global lock",
       "Wrapping values in Lazy<T> ensures the expensive initialization runs only once",
       "Racing callers can end up with different instances for the same key"],
      [0, 2],
      "The factory runs outside the internal locks.",
      "The factory runs outside the locks, so duplicate invocations can occur, but all callers receive the single stored value. Lazy<T> defers and de-duplicates expensive creation.",
      code="""var cache = new ConcurrentDictionary<string, Lazy<Task<Data>>>();
var data = await cache.GetOrAdd(key,
    k => new Lazy<Task<Data>>(() => LoadAsync(k))).Value;""")
