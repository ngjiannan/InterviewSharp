def add(emit):
    H = "Hard"
    MS = " (Select all that apply.)"
    seen = [0]

    def m(level, topic, text, options, correct, hint, explanation, code=None):
        # Spread single-answer positions evenly by rotating the option list.
        if len(correct) == 1:
            n = len(options)
            shift = (seen[0] % n - correct[0]) % n
            seen[0] += 1
            options = [options[(i - shift) % n] for i in range(n)]
            correct = [(correct[0] + shift) % n]
        emit(level, topic, text, options, correct, hint, explanation, code)

    m(H, "Delegates/closures",
      "A lambda increments a captured local and is invoked twice. What is the local's value afterwards?",
      ["0", "1", "2", "It does not compile because lambdas cannot modify captured locals"],
      [2],
      "The lambda captures the variable itself.",
      "A closure captures the variable, not a copy of its value, so each call increments the same local. Lambdas are allowed to modify captured locals, so it does compile.",
      r'''int x = 0;
Func<int> next = () => ++x;
next();
next();
Console.WriteLine(x);''')

    m(H, "Delegates/closures",
      "Lambdas are added to a list inside a for loop and invoked afterwards. What is the output?",
      ["0 1 2", "3 3 3", "2 2 2", "It does not compile because i is modified after capture"],
      [1],
      "Think about how many variables the for loop declares.",
      "A for loop declares a single loop variable shared by all iterations, and the lambdas capture that variable, not its value. By the time they run, i is 3. The 0 1 2 result would need a per-iteration copy such as 'int c = i;'.",
      r'''var actions = new List<Action>();
for (int i = 0; i < 3; i++) actions.Add(() => Console.Write(i + " "));
foreach (var a in actions) a();''')

    m(H, "Delegates/closures",
      "Lambdas are added to a list inside a foreach loop and invoked afterwards. What is the output?",
      ["0 1 2", "2 2 2", "0 0 0", "It does not compile because the foreach variable is read-only inside lambdas"],
      [0],
      "Compare how foreach declares its iteration variable with how for does.",
      "Since C# 5 the foreach iteration variable is scoped inside the loop body, so each iteration gets a fresh variable that the lambda captures. Each action therefore remembers its own value. Capturing a for-loop counter behaves differently.",
      r'''var actions = new List<Action>();
foreach (var i in new[] { 0, 1, 2 }) actions.Add(() => Console.Write(i + " "));
foreach (var a in actions) a();''')

    m(H, "LINQ deferred execution",
      "An element is added to the list after the Where query is defined. What is printed?",
      ["2", "3", "4", "It throws InvalidOperationException because the list was modified"],
      [1],
      "When does Where actually look at the source list?",
      "Where is lazy, so the query is evaluated when Count() enumerates it, after 4 has been added. The elements greater than 1 at that moment are 2, 3 and 4, giving 3. No exception occurs because the list is not modified during enumeration.",
      r'''var list = new List<int> { 1, 2, 3 };
var q = list.Where(x => x > 1);
list.Add(4);
Console.WriteLine(q.Count());''')

    m(H, "LINQ deferred execution",
      "How many times is the Select lambda executed, and what is printed?",
      ["3", "0", "9", "6"],
      [3],
      "Each ToList enumerates the query from scratch.",
      "Select is deferred and not cached, so each ToList call re-runs the lambda for all three elements, giving 6. 3 would be correct only if results were memoized, and nothing is memoized in LINQ to Objects.",
      r'''int calls = 0;
var q = new[] { 1, 2, 3 }.Select(x => { calls++; return x * 2; });
var a = q.ToList();
var b = q.ToList();
Console.WriteLine(calls);''')

    m(H, "LINQ deferred execution",
      "Which of these LINQ operators execute (enumerate the source) immediately when called, rather than deferring until the result is enumerated?" + MS,
      ["ToList()", "Where(...)", "Select(...)", "Count()", "OrderBy(...)"],
      [0, 3],
      "Think about which ones return a materialized value rather than a query.",
      "ToList and Count produce a concrete result so they enumerate immediately. Where, Select and OrderBy return lazy sequences that do no work until enumerated.")

    m(H, "EF Core",
      "A repository method is declared as below. How is the filter applied for a SQL provider?",
      ["It is translated to a SQL WHERE clause because the source is a DbSet",
       "The whole Orders table is loaded and the filter runs in memory",
       "EF Core throws because Where cannot accept a lambda on IEnumerable",
       "Only the first matching row is loaded"],
      [1],
      "Look at the static type of the variable q.",
      "Typing the variable as IEnumerable<Order> makes Where bind to Enumerable.Where, which takes a Func rather than an expression tree. The rest of the query becomes LINQ to Objects, so every row is fetched and filtered in memory. Keeping IQueryable would translate the predicate to SQL.",
      r'''IEnumerable<Order> q = db.Orders;
var big = q.Where(o => o.Total > 100).ToList();''')

    m(H, "EF Core",
      "What happens to the database when this code runs (default tracking behavior)?",
      ["The Price is updated because the entity was loaded from the context",
       "Nothing is written: the entity is not tracked so SaveChanges sees no changes",
       "SaveChangesAsync throws InvalidOperationException because the entity is untracked",
       "A new row is inserted with the new price"],
      [1],
      "What does AsNoTracking skip?",
      "AsNoTracking returns entities that are not attached to the change tracker, so modifying them is invisible to SaveChanges. No exception is thrown and nothing is inserted. You would need Update/Attach to persist the change.",
      r'''var p = await db.Products.AsNoTracking().FirstAsync();
p.Price = 10m;
await db.SaveChangesAsync();''')

    m(H, "EF Core",
      "With lazy-loading proxies enabled and Customer declared as a virtual navigation property, how many SQL queries does this code run for 50 orders?",
      ["1", "2", "51", "50"],
      [2],
      "One query for the list plus one per navigation access.",
      "ToList issues one query for the orders, and the first access to each o.Customer triggers a separate lazy-load query, giving 1 + N = 51 (fewer if customers repeat, since the context caches already loaded ones, but the worst case is 51). This is the classic N+1 problem, fixed with Include or a projection.",
      r'''foreach (var o in db.Orders.ToList())
    Console.WriteLine(o.Customer.Name);''')

    m(H, "EF Core",
      "A query includes two sibling collection navigations (Include(a => a.Orders).Include(a => a.Addresses)) and returns far more rows than expected, causing slow performance. Which approaches mitigate this cartesian explosion?" + MS,
      ["Use AsSplitQuery()", "Use AsNoTracking()", "Load each collection with a separate query", "Call ToList() before Include"],
      [0, 2],
      "The problem is the single JOINed result set.",
      "Multiplying child collections in one JOIN duplicates parent data; AsSplitQuery or manually separate queries avoid it. AsNoTracking affects tracking only, and calling ToList first would make Include unavailable on the in-memory list.")

    m(H, "EF Core",
      "Which of these calls return entity instances that are tracked by the DbContext under default settings?" + MS,
      ["db.Products.ToList()", "db.Products.AsNoTracking().ToList()", "db.Products.Select(p => new { p.Id, p.Name }).ToList()", "db.Products.Find(1)"],
      [0, 3],
      "Anonymous types are not entities.",
      "ToList on a DbSet and Find both return tracked entities. AsNoTracking opts out, and a projection into an anonymous type yields no entity instances to track.")

    m(H, "EF Core",
      "What is the value of p.Price printed at the end?",
      ["The old price: ExecuteUpdate bypasses the change tracker so p is stale",
       "99, because EF Core refreshes tracked entities after ExecuteUpdate",
       "It throws because p is tracked",
       "0"],
      [0],
      "Does set-based SQL know about objects already in memory?",
      "ExecuteUpdateAsync issues a direct UPDATE statement and does not touch tracked entities, so p keeps the value read earlier. The database has 99, but the in-memory object is stale until reloaded.",
      r'''var p = await db.Products.FirstAsync(x => x.Id == 1);
await db.Products.Where(x => x.Id == 1)
    .ExecuteUpdateAsync(s => s.SetProperty(x => x.Price, 99m));
Console.WriteLine(p.Price);''')

    m(H, "EF Core",
      "An entity has a [Timestamp] byte[] RowVersion property. Two users load the same row and both save changes. What happens to the second SaveChanges?",
      ["The second save silently overwrites the first", "It throws DbUpdateConcurrencyException because the UPDATE matched 0 rows",
       "It throws only when both users edit the same column", "EF Core automatically merges both changes"],
      [1],
      "The RowVersion is part of the UPDATE's WHERE clause.",
      "EF Core adds the original RowVersion to the WHERE clause, so after the first save changes the version, the second UPDATE affects zero rows and EF raises DbUpdateConcurrencyException. It does not compare columns individually or merge changes.")

    m(H, "EF Core",
      "What is the result of running this code with a single DbContext instance?",
      ["Both counts run in parallel and complete normally",
       "InvalidOperationException because a second operation was started on the context before the first completed",
       "The second query is automatically queued by the context",
       "A DbUpdateException is raised"],
      [1],
      "Is DbContext thread-safe?",
      "DbContext does not support multiple concurrent operations; EF Core detects this and throws InvalidOperationException. It does not queue requests. Use separate contexts (for example from IDbContextFactory) for parallel queries.",
      r'''var t1 = db.Orders.CountAsync();
var t2 = db.Customers.CountAsync();
await Task.WhenAll(t1, t2);''')

    m(H, "Async/await",
      "This method is called from a WinForms button click handler (UI thread with a SynchronizationContext). What happens?",
      ["It returns \"x\" after about 100 ms", "It deadlocks", "It throws InvalidOperationException for cross-thread access", "It returns null"],
      [1],
      "Who is blocked, and where does the continuation want to run?",
      "The UI thread blocks on .Result while the continuation after await Task.Delay needs to resume on that same UI thread, so neither can proceed. Using await up the call chain or ConfigureAwait(false) inside the helper avoids it.",
      r'''string Get() => GetAsync().Result;

async Task<string> GetAsync()
{
    await Task.Delay(100);
    return "x";
}''')

    m(H, "Async/await",
      "Which statements about async void methods are correct?" + MS,
      ["An exception thrown from one cannot be caught by a try/catch around the call",
       "Callers can await them to observe completion",
       "An unhandled exception in one can crash the process (for example in a console app)",
       "They are the recommended way to start general fire-and-forget work"],
      [0, 2],
      "There is no Task to carry the failure.",
      "async void has no Task, so exceptions are raised on the captured context or thread pool, bypassing the caller's catch and potentially terminating the process. It is meant for event handlers only, and it cannot be awaited.")

    m(H, "Async/await",
      "Which statements about Task.WhenAll are correct when several of the tasks fault?" + MS,
      ["await on the WhenAll task rethrows only the first exception",
       "All exceptions are available in whenAllTask.Exception.InnerExceptions",
       "It cancels the remaining tasks as soon as one faults",
       "It completes as soon as the first task faults"],
      [0, 1],
      "WhenAll waits for everyone.",
      "WhenAll completes only after all tasks finish, aggregating failures; await unwraps and rethrows just the first, and the full set lives in the AggregateException. It never cancels the other tasks.")

    m(H, "Async/await",
      "What is wrong with this method?",
      ["Nothing: ReadToEndAsync completes before the method returns",
       "The reader is disposed before the returned task completes, so the read can fail with ObjectDisposedException",
       "It does not compile because async is missing",
       "ReadToEndAsync cannot be used with using var"],
      [1],
      "When does the using scope end relative to the task?",
      "Without async/await the method returns the Task immediately, the using scope ends and disposes the reader while the read is still in flight. Making the method async and awaiting inside the using fixes it.",
      r'''Task<string> ReadAll(string path)
{
    using var reader = new StreamReader(path);
    return reader.ReadToEndAsync();
}''')

    m(H, "Async/await",
      "Which statements about ConfigureAwait(false) are correct?" + MS,
      ["In ASP.NET Core, omitting it in application code does not cause the classic sync-context deadlock",
       "It forces the awaited operation to run on a thread-pool thread",
       "Code after the await may run without the captured SynchronizationContext",
       "It suppresses exceptions from the awaited task"],
      [0, 2],
      "It controls only where the continuation resumes.",
      "ASP.NET Core has no SynchronizationContext, so blocking there does not deadlock in the classic way, and ConfigureAwait(false) simply says the continuation need not resume on the captured context. It does not change where the awaited operation itself runs and does not touch exceptions.")

    m(H, "Async/await",
      "Which statements about ValueTask<T> are correct?" + MS,
      ["Awaiting the same ValueTask instance twice is not supported",
       "Calling AsTask() once gives a Task that can be awaited multiple times",
       "Calling GetAwaiter().GetResult() on an incomplete ValueTask is a supported way to block",
       "Awaiting a ValueTask once directly is a valid usage"],
      [0, 1, 3],
      "A ValueTask may wrap a reusable pooled source.",
      "A ValueTask must be consumed once; converting with AsTask gives a normal reusable Task. Blocking on an incomplete ValueTask via GetResult is unsupported.")

    m(H, "Async/await",
      "What does this code print?",
      ["after caught", "caught", "after, then an unhandled exception", "It throws InvalidOperationException from the call F()"],
      [0],
      "Where does an async method store an exception thrown before its first await?",
      "In an async method, exceptions are captured in the returned Task, even when thrown before any await, so F() returns a faulted task. 'after' is printed first and await t then throws, which is caught.",
      r'''async Task F() { throw new InvalidOperationException("x"); }

Task t = F();
Console.Write("after ");
try { await t; }
catch (InvalidOperationException) { Console.Write("caught"); }''')

    m(H, "Async/await",
      "What is the main problem with this code?",
      ["Parallel.ForEach cannot take a lambda", "The async lambda becomes async void, so Parallel.ForEach returns before the work finishes and exceptions are lost",
       "The items are processed sequentially", "It deadlocks on the thread pool"],
      [1],
      "Which delegate type does Parallel.ForEach expect?",
      "Parallel.ForEach takes an Action<T>, so the async lambda is compiled as async void and is not awaited. The loop returns when the lambdas hit their first await. Parallel.ForEachAsync or Task.WhenAll should be used.",
      r'''Parallel.ForEach(items, async item => await ProcessAsync(item));
Console.WriteLine("done");''')

    m(H, "DI lifetimes",
      "A singleton service takes a scoped service in its constructor. Which statements are correct?" + MS,
      ["With scope validation on (default in Development) resolving it throws InvalidOperationException",
       "The scoped instance is recreated on every request even though the singleton exists",
       "With validation off, the scoped instance effectively lives as long as the singleton",
       "Registering the dependency as transient makes it per-request inside the singleton"],
      [0, 2],
      "The singleton is built only once.",
      "The singleton's constructor runs once, so it captures one scoped instance for its whole lifetime (a captive dependency); validation detects this. A transient injected into a singleton is also resolved once and kept.")

    m(H, "DI lifetimes",
      "Which statements about disposal in the built-in DI container are correct?" + MS,
      ["A transient IDisposable resolved from the root provider is held until the root provider is disposed",
       "Instances passed in via AddSingleton(instance) are not disposed by the container",
       "The container disposes transient instances immediately after each use",
       "Services created in a request scope are disposed when that scope is disposed"],
      [0, 1, 3],
      "The container disposes only what it created and tracks it.",
      "The container tracks disposable instances it creates and disposes them with their owning scope or root, which makes root-resolved transients a leak risk. It does not own instances you supply. It never disposes transients right after use.")

    m(H, "DI lifetimes",
      "Given these registrations, which statements are correct?" + MS,
      ["GetRequiredService<IFoo>() returns a B", "GetRequiredService<IFoo>() returns an A",
       "GetServices<IFoo>() enumerates A then B", "GetRequiredService<IFoo>() throws an ambiguity exception"],
      [0, 2],
      "The last registration wins for single resolution.",
      "For a single service the last registration wins, while IEnumerable<IFoo> contains all registrations in registration order. The container never throws for multiple registrations of the same service type.",
      r'''services.AddTransient<IFoo, A>();
services.AddTransient<IFoo, B>();''')

    m(H, "DI lifetimes",
      "A BackgroundService needs to use a scoped DbContext each time it processes a message. What is the correct approach?",
      ["Inject the DbContext in the constructor of the BackgroundService",
       "Register the BackgroundService as scoped",
       "Inject IServiceScopeFactory and create a scope per unit of work",
       "Resolve the DbContext from the root IServiceProvider and keep it"],
      [2],
      "Hosted services are singletons.",
      "Hosted services live for the app lifetime, so injecting a scoped service captures it forever. Creating a scope per unit of work gives a fresh DbContext that is disposed afterward. Resolving scoped services from the root provider is invalid or leaky.")

    m(H, "DI lifetimes",
      "What is returned by this code?",
      ["An instance of A", "An instance of B", "An InvalidOperationException because IFoo is registered twice", "null"],
      [0],
      "TryAdd checks for an existing registration.",
      "TryAddSingleton registers only when no registration for the service type already exists, so the earlier AddSingleton wins. B is never registered.",
      r'''services.AddSingleton<IFoo, A>();
services.TryAddSingleton<IFoo, B>();
var foo = services.BuildServiceProvider().GetRequiredService<IFoo>();''')

    m(H, "ASP.NET Core pipeline",
      "Which statements about middleware ordering are correct?" + MS,
      ["UseExceptionHandler should be registered early so it can catch exceptions from later middleware",
       "UseAuthorization must be registered before UseAuthentication",
       "UseAuthentication must be registered before UseAuthorization",
       "Static files middleware must always come after endpoint mapping"],
      [0, 2],
      "Authorization needs an identity to evaluate.",
      "Authorization relies on the user established by authentication, so authentication goes first. An exception handler only sees exceptions from middleware that runs after it. Static files typically come early and short-circuit.")

    m(H, "ASP.NET Core pipeline",
      "What is the response body of a request?",
      ["ABC", "ACB", "AB", "BAC"],
      [0],
      "Code after next() runs after later middleware complete.",
      "The first middleware writes A, awaits next which runs the terminal middleware writing B, and then writes C once control returns. The pipeline unwinds in reverse order, so the sequence is ABC.",
      r'''app.Use(async (ctx, next) =>
{
    await ctx.Response.WriteAsync("A");
    await next();
    await ctx.Response.WriteAsync("C");
});
app.Run(async ctx => await ctx.Response.WriteAsync("B"));''')

    m(H, "ASP.NET Core pipeline",
      "app.UseExceptionHandler(\"/error\") is called after a terminal app.Run(ctx => throw new Exception()). What happens when a request is made?",
      ["The exception handler catches it because it is registered", "The exception propagates to the server because the handler is never reached in the pipeline",
       "The handler runs only in the Development environment", "The request returns 404"],
      [1],
      "A terminal middleware never calls next.",
      "Middleware is a chain in registration order and an exception handler only catches exceptions thrown by components after it. Since app.Run is terminal and comes first, the later handler is never part of the executed path.")

    m(H, "ASP.NET Core pipeline",
      "Which statements about this middleware are correct?" + MS,
      ["Setting the header throws InvalidOperationException because the response has already started",
       "ctx.Response.HasStarted is true after the WriteAsync completes",
       "The header is silently ignored without any exception",
       "Headers are buffered until the middleware returns so the header is sent"],
      [0, 1],
      "Headers must be sent before the body.",
      "Once the body begins to flush, headers are sent and become read-only, so modifying them throws and HasStarted is true. Kestrel does not buffer headers until the middleware ends.",
      r'''app.Use(async (ctx, next) =>
{
    await ctx.Response.WriteAsync("hi");
    ctx.Response.Headers["X-Test"] = "1";
});''')

    m(H, "ASP.NET Core pipeline",
      "In a controller annotated with [ApiController], which statements about parameter binding and validation are correct?" + MS,
      ["A complex type parameter is inferred as [FromBody]",
       "Automatic HTTP 400 for invalid ModelState happens after the action body runs",
       "A simple-type parameter that is not in the route template is inferred as [FromQuery]",
       "Complex type parameters are inferred as [FromForm]"],
      [0, 2],
      "Binding source inference rules.",
      "ApiController infers FromBody for complex types and Route or Query for simple ones. Its validation filter short-circuits with 400 before the action executes. FromForm is inferred only for IFormFile types.")

    m(H, "ASP.NET Core pipeline",
      "With <Nullable>enable</Nullable> in a project using [ApiController], what happens when a POST body {} is bound to this DTO?",
      ["Name is null and the action runs normally", "A 400 response is returned automatically because non-nullable reference type properties are treated as [Required]",
       "A 500 NullReferenceException is thrown", "Name is set to an empty string"],
      [1],
      "Nullable annotations influence validation metadata.",
      "MVC treats non-nullable reference type properties as implicitly required, so the missing Name makes ModelState invalid and ApiController returns 400. This is by default and can be disabled.",
      r'''public class CreateUserDto
{
    public string Name { get; set; }
}''')

    m(H, "ASP.NET Core pipeline",
      "A singleton service must observe configuration values that change at runtime (reloadOnChange). Which type should it inject?",
      ["IOptions<T>", "IOptionsSnapshot<T>", "IOptionsMonitor<T>", "T directly via AddSingleton(T)"],
      [2],
      "One option type is registered as singleton and supports change notifications.",
      "IOptionsMonitor<T> is a singleton that always returns current values and offers OnChange. IOptions<T> is computed once, and IOptionsSnapshot<T> is scoped, so it cannot be injected into a singleton.")

    m(H, "HttpClient",
      "Why is creating a new HttpClient per request inside a using block discouraged in a long-running service?",
      ["HttpClient is not thread-safe", "It can exhaust sockets because disposed connections linger in TIME_WAIT, and the pool is not reused",
       "HttpClient cannot be disposed", "Each HttpClient allocates a new thread"],
      [1],
      "Think about connections, not threads.",
      "Each HttpClient with its own handler opens its own connections, which remain in TIME_WAIT after disposal and can exhaust sockets. HttpClient is safe for concurrent use, and IHttpClientFactory or a long-lived instance reuses the connection pool.")

    m(H, "Generics variance",
      "Which of these declarations compile?" + MS,
      ["IEnumerable<object> a = new List<string>();",
       "List<object> b = new List<string>();",
       "Action<string> c = new Action<object>(o => { });",
       "IList<object> d = new List<string>();"],
      [0, 2],
      "Only some interfaces/delegates have in or out type parameters.",
      "IEnumerable<out T> is covariant and Action<in T> is contravariant. List<T> is a class, and IList<T> is invariant because it both reads and writes T.")

    m(H, "Generics variance",
      "What happens at runtime?",
      ["It runs and stores 42 in arr[1]", "ArrayTypeMismatchException on the last line", "InvalidCastException on the first line", "It does not compile"],
      [1],
      "Array covariance is checked at runtime.",
      "string[] converts to object[] due to array covariance, but the runtime still verifies each store against the real element type. Storing an int throws ArrayTypeMismatchException.",
      r'''object[] arr = new string[2];
arr[0] = "a";
arr[1] = 42;''')

    m(H, "Generics variance",
      "Why does 'IEnumerable<object> e = new List<int>();' fail to compile?",
      ["IEnumerable<T> is invariant", "Variance only applies to reference-type arguments; int needs a boxing conversion, not a reference conversion",
       "List<int> does not implement IEnumerable", "object cannot be used as a type argument"],
      [1],
      "Variance requires an identity or reference conversion.",
      "Generic variance is allowed only when the type arguments are related by identity or reference conversion; int to object is a boxing conversion. IEnumerable<T> is covariant and List<int> does implement it.")

    m(H, "Generics variance",
      "Static counters on a generic class are incremented through different type arguments. What is printed?",
      ["2 1", "3 3", "1 1", "3 0"],
      [0],
      "Each closed generic type gets its own statics.",
      "Static fields are per constructed type, so C<int> and C<string> have separate Count fields. C<int>.Count is incremented twice and C<string>.Count once.",
      r'''class C<T> { public static int Count; }

C<int>.Count++;
C<string>.Count++;
C<int>.Count++;
Console.WriteLine($"{C<int>.Count} {C<string>.Count}");''')

    m(H, "Value vs reference",
      "What happens when the code assigns to a member of a struct element obtained through a List indexer?",
      ["It sets X to 5", "Compile error CS1612: cannot modify the return value because it is not a variable", "InvalidOperationException at runtime", "It sets X on a copy and silently does nothing"],
      [1],
      "What does the List indexer return for a struct element?",
      "The indexer returns a copy of the struct, so assigning to a member of that temporary is rejected by the compiler. Replace the element with a modified copy, or use CollectionsMarshal.AsSpan with ref access.",
      r'''struct Point { public int X; }

var list = new List<Point> { new Point() };
list[0].X = 5;''')

    m(H, "Value vs reference",
      "A mutating method is called on a readonly field holding a struct. What is printed?",
      ["0", "1", "It does not compile", "It throws"],
      [0],
      "Calling a method on a readonly field of struct type.",
      "Because the field is readonly, the call Inc() operates on a defensive copy of the struct, so the original N remains 0. Making Counter a readonly struct or the field non-readonly changes this.",
      r'''struct Counter { public int N; public void Inc() => N++; }
class Holder { public readonly Counter C = new Counter(); }

var h = new Holder();
h.C.Inc();
Console.WriteLine(h.C.N);''')

    m(H, "Value vs reference",
      "An int is boxed and the original variable is changed afterwards. What is printed after unboxing?",
      ["5", "10", "It does not compile", "It throws InvalidCastException"],
      [0],
      "Boxing copies the value.",
      "Boxing copies the int to the heap, so later changes to i do not affect the box. Unboxing yields the copied 5.",
      r'''int i = 5;
object o = i;
i = 10;
Console.WriteLine((int)o);''')

    m(H, "Value vs reference",
      "What does this code do?",
      ["Prints 5", "Throws InvalidCastException because unboxing requires the exact original type", "Prints 5 because int converts implicitly to long", "Does not compile"],
      [1],
      "Unboxing must match the boxed type.",
      "Unboxing is only allowed to the exact boxed type (or its nullable), so unboxing an int box as long throws. You need (long)(int)o instead.",
      r'''object o = 5;
long l = (long)o;
Console.WriteLine(l);''')

    m(H, "Value vs reference",
      "Which of these cause a boxing allocation?" + MS,
      ["string.Format(\"{0}\", 5)", "list.Add(1) where list is List<int>", "int i = 3; string s = i.ToString();", "object o = 3;"],
      [0, 3],
      "Where is a value type converted to object?",
      "The int is boxed to be passed in the object[] params array and assigned to object. List<int>.Add is generic over int, and int.ToString is called directly on the value without boxing.")

    m(H, "Value vs reference",
      "Two object-typed references hold equal string contents. What do == and Equals report?",
      ["True True", "False True", "True False", "False False"],
      [1],
      "== on two object-typed expressions is reference equality.",
      "With both operands typed as object, == compares references, and the two strings are different instances. Equals is virtual and string overrides it for value comparison.",
      r'''object a = "hi";
object b = new string(new[] { 'h', 'i' });
Console.WriteLine($"{a == b} {a.Equals(b)}");''')

    m(H, "Value vs reference",
      "Comparing string references: a literal, a constant concatenation and a runtime concatenation. What is printed?",
      ["True True", "True False", "False True", "False False"],
      [1],
      "Compile-time constants are interned; runtime concatenations are not.",
      "'hel' + 'lo' is folded to the literal 'hello' by the compiler, so it's the same interned reference. The runtime concatenation creates a new string instance, so ReferenceEquals is false.",
      r'''string s1 = "hello";
string s2 = "hel" + "lo";
string part = "hel";
string s3 = part + "lo";
Console.WriteLine(ReferenceEquals(s1, s2));
Console.WriteLine(ReferenceEquals(s1, s3));''')

    m(H, "Records/struct",
      "Two positional records hold different List<int> instances with the same contents. What does == print?",
      ["True", "False", "It does not compile", "It throws"],
      [1],
      "How does a record compare its members?",
      "The synthesized record equality compares each property with EqualityComparer<T>.Default, and List<int> uses reference equality. The two lists are different instances, so the records are not equal.",
      r'''record R(List<int> L);

var x = new R(new List<int> { 1 });
var y = new R(new List<int> { 1 });
Console.WriteLine(x == y);''')

    m(H, "Records/struct",
      "Which statements about records are correct?" + MS,
      ["A with-expression on a record class creates a shallow copy",
       "Records are always value types",
       "== on a record class compares members by value using the synthesized equality",
       "Positional properties of a record struct are init-only like a record class"],
      [0, 2],
      "Compare record class and record struct defaults.",
      "A with-expression copies the object and reference-type members are shared, and the synthesized operator == compares members. Records may be classes or structs, and positional record struct properties are mutable by default.")

    m(H, "Span/ref",
      "What happens when a Span<int> local is used after an await in an async method?",
      ["It compiles and runs", "It does not compile: a ref struct (Span<int>) cannot be used across an await", "It throws at runtime", "It compiles but s becomes empty after the await"],
      [1],
      "Async state machines are heap-allocated classes/structs.",
      "A ref struct must live on the stack, but locals that span an await are hoisted into the state machine. The compiler rejects using the Span after the await. Using it before the await only, or Memory<T>, is fine.",
      r'''async Task F()
{
    Span<int> s = new int[4];
    await Task.Delay(1);
    s[0] = 1;
}''')

    m(H, "Span/ref",
      "A span slice and a range-sliced array are each modified. What is printed?",
      ["99 3", "99 77", "2 3", "1 3"],
      [0],
      "One slice shares memory and the other copies.",
      "AsSpan creates a view into the same array so s[0] = 99 changes a[1]. The range a[1..3] on an array copies the elements, so changing b does not affect a.",
      r'''int[] a = { 1, 2, 3, 4 };
Span<int> s = a.AsSpan(1, 2);
s[0] = 99;
int[] b = a[1..3];
b[1] = 77;
Console.WriteLine($"{a[1]} {a[2]}");''')

    m(H, "Span/ref",
      "A ref local is taken to an array element and the array variable is then reassigned. What is printed?",
      ["10 10", "7 10", "10 7", "7 7"],
      [1],
      "A ref local aliases a specific storage location.",
      "The ref local points at the first element of the original array, and reassigning arr does not retarget it. Writing through r modifies the old array while arr[0] reads from the new one.",
      r'''int[] arr = { 1, 2, 3 };
ref int r = ref arr[0];
arr = new[] { 7, 8, 9 };
r = 10;
Console.WriteLine($"{arr[0]} {r}");''')

    m(H, "Threading",
      "Which are poor choices as a lock target?" + MS,
      ["lock (this)", "lock (typeof(Foo))", "lock (\"gate\")", "lock (_gate) where _gate is a private readonly object"],
      [0, 1, 2],
      "Outside code can reach these objects too.",
      "Publicly reachable objects such as this, Type objects and interned string literals can be locked by unrelated code, creating deadlocks. A private dedicated object cannot.")

    m(H, "Threading",
      "Which approaches make this counter update thread-safe?" + MS,
      ["Interlocked.Increment(ref counter)", "Declaring the field volatile and using counter++", "lock (_gate) { counter++; }", "Making the field static"],
      [0, 2],
      "Read-modify-write needs to be atomic.",
      "Interlocked and lock make the read-modify-write atomic. volatile gives visibility and ordering guarantees only, and static says nothing about atomicity.")

    m(H, "Threading",
      "Which statements about ConcurrentDictionary.GetOrAdd(key, valueFactory) are correct?" + MS,
      ["The valueFactory can be invoked more than once for the same key under contention",
       "Only one value is stored, and all callers get the stored one",
       "The valueFactory is executed while holding the dictionary's lock",
       "The valueFactory is guaranteed to run exactly once per key"],
      [0, 1],
      "The factory is invoked outside of the internal locks.",
      "Competing threads may each run the factory, but only one result wins and is returned to everyone. The factory runs outside the lock, so it needs to be side-effect free. Wrap values in Lazy<T> for single execution.")

    m(H, "Threading",
      "Which statements are correct?" + MS,
      ["Using await inside a lock statement body is a compile-time error",
       "SemaphoreSlim.WaitAsync can be used to guard async critical sections",
       "lock (Monitor) is reentrant for the same thread",
       "SemaphoreSlim(1,1) is reentrant for the same thread"],
      [0, 1, 2],
      "Locks are tied to thread ownership.",
      "A lock body can't contain await because the continuation might resume on another thread, so use SemaphoreSlim.WaitAsync. Monitor-based lock is reentrant but SemaphoreSlim is not, so recursive waits would deadlock.")

    m(H, "Threading",
      "An AsyncLocal value is changed inside Task.Run. What does the caller read afterwards?",
      ["1", "2", "0", "It throws"],
      [0],
      "AsyncLocal values flow downwards via ExecutionContext copies.",
      "Task.Run captures a copy of the ExecutionContext, so changes made inside the child do not flow back to the caller. The parent still sees 1.",
      r'''static readonly AsyncLocal<int> V = new();

static async Task Main()
{
    V.Value = 1;
    await Task.Run(() => { V.Value = 2; });
    Console.WriteLine(V.Value);
}''')

    m(H, "Memory/GC",
      "What is the main effect of giving a class a finalizer on its garbage collection?",
      ["Instances are collected faster", "Instances survive at least one extra GC because they must be queued for finalization first",
       "The finalizer runs immediately when the last reference is dropped", "Instances are allocated on the LOH"],
      [1],
      "The GC cannot reclaim the memory until the finalizer has run.",
      "Finalizable objects are registered, and when found unreachable they are promoted to the f-reachable queue to run their finalizer, delaying reclamation. GC.SuppressFinalize in Dispose removes this cost. Finalizers do not run immediately.")

    m(H, "Memory/GC",
      "A short-lived view model subscribes to a static event with 'Publisher.Changed += OnChanged;' and never unsubscribes. What is the effect?",
      ["Nothing; the GC ignores event subscriptions", "The view model stays reachable via the static event's delegate list, causing a memory leak",
       "The subscription is automatically removed when the view model goes out of scope", "The event raises ObjectDisposedException"],
      [1],
      "Who holds a reference to whom?",
      "The delegate stored in the static event references the view model instance, keeping it reachable from a GC root. Unsubscribe or use weak events.")

    m(H, "Memory/GC",
      "Which statements about the Large Object Heap (LOH) are correct?" + MS,
      ["Objects of 85,000 bytes or more are allocated on the LOH",
       "The LOH is collected only as part of a generation 2 collection",
       "The LOH is compacted on every collection by default",
       "LOH objects start in generation 0 and are promoted"],
      [0, 1],
      "Large objects are treated as part of gen 2.",
      "Large objects go to the LOH, which is logically part of gen 2 so it is collected only with a full GC. It is not compacted by default and objects are not allocated in gen 0.")

    m(H, "Memory/GC",
      "Two using declarations appear in a method body. In what order is output produced?",
      ["body a b", "body b a", "a b body", "b a body"],
      [1],
      "Using declarations dispose at the end of the enclosing scope in reverse order.",
      "A using declaration disposes at the end of the enclosing scope, so the body runs first. Disposal is in reverse order of declaration, b before a.",
      r'''class D : IDisposable
{
    readonly string n;
    public D(string n) => this.n = n;
    public void Dispose() => Console.Write(n + " ");
}

void M()
{
    using var a = new D("a");
    using var b = new D("b");
    Console.Write("body ");
}''')

    m(H, "Memory/GC",
      "Which statements about finalizers are correct?" + MS,
      ["They are not guaranteed to run when the process exits in .NET Core",
       "They run on the thread that dropped the last reference",
       "The order in which finalizers run across objects is not guaranteed",
       "They run immediately when the object becomes unreachable"],
      [0, 2],
      "A dedicated thread runs finalizers.",
      "Finalizers run on a dedicated finalizer thread at an unspecified time, with no ordering guarantee, and .NET Core does not run them at shutdown. They are not immediate.")

    m(H, "Pattern matching",
      "A switch expression with guarded type, property and null patterns is called with four values. What is printed?",
      ["big,int,empty,null", "big,int,empty,other", "int,int,empty,null", "big,int,empty, followed by an exception"],
      [0],
      "Arms are evaluated top to bottom.",
      "11 matches the guarded int arm, 7 falls to the plain int arm, the empty string matches the property pattern, and null matches the null pattern since a type pattern never matches null.",
      r'''string Describe(object o) => o switch
{
    int i when i > 10 => "big",
    int => "int",
    string { Length: 0 } => "empty",
    null => "null",
    _ => "other"
};

Console.WriteLine(string.Join(",", Describe(11), Describe(7), Describe(""), Describe(null)));''')

    m(H, "Pattern matching",
      "What is the behavior of N(Color.Blue)?",
      ["Returns null", "Returns an empty string", "Throws SwitchExpressionException at runtime, with a compiler warning for non-exhaustiveness", "Compile error"],
      [2],
      "Switch expressions must produce a value.",
      "Missing enum cases produce warning CS8509, and when no arm matches at runtime a SwitchExpressionException is thrown. It is not a compile error and no default value is produced.",
      r'''enum Color { Red, Green, Blue }

static string N(Color c) => c switch
{
    Color.Red => "r",
    Color.Green => "g"
};

Console.WriteLine(N(Color.Blue));''')

    m(H, "Pattern matching",
      "For int[] a = { 1, 2, 3 }, which expressions evaluate to true?" + MS,
      ["a is [1, .., 3]", "a is [_, _]", "a is [1, 2, 3, ..]", "a is [.., 2]"],
      [0, 2],
      "A slice pattern can match zero elements.",
      "[1, .., 3] matches first and last, and [1, 2, 3, ..] matches with an empty slice. [_, _] requires exactly two elements and [.., 2] requires the last element to be 2.")

    m(H, "Pattern matching",
      "A class overloads == to always return true. What do 'p == null' and 'p is null' print?",
      ["True True", "True False", "False True", "False False"],
      [1],
      "Constant patterns do not call user-defined operators.",
      "p == null calls the overloaded operator, which always returns true here. 'is null' performs a direct null check and bypasses operator overloading, so it is false.",
      r'''class P
{
    public static bool operator ==(P a, P b) => true;
    public static bool operator !=(P a, P b) => false;
    public override bool Equals(object o) => true;
    public override int GetHashCode() => 0;
}

var p = new P();
Console.WriteLine($"{p == null} {p is null}");''')

    m(H, "LINQ deferred execution",
      "A captured local used in a Where predicate is changed before the query is enumerated. What is printed?",
      ["[ 3, 4 ]", "[ 4 ]", "[ 2, 3, 4 ]", "[ ]"],
      [1],
      "The lambda reads the captured variable when enumerated.",
      "The lambda captures the variable threshold, and the query only runs at ToList, after threshold is 3. Only 4 is greater than 3.",
      r'''int threshold = 2;
var nums = new[] { 1, 2, 3, 4 };
var q = nums.Where(x => x > threshold);
threshold = 3;
Console.WriteLine("[ " + string.Join(", ", q.ToList()) + " ]");''')

    m(H, "LINQ deferred execution",
      "Words are sorted by length with OrderBy. What order is printed?",
      ["a d bb cc", "bb cc a d", "d a bb cc", "a d cc bb"],
      [0],
      "LINQ OrderBy is a stable sort.",
      "OrderBy is stable, so elements with equal keys keep their original relative order: a before d, and bb before cc. An unstable sort like Array.Sort could reorder ties.",
      r'''var words = new[] { "bb", "a", "cc", "d" };
Console.WriteLine(string.Join(" ", words.OrderBy(w => w.Length)));''')

    m(H, "Exceptions",
      "Which statements are correct about rethrowing exceptions?" + MS,
      ["'throw;' preserves the original stack trace", "'throw ex;' preserves the original stack trace",
       "'throw ex;' resets the stack trace to the point of the rethrow",
       "ExceptionDispatchInfo.Capture(ex).Throw() preserves the original stack trace"],
      [0, 2, 3],
      "Only the bare form keeps the origin.",
      "A bare throw rethrows without altering the trace, and ExceptionDispatchInfo does the same from outside a catch. 'throw ex;' restarts the stack trace at that statement.")

    m(H, "Exceptions",
      "An exception filter, an inner finally and a catch all participate in one throw. What is the output order?",
      ["finally filter catch", "filter finally catch", "catch filter finally", "filter catch finally"],
      [1],
      "Exception filters run during the first pass, before unwinding.",
      "The runtime evaluates filters in a first pass before any finally block runs, then unwinds, running the inner finally, and finally enters the catch. So the output is 'filter finally catch'.",
      r'''static bool Log(Exception e) { Console.Write("filter "); return true; }

try
{
    try { throw new Exception("x"); }
    finally { Console.Write("finally "); }
}
catch (Exception e) when (Log(e))
{
    Console.Write("catch ");
}''')

    m(H, "Exceptions",
      "A static field initializer throws, and the field is read twice in separate try blocks. What is printed?",
      ["TypeInitializationException then TypeInitializationException", "Exception then TypeInitializationException",
       "TypeInitializationException then Exception", "Exception then Exception"],
      [0],
      "A failed type initializer leaves the type unusable.",
      "A static initializer failure is wrapped in TypeInitializationException, and the type remains permanently in a failed state, so later accesses throw it again.",
      r'''class Cfg
{
    public static readonly int V = Init();
    static int Init() => throw new Exception("boom");
}

try { _ = Cfg.V; } catch (Exception e) { Console.WriteLine(e.GetType().Name); }
try { _ = Cfg.V; } catch (Exception e) { Console.WriteLine(e.GetType().Name); }''')
