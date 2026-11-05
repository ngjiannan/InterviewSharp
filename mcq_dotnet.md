# .NET / C# MCQ practice (with answers)


## Easy

### 1. [C# basics] Which keyword declares a value that is fixed at compile time and cannot be changed afterward?

- A. readonly
- B. const
- C. static
- D. sealed

**Answer:** B

**Explanation:** const values are substituted at compile time and must be initialized with a constant expression. readonly fields can be assigned at declaration or in a constructor, so they are runtime constants. static and sealed do not make a value immutable.

### 2. [C# basics] What is the default value of an uninitialized bool field in a class?

- A. false
- B. true
- C. null
- D. It is a compile error to leave it uninitialized

**Answer:** A

**Explanation:** Class fields are automatically set to their default value, which is false for bool. bool is a value type so it cannot be null, and fields (unlike locals) do not need definite assignment.

### 3. [Strings] Which statement about System.String is true?

- A. It is a mutable value type
- B. It is a mutable reference type
- C. It is an immutable reference type
- D. It is an immutable value type

**Answer:** C

**Explanation:** string is a reference type whose instances cannot be modified after creation; operations return new strings. It is not a value type, and it is not mutable (that is StringBuilder's role).

### 4. [Collections] Which of the following collection types can grow and shrink dynamically?

- A. int[]
- B. string
- C. Span<int>
- D. List<int>

**Answer:** D

**Explanation:** List<T> manages a resizable internal array and offers Add/Remove. Arrays and Span<T> have a fixed length, and string is an immutable sequence of chars.

### 5. [Collections] What is the main purpose of Dictionary<TKey,TValue>.TryGetValue?

- A. To look up a key without throwing an exception when it is missing
- B. To add a key only if it is absent
- C. To remove a key and return its value
- D. To copy all keys into a list

**Answer:** A

**Explanation:** TryGetValue returns false and a default value when the key is missing, avoiding the KeyNotFoundException that the indexer would throw. Adding is done by Add/TryAdd and removal by Remove.

### 6. [OOP] Which of the following can a C# class do? (Select all that apply.)

- A. Inherit directly from two base classes
- B. Inherit from one base class
- C. Inherit from a struct
- D. Implement multiple interfaces

**Answer:** B, D

**Explanation:** A class has exactly one base class (System.Object by default) and may implement any number of interfaces. Multiple class inheritance is not supported, and structs cannot be base types.

### 7. [Async/await] What does the await keyword do inside an async method?

- A. Blocks the current thread until the task completes
- B. Starts a new thread for the awaited call
- C. Asynchronously suspends the method until the awaited task completes, without blocking the thread
- D. Converts the method to run synchronously

**Answer:** C

**Explanation:** await registers the rest of the method as a continuation and returns control to the caller if the task is not complete. It does not block and does not itself create a thread.

### 8. [Async/await] Which return type should an async method normally use when it produces no value?

- A. void
- B. Task
- C. bool
- D. object

**Answer:** B

**Explanation:** Task lets callers await the method and observe exceptions. async void is reserved for event handlers because errors cannot be caught by the caller. bool and object imply a result that is not produced.

### 9. [LINQ] Which namespace must be imported to use LINQ extension methods such as Where and Select on collections?

- A. System.Linq
- B. System.Collections.Generic
- C. System.Data
- D. System.Text

**Answer:** A

**Explanation:** Enumerable extension methods like Where and Select live in System.Linq. System.Collections.Generic holds the collection types, but not these query operators.

### 10. [Records] What do C# record types provide by default?

- A. Reference equality only
- B. Mandatory immutability of all fields
- C. Value-based equality and a generated ToString
- D. Automatic database mapping

**Answer:** C

**Explanation:** Records generate Equals/GetHashCode based on member values and a ToString that prints them. They are not forced to be immutable (positional properties are init-only, but you can add mutable ones) and have nothing to do with databases.

### 11. [Nullable reference types] With nullable reference types enabled, what does the declaration string? name mean?

- A. name is a value type
- B. name may hold null
- C. name can never be assigned
- D. name is lazily evaluated

**Answer:** B

**Explanation:** string? tells the compiler that null is an expected value, so it warns on unchecked dereference. Without the ? the compiler treats the variable as non-null. It does not change the runtime type.

### 12. [DI] In ASP.NET Core dependency injection, which lifetime creates a new instance every time the service is requested?

- A. Singleton
- B. Scoped
- C. Static
- D. Transient

**Answer:** D

**Explanation:** Transient services are created each time they are resolved. Singleton gives one instance per container and Scoped one per scope (usually per HTTP request). Static is not a DI lifetime.

### 13. [ASP.NET Core] Which file is the default place for application configuration settings in an ASP.NET Core project?

- A. appsettings.json
- B. web.xml
- C. Startup.config
- D. launch.cfg

**Answer:** A

**Explanation:** The default host loads appsettings.json plus appsettings.{Environment}.json. The other names are not used by default.

### 14. [Minimal APIs] What does app.MapGet("/hello", () => "Hi") do in a minimal API?

- A. Registers a handler for HTTP POST requests to /hello
- B. Registers a middleware that runs for every request
- C. Registers a handler for HTTP GET requests to /hello
- D. Reads a value from configuration

**Answer:** C

**Explanation:** MapGet creates an endpoint that responds to GET requests on the given route pattern. Handlers for POST use MapPost, and middleware is registered with Use/Run.

### 15. [EF Core] In EF Core, what does a DbContext represent?

- A. A single table row
- B. A session with the database used to query and save entities
- C. A SQL Server login
- D. A database migration

**Answer:** B

**Explanation:** DbContext is the main class for interacting with the database: it tracks entities, runs queries and saves changes. A table row is an entity instance and a migration is a schema change script.

### 16. [EF Core] In EF Core, what does a DbSet<TEntity> property on a DbContext represent?

- A. A connection string
- B. A transaction
- C. A queryable collection of entities of type TEntity, usually mapped to a table
- D. A migration history

**Answer:** C

**Explanation:** DbSet<T> exposes the set of entities for querying and adding/removing. It is not a connection or transaction, although it is used within them.

### 17. [Exceptions] When does the code in a finally block run?

- A. Only when an exception is thrown
- B. Only when no exception is thrown
- C. Only if there is a catch block
- D. Whether or not an exception occurs

**Answer:** D

**Explanation:** finally runs after the try (and any catch) completes, regardless of whether an exception was thrown. It does not require a catch block; try/finally is valid on its own.

### 18. [Delegates/events] What does the delegate type Func<int, string> represent?

- A. A method that takes an int and returns a string
- B. A method that takes a string and returns an int
- C. A method that takes an int and returns nothing
- D. A property of type int

**Answer:** A

**Explanation:** Func<TArg, TResult> has the result type last, so this is int -> string. A method returning nothing would be Action<int>.

### 19. [Generics] What does the constraint where T : class mean on a generic type parameter?

- A. T must be a struct
- B. T must be a reference type
- C. T must be a class declared in the same assembly
- D. T must be abstract

**Answer:** B

**Explanation:** where T : class restricts T to reference types (classes, interfaces, delegates, arrays). Value types use where T : struct. It says nothing about assembly or being abstract.

### 20. [OOP] Which keyword does a derived class use to replace the implementation of a virtual method of its base class?

- A. new
- B. sealed
- C. override
- D. abstract

**Answer:** C

**Explanation:** override provides a new implementation for a virtual member and participates in polymorphic dispatch. new merely hides the member, and sealed/abstract serve other purposes.

### 21. [OOP] What does marking a class as sealed do?

- A. Prevents other classes from inheriting from it
- B. Prevents creating instances of it
- C. Makes all its members static
- D. Makes it thread-safe

**Answer:** A

**Explanation:** A sealed class cannot be used as a base class. It can still be instantiated (that is what abstract prevents) and its members are unaffected.

### 22. [C# basics] What is true about a local variable declared with var?

- A. Its type is determined at run time
- B. It can hold any type and change type later
- C. It must be a reference type
- D. Its type is inferred by the compiler at compile time

**Answer:** D

**Explanation:** var asks the compiler to infer the static type from the initializer, so the variable has a fixed type afterward. It is not dynamic and works for value types too.

### 23. [Strings] What is the output of this string interpolation example?

```
int x = 5;
Console.WriteLine($"x = {x}");
```

- A. x = {x}
- B. x = x
- C. $x = 5
- D. x = 5

**Answer:** D

**Explanation:** String interpolation replaces {x} with the value of the variable, so the output is x = 5. Without the $ prefix the braces would be printed literally.

### 24. [C# basics] What is printed by this integer arithmetic?

```
Console.WriteLine(10 / 4 + " " + 10 % 4);
```

- A. 2.5 2
- B. 3 2
- C. 2 1
- D. 2 2

**Answer:** D

**Explanation:** Integer division truncates, so 10 / 4 is 2, and 10 % 4 is the remainder 2. Concatenation with a string yields "2 2". 2.5 would need a double operand.

### 25. [C# basics] What is printed when the ?? operator is applied to a null string?

```
string s = null;
Console.WriteLine(s ?? "none");
```

- A. (an empty line)
- B. null
- C. none
- D. It throws NullReferenceException

**Answer:** C

**Explanation:** The null-coalescing operator returns the right operand when the left one is null, so "none" is printed. Console.WriteLine(null string) would print an empty line, but that is not what happens here.

### 26. [LINQ] What does this Where/Select pipeline print?

```
var r = new[] { 1, 2, 3, 4 }.Where(n => n % 2 == 0).Select(n => n * n);
Console.WriteLine(string.Join(",", r));
```

- A. 4,16
- B. 2,4
- C. 1,4,9,16
- D. 2,4,16

**Answer:** A

**Explanation:** Where keeps the even numbers 2 and 4, and Select squares them to 4 and 16. The result is joined as 4,16. 2,4 would be the filter alone.

### 27. [C# basics] Which of the following are value types in C#? (Select all that apply.)

- A. int
- B. List<int>
- C. DateTime
- D. string

**Answer:** A, C

**Explanation:** int and DateTime are structs and therefore value types. string and List<int> are classes (reference types), even though string has value-like equality.

### 28. [OOP] Which of the following are valid C# access modifiers? (Select all that apply.)

- A. public
- B. internal
- C. package
- D. protected
- E. friend

**Answer:** A, B, D

**Explanation:** public, internal and protected are all C# access modifiers (along with private, protected internal and private protected). friend is C++/VB and package is Java.

### 29. [DI] Which of the following are service lifetimes supported by the built-in ASP.NET Core DI container? (Select all that apply.)

- A. Singleton
- B. Transient
- C. Scoped
- D. Static

**Answer:** A, B, C

**Explanation:** The built-in container supports Singleton, Scoped and Transient. Static is a C# modifier but not a DI lifetime.

### 30. [Minimal APIs] Which of these are real endpoint-mapping methods for minimal APIs? (Select all that apply.)

- A. MapGet
- B. MapFetch
- C. MapPost
- D. MapDelete

**Answer:** A, C, D

**Explanation:** MapGet, MapPost, MapPut, MapDelete and MapPatch exist for the corresponding HTTP verbs. MapFetch is not a method; fetch is a JavaScript API.


## Medium

### 31. [Async/await] Why is async void generally discouraged outside of event handlers?

- A. It runs on a dedicated thread
- B. Callers cannot await it, and exceptions thrown inside cannot be caught by the caller
- C. It cannot contain await expressions
- D. It always executes synchronously

**Answer:** B

**Explanation:** An async void method gives the caller no Task, so completion cannot be awaited and unhandled exceptions are raised on the synchronization context, often crashing the process. It can contain await and does not use a special thread.

### 32. [Async/await] Two tasks passed to await Task.WhenAll(t1, t2) both fault with different exceptions. What does the await expression throw?

- A. An AggregateException containing both
- B. Only the first exception; the others are available on the WhenAll task's Exception property
- C. Nothing, because WhenAll swallows exceptions
- D. A TaskCanceledException

**Answer:** B

**Explanation:** await rethrows only the first inner exception for convenience. The task returned by WhenAll still exposes all exceptions through its Exception (AggregateException) property. Exceptions are not swallowed.

### 33. [Async/await] Which problems can result from blocking on an asynchronous operation with task.Result or task.Wait()? (Select all that apply.)

- A. Deadlocks in environments that have a synchronization context
- B. Thread-pool threads are tied up, which can cause starvation under load
- C. Exceptions are wrapped in an AggregateException
- D. The awaited task is executed twice

**Answer:** A, B, C

**Explanation:** Blocking holds a thread while waiting, so many concurrent requests can starve the pool. Result/Wait wrap failures in AggregateException, and where a SynchronizationContext exists (UI apps, classic ASP.NET) the continuation may need the blocked thread, causing a deadlock. The task is never run twice.

### 34. [Async/await] What does this program print?

```
static async Task Main()
{
    var t = DoAsync();
    Console.WriteLine("A");
    await t;
}

static async Task DoAsync()
{
    Console.WriteLine("B");
    await Task.Delay(100);
    Console.WriteLine("C");
}
```

- A. A B C
- B. B C A
- C. B A C
- D. A C B

**Answer:** C

**Explanation:** DoAsync starts running immediately on the calling thread and prints B, then reaches the await on Task.Delay and returns an incomplete task. The caller prints A, then awaits and C is printed after the delay.

### 35. [Async/await] Which statements about cancellation with CancellationToken are true? (Select all that apply.)

- A. Task.Delay(1000, token) completes as canceled if the token is canceled during the delay
- B. Cancellation is cooperative: the code must observe the token
- C. Calling Cancel() immediately aborts the running thread
- D. token.ThrowIfCancellationRequested() throws OperationCanceledException when cancellation was requested

**Answer:** A, B, D

**Explanation:** Cancellation never forcibly aborts a thread; code must check the token or pass it to APIs that do. ThrowIfCancellationRequested throws OperationCanceledException, and Task.Delay with a token ends in the canceled state (awaiting it throws TaskCanceledException, a subclass).

### 36. [Async/await] Each call to FetchAsync takes about one second and the three calls are independent. About how long does this loop take?

```
var ids = new[] { 1, 2, 3 };
foreach (var id in ids)
{
    await FetchAsync(id);
}
```

- A. About 1 second, because await runs them in parallel
- B. About 3 seconds, because each call is awaited before the next starts
- C. About 0 seconds, because nothing is awaited
- D. It deadlocks

**Answer:** B

**Explanation:** Awaiting inside the loop starts the next call only after the previous one finishes, so the calls run sequentially (~3 s). To run them concurrently you would start all tasks first and then await Task.WhenAll.

### 37. [LINQ] What does this deferred-execution query print?

```
var list = new List<int> { 1, 2, 3 };
var q = list.Where(x => x > 1);
list.Add(4);
Console.WriteLine(q.Count());
```

- A. 2
- B. 4
- C. It throws InvalidOperationException
- D. 3

**Answer:** D

**Explanation:** Where is deferred, so the query runs when Count() is called, after 4 was added. The elements greater than 1 are 2, 3 and 4, giving 3. Modifying the list does not throw here because it is not being enumerated at that time.

### 38. [LINQ] For the sequence { 1, 2 }, which calls throw InvalidOperationException? (Select all that apply.)

- A. seq.Single()
- B. seq.SingleOrDefault()
- C. seq.First()
- D. seq.FirstOrDefault()

**Answer:** A, B

**Explanation:** Single and SingleOrDefault throw when more than one element exists (SingleOrDefault only tolerates zero). First and FirstOrDefault simply return the first element.

### 39. [LINQ] What does this SelectMany query print?

```
var r = new[] { "a b", "c" }.SelectMany(s => s.Split(' '));
Console.WriteLine(string.Join("|", r));
```

- A. a b|c
- B. ab|c
- C. a|b|c
- D. System.String[]

**Answer:** C

**Explanation:** Each string is split into an array, and SelectMany flattens the arrays into a single sequence a, b, c. Select would yield two arrays instead.

### 40. [LINQ] What does this code print (one item per line)?

```
var g = new[] { "apple", "avocado", "banana" }.GroupBy(s => s[0]);
foreach (var x in g)
    Console.WriteLine($"{x.Key}:{x.Count()}");
```

- A. a:2 then b:1
- B. a:1 then b:1
- C. a:3
- D. a:2, a:2 then b:1

**Answer:** A

**Explanation:** GroupBy groups by first character: apple and avocado share 'a' (count 2) and banana is alone under 'b'. Groups appear in order of first occurrence.

### 41. [LINQ] What does this OrderBy query print?

```
var r = new[] { "bb", "a", "cc", "d" }.OrderBy(s => s.Length);
Console.WriteLine(string.Join(",", r));
```

- A. bb,cc,a,d
- B. d,a,cc,bb
- C. a,bb,cc,d
- D. a,d,bb,cc

**Answer:** D

**Explanation:** Items are ordered by length ascending; OrderBy is stable, so equal-length items keep their original relative order (a before d, bb before cc).

### 42. [Collections] What does this dictionary indexer code print?

```
var d = new Dictionary<string, int>();
d["a"] = 1;
d["a"] = 2;
Console.WriteLine(d.Count + " " + d["a"]);
```

- A. 2 1
- B. 2 2
- C. 1 2
- D. It throws ArgumentException

**Answer:** C

**Explanation:** Assigning through the indexer adds or replaces, so the dictionary holds one entry with value 2. Only Add would throw ArgumentException for a duplicate key.

### 43. [Collections] What happens if you call list.Remove(x) inside a foreach over the same List<T>?

- A. The item is removed and enumeration continues safely
- B. The next MoveNext throws InvalidOperationException because the collection was modified
- C. The loop silently stops
- D. A compile-time error occurs

**Answer:** B

**Explanation:** List<T>'s enumerator detects structural modification and throws InvalidOperationException on the next iteration. Iterate over a copy or use RemoveAll to avoid this.

### 44. [Collections] Which of these types are safe for concurrent reads and writes from multiple threads without external locking? (Select all that apply.)

- A. List<T>
- B. ConcurrentDictionary<TKey,TValue>
- C. ConcurrentQueue<T>
- D. Dictionary<TKey,TValue>

**Answer:** B, C

**Explanation:** The collections in System.Collections.Concurrent are designed for thread-safe use. List<T> and Dictionary<TKey,TValue> are not safe for concurrent writes.

### 45. [OOP] What does this virtual/override call print?

```
class A { public virtual string N() => "A"; }
class B : A { public override string N() => "B"; }

A a = new B();
Console.WriteLine(a.N());
```

- A. A
- B. AB
- C. It does not compile
- D. B

**Answer:** D

**Explanation:** N is virtual and overridden, so the call through an A reference runs B's implementation, based on the object's runtime type.

### 46. [OOP] What does this method-hiding example print?

```
class A { public string N() => "A"; }
class B : A { public new string N() => "B"; }

A a = new B();
Console.WriteLine(a.N());
```

- A. A
- B. B
- C. AB
- D. It does not compile

**Answer:** A

**Explanation:** The method is not virtual, and new only hides the base member for callers using B. Because the variable's static type is A, A.N() is bound at compile time and returns "A".

### 47. [OOP] Which statements are true? (Select all that apply.)

- A. An abstract class can declare instance fields and constructors
- B. A class can implement several interfaces
- C. An abstract class can be instantiated directly with new
- D. An interface can declare instance fields

**Answer:** A, B

**Explanation:** Abstract classes can hold state and constructors (called by derived classes) and a class can implement many interfaces. Abstract classes cannot be instantiated directly, and interfaces cannot declare instance fields.

### 48. [OOP] What does this struct copy example print?

```
struct P { public int X; }

var a = new P { X = 1 };
var b = a;
b.X = 2;
Console.WriteLine(a.X);
```

- A. 1
- B. 2
- C. 0
- D. It does not compile

**Answer:** A

**Explanation:** struct is a value type, so var b = a copies the data and changing b.X does not affect a. With a class both variables would reference the same object and the output would be 2.

### 49. [Generics] What does the new() constraint on a type parameter allow?

- A. Calling any constructor with arguments
- B. Creating an instance with new T(), because T must have a public parameterless constructor
- C. Restricting T to value types
- D. Allowing T to be null

**Answer:** B

**Explanation:** where T : new() guarantees a public parameterless constructor so the generic code can write new T(). Constructors with arguments cannot be constrained this way.

### 50. [Generics] What does this generic Max call print?

```
static T Max<T>(T a, T b) where T : IComparable<T>
    => a.CompareTo(b) >= 0 ? a : b;

Console.WriteLine(Max("apple", "banana"));
```

- A. apple
- B. It does not compile
- C. It throws ArgumentException
- D. banana

**Answer:** D

**Explanation:** string satisfies IComparable<string>, T is inferred as string, and "apple".CompareTo("banana") is negative so b is returned.

### 51. [Generics] Which of these are valid generic constraints in C#? (Select all that apply.)

- A. where T : unmanaged
- B. where T : class
- C. where T : sealed
- D. where T : struct

**Answer:** A, B, D

**Explanation:** struct, class and unmanaged are valid constraints. sealed is a class modifier, not a constraint.

### 52. [Records] What does this record equality code print?

```
record P(string Name, int Age);

var a = new P("A", 1);
var b = new P("A", 1);
Console.WriteLine((a == b) + " " + ReferenceEquals(a, b));
```

- A. True True
- B. False False
- C. True False
- D. False True

**Answer:** C

**Explanation:** Records generate value-based == and Equals, so a == b is True, but they are still distinct objects so ReferenceEquals returns False.

### 53. [Records] What does this with-expression code print?

```
record P(string Name, int Age);

var a = new P("A", 1);
var b = a with { Age = 2 };
Console.WriteLine(a.Age + " " + b.Age);
```

- A. 1 1
- B. 2 2
- C. 1 2
- D. 2 1

**Answer:** C

**Explanation:** with creates a new record that is a copy of the original with the listed properties changed, leaving the original untouched, so a.Age is 1 and b.Age is 2.

### 54. [Records] For the declaration record P(string Name);, which statements are true? (Select all that apply.)

- A. ToString prints the member values
- B. Name is an init-only property, so it cannot be assigned after construction
- C. Equals compares the Name values
- D. P is a value type

**Answer:** A, B, C

**Explanation:** A positional record class gets value equality, a printing ToString and init-only properties. A record without struct is a reference type; record struct would be the value type.

### 55. [Nullable reference types] What is the effect of enabling nullable reference types in a project?

- A. Reference types can no longer hold null at run time
- B. The compiler produces nullability warnings; no runtime checks are added
- C. All strings become Nullable<string>
- D. Null dereferences throw a different exception

**Answer:** B

**Explanation:** Nullable reference types are annotations used by compiler flow analysis to warn about possible null dereferences. They do not change runtime behavior and string? is not Nullable<string>.

### 56. [Nullable reference types] What does the null-forgiving operator (!) do in expressions like user!.Name?

- A. Throws if user is null
- B. Suppresses the compiler's nullable warning without any runtime null check
- C. Converts null to an empty object
- D. Makes user non-nullable at run time

**Answer:** B

**Explanation:** The ! operator tells the compiler to treat the expression as non-null; it emits no check, so a null value still causes NullReferenceException at the dereference.

### 57. [Nullable reference types] What does this null-conditional code print?

```
#nullable enable
string? s = null;
Console.WriteLine(s?.Length ?? -1);
```

- A. 0
- B. null
- C. -1
- D. It throws NullReferenceException

**Answer:** C

**Explanation:** s?.Length evaluates to a null int?, and ?? supplies -1. No exception occurs because of the null-conditional operator.

### 58. [Pattern matching] What does this switch expression print?

```
static string F(object o) => o switch
{
    int n when n > 10 => "big",
    int => "int",
    string s => s,
    null => "null",
    _ => "other"
};

Console.WriteLine(F(5) + F(50) + F(null));
```

- A. intbignull
- B. intintnull
- C. bigbignull
- D. othersbigother

**Answer:** A

**Explanation:** 5 is an int but fails the guard, so it matches the int arm; 50 matches the guarded arm and gives big; null matches the null arm.

### 59. [Pattern matching] What does this property pattern code print?

```
record P(string Name, int Age);

object o = new P("A", 20);
Console.WriteLine(o is P { Age: >= 18 });
```

- A. True
- B. False
- C. It does not compile
- D. It throws InvalidCastException

**Answer:** A

**Explanation:** o is P { Age: >= 18 } checks that o is a P and that its Age satisfies the relational pattern. The age is 20, so the result is True.

### 60. [Pattern matching] What happens when a switch expression receives a value that none of its arms match and there is no discard arm?

- A. It returns default
- B. It throws a SwitchExpressionException at run time
- C. It falls through to the next arm
- D. It silently returns null

**Answer:** B

**Explanation:** The compiler may warn the switch is not exhaustive, and if no arm matches at run time a SwitchExpressionException is thrown. There is no fall-through or default result.

### 61. [ASP.NET Core] Why does the order of middleware registration in Program.cs matter?

- A. Middleware executes in the order registered for requests, and in reverse order for responses
- B. Middleware always executes alphabetically
- C. Only the last registered middleware runs
- D. Order matters only in Production

**Answer:** A

**Explanation:** Each middleware decides whether to call the next one, and code after await next() runs on the way back. For example UseAuthentication must precede UseAuthorization.

### 62. [ASP.NET Core] What is the order of the console output for one request to this pipeline?

```
app.Use(async (ctx, next) =>
{
    Console.WriteLine("1 in");
    await next();
    Console.WriteLine("1 out");
});

app.Run(async ctx =>
{
    Console.WriteLine("handler");
    await ctx.Response.WriteAsync("hi");
});
```

- A. 1 in, handler, 1 out
- B. handler, 1 in, 1 out
- C. 1 in, 1 out, handler
- D. 1 in, handler

**Answer:** A

**Explanation:** The Use middleware prints 1 in, calls next (reaching the terminal Run handler which prints handler), then resumes and prints 1 out.

### 63. [ASP.NET Core] Which of the following are valid ways to implement middleware? (Select all that apply.)

- A. A class with a RequestDelegate constructor parameter and an Invoke/InvokeAsync(HttpContext) method
- B. A class decorated with a [Middleware] attribute
- C. Inline with app.Use(async (ctx, next) => ...)
- D. A class implementing IMiddleware

**Answer:** A, C, D

**Explanation:** Inline delegates, conventional middleware classes and IMiddleware implementations are all supported. There is no [Middleware] attribute.

### 64. [ASP.NET Core] In conventional (convention-based) middleware, where should you inject a scoped service such as a DbContext?

- A. In the constructor
- B. As a parameter of the InvokeAsync method
- C. In a static field
- D. It cannot be injected

**Answer:** B

**Explanation:** Conventional middleware is constructed once, so constructor dependencies behave as singletons. Scoped services should be taken as InvokeAsync parameters, which are resolved per request.

### 65. [ASP.NET Core] Where in the pipeline should exception-handling middleware such as UseExceptionHandler normally be placed?

- A. As early as possible so it wraps later middleware
- B. After UseEndpoints
- C. Last, after all other middleware
- D. It must be inside every controller

**Answer:** A

**Explanation:** Middleware wraps the ones registered after it, so the exception handler should be registered first to catch their exceptions.

### 66. [ASP.NET Core] Which statement about app.Run(...) is correct?

- A. It starts the web host
- B. It adds terminal middleware that does not call the next delegate
- C. It runs a handler only for POST requests
- D. It runs after the response is sent

**Answer:** B

**Explanation:** app.Run registers a terminal middleware, with no next parameter. app.Run() with no arguments starts the host, which is a different overload.

### 67. [ASP.NET Core] Which are benefits of using IHttpClientFactory instead of creating a new HttpClient for every request? (Select all that apply.)

- A. Handlers are recycled periodically so DNS changes are picked up
- B. Handlers are pooled, which avoids socket exhaustion
- C. It is required to call HTTPS endpoints
- D. HTTP calls become synchronous

**Answer:** A, B

**Explanation:** Creating many HttpClient instances can exhaust sockets, while a single static one can hold stale DNS. The factory manages pooled handlers with periodic recycling. It does not change sync behavior and HTTPS works without it.

### 68. [Configuration] By default in ASP.NET Core, which configuration source has the highest precedence when the same key is defined in several places?

- A. appsettings.json
- B. appsettings.Development.json
- C. Environment variables
- D. Command-line arguments

**Answer:** D

**Explanation:** The default order is appsettings.json, appsettings.{Environment}.json, user secrets (in Development), environment variables, then command-line arguments, and later providers win.

### 69. [Configuration] A singleton service must see updated settings after appsettings.json changes without restarting the app. Which options type is appropriate?

- A. IOptions<T>
- B. IOptionsSnapshot<T>
- C. IOptionsMonitor<T>
- D. A static field

**Answer:** C

**Explanation:** IOptionsMonitor<T> is a singleton that gives current values and change notifications. IOptions<T> is computed once, and IOptionsSnapshot<T> is scoped, so it cannot be injected into singletons.

### 70. [Configuration] How is the configuration key Logging:LogLevel:Default set through an environment variable?

- A. Logging:LogLevel:Default always works on every OS
- B. Logging__LogLevel__Default
- C. Logging.LogLevel.Default
- D. LOGGING-LOGLEVEL-DEFAULT

**Answer:** B

**Explanation:** A double underscore is translated into the configuration key separator by the environment variables provider. The colon form works only on some platforms.

### 71. [Logging] Why is logger.LogInformation("User {UserId} logged in", id) preferred over logger.LogInformation($"User {id} logged in")?

- A. Interpolation does not compile
- B. The message template keeps UserId as a structured property and avoids formatting work when the level is disabled
- C. Interpolation is slower only on Linux
- D. The template version writes to a file

**Answer:** B

**Explanation:** Named placeholders let providers capture values as structured data and format lazily. An interpolated string is built eagerly and loses the structure. Both compile.

### 72. [Logging] The minimum log level is Warning. Which of these calls produce output? (Select all that apply.)

- A. LogDebug
- B. LogWarning
- C. LogError
- D. LogInformation

**Answer:** B, C

**Explanation:** Only messages at or above the minimum level are written, so Warning and Error are output. Information and Debug are lower.

### 73. [Logging] What is the correct way to log an exception with its stack trace using ILogger?

- A. logger.LogError(ex.Message)
- B. logger.LogError(ex, "Failed to process order {OrderId}", id)
- C. logger.LogError("Failed: " + ex.ToString().Length)
- D. Console.WriteLine(ex)

**Answer:** B

**Explanation:** The overload taking Exception first lets providers record the full exception and details. Logging only Message loses the stack trace and Console.WriteLine bypasses the logging system.

### 74. [Minimal APIs] In app.MapGet("/users/{id}", (int id) => ...), where does id come from?

- A. The route value
- B. The request body
- C. A header
- D. A DI service

**Answer:** A

**Explanation:** A simple parameter whose name matches a route template segment is bound from the route. Complex types on POST are bound from the body and services from DI.

### 75. [Minimal APIs] In app.MapPost("/items", (Item item) => ...), where Item is a class, how is item bound?

- A. From the JSON request body
- B. From the query string
- C. From a route value
- D. From a cookie

**Answer:** A

**Explanation:** For POST/PUT/PATCH handlers, a complex type parameter that is not a registered service is bound from the JSON body. Use [FromQuery] etc. to override.

### 76. [DI] A singleton service takes a scoped service in its constructor. What happens when scope validation is enabled (default in Development)?

- A. It works and the scoped service is created per request
- B. The container throws InvalidOperationException when resolving
- C. The singleton becomes scoped
- D. The scoped service becomes transient

**Answer:** B

**Explanation:** Injecting a scoped service into a singleton is a captive dependency, as the scoped instance would live as long as the singleton. Scope validation detects it and throws.

### 77. [DI] What does this scoped-lifetime code print?

```
var services = new ServiceCollection();
services.AddScoped<Foo>();
var sp = services.BuildServiceProvider();

using var s1 = sp.CreateScope();
using var s2 = sp.CreateScope();
var a = s1.ServiceProvider.GetRequiredService<Foo>();
var b = s1.ServiceProvider.GetRequiredService<Foo>();
var c = s2.ServiceProvider.GetRequiredService<Foo>();
Console.WriteLine((a == b) + " " + (a == c));

class Foo { }
```

- A. True True
- B. False True
- C. False False
- D. True False

**Answer:** D

**Explanation:** Within the same scope the same instance is returned (a == b), but a different scope gets its own instance, so a == c is False.

### 78. [DI] IFoo is registered twice: AddTransient<IFoo, A>() then AddTransient<IFoo, B>(). What do GetRequiredService<IFoo>() and GetServices<IFoo>() return?

- A. Error for both calls because of ambiguity
- B. B for the single resolution; both A and B for the collection
- C. A for the single resolution; only B for the collection
- D. Both return a list of A and B

**Answer:** B

**Explanation:** The last registration wins for a single resolve, while resolving IEnumerable<IFoo> returns all registrations in order. There is no ambiguity error.

### 79. [DI] Which statements about service disposal in the built-in container are true? (Select all that apply.)

- A. Instances passed to AddSingleton(instance) are not disposed by the container
- B. IDisposable services created by the container are disposed when their scope or the provider is disposed
- C. Singleton services are disposed at the end of each request
- D. The container never disposes anything

**Answer:** A, B

**Explanation:** The container disposes what it creates, at the end of its owning scope or provider. Instances you supply yourself are left to you. Singletons live until the root provider is disposed.

### 80. [EF Core] Which techniques reduce overhead for a read-only query whose results will not be modified? (Select all that apply.)

- A. Projecting only the needed columns with Select()
- B. Calling SaveChanges() after the query
- C. AsNoTracking()
- D. Calling Include() for every navigation property

**Answer:** A, C

**Explanation:** AsNoTracking skips change tracking and identity resolution, and a projection fetches only the columns you need (projected non-entity results are not tracked at all). Loading every navigation does more work, and SaveChanges is irrelevant to reading.

### 81. [EF Core] What is the N+1 query problem in EF Core?

- A. One query to load the parent entities, plus one additional query per parent to load related data
- B. Running N queries in one transaction
- C. Using more than one DbContext
- D. Having N tables with one foreign key

**Answer:** A

**Explanation:** Iterating over parents and touching a navigation (e.g. with lazy loading) issues extra queries per item. Using Include or a projection loads everything in a few queries.

### 82. [EF Core] After loading a User entity and changing only its Name property, SaveChangesAsync is called. What SQL does EF Core generate?

```
var u = await db.Users.FirstAsync(x => x.Id == 1);
u.Name = "New";
await db.SaveChangesAsync();
```

- A. An INSERT of the whole entity
- B. An UPDATE that sets only the modified column(s)
- C. A DELETE followed by an INSERT
- D. No SQL because it only works with AsNoTracking

**Answer:** B

**Explanation:** Tracked entities have their property changes detected, and EF Core emits an UPDATE with only the modified columns. Tracking is what makes this possible; AsNoTracking would prevent it.

### 83. [EF Core] Which of these calls cause the query to be executed against the database immediately? (Select all that apply.)

- A. Where(x => x.Active)
- B. Select(x => x.Name)
- C. CountAsync()
- D. ToListAsync()

**Answer:** C, D

**Explanation:** ToListAsync and CountAsync materialize a result and run the query. Where and Select only compose a deferred IQueryable.

### 84. [EF Core] What is the default lifetime of a DbContext registered with AddDbContext, and why does it matter?

- A. Scoped; a DbContext is not thread-safe and should not be shared across concurrent requests
- B. Singleton; it caches data forever
- C. Transient; a new one per call
- D. Static; shared across the process

**Answer:** A

**Explanation:** AddDbContext registers it as scoped, so each request gets its own instance. DbContext is not thread-safe, so a singleton would break under concurrency.

### 85. [EF Core] A row has a rowversion/[Timestamp] concurrency token and another user updated it after you loaded it. What does SaveChanges do?

- A. Silently overwrites the other user's change
- B. Throws DbUpdateConcurrencyException
- C. Merges the changes automatically
- D. Rolls back the other user's update

**Answer:** B

**Explanation:** The UPDATE includes the original token in its WHERE clause, affects zero rows, and EF throws DbUpdateConcurrencyException. It does not merge or overwrite the other change.

### 86. [Exceptions] What does this try/catch/finally code print?

```
try
{
    Console.Write("T");
    throw new Exception();
}
catch
{
    Console.Write("C");
}
finally
{
    Console.Write("F");
}
Console.Write("E");
```

- A. TCE
- B. TFCE
- C. TCFE
- D. TCF

**Answer:** C

**Explanation:** T is written, the exception is caught (C), finally runs (F) and then execution continues after the try statement (E).

### 87. [Delegates/events] What does this event code print?

```
class Pub
{
    public event Action<string>? Raised;
    public void Fire() => Raised?.Invoke("hi");
}

var p = new Pub();
p.Raised += s => Console.Write(s);
p.Raised += s => Console.Write(s.ToUpper());
p.Fire();
```

- A. hi
- B. HI
- C. Nothing, because events need a null check
- D. hiHI

**Answer:** D

**Explanation:** Invoke calls all subscribed handlers in subscription order, so hi followed by HI is printed. The null-conditional Invoke handles the case of no subscribers.

### 88. [Delegates/events] What does this closure-in-a-for-loop code print?

```
var acts = new List<Action>();
for (int i = 0; i < 3; i++)
    acts.Add(() => Console.Write(i));
foreach (var a in acts) a();
```

- A. 012
- B. 123
- C. 333
- D. It throws

**Answer:** C

**Explanation:** A for loop declares a single i shared by all closures, which has the value 3 once the loop ends, so 333 is printed. A foreach iteration variable is per-iteration.

### 89. [Strings] What does this Substring and indexer code print?

```
Console.WriteLine("abc".Substring(1, 1) + "abc"[2]);
```

- A. bc
- B. b
- C. c
- D. It does not compile

**Answer:** A

**Explanation:** Substring(1, 1) is "b", and "abc"[2] is the char 'c'. Concatenating string and char gives "bc".

### 90. [Memory] Which restriction applies to Span<T>?

- A. It can only hold reference types
- B. It is a ref struct, so it cannot be a class field or be used across await in an async method
- C. It always allocates on the heap
- D. It can only be used with arrays

**Answer:** B

**Explanation:** Span<T> is a ref struct restricted to the stack, so it cannot be stored in a class field, boxed or kept across an await. It can wrap arrays, stack memory and native memory and works with any T.


## Hard

### 91. [Delegates/closures] A lambda increments a captured local and is invoked twice. What is the local's value afterwards?

```
int x = 0;
Func<int> next = () => ++x;
next();
next();
Console.WriteLine(x);
```

- A. 2
- B. It does not compile because lambdas cannot modify captured locals
- C. 0
- D. 1

**Answer:** A

**Explanation:** A closure captures the variable, not a copy of its value, so each call increments the same local. Lambdas are allowed to modify captured locals, so it does compile.

### 92. [Delegates/closures] Lambdas are added to a list inside a for loop and invoked afterwards. What is the output?

```
var actions = new List<Action>();
for (int i = 0; i < 3; i++) actions.Add(() => Console.Write(i + " "));
foreach (var a in actions) a();
```

- A. 0 1 2
- B. 3 3 3
- C. 2 2 2
- D. It does not compile because i is modified after capture

**Answer:** B

**Explanation:** A for loop declares a single loop variable shared by all iterations, and the lambdas capture that variable, not its value. By the time they run, i is 3. The 0 1 2 result would need a per-iteration copy such as 'int c = i;'.

### 93. [Delegates/closures] Lambdas are added to a list inside a foreach loop and invoked afterwards. What is the output?

```
var actions = new List<Action>();
foreach (var i in new[] { 0, 1, 2 }) actions.Add(() => Console.Write(i + " "));
foreach (var a in actions) a();
```

- A. 0 0 0
- B. It does not compile because the foreach variable is read-only inside lambdas
- C. 0 1 2
- D. 2 2 2

**Answer:** C

**Explanation:** Since C# 5 the foreach iteration variable is scoped inside the loop body, so each iteration gets a fresh variable that the lambda captures. Each action therefore remembers its own value. Capturing a for-loop counter behaves differently.

### 94. [LINQ deferred execution] An element is added to the list after the Where query is defined. What is printed?

```
var list = new List<int> { 1, 2, 3 };
var q = list.Where(x => x > 1);
list.Add(4);
Console.WriteLine(q.Count());
```

- A. 4
- B. It throws InvalidOperationException because the list was modified
- C. 2
- D. 3

**Answer:** D

**Explanation:** Where is lazy, so the query is evaluated when Count() enumerates it, after 4 has been added. The elements greater than 1 at that moment are 2, 3 and 4, giving 3. No exception occurs because the list is not modified during enumeration.

### 95. [LINQ deferred execution] How many times is the Select lambda executed, and what is printed?

```
int calls = 0;
var q = new[] { 1, 2, 3 }.Select(x => { calls++; return x * 2; });
var a = q.ToList();
var b = q.ToList();
Console.WriteLine(calls);
```

- A. 6
- B. 3
- C. 0
- D. 9

**Answer:** A

**Explanation:** Select is deferred and not cached, so each ToList call re-runs the lambda for all three elements, giving 6. 3 would be correct only if results were memoized, and nothing is memoized in LINQ to Objects.

### 96. [LINQ deferred execution] Which of these LINQ operators execute (enumerate the source) immediately when called, rather than deferring until the result is enumerated? (Select all that apply.)

- A. ToList()
- B. Where(...)
- C. OrderBy(...)
- D. Select(...)
- E. Count()

**Answer:** A, E

**Explanation:** ToList and Count produce a concrete result so they enumerate immediately. Where, Select and OrderBy return lazy sequences that do no work until enumerated.

### 97. [EF Core] A repository method is declared as below. How is the filter applied for a SQL provider?

```
IEnumerable<Order> q = db.Orders;
var big = q.Where(o => o.Total > 100).ToList();
```

- A. It is translated to a SQL WHERE clause because the source is a DbSet
- B. The whole Orders table is loaded and the filter runs in memory
- C. EF Core throws because Where cannot accept a lambda on IEnumerable
- D. Only the first matching row is loaded

**Answer:** B

**Explanation:** Typing the variable as IEnumerable<Order> makes Where bind to Enumerable.Where, which takes a Func rather than an expression tree. The rest of the query becomes LINQ to Objects, so every row is fetched and filtered in memory. Keeping IQueryable would translate the predicate to SQL.

### 98. [EF Core] What happens to the database when this code runs (default tracking behavior)?

```
var p = await db.Products.AsNoTracking().FirstAsync();
p.Price = 10m;
await db.SaveChangesAsync();
```

- A. A new row is inserted with the new price
- B. The Price is updated because the entity was loaded from the context
- C. Nothing is written: the entity is not tracked so SaveChanges sees no changes
- D. SaveChangesAsync throws InvalidOperationException because the entity is untracked

**Answer:** C

**Explanation:** AsNoTracking returns entities that are not attached to the change tracker, so modifying them is invisible to SaveChanges. No exception is thrown and nothing is inserted. You would need Update/Attach to persist the change.

### 99. [EF Core] With lazy-loading proxies enabled and Customer declared as a virtual navigation property, how many SQL queries does this code run for 50 orders?

```
foreach (var o in db.Orders.ToList())
    Console.WriteLine(o.Customer.Name);
```

- A. 50
- B. 1
- C. 2
- D. 51

**Answer:** D

**Explanation:** ToList issues one query for the orders, and the first access to each o.Customer triggers a separate lazy-load query, giving 1 + N = 51 (fewer if customers repeat, since the context caches already loaded ones, but the worst case is 51). This is the classic N+1 problem, fixed with Include or a projection.

### 100. [EF Core] A query includes two sibling collection navigations (Include(a => a.Orders).Include(a => a.Addresses)) and returns far more rows than expected, causing slow performance. Which approaches mitigate this cartesian explosion? (Select all that apply.)

- A. Load each collection with a separate query
- B. Use AsSplitQuery()
- C. Use AsNoTracking()
- D. Call ToList() before Include

**Answer:** A, B

**Explanation:** Multiplying child collections in one JOIN duplicates parent data; AsSplitQuery or manually separate queries avoid it. AsNoTracking affects tracking only, and calling ToList first would make Include unavailable on the in-memory list.

### 101. [EF Core] Which of these calls return entity instances that are tracked by the DbContext under default settings? (Select all that apply.)

- A. db.Products.Select(p => new { p.Id, p.Name }).ToList()
- B. db.Products.AsNoTracking().ToList()
- C. db.Products.Find(1)
- D. db.Products.ToList()

**Answer:** C, D

**Explanation:** ToList on a DbSet and Find both return tracked entities. AsNoTracking opts out, and a projection into an anonymous type yields no entity instances to track.

### 102. [EF Core] What is the value of p.Price printed at the end?

```
var p = await db.Products.FirstAsync(x => x.Id == 1);
await db.Products.Where(x => x.Id == 1)
    .ExecuteUpdateAsync(s => s.SetProperty(x => x.Price, 99m));
Console.WriteLine(p.Price);
```

- A. The old price: ExecuteUpdate bypasses the change tracker so p is stale
- B. 99, because EF Core refreshes tracked entities after ExecuteUpdate
- C. It throws because p is tracked
- D. 0

**Answer:** A

**Explanation:** ExecuteUpdateAsync issues a direct UPDATE statement and does not touch tracked entities, so p keeps the value read earlier. The database has 99, but the in-memory object is stale until reloaded.

### 103. [EF Core] An entity has a [Timestamp] byte[] RowVersion property. Two users load the same row and both save changes. What happens to the second SaveChanges?

- A. The second save silently overwrites the first
- B. It throws DbUpdateConcurrencyException because the UPDATE matched 0 rows
- C. It throws only when both users edit the same column
- D. EF Core automatically merges both changes

**Answer:** B

**Explanation:** EF Core adds the original RowVersion to the WHERE clause, so after the first save changes the version, the second UPDATE affects zero rows and EF raises DbUpdateConcurrencyException. It does not compare columns individually or merge changes.

### 104. [EF Core] What is the result of running this code with a single DbContext instance?

```
var t1 = db.Orders.CountAsync();
var t2 = db.Customers.CountAsync();
await Task.WhenAll(t1, t2);
```

- A. A DbUpdateException is raised
- B. Both counts run in parallel and complete normally
- C. InvalidOperationException because a second operation was started on the context before the first completed
- D. The second query is automatically queued by the context

**Answer:** C

**Explanation:** DbContext does not support multiple concurrent operations; EF Core detects this and throws InvalidOperationException. It does not queue requests. Use separate contexts (for example from IDbContextFactory) for parallel queries.

### 105. [Async/await] This method is called from a WinForms button click handler (UI thread with a SynchronizationContext). What happens?

```
string Get() => GetAsync().Result;

async Task<string> GetAsync()
{
    await Task.Delay(100);
    return "x";
}
```

- A. It throws InvalidOperationException for cross-thread access
- B. It returns null
- C. It returns "x" after about 100 ms
- D. It deadlocks

**Answer:** D

**Explanation:** The UI thread blocks on .Result while the continuation after await Task.Delay needs to resume on that same UI thread, so neither can proceed. Using await up the call chain or ConfigureAwait(false) inside the helper avoids it.

### 106. [Async/await] Which statements about async void methods are correct? (Select all that apply.)

- A. An exception thrown from one cannot be caught by a try/catch around the call
- B. Callers can await them to observe completion
- C. An unhandled exception in one can crash the process (for example in a console app)
- D. They are the recommended way to start general fire-and-forget work

**Answer:** A, C

**Explanation:** async void has no Task, so exceptions are raised on the captured context or thread pool, bypassing the caller's catch and potentially terminating the process. It is meant for event handlers only, and it cannot be awaited.

### 107. [Async/await] Which statements about Task.WhenAll are correct when several of the tasks fault? (Select all that apply.)

- A. It cancels the remaining tasks as soon as one faults
- B. It completes as soon as the first task faults
- C. All exceptions are available in whenAllTask.Exception.InnerExceptions
- D. await on the WhenAll task rethrows only the first exception

**Answer:** C, D

**Explanation:** WhenAll completes only after all tasks finish, aggregating failures; await unwraps and rethrows just the first, and the full set lives in the AggregateException. It never cancels the other tasks.

### 108. [Async/await] What is wrong with this method?

```
Task<string> ReadAll(string path)
{
    using var reader = new StreamReader(path);
    return reader.ReadToEndAsync();
}
```

- A. The reader is disposed before the returned task completes, so the read can fail with ObjectDisposedException
- B. It does not compile because async is missing
- C. ReadToEndAsync cannot be used with using var
- D. Nothing: ReadToEndAsync completes before the method returns

**Answer:** A

**Explanation:** Without async/await the method returns the Task immediately, the using scope ends and disposes the reader while the read is still in flight. Making the method async and awaiting inside the using fixes it.

### 109. [Async/await] Which statements about ConfigureAwait(false) are correct? (Select all that apply.)

- A. It forces the awaited operation to run on a thread-pool thread
- B. In ASP.NET Core, omitting it in application code does not cause the classic sync-context deadlock
- C. Code after the await may run without the captured SynchronizationContext
- D. It suppresses exceptions from the awaited task

**Answer:** B, C

**Explanation:** ASP.NET Core has no SynchronizationContext, so blocking there does not deadlock in the classic way, and ConfigureAwait(false) simply says the continuation need not resume on the captured context. It does not change where the awaited operation itself runs and does not touch exceptions.

### 110. [Async/await] Which statements about ValueTask<T> are correct? (Select all that apply.)

- A. Awaiting a ValueTask once directly is a valid usage
- B. Calling GetAwaiter().GetResult() on an incomplete ValueTask is a supported way to block
- C. Awaiting the same ValueTask instance twice is not supported
- D. Calling AsTask() once gives a Task that can be awaited multiple times

**Answer:** A, C, D

**Explanation:** A ValueTask must be consumed once; converting with AsTask gives a normal reusable Task. Blocking on an incomplete ValueTask via GetResult is unsupported.

### 111. [Async/await] What does this code print?

```
async Task F() { throw new InvalidOperationException("x"); }

Task t = F();
Console.Write("after ");
try { await t; }
catch (InvalidOperationException) { Console.Write("caught"); }
```

- A. It throws InvalidOperationException from the call F()
- B. after caught
- C. caught
- D. after, then an unhandled exception

**Answer:** B

**Explanation:** In an async method, exceptions are captured in the returned Task, even when thrown before any await, so F() returns a faulted task. 'after' is printed first and await t then throws, which is caught.

### 112. [Async/await] What is the main problem with this code?

```
Parallel.ForEach(items, async item => await ProcessAsync(item));
Console.WriteLine("done");
```

- A. It deadlocks on the thread pool
- B. Parallel.ForEach cannot take a lambda
- C. The async lambda becomes async void, so Parallel.ForEach returns before the work finishes and exceptions are lost
- D. The items are processed sequentially

**Answer:** C

**Explanation:** Parallel.ForEach takes an Action<T>, so the async lambda is compiled as async void and is not awaited. The loop returns when the lambdas hit their first await. Parallel.ForEachAsync or Task.WhenAll should be used.

### 113. [DI lifetimes] A singleton service takes a scoped service in its constructor. Which statements are correct? (Select all that apply.)

- A. With validation off, the scoped instance effectively lives as long as the singleton
- B. With scope validation on (default in Development) resolving it throws InvalidOperationException
- C. Registering the dependency as transient makes it per-request inside the singleton
- D. The scoped instance is recreated on every request even though the singleton exists

**Answer:** A, B

**Explanation:** The singleton's constructor runs once, so it captures one scoped instance for its whole lifetime (a captive dependency); validation detects this. A transient injected into a singleton is also resolved once and kept.

### 114. [DI lifetimes] Which statements about disposal in the built-in DI container are correct? (Select all that apply.)

- A. Services created in a request scope are disposed when that scope is disposed
- B. Instances passed in via AddSingleton(instance) are not disposed by the container
- C. A transient IDisposable resolved from the root provider is held until the root provider is disposed
- D. The container disposes transient instances immediately after each use

**Answer:** A, B, C

**Explanation:** The container tracks disposable instances it creates and disposes them with their owning scope or root, which makes root-resolved transients a leak risk. It does not own instances you supply. It never disposes transients right after use.

### 115. [DI lifetimes] Given these registrations, which statements are correct? (Select all that apply.)

```
services.AddTransient<IFoo, A>();
services.AddTransient<IFoo, B>();
```

- A. GetRequiredService<IFoo>() returns an A
- B. GetServices<IFoo>() enumerates A then B
- C. GetRequiredService<IFoo>() returns a B
- D. GetRequiredService<IFoo>() throws an ambiguity exception

**Answer:** B, C

**Explanation:** For a single service the last registration wins, while IEnumerable<IFoo> contains all registrations in registration order. The container never throws for multiple registrations of the same service type.

### 116. [DI lifetimes] A BackgroundService needs to use a scoped DbContext each time it processes a message. What is the correct approach?

- A. Resolve the DbContext from the root IServiceProvider and keep it
- B. Inject the DbContext in the constructor of the BackgroundService
- C. Register the BackgroundService as scoped
- D. Inject IServiceScopeFactory and create a scope per unit of work

**Answer:** D

**Explanation:** Hosted services live for the app lifetime, so injecting a scoped service captures it forever. Creating a scope per unit of work gives a fresh DbContext that is disposed afterward. Resolving scoped services from the root provider is invalid or leaky.

### 117. [DI lifetimes] What is returned by this code?

```
services.AddSingleton<IFoo, A>();
services.TryAddSingleton<IFoo, B>();
var foo = services.BuildServiceProvider().GetRequiredService<IFoo>();
```

- A. An instance of A
- B. An instance of B
- C. An InvalidOperationException because IFoo is registered twice
- D. null

**Answer:** A

**Explanation:** TryAddSingleton registers only when no registration for the service type already exists, so the earlier AddSingleton wins. B is never registered.

### 118. [ASP.NET Core pipeline] Which statements about middleware ordering are correct? (Select all that apply.)

- A. Static files middleware must always come after endpoint mapping
- B. UseAuthentication must be registered before UseAuthorization
- C. UseAuthorization must be registered before UseAuthentication
- D. UseExceptionHandler should be registered early so it can catch exceptions from later middleware

**Answer:** B, D

**Explanation:** Authorization relies on the user established by authentication, so authentication goes first. An exception handler only sees exceptions from middleware that runs after it. Static files typically come early and short-circuit.

### 119. [ASP.NET Core pipeline] What is the response body of a request?

```
app.Use(async (ctx, next) =>
{
    await ctx.Response.WriteAsync("A");
    await next();
    await ctx.Response.WriteAsync("C");
});
app.Run(async ctx => await ctx.Response.WriteAsync("B"));
```

- A. BAC
- B. ABC
- C. ACB
- D. AB

**Answer:** B

**Explanation:** The first middleware writes A, awaits next which runs the terminal middleware writing B, and then writes C once control returns. The pipeline unwinds in reverse order, so the sequence is ABC.

### 120. [ASP.NET Core pipeline] app.UseExceptionHandler("/error") is called after a terminal app.Run(ctx => throw new Exception()). What happens when a request is made?

- A. The request returns 404
- B. The exception handler catches it because it is registered
- C. The exception propagates to the server because the handler is never reached in the pipeline
- D. The handler runs only in the Development environment

**Answer:** C

**Explanation:** Middleware is a chain in registration order and an exception handler only catches exceptions thrown by components after it. Since app.Run is terminal and comes first, the later handler is never part of the executed path.

### 121. [ASP.NET Core pipeline] Which statements about this middleware are correct? (Select all that apply.)

```
app.Use(async (ctx, next) =>
{
    await ctx.Response.WriteAsync("hi");
    ctx.Response.Headers["X-Test"] = "1";
});
```

- A. Setting the header throws InvalidOperationException because the response has already started
- B. Headers are buffered until the middleware returns so the header is sent
- C. The header is silently ignored without any exception
- D. ctx.Response.HasStarted is true after the WriteAsync completes

**Answer:** A, D

**Explanation:** Once the body begins to flush, headers are sent and become read-only, so modifying them throws and HasStarted is true. Kestrel does not buffer headers until the middleware ends.

### 122. [ASP.NET Core pipeline] In a controller annotated with [ApiController], which statements about parameter binding and validation are correct? (Select all that apply.)

- A. Complex type parameters are inferred as [FromForm]
- B. Automatic HTTP 400 for invalid ModelState happens after the action body runs
- C. A simple-type parameter that is not in the route template is inferred as [FromQuery]
- D. A complex type parameter is inferred as [FromBody]

**Answer:** C, D

**Explanation:** ApiController infers FromBody for complex types and Route or Query for simple ones. Its validation filter short-circuits with 400 before the action executes. FromForm is inferred only for IFormFile types.

### 123. [ASP.NET Core pipeline] With <Nullable>enable</Nullable> in a project using [ApiController], what happens when a POST body {} is bound to this DTO?

```
public class CreateUserDto
{
    public string Name { get; set; }
}
```

- A. A 500 NullReferenceException is thrown
- B. Name is set to an empty string
- C. Name is null and the action runs normally
- D. A 400 response is returned automatically because non-nullable reference type properties are treated as [Required]

**Answer:** D

**Explanation:** MVC treats non-nullable reference type properties as implicitly required, so the missing Name makes ModelState invalid and ApiController returns 400. This is by default and can be disabled.

### 124. [ASP.NET Core pipeline] A singleton service must observe configuration values that change at runtime (reloadOnChange). Which type should it inject?

- A. IOptionsMonitor<T>
- B. T directly via AddSingleton(T)
- C. IOptions<T>
- D. IOptionsSnapshot<T>

**Answer:** A

**Explanation:** IOptionsMonitor<T> is a singleton that always returns current values and offers OnChange. IOptions<T> is computed once, and IOptionsSnapshot<T> is scoped, so it cannot be injected into a singleton.

### 125. [HttpClient] Why is creating a new HttpClient per request inside a using block discouraged in a long-running service?

- A. HttpClient is not thread-safe
- B. It can exhaust sockets because disposed connections linger in TIME_WAIT, and the pool is not reused
- C. HttpClient cannot be disposed
- D. Each HttpClient allocates a new thread

**Answer:** B

**Explanation:** Each HttpClient with its own handler opens its own connections, which remain in TIME_WAIT after disposal and can exhaust sockets. HttpClient is safe for concurrent use, and IHttpClientFactory or a long-lived instance reuses the connection pool.

### 126. [Generics variance] Which of these declarations compile? (Select all that apply.)

- A. List<object> b = new List<string>();
- B. IEnumerable<object> a = new List<string>();
- C. IList<object> d = new List<string>();
- D. Action<string> c = new Action<object>(o => { });

**Answer:** B, D

**Explanation:** IEnumerable<out T> is covariant and Action<in T> is contravariant. List<T> is a class, and IList<T> is invariant because it both reads and writes T.

### 127. [Generics variance] What happens at runtime?

```
object[] arr = new string[2];
arr[0] = "a";
arr[1] = 42;
```

- A. It does not compile
- B. It runs and stores 42 in arr[1]
- C. ArrayTypeMismatchException on the last line
- D. InvalidCastException on the first line

**Answer:** C

**Explanation:** string[] converts to object[] due to array covariance, but the runtime still verifies each store against the real element type. Storing an int throws ArrayTypeMismatchException.

### 128. [Generics variance] Why does 'IEnumerable<object> e = new List<int>();' fail to compile?

- A. List<int> does not implement IEnumerable
- B. object cannot be used as a type argument
- C. IEnumerable<T> is invariant
- D. Variance only applies to reference-type arguments; int needs a boxing conversion, not a reference conversion

**Answer:** D

**Explanation:** Generic variance is allowed only when the type arguments are related by identity or reference conversion; int to object is a boxing conversion. IEnumerable<T> is covariant and List<int> does implement it.

### 129. [Generics variance] Static counters on a generic class are incremented through different type arguments. What is printed?

```
class C<T> { public static int Count; }

C<int>.Count++;
C<string>.Count++;
C<int>.Count++;
Console.WriteLine($"{C<int>.Count} {C<string>.Count}");
```

- A. 2 1
- B. 3 3
- C. 1 1
- D. 3 0

**Answer:** A

**Explanation:** Static fields are per constructed type, so C<int> and C<string> have separate Count fields. C<int>.Count is incremented twice and C<string>.Count once.

### 130. [Value vs reference] What happens when the code assigns to a member of a struct element obtained through a List indexer?

```
struct Point { public int X; }

var list = new List<Point> { new Point() };
list[0].X = 5;
```

- A. It sets X to 5
- B. Compile error CS1612: cannot modify the return value because it is not a variable
- C. InvalidOperationException at runtime
- D. It sets X on a copy and silently does nothing

**Answer:** B

**Explanation:** The indexer returns a copy of the struct, so assigning to a member of that temporary is rejected by the compiler. Replace the element with a modified copy, or use CollectionsMarshal.AsSpan with ref access.

### 131. [Value vs reference] A mutating method is called on a readonly field holding a struct. What is printed?

```
struct Counter { public int N; public void Inc() => N++; }
class Holder { public readonly Counter C = new Counter(); }

var h = new Holder();
h.C.Inc();
Console.WriteLine(h.C.N);
```

- A. It does not compile
- B. It throws
- C. 0
- D. 1

**Answer:** C

**Explanation:** Because the field is readonly, the call Inc() operates on a defensive copy of the struct, so the original N remains 0. Making Counter a readonly struct or the field non-readonly changes this.

### 132. [Value vs reference] An int is boxed and the original variable is changed afterwards. What is printed after unboxing?

```
int i = 5;
object o = i;
i = 10;
Console.WriteLine((int)o);
```

- A. 10
- B. It does not compile
- C. It throws InvalidCastException
- D. 5

**Answer:** D

**Explanation:** Boxing copies the int to the heap, so later changes to i do not affect the box. Unboxing yields the copied 5.

### 133. [Value vs reference] What does this code do?

```
object o = 5;
long l = (long)o;
Console.WriteLine(l);
```

- A. Throws InvalidCastException because unboxing requires the exact original type
- B. Prints 5 because int converts implicitly to long
- C. Does not compile
- D. Prints 5

**Answer:** A

**Explanation:** Unboxing is only allowed to the exact boxed type (or its nullable), so unboxing an int box as long throws. You need (long)(int)o instead.

### 134. [Value vs reference] Which of these cause a boxing allocation? (Select all that apply.)

- A. int i = 3; string s = i.ToString();
- B. string.Format("{0}", 5)
- C. list.Add(1) where list is List<int>
- D. object o = 3;

**Answer:** B, D

**Explanation:** The int is boxed to be passed in the object[] params array and assigned to object. List<int>.Add is generic over int, and int.ToString is called directly on the value without boxing.

### 135. [Value vs reference] Two object-typed references hold equal string contents. What do == and Equals report?

```
object a = "hi";
object b = new string(new[] { 'h', 'i' });
Console.WriteLine($"{a == b} {a.Equals(b)}");
```

- A. True True
- B. False True
- C. True False
- D. False False

**Answer:** B

**Explanation:** With both operands typed as object, == compares references, and the two strings are different instances. Equals is virtual and string overrides it for value comparison.

### 136. [Value vs reference] Comparing string references: a literal, a constant concatenation and a runtime concatenation. What is printed?

```
string s1 = "hello";
string s2 = "hel" + "lo";
string part = "hel";
string s3 = part + "lo";
Console.WriteLine(ReferenceEquals(s1, s2));
Console.WriteLine(ReferenceEquals(s1, s3));
```

- A. False False
- B. True True
- C. True False
- D. False True

**Answer:** C

**Explanation:** 'hel' + 'lo' is folded to the literal 'hello' by the compiler, so it's the same interned reference. The runtime concatenation creates a new string instance, so ReferenceEquals is false.

### 137. [Records/struct] Two positional records hold different List<int> instances with the same contents. What does == print?

```
record R(List<int> L);

var x = new R(new List<int> { 1 });
var y = new R(new List<int> { 1 });
Console.WriteLine(x == y);
```

- A. It does not compile
- B. It throws
- C. True
- D. False

**Answer:** D

**Explanation:** The synthesized record equality compares each property with EqualityComparer<T>.Default, and List<int> uses reference equality. The two lists are different instances, so the records are not equal.

### 138. [Records/struct] Which statements about records are correct? (Select all that apply.)

- A. A with-expression on a record class creates a shallow copy
- B. == on a record class compares members by value using the synthesized equality
- C. Positional properties of a record struct are init-only like a record class
- D. Records are always value types

**Answer:** A, B

**Explanation:** A with-expression copies the object and reference-type members are shared, and the synthesized operator == compares members. Records may be classes or structs, and positional record struct properties are mutable by default.

### 139. [Span/ref] What happens when a Span<int> local is used after an await in an async method?

```
async Task F()
{
    Span<int> s = new int[4];
    await Task.Delay(1);
    s[0] = 1;
}
```

- A. It does not compile: a ref struct (Span<int>) cannot be used across an await
- B. It throws at runtime
- C. It compiles but s becomes empty after the await
- D. It compiles and runs

**Answer:** A

**Explanation:** A ref struct must live on the stack, but locals that span an await are hoisted into the state machine. The compiler rejects using the Span after the await. Using it before the await only, or Memory<T>, is fine.

### 140. [Span/ref] A span slice and a range-sliced array are each modified. What is printed?

```
int[] a = { 1, 2, 3, 4 };
Span<int> s = a.AsSpan(1, 2);
s[0] = 99;
int[] b = a[1..3];
b[1] = 77;
Console.WriteLine($"{a[1]} {a[2]}");
```

- A. 1 3
- B. 99 3
- C. 99 77
- D. 2 3

**Answer:** B

**Explanation:** AsSpan creates a view into the same array so s[0] = 99 changes a[1]. The range a[1..3] on an array copies the elements, so changing b does not affect a.

### 141. [Span/ref] A ref local is taken to an array element and the array variable is then reassigned. What is printed?

```
int[] arr = { 1, 2, 3 };
ref int r = ref arr[0];
arr = new[] { 7, 8, 9 };
r = 10;
Console.WriteLine($"{arr[0]} {r}");
```

- A. 7 7
- B. 10 10
- C. 7 10
- D. 10 7

**Answer:** C

**Explanation:** The ref local points at the first element of the original array, and reassigning arr does not retarget it. Writing through r modifies the old array while arr[0] reads from the new one.

### 142. [Threading] Which are poor choices as a lock target? (Select all that apply.)

- A. lock (this)
- B. lock (_gate) where _gate is a private readonly object
- C. lock (typeof(Foo))
- D. lock ("gate")

**Answer:** A, C, D

**Explanation:** Publicly reachable objects such as this, Type objects and interned string literals can be locked by unrelated code, creating deadlocks. A private dedicated object cannot.

### 143. [Threading] Which approaches make this counter update thread-safe? (Select all that apply.)

- A. lock (_gate) { counter++; }
- B. Interlocked.Increment(ref counter)
- C. Declaring the field volatile and using counter++
- D. Making the field static

**Answer:** A, B

**Explanation:** Interlocked and lock make the read-modify-write atomic. volatile gives visibility and ordering guarantees only, and static says nothing about atomicity.

### 144. [Threading] Which statements about ConcurrentDictionary.GetOrAdd(key, valueFactory) are correct? (Select all that apply.)

- A. The valueFactory can be invoked more than once for the same key under contention
- B. Only one value is stored, and all callers get the stored one
- C. The valueFactory is executed while holding the dictionary's lock
- D. The valueFactory is guaranteed to run exactly once per key

**Answer:** A, B

**Explanation:** Competing threads may each run the factory, but only one result wins and is returned to everyone. The factory runs outside the lock, so it needs to be side-effect free. Wrap values in Lazy<T> for single execution.

### 145. [Threading] Which statements are correct? (Select all that apply.)

- A. lock (Monitor) is reentrant for the same thread
- B. SemaphoreSlim.WaitAsync can be used to guard async critical sections
- C. Using await inside a lock statement body is a compile-time error
- D. SemaphoreSlim(1,1) is reentrant for the same thread

**Answer:** A, B, C

**Explanation:** A lock body can't contain await because the continuation might resume on another thread, so use SemaphoreSlim.WaitAsync. Monitor-based lock is reentrant but SemaphoreSlim is not, so recursive waits would deadlock.

### 146. [Threading] An AsyncLocal value is changed inside Task.Run. What does the caller read afterwards?

```
static readonly AsyncLocal<int> V = new();

static async Task Main()
{
    V.Value = 1;
    await Task.Run(() => { V.Value = 2; });
    Console.WriteLine(V.Value);
}
```

- A. 2
- B. 0
- C. It throws
- D. 1

**Answer:** D

**Explanation:** Task.Run captures a copy of the ExecutionContext, so changes made inside the child do not flow back to the caller. The parent still sees 1.

### 147. [Memory/GC] What is the main effect of giving a class a finalizer on its garbage collection?

- A. Instances survive at least one extra GC because they must be queued for finalization first
- B. The finalizer runs immediately when the last reference is dropped
- C. Instances are allocated on the LOH
- D. Instances are collected faster

**Answer:** A

**Explanation:** Finalizable objects are registered, and when found unreachable they are promoted to the f-reachable queue to run their finalizer, delaying reclamation. GC.SuppressFinalize in Dispose removes this cost. Finalizers do not run immediately.

### 148. [Memory/GC] A short-lived view model subscribes to a static event with 'Publisher.Changed += OnChanged;' and never unsubscribes. What is the effect?

- A. Nothing; the GC ignores event subscriptions
- B. The view model stays reachable via the static event's delegate list, causing a memory leak
- C. The subscription is automatically removed when the view model goes out of scope
- D. The event raises ObjectDisposedException

**Answer:** B

**Explanation:** The delegate stored in the static event references the view model instance, keeping it reachable from a GC root. Unsubscribe or use weak events.

### 149. [Memory/GC] Which statements about the Large Object Heap (LOH) are correct? (Select all that apply.)

- A. Objects of 85,000 bytes or more are allocated on the LOH
- B. The LOH is compacted on every collection by default
- C. The LOH is collected only as part of a generation 2 collection
- D. LOH objects start in generation 0 and are promoted

**Answer:** A, C

**Explanation:** Large objects go to the LOH, which is logically part of gen 2 so it is collected only with a full GC. It is not compacted by default and objects are not allocated in gen 0.

### 150. [Memory/GC] Two using declarations appear in a method body. In what order is output produced?

```
class D : IDisposable
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
}
```

- A. b a body
- B. body a b
- C. body b a
- D. a b body

**Answer:** C

**Explanation:** A using declaration disposes at the end of the enclosing scope, so the body runs first. Disposal is in reverse order of declaration, b before a.

### 151. [Memory/GC] Which statements about finalizers are correct? (Select all that apply.)

- A. The order in which finalizers run across objects is not guaranteed
- B. They are not guaranteed to run when the process exits in .NET Core
- C. They run on the thread that dropped the last reference
- D. They run immediately when the object becomes unreachable

**Answer:** A, B

**Explanation:** Finalizers run on a dedicated finalizer thread at an unspecified time, with no ordering guarantee, and .NET Core does not run them at shutdown. They are not immediate.

### 152. [Pattern matching] A switch expression with guarded type, property and null patterns is called with four values. What is printed?

```
string Describe(object o) => o switch
{
    int i when i > 10 => "big",
    int => "int",
    string { Length: 0 } => "empty",
    null => "null",
    _ => "other"
};

Console.WriteLine(string.Join(",", Describe(11), Describe(7), Describe(""), Describe(null)));
```

- A. big,int,empty,other
- B. int,int,empty,null
- C. big,int,empty, followed by an exception
- D. big,int,empty,null

**Answer:** D

**Explanation:** 11 matches the guarded int arm, 7 falls to the plain int arm, the empty string matches the property pattern, and null matches the null pattern since a type pattern never matches null.

### 153. [Pattern matching] What is the behavior of N(Color.Blue)?

```
enum Color { Red, Green, Blue }

static string N(Color c) => c switch
{
    Color.Red => "r",
    Color.Green => "g"
};

Console.WriteLine(N(Color.Blue));
```

- A. Throws SwitchExpressionException at runtime, with a compiler warning for non-exhaustiveness
- B. Compile error
- C. Returns null
- D. Returns an empty string

**Answer:** A

**Explanation:** Missing enum cases produce warning CS8509, and when no arm matches at runtime a SwitchExpressionException is thrown. It is not a compile error and no default value is produced.

### 154. [Pattern matching] For int[] a = { 1, 2, 3 }, which expressions evaluate to true? (Select all that apply.)

- A. a is [1, 2, 3, ..]
- B. a is [1, .., 3]
- C. a is [_, _]
- D. a is [.., 2]

**Answer:** A, B

**Explanation:** [1, .., 3] matches first and last, and [1, 2, 3, ..] matches with an empty slice. [_, _] requires exactly two elements and [.., 2] requires the last element to be 2.

### 155. [Pattern matching] A class overloads == to always return true. What do 'p == null' and 'p is null' print?

```
class P
{
    public static bool operator ==(P a, P b) => true;
    public static bool operator !=(P a, P b) => false;
    public override bool Equals(object o) => true;
    public override int GetHashCode() => 0;
}

var p = new P();
Console.WriteLine($"{p == null} {p is null}");
```

- A. True True
- B. True False
- C. False True
- D. False False

**Answer:** B

**Explanation:** p == null calls the overloaded operator, which always returns true here. 'is null' performs a direct null check and bypasses operator overloading, so it is false.

### 156. [LINQ deferred execution] A captured local used in a Where predicate is changed before the query is enumerated. What is printed?

```
int threshold = 2;
var nums = new[] { 1, 2, 3, 4 };
var q = nums.Where(x => x > threshold);
threshold = 3;
Console.WriteLine("[ " + string.Join(", ", q.ToList()) + " ]");
```

- A. [ ]
- B. [ 3, 4 ]
- C. [ 4 ]
- D. [ 2, 3, 4 ]

**Answer:** C

**Explanation:** The lambda captures the variable threshold, and the query only runs at ToList, after threshold is 3. Only 4 is greater than 3.

### 157. [LINQ deferred execution] Words are sorted by length with OrderBy. What order is printed?

```
var words = new[] { "bb", "a", "cc", "d" };
Console.WriteLine(string.Join(" ", words.OrderBy(w => w.Length)));
```

- A. bb cc a d
- B. d a bb cc
- C. a d cc bb
- D. a d bb cc

**Answer:** D

**Explanation:** OrderBy is stable, so elements with equal keys keep their original relative order: a before d, and bb before cc. An unstable sort like Array.Sort could reorder ties.

### 158. [Exceptions] Which statements are correct about rethrowing exceptions? (Select all that apply.)

- A. 'throw ex;' preserves the original stack trace
- B. 'throw ex;' resets the stack trace to the point of the rethrow
- C. 'throw;' preserves the original stack trace
- D. ExceptionDispatchInfo.Capture(ex).Throw() preserves the original stack trace

**Answer:** B, C, D

**Explanation:** A bare throw rethrows without altering the trace, and ExceptionDispatchInfo does the same from outside a catch. 'throw ex;' restarts the stack trace at that statement.

### 159. [Exceptions] An exception filter, an inner finally and a catch all participate in one throw. What is the output order?

```
static bool Log(Exception e) { Console.Write("filter "); return true; }

try
{
    try { throw new Exception("x"); }
    finally { Console.Write("finally "); }
}
catch (Exception e) when (Log(e))
{
    Console.Write("catch ");
}
```

- A. filter finally catch
- B. catch filter finally
- C. filter catch finally
- D. finally filter catch

**Answer:** A

**Explanation:** The runtime evaluates filters in a first pass before any finally block runs, then unwinds, running the inner finally, and finally enters the catch. So the output is 'filter finally catch'.

### 160. [Exceptions] A static field initializer throws, and the field is read twice in separate try blocks. What is printed?

```
class Cfg
{
    public static readonly int V = Init();
    static int Init() => throw new Exception("boom");
}

try { _ = Cfg.V; } catch (Exception e) { Console.WriteLine(e.GetType().Name); }
try { _ = Cfg.V; } catch (Exception e) { Console.WriteLine(e.GetType().Name); }
```

- A. Exception then Exception
- B. TypeInitializationException then TypeInitializationException
- C. Exception then TypeInitializationException
- D. TypeInitializationException then Exception

**Answer:** B

**Explanation:** A static initializer failure is wrapped in TypeInitializationException, and the type remains permanently in a failed state, so later accesses throw it again.


## Expert

### 161. [GC / LOH] Which statement about the Large Object Heap (LOH) in the .NET GC is correct?

- A. Objects of 85,000 bytes or more are allocated on the LOH, which is collected only with gen 0 collections
- B. The LOH is always compacted on every gen 1 collection
- C. Objects of roughly 85,000 bytes or more are allocated on the LOH, which is logically collected together with gen 2
- D. Only arrays can ever be allocated on the LOH; strings never are

**Answer:** C

**Explanation:** Large objects (about 85,000 bytes and up) go to the LOH, which is collected as part of gen 2 collections and is not compacted by default. Gen 0 and gen 1 collections do not touch it. Strings can also land on the LOH when large enough.

### 162. [GC / Server vs Workstation] Which statements about server GC versus workstation GC are correct? (Select all that apply.)

- A. Server GC never compacts the heap
- B. Server GC generally favors throughput at the cost of higher memory use
- C. Server GC creates a separate heap and dedicated GC thread per logical core
- D. Workstation GC cannot perform background (concurrent) gen 2 collections

**Answer:** B, C

**Explanation:** Server GC uses per-core heaps and GC threads and is tuned for throughput, so it uses more memory. Workstation GC does support background GC, and both flavors can compact.

### 163. [Span<T> / ref structs] Which statements about Span<T> are correct? (Select all that apply.)

```
Span<int> buf = stackalloc int[4];
int[] arr = { 1, 2, 3, 4 };
Span<int> view = arr.AsSpan(1, 2); // view over arr, no copy
view[0] = 99;                      // arr[1] is now 99
```

- A. It cannot be captured by a lambda or stored in a closure
- B. It cannot be a field of a class or be boxed because it is a ref struct
- C. It cannot wrap an existing managed array, only stack memory
- D. Slicing it with Slice() copies the elements into a new buffer
- E. It can wrap memory obtained from stackalloc in safe code

**Answer:** A, B, E

**Explanation:** As a ref struct, Span<T> is restricted to the stack: no boxing, no class fields, no closure capture. It can wrap arrays and stackalloc memory, and Slice returns a view over the same memory without copying.

### 164. [ValueTask] Which statements about consuming a ValueTask<T> are correct? (Select all that apply.)

- A. A ValueTask<T> always avoids heap allocation
- B. Task.WhenAll accepts ValueTask<T> instances directly without conversion
- C. Call AsTask() if you need to await it more than once or store it for later use
- D. It must not be awaited multiple times

**Answer:** C, D

**Explanation:** A ValueTask can wrap an IValueTaskSource that is reused, so it is single-consumption; AsTask gives a safely shareable Task. It only avoids allocation when it completes synchronously or is backed by a pooled source, and WhenAll requires Tasks.

### 165. [Async state machines] In the snippet, what happens when F() is called without awaiting it?

```
static async Task F()
{
    throw new InvalidOperationException("boom");
}

static void Main()
{
    Task t = F();            // line A
    Console.WriteLine(t.IsFaulted);
}
```

- A. The call returns a faulted Task and the exception is observed when the Task is awaited or inspected
- B. The exception is thrown synchronously from the call to F()
- C. The exception is swallowed permanently and can never be observed
- D. The process crashes immediately because the exception is unhandled

**Answer:** A

**Explanation:** The compiler-generated state machine wraps the body in try/catch and sets the exception on the AsyncTaskMethodBuilder's Task. The caller therefore gets a faulted Task, and the exception only surfaces on await, Wait or Result. It is not thrown synchronously.

### 166. [SynchronizationContext] In an ASP.NET Core application, which statement about ConfigureAwait(false) and blocking calls is most accurate?

- A. Omitting ConfigureAwait(false) will classically deadlock on .Result, exactly like in ASP.NET Framework
- B. ConfigureAwait(false) makes the awaited operation run on a new dedicated thread
- C. ConfigureAwait(false) prevents the state machine from being generated
- D. ASP.NET Core has no SynchronizationContext, so the classic context deadlock does not occur, but sync-over-async can still cause thread pool starvation

**Answer:** D

**Explanation:** ASP.NET Core does not install a request SynchronizationContext, so the classic deadlock is gone. Blocking on async code still ties up thread pool threads and can starve the pool. ConfigureAwait(false) only controls context capture for continuations.

### 167. [ExecutionContext / AsyncLocal] What does the following code print?

```
static readonly AsyncLocal<int> V = new();

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
}
```

- A. 2
- B. 1
- C. 0
- D. It throws because AsyncLocal cannot be set inside an async method

**Answer:** B

**Explanation:** ExecutionContext flows down into async calls, but modifications made inside the callee's async method apply to its own copy and are undone when control returns to the caller. The caller still sees 1. AsyncLocal can be set anywhere.

### 168. [Channels] Given a bounded channel created with FullMode = BoundedChannelFullMode.Wait that is currently full, which statements are correct? (Select all that apply.)

- A. The ValueTask returned by writer.WriteAsync(item) completes once space becomes available
- B. With BoundedChannelFullMode.DropWrite, WriteAsync completes successfully but the item is discarded
- C. writer.TryWrite(item) returns false
- D. writer.WriteAsync(item) throws ChannelClosedException immediately

**Answer:** A, B, C

**Explanation:** In Wait mode TryWrite fails and WriteAsync asynchronously waits for room. DropWrite silently discards the item being written. A ChannelClosedException is only thrown if the writer was completed.

### 169. [Channels] When does ChannelReader<T>.Completion complete normally?

- A. As soon as the writer calls Complete(), even if items are still buffered
- B. When the channel's buffer first becomes empty
- C. After the writer has called Complete() and all buffered items have been read
- D. Only when the reader's CancellationToken is cancelled

**Answer:** C

**Explanation:** Completion finishes only after the writer is marked complete and the buffer has been drained, which is what lets ReadAllAsync terminate cleanly. Completing the writer alone is not enough while items remain.

### 170. [lock / Monitor] Why does C# forbid await inside a lock statement, and what is the usual alternative?

```
private readonly SemaphoreSlim _gate = new(1, 1);

public async Task UpdateAsync()
{
    await _gate.WaitAsync();
    try { await DoWorkAsync(); }
    finally { _gate.Release(); }
}
```

- A. Monitor is owned by a thread, and the continuation may resume on a different thread; use SemaphoreSlim(1,1) with WaitAsync instead
- B. await is forbidden because the lock keyword compiles to a spin lock; use Thread.Sleep instead
- C. The compiler cannot generate a state machine inside try/finally; use a nested method
- D. It is allowed but only in static methods; use a static lock object

**Answer:** A

**Explanation:** Monitor.Exit must be called by the owning thread, but after an await the code may resume on another thread, so the compiler reports an error. SemaphoreSlim is not thread-affine and supports WaitAsync. Async methods can contain try/finally.

### 171. [SemaphoreSlim / cancellation] In this method, what is the bug and the correct fix?

```
async Task RunAsync(SemaphoreSlim sem, CancellationToken ct)
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
}
```

- A. No bug: Release is always correct in finally
- B. WaitAsync must be called with ConfigureAwait(false) to avoid releasing twice
- C. SemaphoreSlim cannot be used with CancellationToken, so remove the token
- D. If WaitAsync(ct) throws OperationCanceledException, finally still calls Release and inflates the count; move WaitAsync before the try block

**Answer:** D

**Explanation:** When WaitAsync is inside the try and is cancelled, the semaphore was never acquired, yet finally releases it, permanently increasing the available count and breaking mutual exclusion. Acquire before entering try so finally runs only after a successful acquire.

### 172. [Interlocked] Which statements about lock-free updates with Interlocked are correct? (Select all that apply.)

```
static int _max;

static void UpdateMax(int value)
{
    int cur;
    while (value > (cur = Volatile.Read(ref _max)))
    {
        if (Interlocked.CompareExchange(ref _max, value, cur) == cur) break;
    }
}
```

- A. Interlocked.Increment performs an atomic read-modify-write
- B. Interlocked.Read is required to read an int safely on 64-bit platforms
- C. Interlocked.CompareExchange in a retry loop can implement arbitrary atomic read-modify-write updates
- D. Writing count = count + 1 on a volatile int is atomic

**Answer:** A, C

**Explanation:** Interlocked.Increment is atomic, and a CompareExchange loop can build other atomic updates. A volatile read followed by a write is two separate operations, so increments can be lost. Interlocked.Read is only relevant for 64-bit values on 32-bit platforms.

### 173. [Memory model / volatile] What does marking a field volatile guarantee in the .NET memory model?

- A. It makes compound operations like i++ atomic
- B. Reads have acquire semantics and writes have release semantics, but compound operations are not atomic
- C. It forces the field to be allocated on the stack
- D. It gives a full fence around every access, equivalent to a lock

**Answer:** B

**Explanation:** Volatile reads are acquire and volatile writes are release, limiting reordering around them. It does not make read-modify-write atomic and is not a full fence or a lock.

### 174. [Expression trees] Which statements about expression trees are correct? (Select all that apply.)

- A. An Expression<Func<T,bool>> can be inspected by a provider such as EF Core and translated to SQL
- B. C# lets you convert a lambda with a statement body to Expression<Func<T>> without restriction
- C. Expression trees are immutable, so changes are made by rewriting with an ExpressionVisitor
- D. Calling Compile() repeatedly is cheap, so caching the delegate is unnecessary

**Answer:** A, C

**Explanation:** Expression trees describe code as data and are immutable, so ExpressionVisitor builds modified copies. Compile() emits IL and is expensive, so delegates should be cached. The compiler rejects statement lambdas for expression trees.

### 175. [Expression trees] For the lambda below, how is the captured local id represented in the expression tree?

```
record Order(int Id);

int id = 5;
Expression<Func<Order, bool>> e = o => o.Id == id;
var right = ((BinaryExpression)e.Body).Right;
Console.WriteLine(right.NodeType);
```

- A. As a ConstantExpression holding the int 5 evaluated at compile time
- B. As a ParameterExpression named id
- C. As a MemberExpression reading a field of a compiler-generated closure object held in a ConstantExpression
- D. As a MethodCallExpression to Convert.ToInt32

**Answer:** C

**Explanation:** The compiler hoists captured locals into a closure class instance, and the tree contains a field access on a constant of that closure type. That is why providers like EF Core can parameterize it and re-evaluate on each execution. It is not folded to a constant of 5.

### 176. [Source generators] Which statements about Roslyn source generators are correct? (Select all that apply.)

- A. They can rewrite the bodies of existing methods in user files
- B. They can call into the compiled output of the project they are generating code for
- C. They can add new source files to a compilation but cannot modify existing user code
- D. IIncrementalGenerator is preferred over ISourceGenerator because it caches pipeline stages

**Answer:** C, D

**Explanation:** Generators only add code, and incremental generators cache stage results to keep the IDE responsive. They run before the target assembly exists, so they cannot call its compiled output or rewrite existing code.

### 177. [Source generators] In an IIncrementalGenerator pipeline, what is the key practice for good caching and IDE performance?

- A. Transform syntax early into small value-equatable models (such as records) and avoid carrying ISymbol or Compilation objects downstream
- B. Store the full Compilation in each pipeline step so results are always fresh
- C. Use static mutable dictionaries to cache models across runs
- D. Perform all work in the final RegisterSourceOutput step using SyntaxNode trees

**Answer:** A

**Explanation:** The pipeline reuses cached outputs when a stage's input is equal to the previous one, so models need value equality, and symbols or compilations change on nearly every edit and defeat caching. Static mutable caches are unsafe and unnecessary.

### 178. [EF Core change tracker] Which statements about EF Core tracking are correct? (Select all that apply.)

- A. A no-tracking query returns the same instance for repeated rows with the same key
- B. A context can track two different instances with the same primary key at the same time
- C. For tracked entities, DetectChanges compares current property values against a snapshot
- D. AsNoTrackingWithIdentityResolution returns a single instance per key within the query results

**Answer:** C, D

**Explanation:** The default tracker uses snapshots and enforces one instance per key. Plain no-tracking queries may materialize separate instances for repeated rows, which AsNoTrackingWithIdentityResolution fixes within a query. Tracking two instances with the same key throws.

### 179. [EF Core concurrency] How does EF Core optimistic concurrency with a configured concurrency token work? (Select all that apply.)

```
public class Product
{
    public int Id { get; set; }
    public string Name { get; set; } = "";
    [Timestamp] public byte[] RowVersion { get; set; } = null!;
}
```

- A. The UPDATE or DELETE includes the original token value in its WHERE clause
- B. A DbUpdateConcurrencyException is thrown when the affected row count is not the expected one
- C. It takes a pessimistic lock on the row when the entity is loaded
- D. The token value used is re-read from the database at SaveChanges time

**Answer:** A, B

**Explanation:** EF adds the original token value to the WHERE clause and treats an unexpected affected-row count as a conflict. No row lock is taken, and the original value comes from load time, which is the point of the check.

### 180. [EF Core split queries] Which statements about AsSplitQuery in EF Core are correct? (Select all that apply.)

```
var blogs = await db.Blogs
    .Include(b => b.Posts)
    .Include(b => b.Tags)
    .AsSplitQuery()
    .ToListAsync();
```

- A. It requires AsNoTracking to work
- B. It uses multiple round trips, and data can change between them unless a suitable transaction isolation is used
- C. It guarantees a consistent snapshot across all the generated SQL queries
- D. It avoids cartesian explosion when including multiple collection navigations

**Answer:** B, D

**Explanation:** Split queries issue separate SQL statements per collection to avoid duplicated parent rows. Without a snapshot or serializable transaction, results may be inconsistent between the statements. It works with tracking queries.

### 181. [EF Core compiled queries] What is the main benefit of EF.CompileAsyncQuery?

```
static readonly Func<AppDb, int, Task<Customer?>> ById =
    EF.CompileAsyncQuery((AppDb db, int id) =>
        db.Customers.FirstOrDefault(c => c.Id == id));

var c = await ById(db, 42);
```

- A. It caches the result rows in memory between calls
- B. It turns the query into a stored procedure on the database
- C. It disables parameterization to reuse database plans
- D. The query is translated once and reused through a delegate, skipping per-call query cache lookup and preprocessing

**Answer:** D

**Explanation:** A compiled query keeps the translated query in a delegate, removing repeated expression processing and cache-key computation. It does not cache data, create stored procedures, or change parameterization.

### 182. [EF Core bulk operations] What is true about ExecuteUpdateAsync in EF Core?

- A. It loads the entities into the change tracker, modifies them, then calls SaveChanges
- B. It runs a set-based UPDATE directly in the database, and already tracked entities are not refreshed
- C. It only works inside a SaveChanges transaction
- D. It raises DbUpdateConcurrencyException automatically for rowversion columns

**Answer:** B

**Explanation:** ExecuteUpdate translates to a single UPDATE statement without materializing entities, so tracked instances can become stale. It does not use the tracker or concurrency token checks.

### 183. [ASP.NET Core middleware] Which statements about the ASP.NET Core middleware pipeline are correct? (Select all that apply.)

- A. app.Run adds a terminal middleware that has no next delegate
- B. Response processing runs through middleware in the same order as request processing
- C. A middleware that does not call next short-circuits the pipeline
- D. Exception handling middleware registered first can catch exceptions thrown by middleware registered after it

**Answer:** A, C, D

**Explanation:** Middleware are nested delegates: skipping next short-circuits, and an outer try/catch sees exceptions from inner components. Run is terminal. The response travels back through the middleware in reverse order.

### 184. [ASP.NET Core middleware] An exception is thrown after the response body has already started streaming. What can an exception-handling middleware do?

- A. Change the status code to 500 as usual
- B. Clear the already-sent headers with Response.Clear()
- C. Nothing useful to the status code; once HasStarted is true headers are sent, so it can only abort the connection or log
- D. Restart the request pipeline from the beginning

**Answer:** C

**Explanation:** After the first body bytes are flushed, status and headers are already on the wire and cannot be modified. Handlers should check Response.HasStarted and typically log and abort. Clear fails or is ignored once the response has started.

### 185. [Rate limiting] What is a known characteristic of the fixed window rate limiter compared to a sliding window?

- A. Up to about twice the permit limit can pass in a short period that straddles a window boundary
- B. It never allows more than the limit in any time span
- C. It cannot be partitioned per user
- D. It queues requests by default with unlimited queue length

**Answer:** A

**Explanation:** A fixed window resets counts at boundaries, so bursts at the end of one window and the start of the next can approach twice the limit. Sliding windows smooth this. Fixed window limiters can be partitioned and do not queue unboundedly by default.

### 186. [Output caching] Which statements about ASP.NET Core output caching are correct? (Select all that apply.)

- A. By default only 200 responses to GET or HEAD requests are cached
- B. By default it does not honor a client's Cache-Control: no-cache request header the way response caching does
- C. Cache entries can be evicted by tag using IOutputCacheStore.EvictByTagAsync
- D. Responses are stored in the client browser cache

**Answer:** A, B, C

**Explanation:** Output caching stores responses on the server, supports tag-based eviction, and is controlled by server policies rather than client headers. The default policy caches only 200 GET/HEAD responses. Browser storage is a different feature.

### 187. [Health checks] What is the recommended design for liveness versus readiness health checks in an orchestrated environment?

- A. Liveness should check all downstream dependencies so unhealthy pods restart
- B. Both probes should run the same checks to avoid confusion
- C. Readiness should return 200 always so traffic is never interrupted
- D. Liveness should be cheap and reflect only whether the process itself is healthy, while readiness checks dependencies and ability to serve traffic

**Answer:** D

**Explanation:** A liveness probe that depends on a database can restart every instance during a database outage, making things worse. Readiness gates traffic and may check dependencies. Typically these are mapped as separate health check endpoints using tags.

### 188. [Minimal API filters] In the snippet, how does an endpoint filter reject invalid input without invoking the handler?

```
app.MapGet("/items/{id:int}", (int id) => Results.Ok(id))
   .AddEndpointFilter(async (ctx, next) =>
   {
       var id = ctx.GetArgument<int>(0);
       if (id <= 0) return Results.BadRequest("id must be positive");
       return await next(ctx);
   });
```

- A. Throw OperationCanceledException
- B. Return an IResult without calling next(context)
- C. Set context.HttpContext.Response.HasStarted to true
- D. Call next(context) twice

**Answer:** B

**Explanation:** An IEndpointFilter chooses whether to call next. Returning a result directly short-circuits the handler and later filters. Throwing cancellation would not produce a proper validation response.

### 189. [DI scoping] Which statements about dependency injection lifetimes in Microsoft.Extensions.DependencyInjection are correct? (Select all that apply.)

- A. ServiceProviderOptions.ValidateScopes can detect resolving scoped services from the root provider
- B. A singleton that takes a scoped service in its constructor creates a captive dependency
- C. A singleton can create scopes on demand with IServiceScopeFactory to use scoped services safely
- D. Transient IDisposable services are never disposed by the container

**Answer:** A, B, C

**Explanation:** Capturing a scoped service in a singleton keeps it alive for the app lifetime. ValidateScopes and scope factories address that. The container does track and dispose transient disposables it creates, at the end of their scope.

### 190. [Keyed services] Given the registration below, what happens when you call provider.GetRequiredService<ICache>() with no key?

```
builder.Services.AddKeyedSingleton<ICache, RedisCache>("redis");

public class Svc([FromKeyedServices("redis")] ICache cache) { }
```

- A. It returns the RedisCache because it is the only ICache registered
- B. It returns the first keyed registration alphabetically
- C. It returns null
- D. It throws InvalidOperationException because keyed registrations are not resolved by a non-keyed request

**Answer:** D

**Explanation:** A keyed registration only matches requests that supply a matching key, such as [FromKeyedServices("redis")] or GetRequiredKeyedService. A non-keyed request finds no registration and GetRequiredService throws.

### 191. [DI disposal] Which services does the built-in DI container dispose when the provider or scope is disposed?

- A. Only instances it created itself via a type or factory registration; instances registered with AddSingleton(instance) are not disposed by it
- B. All services including pre-created instances registered with AddSingleton(instance)
- C. Only scoped services, never singletons
- D. None; services must always be disposed manually

**Answer:** A

**Explanation:** The container owns and disposes instances it creates, but caller-provided instances remain the caller's responsibility. Singletons created by the container are disposed when the root provider is disposed.

### 192. [Outbox pattern] Which statements about the transactional outbox pattern are correct? (Select all that apply.)

- A. Consumers should be idempotent because a relay can publish a message and crash before marking it sent
- B. Publishing to the broker inside the transaction before committing makes it equivalent
- C. A background relay reads unsent outbox rows and publishes them
- D. The outbox row is inserted in the same database transaction as the business change
- E. It gives exactly-once delivery to the broker without consumer cooperation

**Answer:** A, C, D

**Explanation:** The outbox atomically records intent with the state change, and a relay publishes later, which yields at-least-once delivery with possible duplicates. Publishing before commit can send messages for rolled-back changes, so it is not equivalent.

### 193. [Idempotency] What is the most robust way to implement idempotency keys for a payment API?

- A. Check a cache for the key, then process, with no locking
- B. Rely on clients never retrying
- C. Use the request timestamp as the key
- D. Insert the key under a unique constraint in the same transaction as the side effects, and return the stored response on replay

**Answer:** D

**Explanation:** A unique constraint makes the claim atomic, and committing it together with the side effects avoids processing twice or losing the record. A non-atomic check allows concurrent duplicates. Timestamps do not identify retries.

### 194. [Resilience] Which statements about retry and circuit-breaker strategies are correct? (Select all that apply.)

- A. Exponential backoff with jitter reduces synchronized retry storms
- B. Infinite immediate retries are safe because they maximize success
- C. An open circuit breaker fails calls fast, giving the dependency time to recover
- D. Retrying a non-idempotent POST is safe without idempotency keys

**Answer:** A, C

**Explanation:** Jitter spreads retries and breakers shed load. Unbounded immediate retries can overload a struggling service, and retrying non-idempotent operations risks duplicate effects.

### 195. [Resilience / timeouts] How does a Polly (v8) timeout strategy behave if the guarded delegate ignores its CancellationToken?

- A. It aborts the thread running the delegate
- B. It is cooperative: it signals cancellation through the token, so code that ignores the token keeps running
- C. It throws ThreadAbortException into the delegate
- D. It is guaranteed to terminate the underlying HTTP connection

**Answer:** B

**Explanation:** Timeouts rely on cancellation tokens, and nothing can forcibly stop code that does not observe them. Thread abort is not supported in .NET Core and later, and connection termination is not automatic.

### 196. [Native AOT] Which approach makes JSON serialization compatible with Native AOT and trimming?

```
[JsonSerializable(typeof(WeatherForecast))]
internal partial class AppJsonContext : JsonSerializerContext { }

string json = JsonSerializer.Serialize(
    forecast, AppJsonContext.Default.WeatherForecast);
```

- A. Use the default reflection-based serializer, which works unchanged
- B. Disable the trimmer warnings
- C. Use a source-generated JsonSerializerContext with JsonSerializable attributes
- D. Use Type.GetType with strings to load converters

**Answer:** C

**Explanation:** The source generator emits serialization metadata at compile time, so the trimmer and AOT compiler can see what is needed. Reflection-based serialization may fail when members are trimmed, and suppressing warnings only hides the problem.

### 197. [Trimming] Which statements about trimming and reflection are correct? (Select all that apply.)

- A. The trimmer cannot statically see types accessed only by string name through reflection and may remove them
- B. PublishTrimmed removes only whole unused assemblies and never members
- C. Type.GetType("Namespace.Type") is always safe with trimming
- D. [DynamicallyAccessedMembers] annotations tell the trimmer which members must be preserved

**Answer:** A, D

**Explanation:** The linker works on static reachability, so annotations or explicit roots are needed for reflection targets. Trimming removes unused types and members as well, so string-based lookup can break.

### 198. [BenchmarkDotNet] Which practices avoid common BenchmarkDotNet pitfalls? (Select all that apply.)

```
[Benchmark]
public int Sum() => _data.Sum();   // result returned, not discarded

[GlobalSetup]
public void Setup() => _data = Enumerable.Range(0, 1000).ToArray();
```

- A. Running in Release without a debugger attached
- B. Running benchmarks from a Debug build is fine for relative comparisons
- C. Returning the computed result from the benchmark method so the JIT cannot eliminate the work as dead code
- D. Building the input data inside the benchmark method because setup cost is excluded automatically

**Answer:** A, C

**Explanation:** Release builds are required for meaningful JIT optimization, and returning or consuming results prevents dead-code elimination. Setup inside the benchmark body is measured, so it should be in [GlobalSetup] or [IterationSetup].

### 199. [Cancellation] On which thread do callbacks registered via CancellationToken.Register run when CancellationTokenSource.Cancel() is called?

- A. Synchronously on the thread that calls Cancel(), by default
- B. Always on a new thread pool thread
- C. On the thread that created the token
- D. On the thread that registered the callback

**Answer:** A

**Explanation:** Registered callbacks run inline on the thread that calls Cancel, so slow callbacks block the canceller. Use CancelAsync or move heavy work off the callback. They are not marshaled to the creating or registering thread.

### 200. [Concurrent collections] Which statements about ConcurrentDictionary.GetOrAdd(key, valueFactory) are correct? (Select all that apply.)

```
var cache = new ConcurrentDictionary<string, Lazy<Task<Data>>>();
var data = await cache.GetOrAdd(key,
    k => new Lazy<Task<Data>>(() => LoadAsync(k))).Value;
```

- A. The factory may be invoked more than once concurrently for the same key, but only one value is stored
- B. The factory always runs under the dictionary's global lock
- C. Wrapping values in Lazy<T> ensures the expensive initialization runs only once
- D. Racing callers can end up with different instances for the same key

**Answer:** A, C

**Explanation:** The factory runs outside the locks, so duplicate invocations can occur, but all callers receive the single stored value. Lazy<T> defers and de-duplicates expensive creation.

