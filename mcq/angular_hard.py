def add(m):
    H = "Hard"

    # ---------------- RxJS operators ----------------
    m(H, "RxJS operators",
      "Given the code, when does the subscriber receive values?",
      ["'A' at about 100 ms and 'B' at about 150 ms",
       "'A' and 'B' both at about 150 ms",
       "Only 'B', about 150 ms after subscribing",
       "Only 'A', at about 100 ms"],
      [2],
      "Think about what switchMap does to the in-flight inner observable when a new source value arrives.",
      "At t=50ms 'B' arrives while the inner timer for 'A' (due at 100ms) is still pending, so switchMap unsubscribes from it and 'A' is never emitted. The new inner timer for 'B' fires at 50+100=150ms. mergeMap or concatMap would have produced both values.",
      """const source$ = merge(of('A'), of('B').pipe(delay(50)));
source$
  .pipe(switchMap(v => timer(100).pipe(map(() => v))))
  .subscribe(console.log);""")

    m(H, "RxJS operators",
      "What is logged by this code?",
      ["1, 2, 3",
       "3, 2, 1",
       "Only 3",
       "Only 1"],
      [1],
      "mergeMap does not wait for earlier inner observables; the fastest inner emits first.",
      "mergeMap subscribes to all inner observables concurrently, and emits as each inner emits. The timers are 300ms, 200ms and 100ms for 1, 2 and 3, so the output is 3, 2, 1. concatMap would queue them and log 1, 2, 3.",
      """of(1, 2, 3)
  .pipe(mergeMap(n => timer((4 - n) * 100).pipe(map(() => n))))
  .subscribe(console.log);""")

    m(H, "RxJS operators",
      "Which statements about concatMap are true? (Select all that apply.)",
      ["It queues source values and subscribes to each inner observable only after the previous one completes.",
       "It behaves like mergeMap with a concurrency limit of 1.",
       "It unsubscribes from the active inner observable when a new source value arrives.",
       "Output order follows source order even if a later inner observable would finish faster.",
       "It drops source values that arrive while an inner observable is still active."],
      [0, 1, 3],
      "Compare it with switchMap (cancels) and exhaustMap (drops).",
      "concatMap buffers outer values and runs inner observables strictly one at a time, so ordering is preserved and it equals mergeMap(fn, 1). Cancelling the active inner is switchMap's behavior, and dropping values while busy is exhaustMap's.",
      None)

    m(H, "RxJS operators",
      "A Save button's click$ stream must ignore further clicks while a save request is still in flight, without cancelling that request. Which operator fits best?",
      ["switchMap",
       "concatMap",
       "exhaustMap",
       "mergeMap"],
      [2],
      "You want new outer values discarded, not queued or cancelling.",
      "exhaustMap ignores source values while its current inner observable is active, which prevents double submits. switchMap would cancel the first request, concatMap would queue and send duplicates afterwards, and mergeMap would send them all concurrently.",
      None)

    m(H, "RxJS operators",
      "Which statements about source$.pipe(withLatestFrom(other$)) are true? (Select all that apply.)",
      ["It emits only when source$ emits, paired with the latest value of other$.",
       "Source emissions that occur before other$ has emitted for the first time are dropped.",
       "It emits whenever either source$ or other$ emits, like combineLatest.",
       "It completes as soon as other$ completes.",
       "It subscribes to other$ only after source$ emits its first value."],
      [0, 1],
      "Only one of the two streams drives emissions.",
      "withLatestFrom is driven by the source: it subscribes to other$ at subscription time and emits only on source emissions once other$ has a value. Earlier source values are silently lost. Completion of other$ does not complete the result, and it is not combineLatest.",
      None)

    m(H, "RxJS operators",
      "Which describes forkJoin([a$, b$])?",
      ["It emits every time either source emits, using the latest values.",
       "It emits pairs of values by index, waiting for both at each index.",
       "It emits the first value of each source as soon as both have emitted.",
       "It emits one array of each source's last value after all sources complete; if any completes without emitting, it completes without emitting."],
      [3],
      "Think of Promise.all semantics: nothing happens until completion.",
      "forkJoin waits for every source to complete and then emits the last value from each exactly once. The first option is combineLatest, the second is zip, and the third is not an RxJS operator behavior. A source that never completes keeps forkJoin from emitting.",
      None)

    m(H, "RxJS operators",
      "Which statements about debounceTime(300), throttleTime(300) and auditTime(300) are true? (Select all that apply.)",
      ["debounceTime emits the most recent value only after 300 ms pass with no new source values.",
       "throttleTime by default emits the first value of a window and ignores the others in that window.",
       "debounceTime emits the first value immediately and then silences the stream for 300 ms.",
       "auditTime emits the first value of each window immediately when it arrives."],
      [0, 1],
      "Leading versus trailing edge behavior distinguishes them.",
      "debounce is trailing and resets on each value; throttleTime defaults to leading edge. auditTime is trailing: it emits the latest value when the window ends, not the first immediately. The third option describes a leading throttle, not debounce.",
      None)

    m(H, "RxJS operators",
      "What is the problem with this typeahead pipeline?",
      ["After the first HTTP error the outer stream is terminated; catchError should be placed inside the switchMap's inner pipe.",
       "catchError never runs because HttpClient errors are not delivered as observable errors.",
       "switchMap swallows errors, so catchError is unreachable.",
       "of([]) emits asynchronously, which reorders results."],
      [0],
      "Where does an error end the subscription: on the outer or inner chain?",
      "An error propagates to the outer pipeline, catchError then replaces it with of([]) which completes, so no further searches are processed. Putting catchError on the inner request keeps the outer search$ alive. HttpClient does emit errors via the error channel and switchMap does not swallow them.",
      """this.search$.pipe(
  switchMap(q => this.http.get<Item[]>(`/api?q=${q}`)),
  catchError(() => of([]))
).subscribe(items => this.items = items);""")

    # ---------------- RxJS multicasting / hot-cold ----------------
    m(H, "RxJS multicasting",
      "In RxJS 7, what does source$.pipe(shareReplay(1)) do when all subscribers unsubscribe before the source completes?",
      ["The source subscription is torn down immediately.",
       "It resets and re-subscribes to the source when a new subscriber arrives.",
       "It throws an unsubscription error on the next subscribe.",
       "The source stays subscribed (refCount is false by default) and the latest value is replayed to future subscribers."],
      [3],
      "The refCount behavior is opt-in.",
      "shareReplay(1) with default config keeps the underlying subscription alive after subscribers leave, which can leak long-lived sources. Use shareReplay({ bufferSize: 1, refCount: true }) to tear down when subscribers reach zero. It does not throw or reset by default.",
      None)

    m(H, "RxJS multicasting",
      "What is logged?",
      ["A 1, A 2, A 3, B 3",
       "A 2, A 3, B 2, B 3",
       "A 2, A 3, B 3",
       "A 1, A 2, B 2, A 3, B 3"],
      [2],
      "A plain Subject does not store past values.",
      "A Subject is hot and has no replay: A misses 1 because it subscribed after next(1), and B misses 1 and 2. A receives 2 and 3, B receives only 3. A ReplaySubject or BehaviorSubject would behave differently.",
      """const s = new Subject<number>();
s.next(1);
s.subscribe(v => console.log('A', v));
s.next(2);
s.subscribe(v => console.log('B', v));
s.next(3);""")

    m(H, "RxJS multicasting",
      "Where should takeUntil(destroy$) be placed to avoid leaking inner subscriptions in a pipe that uses switchMap?",
      ["Immediately after the source, before switchMap.",
       "Anywhere; operator order never matters for takeUntil.",
       "Only inside the inner observable.",
       "As the last operator, after switchMap/mergeMap."],
      [3],
      "A takeUntil placed early completes the outer, but the inner may still be running.",
      "If takeUntil precedes switchMap, completing the outer does not unsubscribe a still-active inner observable, which can keep emitting. Placing it last unsubscribes from the whole upstream chain including inners. Order does matter.",
      None)

    m(H, "RxJS multicasting",
      "A template uses `data$ | async` twice for `data$ = this.http.get<Item[]>('/api/items')`. Which statements are true? (Select all that apply.)",
      ["Two HTTP requests are sent because the observable is cold and each async pipe subscribes separately.",
       "Adding shareReplay({ bufferSize: 1, refCount: true }) to data$ makes both pipes share one request.",
       "Using `@if (data$ | async; as data)` once and referencing `data` reduces it to one subscription.",
       "Setting the component to OnPush deduplicates the request."],
      [0, 1, 2],
      "Change detection strategy does not affect how many times an observable is subscribed.",
      "HttpClient observables are cold, so each subscription triggers a request. Multicasting with shareReplay or subscribing once with an alias fixes it. OnPush only affects when views are checked, not subscriptions.",
      None)

    m(H, "RxJS multicasting",
      "Why does this distinctUntilChanged() not suppress duplicate emissions when the form values are identical?",
      ["Each valueChanges emission is a new object, and the default comparison uses reference equality; supply a comparator.",
       "distinctUntilChanged only works on primitive streams created with of().",
       "valueChanges is a Subject so distinct operators are ignored.",
       "distinctUntilChanged needs a debounceTime before it to work."],
      [0],
      "Think about how === compares two objects with equal content.",
      "The default comparator is ===, so two different objects with the same content are considered distinct. Pass a comparator such as (a, b) => JSON.stringify(a) === JSON.stringify(b) or use a field-level comparison. The operator works on any type; it is just reference-based by default.",
      """this.form.valueChanges.pipe(
  distinctUntilChanged()
).subscribe(v => this.save(v));""")

    m(H, "RxJS interop",
      "What does this log?",
      ["0, 1, 2, 3",
       "3",
       "0 and then 3",
       "1, 2, 3"],
      [1],
      "toObservable relies on an effect, which is scheduled rather than synchronous.",
      "toObservable emits via an effect that runs during change detection, so the three synchronous sets are coalesced and the subscriber sees the latest value only. It does not emit the intermediate values or the stale initial one.",
      """count = signal(0);
constructor() {
  toObservable(this.count).subscribe(console.log);
  this.count.set(1);
  this.count.set(2);
  this.count.set(3);
}""")

    m(H, "RxJS interop",
      "What happens when takeUntilDestroyed() is called without arguments inside ngOnInit?",
      ["It works because ngOnInit runs in the component's injection context.",
       "It unsubscribes at the next change detection.",
       "It throws because it is not in an injection context; pass a DestroyRef instead.",
       "It silently does nothing and the subscription leaks."],
      [2],
      "inject(DestroyRef) is used internally.",
      "takeUntilDestroyed() calls inject(DestroyRef) when no argument is given, which fails outside an injection context such as ngOnInit. Capture destroyRef = inject(DestroyRef) in a field and pass it: takeUntilDestroyed(this.destroyRef). It does not silently leak; it throws.",
      """ngOnInit() {
  this.data$.pipe(takeUntilDestroyed()).subscribe();
}""")

    m(H, "RxJS interop",
      "Which statements about toSignal() are true? (Select all that apply.)",
      ["It subscribes immediately and unsubscribes automatically when the calling injection context is destroyed.",
       "Without initialValue, the resulting signal's type includes undefined until the first emission.",
       "requireSync: true is valid for sources that emit synchronously on subscribe, such as BehaviorSubject.",
       "It can be called anywhere, such as inside a click handler, with no injector.",
       "It subscribes lazily on the first read of the signal."],
      [0, 1, 2],
      "Think about injection context and eager subscription.",
      "toSignal subscribes eagerly, ties cleanup to the injection context, and adds undefined to the type unless initialValue or requireSync is set. It must be called in an injection context (or given an injector), and it is not lazy.",
      None)

    # ---------------- Signals ----------------
    m(H, "Signals",
      "Which statements about this computed are true? (Select all that apply.)",
      ["It is lazy: the callback does not run until value() is first read.",
       "While flag() is true, changing b() does not invalidate value.",
       "After a.set(5), the callback re-executes immediately even if nobody reads value().",
       "Reading value() twice with no dependency changes runs the callback once."],
      [0, 1, 3],
      "Computed signals are lazily evaluated, memoized, and track dependencies dynamically.",
      "computed runs only on demand, caches its result, and tracks just the signals read in the last execution; b is not read when flag is true. A change to a dependency only marks it dirty, and recomputation waits for the next read.",
      """flag = signal(true);
a = signal(1);
b = signal(2);
value = computed(() => {
  console.log('run');
  return this.flag() ? this.a() : this.b();
});""")

    m(H, "Signals",
      "What happens with the effect after this code runs?",
      ["The effect does not re-run because the same object reference is set, so signal equality (Object.is) sees no change.",
       "The effect re-runs and logs 'B'.",
       "The effect re-runs only on the next change detection tick.",
       "set() throws because mutating signal values is not allowed."],
      [0],
      "Signals compare values using Object.is by default.",
      "The object was mutated in place and set with the same reference, so the signal considers the value unchanged and notifies no consumers. Use update(u => ({...u, name: 'B'})) to create a new reference. Signals do not throw on mutation but they do not detect it.",
      """user = signal({ name: 'A' });
constructor() {
  effect(() => console.log(this.user().name));
}
rename() {
  const u = this.user();
  u.name = 'B';
  this.user.set(u);
}""")

    m(H, "Signals",
      "Which signal change causes this effect to re-run?",
      ["Only changes to query()",
       "Changes to either query() or user()",
       "Only changes to user()",
       "Neither; effects never re-run"],
      [0],
      "untracked() suppresses dependency tracking inside its callback.",
      "user() is read inside untracked(), so it is not recorded as a dependency; only query() is tracked. Effects do re-run when tracked dependencies change.",
      """effect(() => {
  const q = this.query();
  untracked(() => this.log.record(q, this.user()));
});""")

    m(H, "Signals",
      "What happens when this component is created?",
      ["It logs undefined.",
       "It throws NG0950 because the required input has no value yet during construction.",
       "It logs an empty string.",
       "It logs the parent's bound value."],
      [1],
      "Inputs are set after the instance is constructed.",
      "A required signal input throws if read before the parent binding has been set, and the constructor runs before inputs are assigned. Read it in a computed, effect or later lifecycle hook instead.",
      """name = input.required<string>();
constructor() {
  console.log(this.name());
}""")

    m(H, "Signals",
      "Which statements about model() are true? (Select all that apply.)",
      ["It declares an input and a matching output named <name>Change.",
       "The child can call .set() on it and a parent bound with [(value)] receives the update.",
       "It is read-only like input().",
       "[(value)] on the parent side can bind to a writable signal.",
       "It cannot be declared as required."],
      [0, 1, 3],
      "It is a writable signal designed for two-way binding.",
      "model() combines an input with a change output and is writable by the child. Parent two-way binding works with writable signals or property expressions. It is not read-only, and model.required() exists.",
      None)

    m(H, "Signals",
      "What does selected() return at the end?",
      ["'b'",
       "'x'",
       "'y'",
       "undefined"],
      [1],
      "linkedSignal resets whenever its source signal changes.",
      "linkedSignal is writable, but when its source (options) changes it recomputes, discarding the manual 'b'. The recomputation yields options()[0], which is 'x'.",
      """options = signal(['a', 'b']);
selected = linkedSignal(() => this.options()[0]);

this.selected.set('b');
this.options.set(['x', 'y']);
console.log(this.selected());""")

    m(H, "Signals",
      "An OnPush component reads count() in its template. A service calls count.set() inside a setTimeout. What happens?",
      ["The view is stale until a parent input changes.",
       "The view is stale until markForCheck() is called.",
       "An ExpressionChangedAfterItHasBeenChecked error is thrown.",
       "The view updates because signal reads in the template mark the view for refresh when the value changes."],
      [3],
      "Signals integrate with the reactive consumer of the template.",
      "A template that reads a signal becomes a reactive consumer; when the signal changes, Angular marks the view for refresh even under OnPush. No manual markForCheck is needed, and no NG0100 error occurs since the change happens outside a CD pass.",
      None)

    m(H, "Signals",
      "What does reading the view query signal in the constructor log?",
      ["The ElementRef of the canvas.",
       "null",
       "undefined, because the query result is not available during construction; use an effect or afterNextRender to read it.",
       "It throws NG0950."],
      [2],
      "View queries resolve after the view is created.",
      "Signal-based queries return undefined until the view is created; the constructor runs before that. Read them in effect(), afterNextRender() or later hooks. They do not throw for an optional viewChild and do not return null.",
      """chart = viewChild<ElementRef>('chart');
constructor() {
  console.log(this.chart());
}""")

    m(H, "Signals",
      "When is the cleanup function registered with onCleanup invoked?",
      ["Only when the component is destroyed.",
       "Before the effect re-runs and when the effect is destroyed.",
       "After every change detection pass.",
       "Only if the effect throws."],
      [1],
      "Think of clearing an interval between runs.",
      "Cleanup runs before each subsequent execution of the effect and when it is destroyed, which suits timers and subscriptions that depend on the signal value. It is not tied to CD passes or errors.",
      """effect(onCleanup => {
  const id = setInterval(() => this.tick(), this.ms());
  onCleanup(() => clearInterval(id));
});""")

    m(H, "Signals",
      "How many times, and with what value, does this effect log?",
      ["Three times: 0, 1, 2",
       "Twice: 0, 2",
       "Once: 'count 2'",
       "Never, since effects only run after user events"],
      [2],
      "Component effects run during change detection, not synchronously on set().",
      "A component effect is scheduled to run during change detection, so by its first execution count is already 2, and intermediate values are never observed. Effects are asynchronous and batched, unlike RxJS subscriptions.",
      """count = signal(0);
constructor() {
  effect(() => console.log('count', this.count()));
  this.count.set(1);
  this.count.set(2);
}""")

    # ---------------- Change detection ----------------
    m(H, "Change detection",
      "Which of these cause an OnPush component to be checked? (Select all that apply.)",
      ["The parent binds a new object reference to one of its @Input()s.",
       "A DOM event handler declared in its own template fires.",
       "The parent mutates a property of the same object passed to the @Input().",
       "A setTimeout inside the component changes a plain field.",
       "An observable bound with the async pipe in its template emits."],
      [0, 1, 4],
      "OnPush needs a reference change, an event from within, an async pipe/signal notification, or an explicit mark.",
      "OnPush views are checked on input reference changes, template event handlers, async pipe emissions (which call markForCheck) and signals. Mutating an input object in place or changing a plain field from a timer does not mark the view dirty.",
      None)

    m(H, "Change detection",
      "Why does the child list not update after add() is called?",
      ["push() mutates the array in place, so the OnPush child's input reference is unchanged; use a new array.",
       "OnPush components cannot render arrays.",
       "The @for block requires trackBy to render new items.",
       "Parent change detection is disabled once a child is OnPush."],
      [0],
      "OnPush compares input references.",
      "The child only re-checks when the bound reference changes; push() keeps the same array. Assigning this.names = [...this.names, 'x'] works. OnPush does not block rendering arrays or the parent's own CD.",
      """// child
@Component({
  selector: 'app-list',
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `@for (i of items; track i) { <li>{{ i }}</li> }`
})
class ListComponent { @Input() items: string[] = []; }

// parent
add() { this.names.push('x'); }""")

    m(H, "Change detection",
      "What happens in development mode when this component is first rendered?",
      ["It throws ExpressionChangedAfterItHasBeenChecked (NG0100) because a binding changed after it was checked.",
       "No error; the view shows 'Loaded' immediately.",
       "The error only occurs in production builds.",
       "It causes an infinite change detection loop."],
      [0],
      "Dev mode runs a second verification pass.",
      "ngAfterViewInit runs after the view's bindings were evaluated, so the dev-mode check pass sees title differing from the previously rendered value and throws NG0100. It does not occur only in production and does not loop.",
      """@Component({ selector: 'app-x', template: `{{ title }}` })
class X implements AfterViewInit {
  title = 'Initial';
  ngAfterViewInit() { this.title = 'Loaded'; }
}""")

    m(H, "Change detection",
      "A field bound in the template is set from a @ViewChild value in ngAfterViewInit, causing NG0100. Which fixes work? (Select all that apply.)",
      ["Inject ChangeDetectorRef and call detectChanges() right after assigning.",
       "Defer the assignment with Promise.resolve().then(...) so a later CD pass renders it.",
       "Call markForCheck() after assigning.",
       "Move the assignment to ngAfterViewChecked."],
      [0, 1],
      "Either re-render synchronously or move the change into a later turn.",
      "detectChanges() re-evaluates the view immediately, and a microtask schedules a subsequent CD pass, so the verification pass does not see a stale value. markForCheck only schedules future checks and the dev-mode check still fails, while ngAfterViewChecked is subject to the same problem.",
      None)

    m(H, "Change detection",
      "Which statements about markForCheck() and detectChanges() are true? (Select all that apply.)",
      ["markForCheck() marks the view and its ancestors as dirty so they are checked in the next CD cycle; it does not run CD itself.",
       "detectChanges() runs change detection synchronously on the view and its children.",
       "markForCheck() runs change detection synchronously on the component.",
       "detectChanges() marks ancestors up to the root as dirty."],
      [0, 1],
      "One schedules, the other executes.",
      "markForCheck is a flag-setting operation that relies on a later tick, which is why it is used with OnPush. detectChanges performs an immediate check of that subtree and does not touch ancestors' dirty state.",
      None)

    m(H, "Change detection",
      "Why would you register a mousemove listener inside ngZone.runOutsideAngular()?",
      ["It makes the handler run faster than native listeners.",
       "So the handler is not patched and never runs.",
       "It avoids triggering an application-wide change detection per event; re-enter the zone or notify Angular when the UI actually needs updating.",
       "It lets the handler update templates without any change detection."],
      [2],
      "Zone.js triggers ApplicationRef.tick after handlers it tracks.",
      "Events registered within the Angular zone trigger CD after each invocation; outside it, they don't. You must call ngZone.run, markForCheck, or set a signal when something visible needs to change. It does not make the handler itself faster and the handler still runs.",
      None)

    m(H, "Zone.js",
      "In a zone.js-based app, which of these cause Angular to run change detection after they complete? (Select all that apply.)",
      ["A setTimeout callback running in the Angular zone",
       "A Promise.then callback running in the Angular zone",
       "An XHR or fetch response handled in the Angular zone",
       "A field changed by code running in runOutsideAngular",
       "Reading a signal in a plain TypeScript function"],
      [0, 1, 2],
      "Zone.js patches async APIs and notifies NgZone when its microtask queue empties.",
      "NgZone emits onMicrotaskEmpty after patched async tasks run inside the zone, which drives ApplicationRef.tick. Code outside the zone does not notify Angular, and merely reading a signal triggers nothing.",
      None)

    m(H, "Zoneless",
      "In a zoneless app (provideZonelessChangeDetection), which of these schedule change detection? (Select all that apply.)",
      ["A signal read in a template changes.",
       "markForCheck() is called.",
       "A template event listener fires.",
       "A setTimeout callback mutates a plain field.",
       "A Promise resolution mutates a plain field."],
      [0, 1, 2],
      "Without zone.js, Angular needs explicit notifications.",
      "Zoneless scheduling reacts to signals, markForCheck, async pipe, and template listener events. Mutating plain fields in timers or promises is not detected, so those would require signals or markForCheck.",
      None)

    m(H, "Change detection",
      "The parent runs change detection but passes no new inputs to an OnPush child. What is true for the child?",
      ["Neither its hooks nor its template are touched.",
       "Its template is re-checked but ngDoCheck is skipped.",
       "ngDoCheck is still called, but its template is not re-checked unless marked dirty.",
       "Its template is checked only in production mode."],
      [2],
      "ngDoCheck is invoked from the parent's view.",
      "ngDoCheck runs as part of the parent's check of the child directive, regardless of OnPush; the child's own view is skipped unless dirty. That is why ngDoCheck can be used to call markForCheck manually.",
      None)

    m(H, "Change detection",
      "How often is getTotal() evaluated in this default (non-OnPush) component template?",
      ["Only once when the view is created.",
       "Only when its dependencies change.",
       "Only on events from the template.",
       "On every change detection cycle that checks this view, regardless of whether inputs changed."],
      [3],
      "Angular does not memoize plain method calls in templates.",
      "Template expressions with method calls are re-evaluated on every check of that view. Use a computed signal, a pure pipe or precomputed fields to avoid repeated work; Angular does not track what the method depends on.",
      """<p>{{ getTotal() }}</p>""")

    m(H, "Pipes",
      "What happens in the template after toggleFirst() runs?",
      ["The list updates because pipes always re-run.",
       "Pure pipes are re-run only when the input reference changes, so the mutation is not reflected.",
       "Angular throws an error for mutating bound arrays.",
       "The pipe re-runs only if it is marked impure through OnPush."],
      [1],
      "Pure pipes compare their arguments by reference.",
      "A pure pipe is re-executed only when its input value (by reference for objects) or arguments change; mutating an object inside the array doesn't qualify. Replace the array immutably or use an impure pipe (with performance cost).",
      """@Pipe({ name: 'active' })
class ActivePipe {
  transform(users: User[]) { return users.filter(u => u.active); }
}
// template: @for (u of users | active; track u.id) { ... }
toggleFirst() { this.users[0].active = false; }""")

    # ---------------- DI ----------------
    m(H, "DI",
      "CounterService is providedIn: 'root', and a component also declares providers: [CounterService]. Which instance does that component (and its children) receive?",
      ["The root singleton.",
       "A new instance created for that component's element injector, shared with its children but not with other component instances.",
       "A new instance shared by all instances of the component.",
       "An error for duplicate providers."],
      [1],
      "Element injectors resolve before the environment injector.",
      "Component-level providers register on the element injector, so each component instance gets its own service, visible to its view children and content. The root provider is shadowed rather than conflicting.",
      None)

    m(H, "DI",
      "In what order does Angular resolve a dependency requested by a component?",
      ["Root environment injector first, then element injectors.",
       "Platform injector, then module injector, then component.",
       "The element injector hierarchy (self and ancestors) first, then the environment injector chain, then the platform.",
       "Only the nearest component's providers are considered."],
      [2],
      "Think of two trees: element and environment.",
      "Resolution walks up the element injector tree and then continues to the environment injector hierarchy (route/lazy, root) and finally the platform, ending at NullInjector. Starting from root would defeat component-level overrides.",
      None)

    m(H, "DI",
      "Which statements about injection flags and options are true? (Select all that apply.)",
      ["skipSelf starts resolution at the parent injector instead of the current one.",
       "With optional, a missing dependency yields null instead of throwing NullInjectorError.",
       "self restricts lookup to the current node's own injector.",
       "host searches all the way up to the root injector."],
      [0, 1, 2],
      "host stops at the host element of the current component.",
      "skipSelf, optional and self behave as described and combine, as in inject(Parent, { optional: true, skipSelf: true }). host limits the search to the host element boundary, it does not extend to the root.",
      """constructor(@Optional() @SkipSelf() parent: ParentService | null) {}
// or
parent = inject(ParentService, { optional: true, skipSelf: true });""")

    m(H, "DI",
      "Which statements about multi providers are true? (Select all that apply.)",
      ["Injecting a multi token returns an array of all provided values.",
       "Mixing multi and non-multi providers for the same token is an error.",
       "A later non-multi provider silently overrides earlier multi providers.",
       "Values are collected in the order they were registered."],
      [0, 1, 3],
      "Angular refuses to mix the two kinds.",
      "multi: true collects values into an array in provision order. Mixing with non-multi providers throws an error rather than overriding silently.",
      None)

    m(H, "DI",
      "What is the difference in this setup between inject(Logger) and inject(LoggerService)?",
      ["They are the same instance.",
       "inject(Logger) throws since Logger is abstract.",
       "inject(LoggerService) is undefined.",
       "They are two separate instances because useClass creates a new instance; use useExisting to alias."],
      [3],
      "useClass versus useExisting.",
      "useClass instantiates its own object for the Logger token, separate from the LoggerService provider. useExisting aliases the token to the existing provider so a single instance is shared.",
      """providers: [
  LoggerService,
  { provide: Logger, useClass: LoggerService }
]""")

    m(H, "DI",
      "Where is inject() allowed? (Select all that apply.)",
      ["In a field initializer of a component or service",
       "In a constructor body",
       "Inside ngOnInit",
       "Synchronously inside a functional CanActivateFn",
       "Inside a setTimeout callback created in the constructor"],
      [0, 1, 3],
      "It requires an active injection context.",
      "Injection contexts exist during construction, field initialization, factory functions and framework-invoked functional guards. Lifecycle hooks and later async callbacks are not injection contexts unless wrapped with runInInjectionContext.",
      None)

    m(H, "DI",
      "A service is listed in providers of a lazy-loaded NgModule (classic loadChildren). What is the effect?",
      ["It becomes a root singleton.",
       "The lazy module gets its own child environment injector with its own instance of the service, separate from any root provider.",
       "It is available only to the lazy module's components, never services.",
       "Angular throws a duplicate provider error."],
      [1],
      "Lazy modules create child injectors.",
      "Providers in a lazy-loaded NgModule are registered on a child environment injector, so code in that subtree sees its own instance, shadowing any root-level provider. This is a common source of 'two instances' bugs.",
      None)

    m(H, "DI",
      "How do viewProviders differ from providers in a component?",
      ["viewProviders are not visible to content projected into the component via ng-content.",
       "viewProviders are visible only to the component class itself.",
       "viewProviders are tree-shaken.",
       "viewProviders are visible to the parent component."],
      [0],
      "Think about view versus content children.",
      "viewProviders are visible to the component's view children only; projected content queries the injector tree of its declaring context and cannot see them. providers are visible to both.",
      None)

    # ---------------- Routing ----------------
    m(H, "Routing",
      "What happens when a user who is not logged in navigates to a route protected by this guard?",
      ["The navigation is cancelled and the router redirects to /login.",
       "The navigation is blocked and the user stays on the current page silently.",
       "An error is thrown because guards cannot return UrlTree.",
       "The route activates and the login page shows as an overlay."],
      [0],
      "Guards can return booleans, UrlTrees or observables/promises of them.",
      "Returning a UrlTree cancels the current navigation and starts a new one to the tree's URL, which is cleaner than calling router.navigate inside the guard. Returning false would block silently.",
      """export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  const router = inject(Router);
  return auth.isLoggedIn() ? true : router.createUrlTree(['/login']);
};""")

    m(H, "Routing",
      "Which statements about route resolvers are true? (Select all that apply.)",
      ["Navigation waits for resolvers to produce a value before activating the route.",
       "Resolved data can be read from ActivatedRoute.data or bound to inputs with withComponentInputBinding().",
       "If a resolver's observable completes without emitting, the navigation is cancelled.",
       "Resolvers run after the target component's constructor."],
      [0, 1, 2],
      "Resolvers run before the route component exists.",
      "The router resolves data before activation and exposes it via data. An empty observable results in cancelled navigation. Since resolution precedes activation, the component is not constructed first.",
      None)

    m(H, "Routing",
      "How does canMatch differ from canActivate?",
      ["canMatch runs after the component is created.",
       "canMatch can only return booleans.",
       "canMatch is evaluated during route matching; if it returns false the route is skipped, other matching routes are considered, and a lazy bundle is not loaded.",
       "They are identical aside from naming."],
      [2],
      "One affects which route config matches.",
      "canMatch participates in matching, so a false result lets the router try the next route with the same path and avoids downloading lazy code. canActivate runs after a route has matched and blocks the navigation instead.",
      None)

    m(H, "Routing",
      "Navigating from /user/1 to /user/2 on the same route config with the same component. What happens?",
      ["The component is reused; ngOnInit does not run again, so read params through paramMap observable or input binding.",
       "The component is destroyed and recreated.",
       "ngOnInit runs again but the constructor does not.",
       "Navigation is ignored."],
      [0],
      "The default reuse strategy reuses the component when only params differ.",
      "The default RouteReuseStrategy reuses the component instance if the route config is the same, updating ActivatedRoute observables. Snapshot reads in ngOnInit then go stale. Subscribe to paramMap or use component input binding.",
      None)

    m(H, "Routing",
      "Which statements about lazy loading with standalone routes are true? (Select all that apply.)",
      ["loadComponent: () => import('./a').then(m => m.A) lazily loads a standalone component.",
       "loadChildren can point to a file exporting a Routes array.",
       "A static import of the same component elsewhere in eager code can pull it into the main bundle, defeating the lazy split.",
       "Lazy loading requires NgModules."],
      [0, 1, 2],
      "Bundlers split on dynamic imports only.",
      "Dynamic import() is the split point for both loadComponent and loadChildren. If the class is also statically imported in eagerly loaded code, it ends up in the main chunk. NgModules are not required.",
      None)

    m(H, "Routing",
      "A route is declared with providers: [AdminService] and children. Where does AdminService live?",
      ["On the root injector, shared app-wide.",
       "In a route environment injector shared by that route and its children, separate from root.",
       "On the injector of each routed component individually.",
       "Providers are not allowed on routes."],
      [1],
      "Routes can create their own environment injector.",
      "Route-level providers create an environment injector for that route and its descendants, so the service is created lazily when the route is activated and is shared within the subtree.",
      None)

    # ---------------- Reactive forms ----------------
    m(H, "Reactive forms",
      "Given this group, which statements are true? (Select all that apply.)",
      ["form.value omits b.",
       "form.getRawValue() includes b.",
       "form.valid ignores b's validators.",
       "form.value includes b."],
      [0, 1, 2],
      "Disabled controls are excluded from value and validation aggregation.",
      "Disabled controls are excluded from the parent's value and from validity calculations, but getRawValue() returns all controls. Thus form.value omits b.",
      """form = this.fb.group({
  a: ['x', Validators.required],
  b: [{ value: 'y', disabled: true }, Validators.required]
});""")

    m(H, "Reactive forms",
      "Which statements about setValue and patchValue on a FormGroup are true? (Select all that apply.)",
      ["setValue requires an object matching the group's structure and throws on missing controls.",
       "patchValue accepts partial objects and ignores unknown keys.",
       "patchValue throws when a key is missing.",
       "setValue silently ignores unknown keys."],
      [0, 1],
      "One is strict, one is lenient.",
      "setValue is strict about structure and throws for missing or unknown controls, while patchValue is lenient and ignores keys without matching controls.",
      None)

    m(H, "Reactive forms",
      "What happens when a control has both a sync validator and an async validator, and the sync validator fails?",
      ["Both run in parallel.",
       "The async validator is invoked first.",
       "Only the async validator result is reported.",
       "The async validator is not invoked; status is INVALID from the sync errors."],
      [3],
      "Async validators run only if sync ones pass.",
      "Angular runs async validators only when sync validators produce no errors; status then becomes PENDING while it runs. This avoids unnecessary calls such as server requests for obviously invalid input.",
      None)

    m(H, "Reactive forms",
      "What does { updateOn: 'blur' } do on a FormControl?",
      ["It only delays validation messages.",
       "It makes the control disabled until blur.",
       "It runs async validators on blur only.",
       "The control's value, validity and valueChanges update on blur instead of on each input event."],
      [3],
      "It changes when the view value is propagated to the model.",
      "updateOn controls when the control's value updates and validation runs; with 'blur' these occur when the element loses focus. It is not limited to messages or async validators.",
      """name = new FormControl('', { updateOn: 'blur' });""")

    m(H, "Reactive forms",
      "What does form.reset() do to this control, and what is its type?",
      ["Resets to 'a' and the type is string.",
       "Resets to '' and the type is string.",
       "Throws because no reset value was supplied.",
       "Sets it to null and the type is string | null."],
      [3],
      "By default reset goes to null unless nonNullable.",
      "A typed FormControl('a') resets to null and is typed string | null. new FormControl('a', { nonNullable: true }) resets to its initial value and is typed string.",
      """const c = new FormControl('a');
c.reset();""")

    m(H, "Reactive forms",
      "A cross-field validator is attached to the FormGroup. Where can the mismatch error be read?",
      ["On the group via form.errors / form.hasError('mismatch'), not on the child controls.",
       "On form.get('confirm')?.errors.",
       "On every control in the group.",
       "Nowhere; group validators cannot produce errors."],
      [0],
      "Validators attach errors to the control they are assigned to.",
      "The validator runs against the group so errors are on the group. To show them on a child you must set errors there manually or check the group's error in the template.",
      """form = new FormGroup(
  { pw: new FormControl(''), confirm: new FormControl('') },
  { validators: matchValidator }
);""")

    m(H, "Reactive forms",
      "Which are true when building a custom ControlValueAccessor? (Select all that apply.)",
      ["You implement writeValue, registerOnChange and registerOnTouched.",
       "You provide NG_VALUE_ACCESSOR with multi: true, usually via useExisting and forwardRef.",
       "The class must extend FormControl.",
       "setDisabledState is optional.",
       "Calling the registered onChange is unnecessary since Angular watches inner DOM events."],
      [0, 1, 3],
      "The accessor bridges Angular's forms API and your element.",
      "The three core methods and the NG_VALUE_ACCESSOR provider are required, while setDisabledState is optional. You must call onChange yourself to push values to the form model, and the class does not extend FormControl.",
      None)

    # ---------------- HttpClient ----------------
    m(H, "HttpClient/interceptors",
      "With provideHttpClient(withInterceptors([a, b, c])), what is the order?",
      ["Requests pass c, b, a; responses pass a, b, c.",
       "Both requests and responses pass a, b, c.",
       "Requests pass a, b, c; responses pass c, b, a.",
       "Order is arbitrary."],
      [2],
      "It's like nested middleware.",
      "Interceptors form a chain: a wraps b wraps c. Requests go through them in array order and responses come back through in reverse order.",
      None)

    m(H, "HttpClient/interceptors",
      "Why does this interceptor fail to add the header?",
      ["next(req) cannot be called synchronously.",
       "Headers cannot be set in interceptors.",
       "HttpHeaders and HttpRequest are immutable; set() returns a new instance, so use req.clone({ setHeaders: ... }).",
       "Interceptors must return a Promise."],
      [2],
      "Check the return value of set().",
      "HttpRequest and HttpHeaders are immutable, and set() returns a new HttpHeaders that is discarded here. The original req is passed on unchanged. Clone the request with the new header.",
      """export const auth: HttpInterceptorFn = (req, next) => {
  req.headers.set('Authorization', 'Bearer x');
  return next(req);
};""")

    m(H, "HttpClient/interceptors",
      "A class-based interceptor is registered via HTTP_INTERCEPTORS but the app uses provideHttpClient() with no features. What happens?",
      ["It is ignored unless withInterceptorsFromDi() is added.",
       "It runs first, before functional interceptors.",
       "Angular throws at startup.",
       "It runs but only for POST requests."],
      [0],
      "DI-based interceptors are opt-in with the functional API.",
      "provideHttpClient doesn't pick up legacy DI interceptors by default; you must include withInterceptorsFromDi(). It's not an error, but the interceptor never runs.",
      None)

    m(H, "HttpClient/interceptors",
      "Which statements about HttpClient observables are true? (Select all that apply.)",
      ["They emit once and complete for a normal response.",
       "Unsubscribing before the response arrives cancels the underlying request.",
       "You must unsubscribe after completion to prevent a memory leak.",
       "Subscribing twice to the same cold observable sends two requests."],
      [0, 1, 3],
      "They are cold single-shot observables.",
      "HttpClient returns cold observables that complete after the response; unsubscribing early aborts the request, and each subscription triggers its own call. Unsubscribing after completion is unnecessary.",
      None)

    # ---------------- Templates / lifecycle / standalone ----------------
    m(H, "Deferrable views",
      "Which statements about @defer are true? (Select all that apply.)",
      ["Components, directives and pipes used inside the block must be standalone to be deferred.",
       "If a deferred dependency is also used eagerly outside the block in the same component, it is not lazily loaded.",
       "The default trigger is on idle.",
       "Dependencies of @placeholder are loaded lazily with the deferred content.",
       "@loading content is shown before the trigger fires."],
      [0, 1, 2],
      "Placeholder content must be available immediately.",
      "Only standalone dependencies referenced solely inside the block are split out, and default trigger is idle. @placeholder dependencies are eager since they render first, and @loading shows only once loading started.",
      None)

    m(H, "Content projection",
      "app-card renders <ng-content /> inside @if (open). With open === false, what about the projected <heavy-cmp />?",
      ["It is not created until open becomes true.",
       "It is created by the parent regardless but not attached to the DOM while the ng-content isn't rendered.",
       "Angular throws an error.",
       "It is created lazily like @defer."],
      [1],
      "Projected content belongs to the parent's template.",
      "Content projection is evaluated in the declaring parent's context, so projected components are instantiated even if the slot is not rendered. Use @defer or ng-template with a structural directive to defer creation.",
      """<app-card>
  <heavy-cmp />
</app-card>

<!-- app-card template -->
@if (open) { <ng-content /> }""")

    m(H, "Lifecycle",
      "Which statement about first availability of queries is correct?",
      ["Both @ViewChild and @ContentChild are available in ngOnInit.",
       "Non-static @ContentChild is available in ngAfterContentInit and @ViewChild in ngAfterViewInit (static queries earlier).",
       "@ContentChild is available only in ngAfterViewInit.",
       "Both are available only after ngOnDestroy."],
      [1],
      "Content is initialized before the view.",
      "Content queries resolve before view queries: ngAfterContentInit runs before ngAfterViewInit. Static view queries can be available in ngOnInit, but dynamic ones need ngAfterViewInit.",
      None)

    m(H, "Lifecycle",
      "Which statements about ngOnChanges are true? (Select all that apply.)",
      ["It is called before ngOnInit when the component has bound @Input()s.",
       "It is not called when the parent mutates a property of the same object reference passed in.",
       "It is not called for changes the component makes to its own @Input property from inside.",
       "It is called whenever any field of the component changes."],
      [0, 1, 2],
      "It reacts to binding changes from the parent only.",
      "ngOnChanges receives SimpleChanges for bindings updated by the parent, based on reference checks. Internal assignments and in-place mutations do not trigger it, and it is not a general field watcher.",
      None)

    m(H, "Standalone",
      "A standalone component uses <app-child /> in its template but does not list ChildComponent in its imports. What happens?",
      ["It works because all standalone components are globally registered.",
       "It works at runtime but warns in the console.",
       "It compiles because Angular auto-imports from the file.",
       "The compiler reports an unknown element error (NG8001); the component must be imported."],
      [3],
      "Standalone components have explicit template scope.",
      "A standalone component's template scope consists of its own imports; unknown elements cause a compile error under AOT. No global registration or auto-import exists.",
      None)

    # ---------------- Testing ----------------
    m(H, "Testing",
      "In a test for an OnPush component, setting componentInstance.name = 'X' followed by fixture.detectChanges() works the first time but not afterwards. What is the proper fix?",
      ["Use fixture.componentRef.setInput('name', 'X') then detectChanges().",
       "Call fixture.autoDetectChanges(false).",
       "Remove OnPush in the test with overrideComponent only.",
       "Call tick() inside the test."],
      [0],
      "OnPush needs input changes via bindings.",
      "OnPush views are checked on the first detectChanges but afterwards only when marked dirty; setInput goes through the input binding path and marks it dirty. Setting a property directly bypasses that. Overriding strategy changes behavior under test.",
      """fixture.componentInstance.name = 'X';
fixture.detectChanges();""")

    m(H, "Testing",
      "A fakeAsync test calls component.search('a') where search uses debounceTime(300) and ends without further calls. What happens?",
      ["It passes; timers are discarded.",
       "It fails with an error about 1 timer(s) still in the queue; use tick(300) or flush().",
       "It hangs forever.",
       "It passes but the subscription is not executed."],
      [1],
      "fakeAsync verifies that no timers remain.",
      "fakeAsync throws if pending timers exist at test end. Advance virtual time with tick(300) or run all with flush(). It does not hang, since time is virtual.",
      """it('searches', fakeAsync(() => {
  component.search('a');
}));""")

    m(H, "RxJS state",
      "What does the subscriber of this pipeline receive when the user clicks the button three times?",
      ["1, 2, 3 as the clicks happen",
       "3 once, after the third click",
       "Nothing, because reduce emits only when the source completes and fromEvent never completes",
       "0, 1, 2, 3"],
      [2],
      "Compare reduce with scan.",
      "reduce accumulates silently and emits the final value only on source completion, and a DOM event stream never completes, so nothing is emitted. scan emits each intermediate accumulation, which is what is wanted for running counts.",
      """fromEvent(button, 'click')
  .pipe(reduce(count => count + 1, 0))
  .subscribe(console.log);""")
