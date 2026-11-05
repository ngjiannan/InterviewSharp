def add(m_raw):
    import random
    rng = random.Random(2024)

    def m(level, topic, text, options, correct, hint, explanation, code=None):
        # Spread correct answer positions evenly (deterministic shuffle)
        order = list(range(len(options)))
        rng.shuffle(order)
        opts = [options[i] for i in order]
        corr = sorted(order.index(c) for c in correct)
        m_raw(level, topic, text, opts, corr, hint, explanation, code)

    E = "Easy"
    # ---------------- EASY (30) ----------------
    m(E, "Components", "Which decorator marks a TypeScript class as an Angular component?",
      ["@Injectable()", "@Component()", "@NgModule()", "@Directive()"], [1],
      "It is the decorator that accepts a selector and a template.",
      "@Component() attaches metadata such as selector, template and styles to the class. @Injectable() is for services, @NgModule() groups declarations in classic modules, and @Directive() has no template.")
    m(E, "Standalone", "In a standalone component, which metadata property lists the other components, directives and pipes its template uses?",
      ["declarations", "imports", "providers", "exports"], [1],
      "A standalone component has no NgModule to borrow dependencies from.",
      "Standalone components declare their template dependencies directly in the imports array. declarations belongs to NgModules, providers configures DI, and exports is for NgModules.")
    m(E, "Control flow", "What does the @for block require in Angular's built-in control flow?",
      ["A trackBy function declared in the class", "A track expression", "The CommonModule import", "An index alias"], [1],
      "The compiler insists on a way to identify items between changes.",
      "@for (item of items; track item.id) requires a track expression so the DOM can be reused efficiently. No CommonModule import is needed, and an index alias is optional.",
      "@for (item of items; track item.id) {\n  <li>{{ item.name }}</li>\n}")
    m(E, "Signals", "How do you create a writable signal holding the number 0?",
      ["const count = new Signal(0);", "const count = signal(0);", "const count = computed(0);", "const count = ref(0);"], [1],
      "It is a plain factory function imported from @angular/core.",
      "signal(0) returns a WritableSignal<number>. computed() takes a derivation function and is read-only, ref() is Vue, and Signal is not constructed with new.")
    m(E, "Signals", "How do you read the current value of a signal named count in a template?",
      ["{{ count.value }}", "{{ count }}", "{{ count() }}", "{{ count.get }}"], [2],
      "Signals are getter functions.",
      "A signal is read by calling it: count(). Without parentheses you get the function itself, and signals have no value or get property.")
    m(E, "DI", "Which function can be used instead of constructor parameters to obtain a dependency in modern Angular?",
      ["inject()", "resolve()", "provide()", "require()"], [0],
      "It is imported from @angular/core and called in an injection context.",
      "inject(MyService) retrieves a dependency, for example in a field initializer. resolve, provide and require are not Angular DI retrieval functions.",
      "export class UserComponent {\n  private http = inject(HttpClient);\n}")
    m(E, "Pipes", "What is the main benefit of the async pipe?",
      ["It makes HTTP calls synchronous", "It subscribes to an Observable or Promise and unsubscribes automatically", "It converts any value to a Promise", "It caches API responses"], [1],
      "Think about subscription management in templates.",
      "The async pipe subscribes, exposes the latest value, marks the view for check, and unsubscribes on destroy. It does not make anything synchronous or cache responses.")
    m(E, "Directives", "Which of these are built-in structural directives? (Select all that apply.)",
      ["*ngIf", "ngClass", "*ngFor", "ngStyle"], [0, 2],
      "Structural directives add or remove elements from the DOM.",
      "*ngIf and *ngFor change the DOM structure. ngClass and ngStyle are attribute directives that modify existing elements.")
    m(E, "Lifecycle", "Which lifecycle hook is typically used for initialization logic after the first inputs are set?",
      ["ngOnInit", "ngOnDestroy", "ngAfterViewChecked", "ngDoCheck"], [0],
      "It runs once after the first ngOnChanges.",
      "ngOnInit runs once after input properties are initialized. ngOnDestroy is for cleanup, while ngAfterViewChecked and ngDoCheck run repeatedly.")
    m(E, "Lifecycle", "Where should you release resources such as manual subscriptions or timers?",
      ["constructor", "ngOnInit", "ngOnDestroy", "ngOnChanges"], [2],
      "It is called just before Angular removes the component.",
      "ngOnDestroy runs right before the component is destroyed, making it the place for cleanup. The other hooks run during creation or updates.")
    m(E, "Data binding", "Which syntax binds a component property to a DOM element property?",
      ["(value)=\"name\"", "[value]=\"name\"", "{value}=\"name\"", "#value=\"name\""], [1],
      "Square brackets point data toward the template.",
      "[value]=\"name\" is property binding. Parentheses are event binding, and # declares a template reference variable.")
    m(E, "Data binding", "Which of the following are valid ways to bind a click event? (Select all that apply.)",
      ["(click)=\"save()\"", "[click]=\"save()\"", "on-click=\"save()\"", "@click=\"save()\""], [0, 2],
      "One is the shorthand and one is the canonical prefix form.",
      "(click) and on-click are equivalent event bindings. [click] is property binding and @click is Vue syntax.")
    m(E, "Forms", "What does the banana-in-a-box syntax [(ngModel)] provide, and what is required for it?",
      ["One-way binding; ReactiveFormsModule", "Two-way binding; FormsModule", "Event binding only; CommonModule", "Two-way binding; HttpClientModule"], [1],
      "Combines property and event binding for template-driven forms.",
      "[(ngModel)] is two-way binding for template-driven forms and needs FormsModule (or importing NgModel in a standalone component). ReactiveFormsModule is for FormControl-based forms.")
    m(E, "Routing", "Which element marks where the router renders the matched component?",
      ["<router-view>", "<ng-container>", "<router-outlet>", "<ng-content>"], [2],
      "It is a placeholder directive from RouterModule.",
      "<router-outlet> is where routed components are displayed. router-view is not Angular, ng-container is a grouping element, and ng-content projects content.")
    m(E, "Routing", "Which directive creates a navigation link without a full page reload?",
      ["href", "routerLink", "navigateTo", "ngLink"], [1],
      "It is applied to an anchor in place of href.",
      "routerLink builds the URL and navigates through the Router. A plain href triggers a full reload; navigateTo and ngLink do not exist.")
    m(E, "HttpClient", "Which of these are methods provided by HttpClient? (Select all that apply.)",
      ["get", "post", "fetch", "delete"], [0, 1, 3],
      "They mirror HTTP verbs.",
      "HttpClient exposes get, post, put, patch, delete and others, each returning an Observable. There is no fetch method on HttpClient.")
    m(E, "HttpClient", "In a standalone application, how do you make HttpClient available?",
      ["Add provideHttpClient() to the application providers", "Import HttpClient in the component's imports", "Declare HttpClient in declarations", "Call new HttpClient()"], [0],
      "It is a provider function used in bootstrapApplication or app config.",
      "provideHttpClient() registers HttpClient and its backend. HttpClient is a service, not a component or module import, and should not be constructed manually.",
      "bootstrapApplication(AppComponent, {\n  providers: [provideHttpClient()]\n});")
    m(E, "Forms", "Which of these classes belong to Reactive Forms? (Select all that apply.)",
      ["FormGroup", "FormControl", "NgModel", "FormArray"], [0, 1, 3],
      "NgModel is a directive used in the other style of forms.",
      "FormGroup, FormControl and FormArray are the building blocks of reactive forms. NgModel is the directive behind template-driven forms.")
    m(E, "RxJS", "When does a cold Observable such as one returned by HttpClient.get start doing work?",
      ["When it is created", "When it is subscribed to", "When the component initializes", "When pipe() is called"], [1],
      "Observables are lazy.",
      "Observables execute only on subscribe. Creating one or adding operators with pipe() does not start the request.")
    m(E, "RxJS", "Which of the following are RxJS operators? (Select all that apply.)",
      ["map", "ngOnInit", "filter", "tap"], [0, 2, 3],
      "One of the options is a lifecycle hook.",
      "map, filter and tap are operators used inside pipe(). ngOnInit is an Angular lifecycle hook.")
    m(E, "NgModules", "In a classic NgModule, what is the purpose of the declarations array?",
      ["List services to inject", "List components, directives and pipes that belong to the module", "List modules to import", "List routes"], [1],
      "It defines which view classes the module owns.",
      "declarations registers the module's components, directives and pipes. Services go in providers, other modules go in imports.")
    m(E, "Components", "Which are valid ways to declare a component input? (Select all that apply.)",
      ["@Input() title = '';", "title = input<string>();", "@Output() title = '';", "title = output<string>();"], [0, 1],
      "One is the decorator, one is the signal-based function.",
      "@Input() and the input() function both declare inputs. @Output and output() declare events emitted to the parent.")
    m(E, "Components", "Which combination lets a child component send an event to its parent?",
      ["@Output() with EventEmitter", "@Input() with a callback signal", "@ViewChild with ngOnInit", "@Injectable with providedIn"], [0],
      "Data flows up via events.",
      "An @Output EventEmitter (or the output() function) emits events the parent listens to with (event) binding. @Input flows data downward.")
    m(E, "Change detection", "Which snippet configures a component to use the OnPush change detection strategy?",
      ["@Component({ changeDetection: ChangeDetectionStrategy.OnPush })", "@Component({ strategy: 'OnPush' })", "@Component({ onPush: true })", "@Component({ detection: ChangeDetectionStrategy.Default })"], [0],
      "The property name is changeDetection.",
      "changeDetection: ChangeDetectionStrategy.OnPush opts into OnPush checks. The other property names do not exist or select Default.")
    m(E, "Testing", "Which Angular utility configures and creates a testing module for unit tests?",
      ["TestRunner", "TestBed", "NgTest", "ComponentFactory"], [1],
      "It is the primary API from @angular/core/testing.",
      "TestBed.configureTestingModule sets up providers and imports for tests. The other names are not Angular testing APIs for this purpose.")
    m(E, "Deferrable views", "What is the purpose of the @defer block?",
      ["To delay a component's lifecycle hooks", "To lazy load the template dependencies it contains", "To debounce user input", "To defer HTTP requests"], [1],
      "It affects bundle loading.",
      "@defer splits the enclosed standalone components, directives and pipes into separate chunks loaded on a trigger. It does not debounce or delay HTTP.",
      "@defer (on viewport) {\n  <app-chart />\n} @placeholder {\n  <p>Chart</p>\n}")
    m(E, "Tooling", "Which Angular CLI command generates a new component?",
      ["ng new component", "ng generate component hero", "ng build component", "ng add component"], [1],
      "Short form is ng g.",
      "ng generate component hero (or ng g c hero) scaffolds a component. ng new creates a workspace, ng build compiles, ng add installs packages.")
    m(E, "Pipes", "Which of these are built-in Angular pipes? (Select all that apply.)",
      ["date", "currency", "uppercase", "reverse"], [0, 1, 2],
      "One name is not in CommonModule.",
      "date, currency and uppercase are built in. There is no built-in reverse pipe.")
    m(E, "DI", "What does @Injectable({ providedIn: 'root' }) do?",
      ["Registers the service in the root injector as a tree-shakable singleton", "Creates a new instance per component", "Makes the service available only in AppModule providers", "Prevents the service from being injected"], [0],
      "Root means application-wide.",
      "providedIn: 'root' registers one shared instance in the root environment injector and lets unused services be tree-shaken. A new instance per component requires component-level providers.")
    m(E, "Control flow", "Which built-in control flow block replaces *ngIf in Angular 17+?",
      ["@when", "@if", "@show", "@check"], [1],
      "It can be followed by @else.",
      "@if (condition) { } @else { } is the built-in conditional. The other names do not exist.",
      "@if (user) {\n  <p>{{ user.name }}</p>\n} @else {\n  <p>Guest</p>\n}")

    M = "Medium"
    # ---------------- MEDIUM (60) ----------------
    m(M, "Change detection", "For a component with OnPush change detection, which situations cause it to be checked? (Select all that apply.)",
      ["A parent mutates a property of an object passed as input", "An input receives a new object reference", "A DOM event handler in its template runs", "A field changes inside an unrelated service timer"], [1, 2],
      "OnPush looks for specific triggers, not any change.",
      "OnPush checks on input reference changes, events from the component's template, async pipe emissions, signal changes or markForCheck. In-place mutation and unrelated timer changes are not triggers.")
    m(M, "Change detection", "A parent does this.items.push(newItem) and passes items to an OnPush child's @Input. The child's template does not update. Which fix is best?",
      ["Pass a new array such as this.items = [...this.items, newItem]", "Change the child to ChangeDetectionStrategy.Default only in production", "Call ngOnInit manually on the child", "Wrap the push in setTimeout"], [0],
      "OnPush compares input references.",
      "OnPush only sees input changes when the reference changes, so creating a new array triggers a check. Calling ngOnInit or setTimeout does not alter reference comparison.")
    m(M, "Signals", "Which statements about computed() signals are true? (Select all that apply.)",
      ["It is read-only", "Its value is lazily evaluated", "Its result is memoized until dependencies change", "It can be updated with set()"], [0, 1, 2],
      "It derives values rather than storing them.",
      "computed signals are lazy, cached, and read-only. There is no set() on them.")
    m(M, "Signals", "What is effect() best suited for?",
      ["Deriving a value from other signals", "Running side effects such as logging or syncing to localStorage when signals change", "Replacing all template bindings", "Creating HTTP requests on every render"], [1],
      "Think of work that does not produce a new value.",
      "effect() runs side effects when the signals it reads change. Deriving values is the job of computed().")
    m(M, "Signals", "Which line correctly increments a writable signal count based on its previous value?",
      ["count++", "count(count() + 1)", "count.update(c => c + 1)", "count = count() + 1"], [2],
      "Signals expose update and set methods.",
      "count.update(c => c + 1) is the idiomatic form. count++ and reassignment break the signal, and count(x) is a call that reads, not writes.")
    m(M, "Signals", "What happens if you try to call set() on a signal created with computed()?",
      ["It overrides the derived value until dependencies change", "It is a compile-time error because computed signals are read-only", "It resets the dependencies", "It works only inside effect()"], [1],
      "The type returned is Signal, not WritableSignal.",
      "computed returns a read-only Signal<T> without set or update. The value can only change via its dependencies.")
    m(M, "RxJS", "A search box fires a request per keystroke and stale responses must be discarded. Which operator fits?",
      ["mergeMap", "concatMap", "switchMap", "forkJoin"], [2],
      "You want to cancel the previous inner Observable.",
      "switchMap unsubscribes from the previous inner Observable when a new value arrives, so only the latest response counts. mergeMap and concatMap would keep older requests running.",
      "this.term$.pipe(\n  debounceTime(300),\n  distinctUntilChanged(),\n  switchMap(t => this.api.search(t))\n)")
    m(M, "RxJS", "You must run save requests one after another in the order triggered. Which operator is appropriate?",
      ["concatMap", "switchMap", "mergeMap", "exhaustMap"], [0],
      "It queues inner Observables.",
      "concatMap waits for each inner Observable to complete before starting the next. mergeMap runs concurrently, switchMap cancels, exhaustMap ignores new ones.")
    m(M, "RxJS", "A login button may be clicked many times quickly; you want to ignore clicks while a request is in flight. Which operator?",
      ["switchMap", "exhaustMap", "concatMap", "mergeMap"], [1],
      "New outer values should be dropped while busy.",
      "exhaustMap ignores outer emissions while its current inner Observable is active. switchMap would cancel the in-flight request and concatMap would queue them.")
    m(M, "RxJS", "How does combineLatest behave?",
      ["Emits after all sources complete", "Emits an array of latest values whenever any source emits, once each has emitted at least once", "Emits sources one after another", "Emits only the first source value"], [1],
      "Every source needs one value before the first emission.",
      "combineLatest emits the combined latest values after every input has emitted once, and again on every later emission. Waiting for completion describes forkJoin.")
    m(M, "RxJS", "What does forkJoin do when given several HTTP request Observables?",
      ["Runs them in sequence", "Runs them in parallel and emits the last values once all complete", "Emits each response as it arrives", "Cancels all but the fastest"], [1],
      "It needs every source to complete.",
      "forkJoin subscribes to all sources concurrently and emits one array of final values after all complete. Emitting as they arrive is closer to merge; the fastest wins with race.")
    m(M, "HttpClient", "Two components each subscribe to the same this.http.get(url) Observable stored in a variable. How many HTTP requests are made?",
      ["One, because the Observable is shared automatically", "Two, because the Observable is cold", "Zero until the component renders", "One per second"], [1],
      "Think about cold Observables and shareReplay.",
      "Each subscription to an HttpClient Observable triggers its own request. Use shareReplay or a signal/store to share one response.")
    m(M, "RxJS", "How does BehaviorSubject differ from Subject?",
      ["It requires an initial value and emits the current value to new subscribers", "It cannot be completed", "It replays all past values", "It is unicast"], [0],
      "Think of state holders.",
      "BehaviorSubject holds a current value, requires an initial one, and immediately emits it to new subscribers. ReplaySubject can replay many values; Subject emits only future ones.")
    m(M, "Memory management", "You want an Observable subscription to auto-unsubscribe when the component is destroyed, inside a field initializer. Which approach fits?",
      ["Pipe through takeUntilDestroyed()", "Use takeUntil(this.ngOnDestroy)", "Call unsubscribe in ngOnInit", "Use first() always"], [0],
      "It comes from @angular/core/rxjs-interop and uses the injection context.",
      "takeUntilDestroyed() completes the stream when the owning context is destroyed. The others do not tie to destruction.",
      "private destroyRef = inject(DestroyRef);\nngOnInit() {\n  this.ticks$.pipe(takeUntilDestroyed(this.destroyRef)).subscribe();\n}")
    m(M, "Error handling", "What must the selector function of catchError return?",
      ["A plain value", "An Observable", "void", "A Promise only"], [1],
      "It replaces the failed stream.",
      "catchError returns an ObservableInput, e.g. of([]) or EMPTY, or rethrows via throwError. A plain value is not valid.")
    m(M, "Memory management", "Which subscriptions typically need manual cleanup in a component? (Select all that apply.)",
      ["interval(1000).subscribe(...)", "fromEvent(document, 'click').subscribe(...)", "http.get(url).subscribe(...)", "An Observable consumed with the async pipe"], [0, 1],
      "Look for streams that never complete.",
      "interval and DOM event streams never complete. HttpClient requests complete after a response and the async pipe unsubscribes itself.")
    m(M, "DI", "A service is listed in a component's providers array. What is the effect?",
      ["It is a singleton across the app", "Each component instance gets its own service instance", "It is shared with all lazy modules", "It is ignored"], [1],
      "Component-level providers belong to the element injector.",
      "Providing at component level creates a new instance per component instance, also visible to its children. Root-level providers are shared.")
    m(M, "DI", "Why use an InjectionToken?",
      ["To inject non-class values such as config objects or primitives", "To speed up bootstrapping", "To replace @Injectable", "To make services lazy"], [0],
      "Interfaces vanish at runtime.",
      "Types and interfaces have no runtime identity, so a token identifies the dependency. It does not replace @Injectable for classes.",
      "export const API_URL = new InjectionToken<string>('API_URL');\nproviders: [{ provide: API_URL, useValue: '/api' }]")
    m(M, "DI", "Which provider form supplies a ready-made constant object for a token?",
      ["useClass", "useValue", "useExisting", "useFactory with deps only"], [1],
      "It uses the object as is.",
      "useValue provides the literal value. useClass instantiates a class, useExisting aliases another token, and useFactory runs a function.")
    m(M, "DI", "What does inject(Logger, { optional: true }) return if no provider exists?",
      ["Throws NullInjectorError", "null", "undefined", "A new Logger"], [1],
      "It is the modern equivalent of @Optional().",
      "With optional: true, a missing provider yields null instead of an error.")
    m(M, "DI", "Where does Angular's injector first look for a dependency requested by a component?",
      ["Root environment injector", "The component's own element injector, then up the element tree, then environment injectors", "Only the NgModule", "The browser's global scope"], [1],
      "Resolution walks from the closest to the broadest.",
      "Angular checks the element injector hierarchy (component and directive providers, viewProviders) and then falls back to environment injectors such as root. It is not global.")
    m(M, "DI", "Where is calling inject() valid? (Select all that apply.)",
      ["A field initializer in a component", "The constructor", "Inside a setTimeout callback", "Inside ngOnInit"], [0, 1],
      "It needs an injection context.",
      "inject() works during construction (constructor and field initializers) and in factory functions, not in later lifecycle methods or async callbacks.")
    m(M, "HttpClient", "Why must an interceptor call req.clone({...}) to add a header?",
      ["HttpRequest objects are immutable", "clone is faster", "Headers cannot be set otherwise in Angular", "It triggers a new subscription"], [0],
      "Requests cannot be changed in place.",
      "HttpRequest is immutable, so you create a modified copy with clone and pass it to next(). The reason is immutability, not performance.",
      "export const authInterceptor: HttpInterceptorFn = (req, next) => {\n  const r = req.clone({ setHeaders: { Authorization: 'Bearer x' } });\n  return next(r);\n};")
    m(M, "HttpClient", "How do you register a functional interceptor?",
      ["provideHttpClient(withInterceptors([authInterceptor]))", "providers: [{ provide: INTERCEPTOR, useValue: authInterceptor }]", "HttpClient.use(authInterceptor)", "imports: [InterceptorModule]"], [0],
      "Use a feature function with provideHttpClient.",
      "withInterceptors takes an array of functional interceptors. The other forms are not valid APIs.")
    m(M, "Routing", "Which values may a CanActivateFn return? (Select all that apply.)",
      ["boolean", "UrlTree", "An Observable of boolean or UrlTree", "A string route name"], [0, 1, 2],
      "A redirect is represented by an object, not a string.",
      "Guards can return boolean, UrlTree (to redirect), or Observable/Promise of those. Strings are not accepted.",
      "export const authGuard: CanActivateFn = () => {\n  return inject(AuthService).loggedIn() || inject(Router).parseUrl('/login');\n};")
    m(M, "Routing", "Which route properties enable lazy loading? (Select all that apply.)",
      ["loadComponent", "loadChildren", "lazy: true", "import"], [0, 1],
      "Both take a dynamic import function.",
      "loadComponent lazy loads a standalone component and loadChildren a routes array or module. lazy and import are not route properties.",
      "{ path: 'admin', loadChildren: () => import('./admin/routes').then(m => m.ADMIN_ROUTES) }")
    m(M, "Routing", "A route /user/:id navigates from /user/1 to /user/2, reusing the same component instance. How do you reliably see the new id? (Select all that apply.)",
      ["Subscribe to route.paramMap", "Read route.snapshot.paramMap in ngOnInit only", "Use withComponentInputBinding and an input named id", "Rely on ngOnInit running again"], [0, 2],
      "The instance is reused.",
      "Observable params and bound inputs update. The snapshot read once in ngOnInit is stale and ngOnInit does not run again for a reused instance.")
    m(M, "Routing", "What problem does withComponentInputBinding() solve?",
      ["It binds route params, query params and data to component inputs", "It binds two components together", "It makes guards synchronous", "It enables SSR"], [0],
      "It is a router feature passed to provideRouter.",
      "With it, route parameters and data are set directly on matching inputs, removing the need to inject ActivatedRoute.")
    m(M, "Routing", "What is a route resolver used for?",
      ["Prefetching data before the route activates", "Blocking unauthenticated users", "Lazy loading modules", "Rendering 404 pages"], [0],
      "Data is ready when the component is created.",
      "Resolvers fetch data before activation, exposing it via route data. Guards handle access, and loadChildren handles lazy loading.")
    m(M, "Routing", "Why is pathMatch: 'full' needed on { path: '', redirectTo: 'home', pathMatch: 'full' }?",
      ["Without it, the empty path prefix matches every URL and causes redirect loops", "It improves SEO", "It makes the route case-sensitive", "It enables lazy loading"], [0],
      "The default match is prefix.",
      "An empty path is a prefix of every URL, so with the default 'prefix' strategy everything would redirect. 'full' matches only an empty URL.")
    m(M, "Forms", "Which form control state flags exist in Angular forms? (Select all that apply.)",
      ["touched", "dirty", "pristine", "visited"], [0, 1, 2],
      "One name is not part of AbstractControl.",
      "touched, dirty and pristine are properties on controls. visited is not.")
    m(M, "Forms", "How do you react to value changes of a reactive FormControl?",
      ["Subscribe to control.valueChanges", "Listen for the ngChange event", "Poll control.value in ngDoCheck only", "Use @Output on the control"], [0],
      "It is an Observable.",
      "valueChanges emits each time the value changes. ngChange and @Output on controls do not exist.")
    m(M, "Forms", "What should a synchronous custom validator function return when the value is valid?",
      ["true", "null", "undefined", "An empty string"], [1],
      "Errors are represented as an object.",
      "A ValidatorFn returns null for valid and a ValidationErrors object like { forbidden: true } for invalid.",
      "const noSpaces: ValidatorFn = c =>\n  /\\s/.test(c.value) ? { spaces: true } : null;")
    m(M, "Forms", "What is the difference between setValue and patchValue on a FormGroup?",
      ["patchValue allows a partial object while setValue requires all controls", "setValue allows partial objects", "They are identical", "patchValue only works for FormArray"], [0],
      "One is strict about the shape.",
      "setValue throws if any control is missing, while patchValue updates only the supplied properties.")
    m(M, "Forms", "Which statements about reactive forms are true? (Select all that apply.)",
      ["The form model is defined in the component class", "Values can be read synchronously", "They are generally easier to unit test than template-driven forms", "They require ngModel on every input"], [0, 1, 2],
      "They use formControl directives, not ngModel.",
      "Reactive forms make the model explicit, synchronous and testable. They use formControlName/formControl, not ngModel.")
    m(M, "Forms", "What is the purpose of implementing ControlValueAccessor?",
      ["To let a custom component work with Angular forms directives like formControl or ngModel", "To validate asynchronously", "To lazy load a form", "To intercept HTTP calls"], [0],
      "It bridges the view and the forms model.",
      "ControlValueAccessor defines writeValue and change/touch callbacks so custom components integrate with form controls. Validation uses Validators.")
    m(M, "Control flow", "Which contextual variables are available inside @for? (Select all that apply.)",
      ["$index", "$first", "$key", "$item"], [0, 1],
      "Think of loop positions.",
      "@for provides $index, $first, $last, $even, $odd and $count. $key and $item do not exist.",
      "@for (u of users; track u.id; let i = $index) {\n  <li>{{ i }} {{ u.name }}</li>\n} @empty {\n  <li>No users</li>\n}")
    m(M, "Control flow", "In a standalone component, what is a practical difference between @if and *ngIf?",
      ["@if needs no import of NgIf or CommonModule", "@if is slower", "*ngIf supports @else but @if does not", "@if works only in NgModules"], [0],
      "Built-in control flow is part of the template syntax.",
      "The new blocks are built into the compiler and require no imports, whereas *ngIf requires NgIf. @if fully supports @else.")
    m(M, "Control flow", "Why is track important in @for?",
      ["It lets Angular reuse DOM nodes for unchanged items when the list changes", "It sorts the list", "It filters null items", "It subscribes to the array"], [0],
      "Think about re-rendering cost.",
      "A stable identity like track item.id lets Angular move and reuse nodes instead of recreating them. It does not sort or filter.")
    m(M, "Deferrable views", "Which are valid @defer triggers? (Select all that apply.)",
      ["on idle", "on viewport", "on hover", "on scroll"], [0, 1, 2],
      "One is not a defer trigger.",
      "on idle, on viewport, on hover, on interaction, on immediate and on timer are supported, as is when condition. There is no on scroll trigger.")
    m(M, "Deferrable views", "Which @defer sub-block displays content while the deferred dependencies are being fetched?",
      ["@placeholder", "@loading", "@error", "@fallback"], [1],
      "It can have minimum and after parameters.",
      "@loading shows during loading, @placeholder before the trigger, and @error on failure. @fallback is not a defer block.")
    m(M, "Deferrable views", "A component inside @defer still loads eagerly. What is a likely cause?",
      ["It is also referenced outside the @defer block, such as in the imports usage elsewhere in the template", "@defer only works with NgModules", "The component lacks @Input", "The route is not lazy"], [0],
      "Deferral works only if nothing else references it directly.",
      "Deferred dependencies must be standalone and not used eagerly elsewhere in the same file, otherwise they are in the main bundle.")
    m(M, "Standalone", "What does bootstrapApplication(AppComponent, { providers: [...] }) replace?",
      ["platformBrowserDynamic().bootstrapModule(AppModule)", "ng serve", "TestBed", "RouterModule.forRoot"], [0],
      "It bootstraps without a root NgModule.",
      "bootstrapApplication starts a standalone root component directly and takes app-wide providers, replacing bootstrapModule with an AppModule.")
    m(M, "Standalone", "What can a standalone component list in its imports array? (Select all that apply.)",
      ["Other standalone components and pipes", "NgModules", "Injectable services", "Route definitions"], [0, 1],
      "Think of template dependencies.",
      "imports accepts standalone components, directives, pipes and NgModules. Services use providers and routes are given to the router.")
    m(M, "Standalone", "Which are valid provider functions in a standalone application? (Select all that apply.)",
      ["provideRouter(routes)", "provideHttpClient()", "provideModule()", "provideComponent()"], [0, 1],
      "Two of them are real APIs.",
      "provideRouter and provideHttpClient configure the router and HttpClient. provideModule and provideComponent do not exist.")
    m(M, "NgModules", "What is the purpose of the forRoot/forChild convention in modules such as RouterModule?",
      ["To provide singleton services once in the root while child modules only add configuration or routes", "To make modules lazy", "To define two components", "To replace declarations"], [0],
      "It avoids duplicated providers.",
      "forRoot returns a ModuleWithProviders with app-wide services, while forChild registers only extra routes without re-providing services.")
    m(M, "NgModules", "You declare the same component in two NgModules. What happens?",
      ["Angular merges them", "Compilation error: a component can be declared in only one module", "The second is ignored silently", "It becomes a singleton"], [1],
      "Ownership must be unique.",
      "Each non-standalone component belongs to exactly one NgModule. To reuse it, export it from that module or make it standalone.")
    m(M, "NgModules", "A SharedModule declares AppButtonComponent. A FeatureModule imports SharedModule but cannot use <app-button>. What is missing?",
      ["SharedModule must export AppButtonComponent", "FeatureModule must provide it", "AppButtonComponent needs providedIn root", "bootstrap must include it"], [0],
      "Importing alone does not make declarations visible.",
      "Only exported declarations are usable by importing modules. providers and bootstrap are unrelated to template visibility.")
    m(M, "Pipes", "When does a pure pipe re-run its transform?",
      ["On every change detection cycle", "Only when its input value or parameters change by reference or primitive value", "Only on route change", "Only once"], [1],
      "Pure means same input gives same output.",
      "Pure pipes are re-executed only when their input changes (primitive value or new reference), so mutating an array in place will not retrigger them.")
    m(M, "Pipes", "What is the main drawback of setting pure: false on a custom pipe?",
      ["It runs on every change detection cycle, which may hurt performance", "It cannot take arguments", "It is not allowed with standalone pipes", "It cannot be used with the async pipe"], [0],
      "Think of how often it is called.",
      "Impure pipes run every cycle, so expensive transforms can slow the app. They can take arguments and be standalone.")
    m(M, "Pipes", "A template uses (user$ | async)?.name and (user$ | async)?.email. What is the problem?",
      ["Each async pipe creates its own subscription, possibly duplicating requests", "async cannot be used twice", "The optional chaining operator is invalid", "It leaks memory in all cases"], [0],
      "How many subscriptions are made?",
      "Each use subscribes separately, which can fire multiple HTTP calls for cold Observables. Use @if (user$ | async; as user) once instead.",
      "@if (user$ | async; as user) {\n  <p>{{ user.name }} {{ user.email }}</p>\n}")
    m(M, "Directives", "Which decorators are used in an attribute directive to listen for host events and bind host properties? (Select all that apply.)",
      ["@HostListener", "@HostBinding", "@ViewChild", "@Output"], [0, 1],
      "They interact with the host element.",
      "@HostListener subscribes to host events and @HostBinding sets host properties or attributes. @ViewChild queries the template and @Output emits events.")
    m(M, "Directives", "What does <ng-content></ng-content> do inside a component template?",
      ["Projects content supplied between the component's tags", "Creates a new component", "Renders content in a different route", "Lazy loads the content"], [0],
      "It is used for content projection.",
      "ng-content marks where parent-supplied child content is rendered. It does not create components or load anything lazily.")
    m(M, "Lifecycle", "A @ViewChild({ static: false }) query (default) is first reliably available in which hook?",
      ["constructor", "ngOnInit", "ngAfterViewInit", "ngOnChanges"], [2],
      "View children are created after the view is initialized.",
      "Dynamic view queries are resolved by ngAfterViewInit. At constructor time and ngOnInit they may be undefined (unless static: true).")
    m(M, "Lifecycle", "A parent changes a property of an object bound to a child's @Input without replacing the reference. Will the child's ngOnChanges fire?",
      ["Yes, always", "No, ngOnChanges fires only when the input binding value or reference changes", "Only in production mode", "Only if OnPush is used"], [1],
      "Angular compares the bound value, not nested fields.",
      "ngOnChanges compares binding values using identity, so in-place mutation is not detected. Use a new reference or ngDoCheck.")
    m(M, "Testing", "Which methods of HttpTestingController are commonly used in tests? (Select all that apply.)",
      ["expectOne", "verify", "mockResponse", "flush on the returned TestRequest"], [0, 1, 3],
      "One name is invented.",
      "expectOne finds a pending request, flush supplies a response, and verify asserts none are left. mockResponse does not exist.")
    m(M, "Testing", "Why call fixture.detectChanges() in a component test?",
      ["To run change detection so bindings render and ngOnInit runs for the first time", "To compile the module", "To clear the DOM", "To restart the test runner"], [0],
      "Tests do not auto-run change detection by default.",
      "The first detectChanges triggers ngOnInit and updates the view. Without it the template shows initial, unrendered state.")
    m(M, "Testing", "How do you replace a real service with a fake in a TestBed?",
      ["providers: [{ provide: DataService, useValue: fakeService }]", "imports: [fakeService]", "declarations: [fakeService]", "Call new DataService() in the component"], [0],
      "Override the DI provider.",
      "Providing the same token with useValue (or useClass) swaps the implementation. imports and declarations are for modules and view classes.")
    m(M, "Signals", "How do you declare a required signal input in a component?",
      ["name = input.required<string>();", "@Input({ signal: true }) name!: string;", "name = signal.required<string>();", "name = required(input<string>());"], [0],
      "It is a static helper on input.",
      "input.required<T>() declares a required signal input read as name(). The other forms are not valid APIs.")
    m(M, "Signals", "What does toSignal() from @angular/core/rxjs-interop do?",
      ["Converts an Observable into a signal that holds its latest value", "Converts a signal into a Promise", "Subscribes without cleanup", "Creates a Subject"], [0],
      "It bridges RxJS and signals.",
      "toSignal subscribes to the Observable and exposes the latest value as a read-only signal, unsubscribing automatically when its context is destroyed.",
      "users = toSignal(this.http.get<User[]>('/api/users'), { initialValue: [] });")
