def add(m0):
    n = [0]

    def m(level, topic, text, options, correct, hint, explanation, code=None):
        k = (n[0] * 3 + 1) % len(options)
        n[0] += 1
        opts = options[k:] + options[:k]
        corr = sorted((i - k) % len(options) for i in correct)
        m0(level, topic, text, opts, corr, hint, explanation, code)

    L = "Expert"
    SA = " (Select all that apply.)"

    m(L, "Zone.js", "A component registers a high-frequency mousemove listener inside ngOnInit. Which approach avoids an application-wide change detection pass per event while still allowing selective updates?",
      ["Wrap the registration in NgZone.runOutsideAngular and re-enter with ngZone.run only when state must update",
       "Mark the component OnPush so Zone.js stops patching addEventListener",
       "Use setTimeout inside the handler to defer the tick",
       "Call ChangeDetectorRef.detach() in the constructor, which also unpatches the listener"],
      [0], "Think about which zone the listener is registered in.",
      "Listeners registered in the Angular zone trigger ApplicationRef.tick after each event. Registering in runOutsideAngular avoids that, and ngZone.run re-enters when needed. OnPush does not change zone patching, and detach only affects one view, not the global tick.",
      "ngOnInit() {\n  this.zone.runOutsideAngular(() => {\n    window.addEventListener('mousemove', this.onMove);\n  });\n}")

    m(L, "Zoneless", "In a zoneless application (provideZonelessChangeDetection), which of the following schedule a change detection run?" + SA,
      ["Setting a signal that is read in a component template",
       "Updating a plain class field inside a setTimeout callback",
       "Calling ChangeDetectorRef.markForCheck()",
       "A Promise.then callback that mutates a plain field",
       "An async pipe receiving a new emission"],
      [0, 2, 4], "Zoneless relies on explicit notifications, not on patched async APIs.",
      "Signals read in templates, markForCheck, async pipe emissions and template event listeners notify the scheduler. Plain field mutations in timers or promises produce no notification without Zone.js, so the view stays stale.")

    m(L, "OnPush", "Which of the following mark an OnPush component view as dirty?" + SA,
      ["An @Input receives a new object reference",
       "A property of an input object is mutated in place by the parent",
       "A DOM event handler bound in the component's own template runs",
       "An async pipe in its template receives a new value",
       "A plain field is changed by a setTimeout callback in the component"],
      [0, 2, 3], "OnPush reacts to references and explicit events, not mutation.",
      "New input references, template-bound events, and async pipe emissions (via markForCheck) dirty the view. In-place mutation keeps the same reference, and a timer changing a field does not mark the view dirty.")

    m(L, "Signals", "What happens when signal.set() is called with a value equal (Object.is) to the current value using the default equality?",
      ["Dependents are not notified and no recomputation occurs",
       "Effects re-run once but computed signals are skipped",
       "Computed signals recompute but templates are not refreshed",
       "The signal version increments and consumers are marked dirty"],
      [0], "Default equality short-circuits notifications.",
      "The signal compares with Object.is and, if equal, does nothing, so no consumers are dirtied. Effects and computeds are consumers and are not notified either.")

    m(L, "Signals", "How does a computed() signal behave with respect to evaluation?",
      ["It is lazy and memoized: it recomputes only when read after a dependency changed",
       "It recomputes eagerly on every dependency change",
       "It recomputes on every change detection pass",
       "It recomputes on every read regardless of dependency changes"],
      [0], "Think pull-based, not push-based.",
      "Computeds are lazily evaluated and cached until a dependency marks them stale. They are not eager, and they do not recompute on each read when dependencies are unchanged.")

    m(L, "Signals", "Which statements about effect() in Angular are true?" + SA,
      ["Effects are scheduled and flushed asynchronously, not synchronously when a signal is set",
       "Signals read inside untracked() do not become dependencies of the effect",
       "The onCleanup callback runs before the next execution and on destroy",
       "Setting a signal always runs dependent effects immediately before set() returns",
       "Effects must always be destroyed manually with destroy() or they leak, even in components"],
      [0, 1, 2], "Effects are reactive side effects with managed lifetimes.",
      "Effects are batched and run during change detection or the scheduler flush, with cleanups between runs, and untracked reads add no dependency. They do not run synchronously inside set(). Effects created in an injection context are destroyed automatically with their owner, so manual destroy is not required.",
      "effect((onCleanup) => {\n  const id = setInterval(() => log(this.count()), 1000);\n  onCleanup(() => clearInterval(id));\n});")

    m(L, "Dependency Injection", "A component declares a service in viewProviders. Which consumer can NOT inject it?",
      ["A component projected through <ng-content> into this component's template",
       "A directive on an element inside this component's template",
       "A child component declared in this component's template",
       "The component itself"],
      [0], "viewProviders are visible only to the view, not content.",
      "viewProviders are visible to the component and nodes in its own view but hidden from projected content, which belongs to the parent's declaration. Providers in 'providers' are visible to content children too.")

    m(L, "Dependency Injection", "A component provides FormStateService in its providers and a child component needs the parent component's instance, while the child itself also provides FormStateService. How does the child obtain the parent's instance?",
      ["inject(FormStateService, { skipSelf: true })",
       "inject(FormStateService, { self: true })",
       "inject(FormStateService, { host: true, self: true })",
       "inject(FormStateService, { optional: true })"],
      [0], "Skip the node's own injector.",
      "skipSelf starts resolution at the parent element injector. self restricts to the node itself and would return the child's own instance, and optional only changes failure behavior.")

    m(L, "Dependency Injection", "Which statements about providedIn: 'root' services are true?" + SA,
      ["They are tree-shakable if never injected",
       "A lazy-loaded route that injects one gets a new instance per route by default",
       "They are singletons in the root environment injector unless overridden",
       "They are registered by listing them in AppModule providers",
       "A lazy route's providers array can override them for that subtree"],
      [0, 2, 4], "Think about where the root injector sits relative to route injectors.",
      "providedIn root registers a tree-shakable factory in the root injector, so one instance is shared, including lazy routes, unless a route's providers override it. No per-route instance is created unless the route provides its own.")

    m(L, "Routing", "Services listed in a Route's providers array are scoped how?",
      ["To an environment injector created for that route and its child routes",
       "To the root injector globally",
       "To the component rendered by the route only",
       "To the router-outlet element injector"],
      [0], "Routes can create their own environment injectors.",
      "Route providers create a route-level EnvironmentInjector shared by the route and its children. They are not global, and they are not element-level providers of the component.")

    m(L, "Forms", "Which are required or correct when implementing a custom ControlValueAccessor?" + SA,
      ["Provide NG_VALUE_ACCESSOR with useExisting (forwardRef) and multi: true",
       "writeValue is called by the forms API to push model values into the view",
       "Call the registered onTouched callback when the control is blurred",
       "writeValue should call onChange so the model stays in sync",
       "registerOnChange stores a function to call when the user changes the value"],
      [0, 1, 2, 4], "Direction of data flow matters for each method.",
      "The token provider, writeValue (model to view), onTouched, and onChange (view to model) are all part of the contract. Calling onChange inside writeValue would echo the change back and incorrectly mark the control dirty.",
      "@Component({\n  selector: 'app-rating',\n  providers: [{\n    provide: NG_VALUE_ACCESSOR,\n    useExisting: forwardRef(() => RatingComponent),\n    multi: true\n  }]\n})\nexport class RatingComponent implements ControlValueAccessor { }")

    m(L, "Forms", "When is the optional ControlValueAccessor.setDisabledState called?",
      ["When the bound control's disabled status changes, for example via control.disable()",
       "Only once when the form is first created",
       "Whenever writeValue is called",
       "When the control becomes invalid"],
      [0], "It mirrors the control's enabled/disabled state.",
      "Forms calls setDisabledState to reflect enable/disable calls on the control. It is unrelated to validity or to value writes.")

    m(L, "Dynamic Components", "After ViewContainerRef.createComponent for an OnPush component, how should a parent supply an input so ngOnChanges and the view update correctly?",
      ["componentRef.setInput('name', value)",
       "componentRef.instance.name = value",
       "Object.assign(componentRef.instance, { name: value })",
       "componentRef.changeDetectorRef.detach()"],
      [0], "There is an API that behaves like a template binding.",
      "setInput marks the view dirty and triggers input handling like a binding. Assigning to the instance bypasses ngOnChanges and does not mark an OnPush view for check.",
      "const ref = vcr.createComponent(CardComponent);\nref.setInput('name', 'Ada');")

    m(L, "Dynamic Components", "A component is created with createComponent(Comp, { environmentInjector, hostElement }) outside any view container. What is needed for it to be change-detected?",
      ["appRef.attachView(ref.hostView), and destroy it when done",
       "Nothing; it is automatically attached to the ApplicationRef",
       "Call NgZone.run once at creation",
       "Add it to the declarations of the root module"],
      [0], "Who owns the view's change detection?",
      "A component created standalone is not part of any tree until its host view is attached to ApplicationRef; it must also be destroyed manually. It is not auto-attached, and zone runs or declarations do not attach it.",
      "const ref = createComponent(Toast, { environmentInjector: this.envInjector, hostElement: el });\nthis.appRef.attachView(ref.hostView);")

    m(L, "SSR and Hydration", "Which statements about Angular hydration are true?" + SA,
      ["It reuses server-rendered DOM instead of recreating it",
       "Manual DOM manipulation of Angular-owned nodes can cause hydration mismatches",
       "ngSkipHydration opts a component out of hydration",
       "Hydration discards the server HTML and re-renders everything",
       "It requires ngSkipHydration on every component"],
      [0, 1, 2], "Hydration relies on server and client DOM matching.",
      "Hydration reuses existing DOM and requires structure to match, so direct manipulation can break it; ngSkipHydration opts out. It does not discard the server output, and ngSkipHydration is only an opt-out, not a requirement.")

    m(L, "SSR and Hydration", "How does withHttpTransferCache help an SSR app?",
      ["Server HttpClient responses are serialized into the page and reused by the client, avoiding duplicate requests",
       "It caches all responses in localStorage permanently",
       "It disables HTTP requests on the server",
       "It converts HttpClient to the fetch API"],
      [0], "Think about duplicate fetches after hydration.",
      "Responses made on the server are stored in TransferState and replayed on the client for matching requests. It is not persistent browser storage and does not stop server requests.")

    m(L, "SSR and Hydration", "Which practices keep code safe for server-side rendering?" + SA,
      ["Guard browser-only APIs with isPlatformBrowser or run them in afterNextRender",
       "Access window or document directly in constructors",
       "Inject DOCUMENT instead of using the global document",
       "Assume ngOnInit only runs in the browser",
       "Avoid unbounded timers that keep the server render from stabilizing"],
      [0, 2, 4], "The server has no window and waits for stability.",
      "Platform guards, afterNextRender (browser only), and DOCUMENT injection keep code portable, and pending macrotasks delay stability. Constructors and ngOnInit run on the server too, so global browser access breaks there.")

    m(L, "Lazy Loading", "How is a custom preloading strategy implemented to preload only routes flagged in data?",
      ["Implement PreloadingStrategy.preload(route, load) returning load() or of(null) based on route.data",
       "Override Router.navigate to prefetch chunks",
       "Add providedIn: 'root' to the lazy route's component",
       "Use canMatch to return true for flagged routes"],
      [0], "The strategy decides whether to call the loader.",
      "preload receives the route and a loader function; returning load() fetches the chunk and of(null) skips it. canMatch gates matching, not background preloading.",
      "export class FlagPreload implements PreloadingStrategy {\n  preload(route: Route, load: () => Observable<any>) {\n    return route.data?.['preload'] ? load() : of(null);\n  }\n}")

    m(L, "Lazy Loading", "Which statements about @defer blocks are true?" + SA,
      ["Dependencies used only within the block can be split into a separate lazy chunk",
       "A standalone component also referenced eagerly elsewhere is still split out into the lazy chunk",
       "The @placeholder content is shown before the trigger fires",
       "@defer works with NgModule-declared (non-standalone) components in all cases",
       "on viewport triggers loading when the placeholder enters the viewport"],
      [0, 2, 4], "Deferral depends on how the dependency is referenced.",
      "Standalone dependencies referenced only inside the block are lazily loaded, but eager use elsewhere keeps them in the main bundle. Placeholders and the viewport trigger work as described. Non-standalone dependencies are not deferrable by default.")

    m(L, "Bundle Performance", "What does setting \"sideEffects\": false in a library's package.json allow bundlers to do?",
      ["Drop unused modules/exports during tree shaking",
       "Disable zone patching in the library",
       "Skip type checking during the build",
       "Make the library load lazily at runtime"],
      [0], "It's a promise about import statements having no effects.",
      "The flag tells the bundler that unused imports can be removed safely, improving tree shaking. It has nothing to do with zones, typing, or runtime lazy loading.",
      "{\n  \"name\": \"my-lib\",\n  \"sideEffects\": false\n}")

    m(L, "RxJS", "What is the difference between shareReplay(1) and shareReplay({ bufferSize: 1, refCount: true })?",
      ["Without refCount the source subscription stays open after all subscribers leave; with it the source is unsubscribed at zero subscribers",
       "refCount makes the replayed value expire after one second",
       "Without refCount, values are never replayed",
       "refCount makes the observable hot, otherwise it is cold"],
      [0], "Think about when the upstream subscription is released.",
      "Plain shareReplay keeps the upstream subscription alive, which can leak with long-lived sources. With refCount true it unsubscribes at zero subscribers, though replay buffers behave normally in both.")

    m(L, "RxJS", "Which of these help prevent subscription leaks in components?" + SA,
      ["takeUntilDestroyed() inside an injection context, or with a passed DestroyRef elsewhere",
       "Using the async pipe in the template",
       "Calling takeUntilDestroyed() with no argument inside ngOnInit",
       "Storing Subscriptions and unsubscribing in ngOnDestroy",
       "Subscribing to HttpClient calls always leaks unless unsubscribed"],
      [0, 1, 3], "Some operators require an injection context.",
      "takeUntilDestroyed with DestroyRef, async pipe, and manual unsubscription all release subscriptions. Without an argument outside an injection context it throws, and HttpClient observables complete after the response.")

    m(L, "RxJS", "By default, what does the share() operator do when the subscriber count falls to zero and a new subscriber arrives later?",
      ["It resets and resubscribes to the source, because resetOnRefCountZero is true by default",
       "It replays the last value without resubscribing",
       "It throws an error",
       "It keeps the source subscribed forever"],
      [0], "share resets by default.",
      "share() uses a Subject connector and resets on refCount zero, error, and complete, so late subscribers trigger a new source subscription. Replay behavior needs shareReplay or explicit config.",
      "const shared$ = source$.pipe(share());")

    m(L, "Testing", "Which approaches are appropriate when testing components in a modern Angular app?" + SA,
      ["Use fixture.componentRef.setInput to set signal inputs",
       "Assign directly to a signal input property on the instance",
       "Use HttpTestingController and call verify() in afterEach",
       "Use component harnesses to decouple tests from DOM structure",
       "Use real timers and sleep() to wait for async work"],
      [0, 2, 3], "Signal inputs are read-only from the consumer.",
      "setInput works with signal inputs, HttpTestingController.verify checks outstanding requests, and harnesses abstract DOM. Real sleeps make tests slow and flaky; use fakeAsync or whenStable instead. Signal inputs cannot be assigned directly.",
      "fixture.componentRef.setInput('title', 'Hi');\nfixture.detectChanges();\nhttp.expectOne('/api').flush([]);")

    m(L, "State Management", "Which are sound NgRx-style state design principles?" + SA,
      ["Reducers must be pure functions",
       "Normalize entity collections and derive view data through selectors",
       "Duplicate derived data in the store for convenience",
       "Keep side effects like HTTP calls in effects, not reducers",
       "Mutate state objects in place for performance"],
      [0, 1, 3], "Keep state minimal and predictable.",
      "Pure reducers, normalized state with derived selectors, and side effects in effects keep state predictable. Duplicated derived data goes stale and in-place mutation breaks change detection.")

    m(L, "State Management", "When does a memoized createSelector recompute its projector?",
      ["When any input selector returns a result that is not reference-equal to the previous one",
       "On every store emission",
       "On every change detection cycle",
       "Only when the whole state reference changes"],
      [0], "Memoization is by input results.",
      "A createSelector reruns the projector only if its input selectors' results changed by reference. A new state object alone is not enough if the slices it reads are unchanged.")

    m(L, "Micro-frontends", "In a Module Federation setup, which configuration choices reduce duplicate Angular runtimes?" + SA,
      ["Declare @angular/core as shared with singleton: true",
       "Use strictVersion to fail loudly on incompatible versions",
       "Give each remote its own bundled copy of Angular",
       "Share the same Router and Injector instance automatically without configuration",
       "Align the Angular versions across host and remotes"],
      [0, 1, 4], "One Angular runtime is the goal.",
      "Singleton sharing, strict versions, and aligned versions avoid duplicate runtimes. Bundling separate copies defeats this, and shared packages do not auto-share injectors.")

    m(L, "Templates", "In @for, what does `track item.id` achieve compared with `track $index` when a list is reordered?",
      ["DOM nodes and component instances are moved with their items instead of being rebound to different data",
       "It disables DOM updates entirely",
       "It sorts the list by id",
       "It makes the iteration lazy"],
      [0], "Identity decides what is reused.",
      "Tracking by a stable id lets the diff move existing views, preserving state. Tracking by index reuses views by position and rebinds them to different items.",
      "@for (item of items(); track item.id) {\n  <app-row [item]=\"item\" />\n} @empty {\n  <p>None</p>\n}")

    m(L, "Templates", "Which statements about the @for block are true?" + SA,
      ["The track expression is required",
       "Contextual variables such as $index, $first, $last and $count are available",
       "An @empty block renders when the collection is empty",
       "track is optional and defaults to object identity",
       "It only accepts arrays, never other iterables"],
      [0, 1, 2], "The compiler enforces a track expression.",
      "track is mandatory, context variables and @empty exist, and it works with any iterable, not only arrays. There is no optional default tracking.")

    m(L, "Routing", "A route is lazy-loaded with loadChildren. Which guard prevents the lazy chunk from being downloaded for unauthorized users?",
      ["canMatch",
       "canActivate",
       "canDeactivate",
       "resolve"],
      [0], "Which guard runs while matching, before loading?",
      "canMatch runs during route matching, so a false result skips the route and its lazy loading. canActivate runs after the route has matched and the chunk loaded; resolve and canDeactivate come later.",
      "{\n  path: 'admin',\n  canMatch: [() => inject(Auth).isAdmin()],\n  loadChildren: () => import('./admin/routes')\n}")

    m(L, "Routing", "Which statements about functional route guards are true?" + SA,
      ["They can call inject() to obtain services",
       "Returning a UrlTree redirects navigation",
       "Returning false cancels navigation without redirecting",
       "They must be classes implementing CanActivate",
       "They are skipped for lazy-loaded routes"],
      [0, 1, 2], "Functions run in an injection context.",
      "Guard functions run in an injection context, may be async, and results are boolean or UrlTree (sync or async). Class-based guards are not required.")

    m(L, "Routing", "When are route resolvers executed relative to guards?",
      ["After guards pass, before the route is activated",
       "Before canMatch",
       "After the component is rendered",
       "In parallel with canDeactivate"],
      [0], "Resolvers need navigation to be allowed first.",
      "Resolvers run once guards have allowed navigation and complete before activation. They do not run before matching or after rendering.")

    m(L, "Standalone Migration", "Which are correct when migrating an NgModule app to standalone?" + SA,
      ["Standalone components can import NgModules and other standalone items",
       "NgModule providers can be brought in with importProvidersFrom",
       "The migration schematic can convert declarations stepwise",
       "Standalone components cannot import any NgModule",
       "All NgModules must be deleted before any component can be standalone"],
      [0, 1, 2], "Standalone is interoperable with modules.",
      "Standalone components may import NgModules, importProvidersFrom bridges module providers, and the schematic runs in steps. The cannot-import and must-delete claims are false.",
      "bootstrapApplication(AppComponent, {\n  providers: [importProvidersFrom(LegacyModule)]\n});")

    m(L, "Change Detection", "The ExpressionChangedAfterItHasBeenCheckedError occurs because:",
      ["In dev mode, a second verification pass finds a binding value that changed during the first pass",
       "Change detection ran twice in production",
       "The component was OnPush",
       "A subscription was left open"],
      [0], "It's a dev-mode check.",
      "Angular re-checks bindings in dev mode and throws if a value changed after being checked, typically due to child-to-parent state changes. It is not produced in production builds.")

    m(L, "Change Detection", "What does ChangeDetectorRef.markForCheck() do?",
      ["Marks the view and its ancestors for checking at the next tick without running change detection itself",
       "Runs change detection immediately on this view",
       "Detaches the view from the tree",
       "Marks only this view and not its ancestors"],
      [0], "It schedules, not runs.",
      "markForCheck marks the path to the root dirty so the next tick checks it. detectChanges is the call that runs it immediately.")

    m(L, "Signals", "Which are true of signal-based inputs and model()?" + SA,
      ["Signal inputs are read-only in the component",
       "model() enables two-way binding with [(value)]",
       "input.required() must be provided by the parent or compilation fails",
       "Signal inputs can be updated with .set() inside the child",
       "Signal inputs cannot be read inside computed()"],
      [0, 1, 2], "The consumer cannot write inputs.",
      "Inputs are read-only, model is writable and bindable two-way, and required inputs are compile-checked. Inputs are normal signals and work in computed(). .set() exists on model, not input.")

    m(L, "Signals", "Which statements about converting Observables with toSignal() in a large application are true?" + SA,
      ["It subscribes immediately and unsubscribes when the owning context is destroyed",
       "Without initialValue, the signal's type includes undefined until the first emission",
       "If the observable errors, reading the signal throws that error",
       "It must be called in ngOnInit",
       "It never unsubscribes automatically"],
      [0, 1, 2], "It needs an injection context.",
      "toSignal subscribes eagerly with automatic cleanup, includes undefined without an initial value, and rethrows errors on read. It needs an injection context, not ngOnInit.")

    m(L, "Zone.js", "Why does making every component OnPush not stop Zone.js from triggering ApplicationRef.tick on each async event?",
      ["Zone.js notifies on task completion regardless; OnPush only skips unchanged views during the pass",
       "OnPush components are never skipped",
       "Zone.js ignores OnPush components",
       "OnPush disables Zone.js patches"],
      [0], "Scheduling and traversal are separate.",
      "Zone triggers a tick whenever microtasks drain, and OnPush only prunes which views are checked. The tick still happens.")

    m(L, "Dependency Injection", "What is the difference between { provide: A, useClass: B } and { provide: A, useExisting: B }?",
      ["useClass creates a separate B instance for A; useExisting aliases A to the existing B instance",
       "They are identical",
       "useExisting creates a new instance each time",
       "useClass requires providedIn root"],
      [0], "One aliases, the other instantiates.",
      "useExisting points the token at the same provider's instance so A and B share state, while useClass instantiates its own.",
      "providers: [\n  { provide: Logger, useClass: ConsoleLogger },\n  { provide: Alias, useExisting: ConsoleLogger }\n]")

    m(L, "HTTP", "Which are true about functional HTTP interceptors registered with provideHttpClient(withInterceptors([...]))?" + SA,
      ["They can use inject() to access services",
       "Request handling runs in array order and responses flow back in reverse",
       "They must return an Observable of HttpEvent",
       "They run in a different order than registered for requests",
       "They cannot modify the outgoing request"],
      [0, 1, 2], "Interceptors form a chain.",
      "Functional interceptors have an injection context, form a chain in order, and return an event stream. Requests are immutable but can be cloned and modified. Claiming that request order differs from registration is false.",
      "export const authInterceptor: HttpInterceptorFn = (req, next) =>\n  next(req.clone({ setHeaders: { Authorization: inject(Auth).token() } }));")
