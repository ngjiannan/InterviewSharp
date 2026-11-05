def add(m):
    # ---------------- EASY (30) ----------------
    m("Easy", "C# basics", "Which keyword declares a value that is fixed at compile time and cannot be changed afterward?",
      ["readonly", "const", "static", "sealed"], [1],
      "Think of the keyword used for compile-time constants such as const int Max = 10;.",
      "const values are substituted at compile time and must be initialized with a constant expression. readonly fields can be assigned at declaration or in a constructor, so they are runtime constants. static and sealed do not make a value immutable.")
    m("Easy", "C# basics", "What is the default value of an uninitialized bool field in a class?",
      ["false", "true", "null", "It is a compile error to leave it uninitialized"], [0],
      "Fields are zero-initialized by the runtime.",
      "Class fields are automatically set to their default value, which is false for bool. bool is a value type so it cannot be null, and fields (unlike locals) do not need definite assignment.")
    m("Easy", "Strings", "Which statement about System.String is true?",
      ["It is a mutable value type", "It is a mutable reference type", "It is an immutable reference type", "It is an immutable value type"], [2],
      "Methods such as Replace or ToUpper return something new.",
      "string is a reference type whose instances cannot be modified after creation; operations return new strings. It is not a value type, and it is not mutable (that is StringBuilder's role).")
    m("Easy", "Collections", "Which of the following collection types can grow and shrink dynamically?",
      ["int[]", "string", "Span<int>", "List<int>"], [3],
      "Arrays have a fixed length once created.",
      "List<T> manages a resizable internal array and offers Add/Remove. Arrays and Span<T> have a fixed length, and string is an immutable sequence of chars.")
    m("Easy", "Collections", "What is the main purpose of Dictionary<TKey,TValue>.TryGetValue?",
      ["To look up a key without throwing an exception when it is missing", "To add a key only if it is absent", "To remove a key and return its value", "To copy all keys into a list"], [0],
      "It returns a bool.",
      "TryGetValue returns false and a default value when the key is missing, avoiding the KeyNotFoundException that the indexer would throw. Adding is done by Add/TryAdd and removal by Remove.")
    m("Easy", "OOP", "Which of the following can a C# class do? (Select all that apply.)",
      ["Implement multiple interfaces", "Inherit from one base class", "Inherit directly from two base classes", "Inherit from a struct"], [0, 1],
      "C# allows single class inheritance but multiple interface implementation.",
      "A class has exactly one base class (System.Object by default) and may implement any number of interfaces. Multiple class inheritance is not supported, and structs cannot be base types.")
    m("Easy", "Async/await", "What does the await keyword do inside an async method?",
      ["Blocks the current thread until the task completes", "Starts a new thread for the awaited call", "Asynchronously suspends the method until the awaited task completes, without blocking the thread", "Converts the method to run synchronously"], [2],
      "The thread is freed to do other work in the meantime.",
      "await registers the rest of the method as a continuation and returns control to the caller if the task is not complete. It does not block and does not itself create a thread.")
    m("Easy", "Async/await", "Which return type should an async method normally use when it produces no value?",
      ["void", "Task", "bool", "object"], [1],
      "The caller must be able to await it and observe exceptions.",
      "Task lets callers await the method and observe exceptions. async void is reserved for event handlers because errors cannot be caught by the caller. bool and object imply a result that is not produced.")
    m("Easy", "LINQ", "Which namespace must be imported to use LINQ extension methods such as Where and Select on collections?",
      ["System.Linq", "System.Collections.Generic", "System.Data", "System.Text"], [0],
      "The namespace is named after the feature.",
      "Enumerable extension methods like Where and Select live in System.Linq. System.Collections.Generic holds the collection types, but not these query operators.")
    m("Easy", "Records", "What do C# record types provide by default?",
      ["Reference equality only", "Mandatory immutability of all fields", "Value-based equality and a generated ToString", "Automatic database mapping"], [2],
      "Two records with the same data compare as equal.",
      "Records generate Equals/GetHashCode based on member values and a ToString that prints them. They are not forced to be immutable (positional properties are init-only, but you can add mutable ones) and have nothing to do with databases.")
    m("Easy", "Nullable reference types", "With nullable reference types enabled, what does the declaration string? name mean?",
      ["name is a value type", "name may hold null", "name can never be assigned", "name is lazily evaluated"], [1],
      "The question mark is an annotation about null.",
      "string? tells the compiler that null is an expected value, so it warns on unchecked dereference. Without the ? the compiler treats the variable as non-null. It does not change the runtime type.")
    m("Easy", "DI", "In ASP.NET Core dependency injection, which lifetime creates a new instance every time the service is requested?",
      ["Singleton", "Scoped", "Static", "Transient"], [3],
      "The name suggests a short-lived instance.",
      "Transient services are created each time they are resolved. Singleton gives one instance per container and Scoped one per scope (usually per HTTP request). Static is not a DI lifetime.")
    m("Easy", "ASP.NET Core", "Which file is the default place for application configuration settings in an ASP.NET Core project?",
      ["appsettings.json", "web.xml", "Startup.config", "launch.cfg"], [0],
      "It is a JSON file loaded by the default host builder.",
      "The default host loads appsettings.json plus appsettings.{Environment}.json. The other names are not used by default.")
    m("Easy", "Minimal APIs", "What does app.MapGet(\"/hello\", () => \"Hi\") do in a minimal API?",
      ["Registers a handler for HTTP POST requests to /hello", "Registers a middleware that runs for every request", "Registers a handler for HTTP GET requests to /hello", "Reads a value from configuration"], [2],
      "Match the verb in the method name.",
      "MapGet creates an endpoint that responds to GET requests on the given route pattern. Handlers for POST use MapPost, and middleware is registered with Use/Run.")
    m("Easy", "EF Core", "In EF Core, what does a DbContext represent?",
      ["A single table row", "A session with the database used to query and save entities", "A SQL Server login", "A database migration"], [1],
      "It combines the unit of work and repository ideas.",
      "DbContext is the main class for interacting with the database: it tracks entities, runs queries and saves changes. A table row is an entity instance and a migration is a schema change script.")
    m("Easy", "EF Core", "In EF Core, what does a DbSet<TEntity> property on a DbContext represent?",
      ["A connection string", "A transaction", "A queryable collection of entities of type TEntity, usually mapped to a table", "A migration history"], [2],
      "You write context.Customers.Where(...) using it.",
      "DbSet<T> exposes the set of entities for querying and adding/removing. It is not a connection or transaction, although it is used within them.")
    m("Easy", "Exceptions", "When does the code in a finally block run?",
      ["Only when an exception is thrown", "Only when no exception is thrown", "Only if there is a catch block", "Whether or not an exception occurs"], [3],
      "It is used for cleanup.",
      "finally runs after the try (and any catch) completes, regardless of whether an exception was thrown. It does not require a catch block; try/finally is valid on its own.")
    m("Easy", "Delegates/events", "What does the delegate type Func<int, string> represent?",
      ["A method that takes an int and returns a string", "A method that takes a string and returns an int", "A method that takes an int and returns nothing", "A property of type int"], [0],
      "In Func, the last type argument is the return type.",
      "Func<TArg, TResult> has the result type last, so this is int -> string. A method returning nothing would be Action<int>.")
    m("Easy", "Generics", "What does the constraint where T : class mean on a generic type parameter?",
      ["T must be a struct", "T must be a reference type", "T must be a class declared in the same assembly", "T must be abstract"], [1],
      "It limits the kind of types allowed, not their location.",
      "where T : class restricts T to reference types (classes, interfaces, delegates, arrays). Value types use where T : struct. It says nothing about assembly or being abstract.")
    m("Easy", "OOP", "Which keyword does a derived class use to replace the implementation of a virtual method of its base class?",
      ["new", "sealed", "override", "abstract"], [2],
      "The base method must be marked virtual, abstract or override.",
      "override provides a new implementation for a virtual member and participates in polymorphic dispatch. new merely hides the member, and sealed/abstract serve other purposes.")
    m("Easy", "OOP", "What does marking a class as sealed do?",
      ["Prevents other classes from inheriting from it", "Prevents creating instances of it", "Makes all its members static", "Makes it thread-safe"], [0],
      "Think of closing the inheritance chain.",
      "A sealed class cannot be used as a base class. It can still be instantiated (that is what abstract prevents) and its members are unaffected.")
    m("Easy", "C# basics", "What is true about a local variable declared with var?",
      ["Its type is determined at run time", "It can hold any type and change type later", "It must be a reference type", "Its type is inferred by the compiler at compile time"], [3],
      "C# remains statically typed.",
      "var asks the compiler to infer the static type from the initializer, so the variable has a fixed type afterward. It is not dynamic and works for value types too.")
    m("Easy", "Strings",     "What is the output of this string interpolation example?",
          ["x = {x}", "x = x", "$x = 5", "x = 5"], [3],
      "The $ prefix evaluates expressions inside braces.",
      "String interpolation replaces {x} with the value of the variable, so the output is x = 5. Without the $ prefix the braces would be printed literally.",
      code='int x = 5;\nConsole.WriteLine($"x = {x}");')
    m("Easy", "C# basics",     "What is printed by this integer arithmetic?",
          ["2.5 2", "3 2", "2 1", "2 2"], [3],
      "Both operands are int.",
      "Integer division truncates, so 10 / 4 is 2, and 10 % 4 is the remainder 2. Concatenation with a string yields \"2 2\". 2.5 would need a double operand.",
      code='Console.WriteLine(10 / 4 + " " + 10 % 4);')
    m("Easy", "C# basics",     "What is printed when the ?? operator is applied to a null string?",
      ["(an empty line)", "null", "none", "It throws NullReferenceException"], [2],
      "The ?? operator supplies a fallback for null.",
      "The null-coalescing operator returns the right operand when the left one is null, so \"none\" is printed. Console.WriteLine(null string) would print an empty line, but that is not what happens here.",
      code='string s = null;\nConsole.WriteLine(s ?? "none");')
    m("Easy", "LINQ",     "What does this Where/Select pipeline print?",
      ["4,16", "2,4", "1,4,9,16", "2,4,16"], [0],
      "Where filters first, then Select transforms.",
      "Where keeps the even numbers 2 and 4, and Select squares them to 4 and 16. The result is joined as 4,16. 2,4 would be the filter alone.",
      code='var r = new[] { 1, 2, 3, 4 }.Where(n => n % 2 == 0).Select(n => n * n);\nConsole.WriteLine(string.Join(",", r));')
    m("Easy", "C# basics", "Which of the following are value types in C#? (Select all that apply.)",
      ["int", "string", "DateTime", "List<int>"], [0, 2],
      "Value types include primitives and structs.",
      "int and DateTime are structs and therefore value types. string and List<int> are classes (reference types), even though string has value-like equality.")
    m("Easy", "OOP", "Which of the following are valid C# access modifiers? (Select all that apply.)",
      ["public", "internal", "protected", "friend", "package"], [0, 1, 2],
      "friend and package belong to other languages.",
      "public, internal and protected are all C# access modifiers (along with private, protected internal and private protected). friend is C++/VB and package is Java.")
    m("Easy", "DI", "Which of the following are service lifetimes supported by the built-in ASP.NET Core DI container? (Select all that apply.)",
      ["Scoped", "Static", "Singleton", "Transient"], [0, 2, 3],
      "There are exactly three lifetimes.",
      "The built-in container supports Singleton, Scoped and Transient. Static is a C# modifier but not a DI lifetime.")
    m("Easy", "Minimal APIs", "Which of these are real endpoint-mapping methods for minimal APIs? (Select all that apply.)",
      ["MapGet", "MapPost", "MapFetch", "MapDelete"], [0, 1, 3],
      "They mirror HTTP verbs.",
      "MapGet, MapPost, MapPut, MapDelete and MapPatch exist for the corresponding HTTP verbs. MapFetch is not a method; fetch is a JavaScript API.")

    # ---------------- MEDIUM (60) ----------------
    m("Medium", "Async/await", "Why is async void generally discouraged outside of event handlers?",
      ["It runs on a dedicated thread", "Callers cannot await it, and exceptions thrown inside cannot be caught by the caller", "It cannot contain await expressions", "It always executes synchronously"], [1],
      "Consider how a caller can observe completion or failure.",
      "An async void method gives the caller no Task, so completion cannot be awaited and unhandled exceptions are raised on the synchronization context, often crashing the process. It can contain await and does not use a special thread.")
    m("Medium", "Async/await", "Two tasks passed to await Task.WhenAll(t1, t2) both fault with different exceptions. What does the await expression throw?",
      ["An AggregateException containing both", "Only the first exception; the others are available on the WhenAll task's Exception property", "Nothing, because WhenAll swallows exceptions", "A TaskCanceledException"], [1],
      "await unwraps AggregateException.",
      "await rethrows only the first inner exception for convenience. The task returned by WhenAll still exposes all exceptions through its Exception (AggregateException) property. Exceptions are not swallowed.")
    m("Medium", "Async/await", "Which problems can result from blocking on an asynchronous operation with task.Result or task.Wait()? (Select all that apply.)",
      ["The awaited task is executed twice", "Thread-pool threads are tied up, which can cause starvation under load", "Exceptions are wrapped in an AggregateException", "Deadlocks in environments that have a synchronization context"], [1, 2, 3],
      "Think about threads, exceptions and contexts.",
      "Blocking holds a thread while waiting, so many concurrent requests can starve the pool. Result/Wait wrap failures in AggregateException, and where a SynchronizationContext exists (UI apps, classic ASP.NET) the continuation may need the blocked thread, causing a deadlock. The task is never run twice.")
    m("Medium", "Async/await", "What does this program print?",
      ["A B C", "B C A", "B A C", "A C B"], [2],
      "An async method runs synchronously until its first incomplete await.",
      "DoAsync starts running immediately on the calling thread and prints B, then reaches the await on Task.Delay and returns an incomplete task. The caller prints A, then awaits and C is printed after the delay.",
      code='static async Task Main()\n{\n    var t = DoAsync();\n    Console.WriteLine("A");\n    await t;\n}\n\nstatic async Task DoAsync()\n{\n    Console.WriteLine("B");\n    await Task.Delay(100);\n    Console.WriteLine("C");\n}')
    m("Medium", "Async/await", "Which statements about cancellation with CancellationToken are true? (Select all that apply.)",
      ["Cancellation is cooperative: the code must observe the token", "token.ThrowIfCancellationRequested() throws OperationCanceledException when cancellation was requested", "Calling Cancel() immediately aborts the running thread", "Task.Delay(1000, token) completes as canceled if the token is canceled during the delay"], [0, 1, 3],
      "Cancel() only sets a flag and runs callbacks.",
      "Cancellation never forcibly aborts a thread; code must check the token or pass it to APIs that do. ThrowIfCancellationRequested throws OperationCanceledException, and Task.Delay with a token ends in the canceled state (awaiting it throws TaskCanceledException, a subclass).")
    m("Medium", "Async/await", "Each call to FetchAsync takes about one second and the three calls are independent. About how long does this loop take?",
      ["About 1 second, because await runs them in parallel", "About 3 seconds, because each call is awaited before the next starts", "About 0 seconds, because nothing is awaited", "It deadlocks"], [1],
      "Look at where the await is placed.",
      "Awaiting inside the loop starts the next call only after the previous one finishes, so the calls run sequentially (~3 s). To run them concurrently you would start all tasks first and then await Task.WhenAll.",
      code='var ids = new[] { 1, 2, 3 };\nforeach (var id in ids)\n{\n    await FetchAsync(id);\n}')


    m("Medium", "LINQ",     "What does this deferred-execution query print?",
          ["2", "4", "It throws InvalidOperationException", "3"], [3],
      "The query is not executed when it is defined.",
      "Where is deferred, so the query runs when Count() is called, after 4 was added. The elements greater than 1 are 2, 3 and 4, giving 3. Modifying the list does not throw here because it is not being enumerated at that time.",
      code='var list = new List<int> { 1, 2, 3 };\nvar q = list.Where(x => x > 1);\nlist.Add(4);\nConsole.WriteLine(q.Count());')
    m("Medium", "LINQ", "For the sequence { 1, 2 }, which calls throw InvalidOperationException? (Select all that apply.)",
      ["seq.Single()", "seq.SingleOrDefault()", "seq.First()", "seq.FirstOrDefault()"], [0, 1],
      "Single variants require at most one match.",
      "Single and SingleOrDefault throw when more than one element exists (SingleOrDefault only tolerates zero). First and FirstOrDefault simply return the first element.")
    m("Medium", "LINQ",     "What does this SelectMany query print?",
          ["a b|c", "ab|c", "a|b|c", "System.String[]"], [2],
      "SelectMany flattens the inner sequences.",
      "Each string is split into an array, and SelectMany flattens the arrays into a single sequence a, b, c. Select would yield two arrays instead.",
      code='var r = new[] { "a b", "c" }.SelectMany(s => s.Split(\' \'));\nConsole.WriteLine(string.Join("|", r));')
    m("Medium", "LINQ", "What does this code print (one item per line)?",
      ["a:2 then b:1", "a:1 then b:1", "a:3", "a:2, a:2 then b:1"], [0],
      "GroupBy groups by the key selector result.",
      "GroupBy groups by first character: apple and avocado share 'a' (count 2) and banana is alone under 'b'. Groups appear in order of first occurrence.",
      code='var g = new[] { "apple", "avocado", "banana" }.GroupBy(s => s[0]);\nforeach (var x in g)\n    Console.WriteLine($"{x.Key}:{x.Count()}");')
    m("Medium", "LINQ",     "What does this OrderBy query print?",
          ["bb,cc,a,d", "d,a,cc,bb", "a,bb,cc,d", "a,d,bb,cc"], [3],
      "OrderBy is a stable sort.",
      "Items are ordered by length ascending; OrderBy is stable, so equal-length items keep their original relative order (a before d, bb before cc).",
      code='var r = new[] { "bb", "a", "cc", "d" }.OrderBy(s => s.Length);\nConsole.WriteLine(string.Join(",", r));')

    m("Medium", "Collections",     "What does this dictionary indexer code print?",
          ["2 1", "2 2", "1 2", "It throws ArgumentException"], [2],
      "The indexer setter overwrites existing keys.",
      "Assigning through the indexer adds or replaces, so the dictionary holds one entry with value 2. Only Add would throw ArgumentException for a duplicate key.",
      code='var d = new Dictionary<string, int>();\nd["a"] = 1;\nd["a"] = 2;\nConsole.WriteLine(d.Count + " " + d["a"]);')
    m("Medium", "Collections", "What happens if you call list.Remove(x) inside a foreach over the same List<T>?",
      ["The item is removed and enumeration continues safely", "The next MoveNext throws InvalidOperationException because the collection was modified", "The loop silently stops", "A compile-time error occurs"], [1],
      "List<T> tracks a version number.",
      "List<T>'s enumerator detects structural modification and throws InvalidOperationException on the next iteration. Iterate over a copy or use RemoveAll to avoid this.")
    m("Medium", "Collections", "Which of these types are safe for concurrent reads and writes from multiple threads without external locking? (Select all that apply.)",
      ["ConcurrentDictionary<TKey,TValue>", "ConcurrentQueue<T>", "List<T>", "Dictionary<TKey,TValue>"], [0, 1],
      "Look for the Concurrent prefix.",
      "The collections in System.Collections.Concurrent are designed for thread-safe use. List<T> and Dictionary<TKey,TValue> are not safe for concurrent writes.")

    m("Medium", "OOP",     "What does this virtual/override call print?",
          ["A", "AB", "It does not compile", "B"], [3],
      "Virtual dispatch uses the runtime type.",
      "N is virtual and overridden, so the call through an A reference runs B's implementation, based on the object's runtime type.",
      code='class A { public virtual string N() => "A"; }\nclass B : A { public override string N() => "B"; }\n\nA a = new B();\nConsole.WriteLine(a.N());')
    m("Medium", "OOP",     "What does this method-hiding example print?",
      ["A", "B", "AB", "It does not compile"], [0],
      "The new modifier hides rather than overrides.",
      "The method is not virtual, and new only hides the base member for callers using B. Because the variable's static type is A, A.N() is bound at compile time and returns \"A\".",
      code='class A { public string N() => "A"; }\nclass B : A { public new string N() => "B"; }\n\nA a = new B();\nConsole.WriteLine(a.N());')
    m("Medium", "OOP", "Which statements are true? (Select all that apply.)",
      ["An abstract class can declare instance fields and constructors", "A class can implement several interfaces", "An abstract class can be instantiated directly with new", "An interface can declare instance fields"], [0, 1],
      "Abstract means it needs a derived class.",
      "Abstract classes can hold state and constructors (called by derived classes) and a class can implement many interfaces. Abstract classes cannot be instantiated directly, and interfaces cannot declare instance fields.")
    m("Medium", "OOP",     "What does this struct copy example print?",
      ["1", "2", "0", "It does not compile"], [0],
      "Structs are copied on assignment.",
      "struct is a value type, so var b = a copies the data and changing b.X does not affect a. With a class both variables would reference the same object and the output would be 2.",
      code='struct P { public int X; }\n\nvar a = new P { X = 1 };\nvar b = a;\nb.X = 2;\nConsole.WriteLine(a.X);')

    m("Medium", "Generics", "What does the new() constraint on a type parameter allow?",
      ["Calling any constructor with arguments", "Creating an instance with new T(), because T must have a public parameterless constructor", "Restricting T to value types", "Allowing T to be null"], [1],
      "Only the parameterless form is expressible.",
      "where T : new() guarantees a public parameterless constructor so the generic code can write new T(). Constructors with arguments cannot be constrained this way.")
    m("Medium", "Generics",     "What does this generic Max call print?",
          ["apple", "It does not compile", "It throws ArgumentException", "banana"], [3],
      "string implements IComparable<string>.",
      "string satisfies IComparable<string>, T is inferred as string, and \"apple\".CompareTo(\"banana\") is negative so b is returned.",
      code='static T Max<T>(T a, T b) where T : IComparable<T>\n    => a.CompareTo(b) >= 0 ? a : b;\n\nConsole.WriteLine(Max("apple", "banana"));')
    m("Medium", "Generics", "Which of these are valid generic constraints in C#? (Select all that apply.)",
      ["where T : struct", "where T : class", "where T : unmanaged", "where T : sealed"], [0, 1, 2],
      "Constraints describe capabilities, not modifiers.",
      "struct, class and unmanaged are valid constraints. sealed is a class modifier, not a constraint.")

    m("Medium", "Records",     "What does this record equality code print?",
          ["True True", "False False", "True False", "False True"], [2],
      "Record equality compares members, not references.",
      "Records generate value-based == and Equals, so a == b is True, but they are still distinct objects so ReferenceEquals returns False.",
      code='record P(string Name, int Age);\n\nvar a = new P("A", 1);\nvar b = new P("A", 1);\nConsole.WriteLine((a == b) + " " + ReferenceEquals(a, b));')
    m("Medium", "Records",     "What does this with-expression code print?",
      ["1 1", "2 2", "1 2", "2 1"], [2],
      "A with-expression creates a copy.",
      "with creates a new record that is a copy of the original with the listed properties changed, leaving the original untouched, so a.Age is 1 and b.Age is 2.",
      code='record P(string Name, int Age);\n\nvar a = new P("A", 1);\nvar b = a with { Age = 2 };\nConsole.WriteLine(a.Age + " " + b.Age);')
    m("Medium", "Records", "For the declaration record P(string Name);, which statements are true? (Select all that apply.)",
      ["Equals compares the Name values", "ToString prints the member values", "Name is an init-only property, so it cannot be assigned after construction", "P is a value type"], [0, 1, 2],
      "A plain record is a class.",
      "A positional record class gets value equality, a printing ToString and init-only properties. A record without struct is a reference type; record struct would be the value type.")

    m("Medium", "Nullable reference types", "What is the effect of enabling nullable reference types in a project?",
      ["Reference types can no longer hold null at run time", "The compiler produces nullability warnings; no runtime checks are added", "All strings become Nullable<string>", "Null dereferences throw a different exception"], [1],
      "It is a static analysis feature.",
      "Nullable reference types are annotations used by compiler flow analysis to warn about possible null dereferences. They do not change runtime behavior and string? is not Nullable<string>.")
    m("Medium", "Nullable reference types", "What does the null-forgiving operator (!) do in expressions like user!.Name?",
      ["Throws if user is null", "Suppresses the compiler's nullable warning without any runtime null check", "Converts null to an empty object", "Makes user non-nullable at run time"], [1],
      "It only silences the compiler.",
      "The ! operator tells the compiler to treat the expression as non-null; it emits no check, so a null value still causes NullReferenceException at the dereference.")
    m("Medium", "Nullable reference types",     "What does this null-conditional code print?",
      ["0", "null", "-1", "It throws NullReferenceException"], [2],
      "?. short-circuits to null.",
      "s?.Length evaluates to a null int?, and ?? supplies -1. No exception occurs because of the null-conditional operator.",
      code='#nullable enable\nstring? s = null;\nConsole.WriteLine(s?.Length ?? -1);')

    m("Medium", "Pattern matching",     "What does this switch expression print?",
      ["intbignull", "intintnull", "bigbignull", "othersbigother"], [0],
      "Switch expression arms are evaluated top to bottom.",
      "5 is an int but fails the guard, so it matches the int arm; 50 matches the guarded arm and gives big; null matches the null arm.",
      code='static string F(object o) => o switch\n{\n    int n when n > 10 => "big",\n    int => "int",\n    string s => s,\n    null => "null",\n    _ => "other"\n};\n\nConsole.WriteLine(F(5) + F(50) + F(null));')
    m("Medium", "Pattern matching",     "What does this property pattern code print?",
      ["True", "False", "It does not compile", "It throws InvalidCastException"], [0],
      "A property pattern tests type and members together.",
      "o is P { Age: >= 18 } checks that o is a P and that its Age satisfies the relational pattern. The age is 20, so the result is True.",
      code='record P(string Name, int Age);\n\nobject o = new P("A", 20);\nConsole.WriteLine(o is P { Age: >= 18 });')
    m("Medium", "Pattern matching", "What happens when a switch expression receives a value that none of its arms match and there is no discard arm?",
      ["It returns default", "It throws a SwitchExpressionException at run time", "It falls through to the next arm", "It silently returns null"], [1],
      "Switch expressions must produce a value.",
      "The compiler may warn the switch is not exhaustive, and if no arm matches at run time a SwitchExpressionException is thrown. There is no fall-through or default result.")

    m("Medium", "ASP.NET Core", "Why does the order of middleware registration in Program.cs matter?",
      ["Middleware executes in the order registered for requests, and in reverse order for responses", "Middleware always executes alphabetically", "Only the last registered middleware runs", "Order matters only in Production"], [0],
      "It forms a pipeline.",
      "Each middleware decides whether to call the next one, and code after await next() runs on the way back. For example UseAuthentication must precede UseAuthorization.")
    m("Medium", "ASP.NET Core", "What is the order of the console output for one request to this pipeline?",
      ["1 in, handler, 1 out", "handler, 1 in, 1 out", "1 in, 1 out, handler", "1 in, handler"], [0],
      "Code after next() runs after later middleware returns.",
      "The Use middleware prints 1 in, calls next (reaching the terminal Run handler which prints handler), then resumes and prints 1 out.",
      code='app.Use(async (ctx, next) =>\n{\n    Console.WriteLine("1 in");\n    await next();\n    Console.WriteLine("1 out");\n});\n\napp.Run(async ctx =>\n{\n    Console.WriteLine("handler");\n    await ctx.Response.WriteAsync("hi");\n});')
    m("Medium", "ASP.NET Core", "Which of the following are valid ways to implement middleware? (Select all that apply.)",
      ["Inline with app.Use(async (ctx, next) => ...)", "A class with a RequestDelegate constructor parameter and an Invoke/InvokeAsync(HttpContext) method", "A class implementing IMiddleware", "A class decorated with a [Middleware] attribute"], [0, 1, 2],
      "No special attribute exists for middleware.",
      "Inline delegates, conventional middleware classes and IMiddleware implementations are all supported. There is no [Middleware] attribute.")
    m("Medium", "ASP.NET Core", "In conventional (convention-based) middleware, where should you inject a scoped service such as a DbContext?",
      ["In the constructor", "As a parameter of the InvokeAsync method", "In a static field", "It cannot be injected"], [1],
      "The middleware instance is created once at startup.",
      "Conventional middleware is constructed once, so constructor dependencies behave as singletons. Scoped services should be taken as InvokeAsync parameters, which are resolved per request.")
    m("Medium", "ASP.NET Core", "Where in the pipeline should exception-handling middleware such as UseExceptionHandler normally be placed?",
      ["As early as possible so it wraps later middleware", "After UseEndpoints", "Last, after all other middleware", "It must be inside every controller"], [0],
      "It can only catch exceptions from middleware after it.",
      "Middleware wraps the ones registered after it, so the exception handler should be registered first to catch their exceptions.")
    m("Medium", "ASP.NET Core", "Which statement about app.Run(...) is correct?",
      ["It starts the web host", "It adds terminal middleware that does not call the next delegate", "It runs a handler only for POST requests", "It runs after the response is sent"], [1],
      "Compare with app.Use.",
      "app.Run registers a terminal middleware, with no next parameter. app.Run() with no arguments starts the host, which is a different overload.")
    m("Medium", "ASP.NET Core", "Which are benefits of using IHttpClientFactory instead of creating a new HttpClient for every request? (Select all that apply.)",
      ["Handlers are pooled, which avoids socket exhaustion", "HTTP calls become synchronous", "Handlers are recycled periodically so DNS changes are picked up", "It is required to call HTTPS endpoints"], [0, 2],
      "Think about the HttpMessageHandler lifetime.",
      "Creating many HttpClient instances can exhaust sockets, while a single static one can hold stale DNS. The factory manages pooled handlers with periodic recycling. It does not change sync behavior and HTTPS works without it.")

    m("Medium", "Configuration", "By default in ASP.NET Core, which configuration source has the highest precedence when the same key is defined in several places?",
      ["appsettings.json", "appsettings.Development.json", "Environment variables", "Command-line arguments"], [3],
      "Later sources override earlier ones.",
      "The default order is appsettings.json, appsettings.{Environment}.json, user secrets (in Development), environment variables, then command-line arguments, and later providers win.")
    m("Medium", "Configuration", "A singleton service must see updated settings after appsettings.json changes without restarting the app. Which options type is appropriate?",
      ["IOptions<T>", "IOptionsSnapshot<T>", "IOptionsMonitor<T>", "A static field"], [2],
      "Snapshot is scoped, so it cannot be injected into a singleton.",
      "IOptionsMonitor<T> is a singleton that gives current values and change notifications. IOptions<T> is computed once, and IOptionsSnapshot<T> is scoped, so it cannot be injected into singletons.")
    m("Medium", "Configuration", "How is the configuration key Logging:LogLevel:Default set through an environment variable?",
      ["Logging:LogLevel:Default always works on every OS", "Logging__LogLevel__Default", "Logging.LogLevel.Default", "LOGGING-LOGLEVEL-DEFAULT"], [1],
      "Colons are not portable in environment variable names.",
      "A double underscore is translated into the configuration key separator by the environment variables provider. The colon form works only on some platforms.")

    m("Medium", "Logging", "Why is logger.LogInformation(\"User {UserId} logged in\", id) preferred over logger.LogInformation($\"User {id} logged in\")?",
      ["Interpolation does not compile", "The message template keeps UserId as a structured property and avoids formatting work when the level is disabled", "Interpolation is slower only on Linux", "The template version writes to a file"], [1],
      "Think of structured logging sinks.",
      "Named placeholders let providers capture values as structured data and format lazily. An interpolated string is built eagerly and loses the structure. Both compile.")
    m("Medium", "Logging", "The minimum log level is Warning. Which of these calls produce output? (Select all that apply.)",
      ["LogInformation", "LogWarning", "LogError", "LogDebug"], [1, 2],
      "Levels order: Trace, Debug, Information, Warning, Error, Critical.",
      "Only messages at or above the minimum level are written, so Warning and Error are output. Information and Debug are lower.")
    m("Medium", "Logging", "What is the correct way to log an exception with its stack trace using ILogger?",
      ["logger.LogError(ex.Message)", "logger.LogError(ex, \"Failed to process order {OrderId}\", id)", "logger.LogError(\"Failed: \" + ex.ToString().Length)", "Console.WriteLine(ex)"], [1],
      "Pass the exception as the first argument.",
      "The overload taking Exception first lets providers record the full exception and details. Logging only Message loses the stack trace and Console.WriteLine bypasses the logging system.")

    m("Medium", "Minimal APIs", "In app.MapGet(\"/users/{id}\", (int id) => ...), where does id come from?",
      ["The route value", "The request body", "A header", "A DI service"], [0],
      "The name matches a route template parameter.",
      "A simple parameter whose name matches a route template segment is bound from the route. Complex types on POST are bound from the body and services from DI.")
    m("Medium", "Minimal APIs", "In app.MapPost(\"/items\", (Item item) => ...), where Item is a class, how is item bound?",
      ["From the JSON request body", "From the query string", "From a route value", "From a cookie"], [0],
      "Complex types are read from the body by default.",
      "For POST/PUT/PATCH handlers, a complex type parameter that is not a registered service is bound from the JSON body. Use [FromQuery] etc. to override.")

    m("Medium", "DI", "A singleton service takes a scoped service in its constructor. What happens when scope validation is enabled (default in Development)?",
      ["It works and the scoped service is created per request", "The container throws InvalidOperationException when resolving", "The singleton becomes scoped", "The scoped service becomes transient"], [1],
      "The singleton would capture a short-lived dependency.",
      "Injecting a scoped service into a singleton is a captive dependency, as the scoped instance would live as long as the singleton. Scope validation detects it and throws.")
    m("Medium", "DI",     "What does this scoped-lifetime code print?",
          ["True True", "False True", "False False", "True False"], [3],
      "Scoped means one instance per scope.",
      "Within the same scope the same instance is returned (a == b), but a different scope gets its own instance, so a == c is False.",
      code='var services = new ServiceCollection();\nservices.AddScoped<Foo>();\nvar sp = services.BuildServiceProvider();\n\nusing var s1 = sp.CreateScope();\nusing var s2 = sp.CreateScope();\nvar a = s1.ServiceProvider.GetRequiredService<Foo>();\nvar b = s1.ServiceProvider.GetRequiredService<Foo>();\nvar c = s2.ServiceProvider.GetRequiredService<Foo>();\nConsole.WriteLine((a == b) + " " + (a == c));\n\nclass Foo { }')
    m("Medium", "DI", "IFoo is registered twice: AddTransient<IFoo, A>() then AddTransient<IFoo, B>(). What do GetRequiredService<IFoo>() and GetServices<IFoo>() return?",
      ["Error for both calls because of ambiguity", "B for the single resolution; both A and B for the collection", "A for the single resolution; only B for the collection", "Both return a list of A and B"], [1],
      "Later registrations override earlier ones for single resolution.",
      "The last registration wins for a single resolve, while resolving IEnumerable<IFoo> returns all registrations in order. There is no ambiguity error.")
    m("Medium", "DI", "Which statements about service disposal in the built-in container are true? (Select all that apply.)",
      ["IDisposable services created by the container are disposed when their scope or the provider is disposed", "Instances passed to AddSingleton(instance) are not disposed by the container", "Singleton services are disposed at the end of each request", "The container never disposes anything"], [0, 1],
      "Ownership matters: who created the object?",
      "The container disposes what it creates, at the end of its owning scope or provider. Instances you supply yourself are left to you. Singletons live until the root provider is disposed.")

    m("Medium", "EF Core", "Which techniques reduce overhead for a read-only query whose results will not be modified? (Select all that apply.)",
      ["Calling Include() for every navigation property", "AsNoTracking()", "Calling SaveChanges() after the query", "Projecting only the needed columns with Select()"], [1, 3],
      "Avoid tracking and avoid loading unneeded data.",
      "AsNoTracking skips change tracking and identity resolution, and a projection fetches only the columns you need (projected non-entity results are not tracked at all). Loading every navigation does more work, and SaveChanges is irrelevant to reading.")
    m("Medium", "EF Core", "What is the N+1 query problem in EF Core?",
      ["One query to load the parent entities, plus one additional query per parent to load related data", "Running N queries in one transaction", "Using more than one DbContext", "Having N tables with one foreign key"], [0],
      "Related data is loaded lazily in a loop.",
      "Iterating over parents and touching a navigation (e.g. with lazy loading) issues extra queries per item. Using Include or a projection loads everything in a few queries.")
    m("Medium", "EF Core", "After loading a User entity and changing only its Name property, SaveChangesAsync is called. What SQL does EF Core generate?",
      ["An INSERT of the whole entity", "An UPDATE that sets only the modified column(s)", "A DELETE followed by an INSERT", "No SQL because it only works with AsNoTracking"], [1],
      "The change tracker knows what changed.",
      "Tracked entities have their property changes detected, and EF Core emits an UPDATE with only the modified columns. Tracking is what makes this possible; AsNoTracking would prevent it.",
      code='var u = await db.Users.FirstAsync(x => x.Id == 1);\nu.Name = "New";\nawait db.SaveChangesAsync();')
    m("Medium", "EF Core", "Which of these calls cause the query to be executed against the database immediately? (Select all that apply.)",
      ["ToListAsync()", "Where(x => x.Active)", "CountAsync()", "Select(x => x.Name)"], [0, 2],
      "Operators that return IQueryable are lazy.",
      "ToListAsync and CountAsync materialize a result and run the query. Where and Select only compose a deferred IQueryable.")
    m("Medium", "EF Core", "What is the default lifetime of a DbContext registered with AddDbContext, and why does it matter?",
      ["Scoped; a DbContext is not thread-safe and should not be shared across concurrent requests", "Singleton; it caches data forever", "Transient; a new one per call", "Static; shared across the process"], [0],
      "Think of one unit of work per request.",
      "AddDbContext registers it as scoped, so each request gets its own instance. DbContext is not thread-safe, so a singleton would break under concurrency.")
    m("Medium", "EF Core", "A row has a rowversion/[Timestamp] concurrency token and another user updated it after you loaded it. What does SaveChanges do?",
      ["Silently overwrites the other user's change", "Throws DbUpdateConcurrencyException", "Merges the changes automatically", "Rolls back the other user's update"], [1],
      "EF adds the token to the WHERE clause.",
      "The UPDATE includes the original token in its WHERE clause, affects zero rows, and EF throws DbUpdateConcurrencyException. It does not merge or overwrite the other change.")

    m("Medium", "Exceptions",     "What does this try/catch/finally code print?",
          ["TCE", "TFCE", "TCFE", "TCF"], [2],
      "finally runs before control continues after the try statement.",
      "T is written, the exception is caught (C), finally runs (F) and then execution continues after the try statement (E).",
      code='try\n{\n    Console.Write("T");\n    throw new Exception();\n}\ncatch\n{\n    Console.Write("C");\n}\nfinally\n{\n    Console.Write("F");\n}\nConsole.Write("E");')

    m("Medium", "Delegates/events",     "What does this event code print?",
          ["hi", "HI", "Nothing, because events need a null check", "hiHI"], [3],
      "Both handlers are subscribed.",
      "Invoke calls all subscribed handlers in subscription order, so hi followed by HI is printed. The null-conditional Invoke handles the case of no subscribers.",
      code='class Pub\n{\n    public event Action<string>? Raised;\n    public void Fire() => Raised?.Invoke("hi");\n}\n\nvar p = new Pub();\np.Raised += s => Console.Write(s);\np.Raised += s => Console.Write(s.ToUpper());\np.Fire();')
    m("Medium", "Delegates/events",     "What does this closure-in-a-for-loop code print?",
          ["012", "123", "333", "It throws"], [2],
      "How many i variables does a for loop create?",
      "A for loop declares a single i shared by all closures, which has the value 3 once the loop ends, so 333 is printed. A foreach iteration variable is per-iteration.",
      code='var acts = new List<Action>();\nfor (int i = 0; i < 3; i++)\n    acts.Add(() => Console.Write(i));\nforeach (var a in acts) a();')

    m("Medium", "Strings",     "What does this Substring and indexer code print?",
      ["bc", "b", "c", "It does not compile"], [0],
      "string + char produces a string.",
      "Substring(1, 1) is \"b\", and \"abc\"[2] is the char 'c'. Concatenating string and char gives \"bc\".",
      code='Console.WriteLine("abc".Substring(1, 1) + "abc"[2]);')

    m("Medium", "Memory", "Which restriction applies to Span<T>?",
      ["It can only hold reference types", "It is a ref struct, so it cannot be a class field or be used across await in an async method", "It always allocates on the heap", "It can only be used with arrays"], [1],
      "It must live on the stack.",
      "Span<T> is a ref struct restricted to the stack, so it cannot be stored in a class field, boxed or kept across an await. It can wrap arrays, stack memory and native memory and works with any T.")
