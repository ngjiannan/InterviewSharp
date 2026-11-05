# Angular MCQ practice (with answers)


## Easy

### 1. [Components] Which decorator marks a TypeScript class as an Angular component?

- A. @NgModule()
- B. @Component()
- C. @Injectable()
- D. @Directive()

**Answer:** B

**Explanation:** @Component() attaches metadata such as selector, template and styles to the class. @Injectable() is for services, @NgModule() groups declarations in classic modules, and @Directive() has no template.

### 2. [Standalone] In a standalone component, which metadata property lists the other components, directives and pipes its template uses?

- A. declarations
- B. exports
- C. providers
- D. imports

**Answer:** D

**Explanation:** Standalone components declare their template dependencies directly in the imports array. declarations belongs to NgModules, providers configures DI, and exports is for NgModules.

### 3. [Control flow] What does the @for block require in Angular's built-in control flow?

```
@for (item of items; track item.id) {
  <li>{{ item.name }}</li>
}
```

- A. A track expression
- B. A trackBy function declared in the class
- C. An index alias
- D. The CommonModule import

**Answer:** A

**Explanation:** @for (item of items; track item.id) requires a track expression so the DOM can be reused efficiently. No CommonModule import is needed, and an index alias is optional.

### 4. [Signals] How do you create a writable signal holding the number 0?

- A. const count = new Signal(0);
- B. const count = computed(0);
- C. const count = signal(0);
- D. const count = ref(0);

**Answer:** C

**Explanation:** signal(0) returns a WritableSignal<number>. computed() takes a derivation function and is read-only, ref() is Vue, and Signal is not constructed with new.

### 5. [Signals] How do you read the current value of a signal named count in a template?

- A. {{ count.value }}
- B. {{ count() }}
- C. {{ count.get }}
- D. {{ count }}

**Answer:** B

**Explanation:** A signal is read by calling it: count(). Without parentheses you get the function itself, and signals have no value or get property.

### 6. [DI] Which function can be used instead of constructor parameters to obtain a dependency in modern Angular?

```
export class UserComponent {
  private http = inject(HttpClient);
}
```

- A. resolve()
- B. require()
- C. provide()
- D. inject()

**Answer:** D

**Explanation:** inject(MyService) retrieves a dependency, for example in a field initializer. resolve, provide and require are not Angular DI retrieval functions.

### 7. [Pipes] What is the main benefit of the async pipe?

- A. It subscribes to an Observable or Promise and unsubscribes automatically
- B. It makes HTTP calls synchronous
- C. It converts any value to a Promise
- D. It caches API responses

**Answer:** A

**Explanation:** The async pipe subscribes, exposes the latest value, marks the view for check, and unsubscribes on destroy. It does not make anything synchronous or cache responses.

### 8. [Directives] Which of these are built-in structural directives? (Select all that apply.)

- A. ngStyle
- B. *ngFor
- C. ngClass
- D. *ngIf

**Answer:** B, D

**Explanation:** *ngIf and *ngFor change the DOM structure. ngClass and ngStyle are attribute directives that modify existing elements.

### 9. [Lifecycle] Which lifecycle hook is typically used for initialization logic after the first inputs are set?

- A. ngOnInit
- B. ngOnDestroy
- C. ngDoCheck
- D. ngAfterViewChecked

**Answer:** A

**Explanation:** ngOnInit runs once after input properties are initialized. ngOnDestroy is for cleanup, while ngAfterViewChecked and ngDoCheck run repeatedly.

### 10. [Lifecycle] Where should you release resources such as manual subscriptions or timers?

- A. ngOnInit
- B. ngOnDestroy
- C. constructor
- D. ngOnChanges

**Answer:** B

**Explanation:** ngOnDestroy runs right before the component is destroyed, making it the place for cleanup. The other hooks run during creation or updates.

### 11. [Data binding] Which syntax binds a component property to a DOM element property?

- A. (value)="name"
- B. #value="name"
- C. [value]="name"
- D. {value}="name"

**Answer:** C

**Explanation:** [value]="name" is property binding. Parentheses are event binding, and # declares a template reference variable.

### 12. [Data binding] Which of the following are valid ways to bind a click event? (Select all that apply.)

- A. @click="save()"
- B. [click]="save()"
- C. (click)="save()"
- D. on-click="save()"

**Answer:** C, D

**Explanation:** (click) and on-click are equivalent event bindings. [click] is property binding and @click is Vue syntax.

### 13. [Forms] What does the banana-in-a-box syntax [(ngModel)] provide, and what is required for it?

- A. One-way binding; ReactiveFormsModule
- B. Event binding only; CommonModule
- C. Two-way binding; FormsModule
- D. Two-way binding; HttpClientModule

**Answer:** C

**Explanation:** [(ngModel)] is two-way binding for template-driven forms and needs FormsModule (or importing NgModel in a standalone component). ReactiveFormsModule is for FormControl-based forms.

### 14. [Routing] Which element marks where the router renders the matched component?

- A. <router-outlet>
- B. <router-view>
- C. <ng-content>
- D. <ng-container>

**Answer:** A

**Explanation:** <router-outlet> is where routed components are displayed. router-view is not Angular, ng-container is a grouping element, and ng-content projects content.

### 15. [Routing] Which directive creates a navigation link without a full page reload?

- A. ngLink
- B. navigateTo
- C. href
- D. routerLink

**Answer:** D

**Explanation:** routerLink builds the URL and navigates through the Router. A plain href triggers a full reload; navigateTo and ngLink do not exist.

### 16. [HttpClient] Which of these are methods provided by HttpClient? (Select all that apply.)

- A. delete
- B. fetch
- C. post
- D. get

**Answer:** A, C, D

**Explanation:** HttpClient exposes get, post, put, patch, delete and others, each returning an Observable. There is no fetch method on HttpClient.

### 17. [HttpClient] In a standalone application, how do you make HttpClient available?

```
bootstrapApplication(AppComponent, {
  providers: [provideHttpClient()]
});
```

- A. Import HttpClient in the component's imports
- B. Add provideHttpClient() to the application providers
- C. Declare HttpClient in declarations
- D. Call new HttpClient()

**Answer:** B

**Explanation:** provideHttpClient() registers HttpClient and its backend. HttpClient is a service, not a component or module import, and should not be constructed manually.

### 18. [Forms] Which of these classes belong to Reactive Forms? (Select all that apply.)

- A. NgModel
- B. FormGroup
- C. FormArray
- D. FormControl

**Answer:** B, C, D

**Explanation:** FormGroup, FormControl and FormArray are the building blocks of reactive forms. NgModel is the directive behind template-driven forms.

### 19. [RxJS] When does a cold Observable such as one returned by HttpClient.get start doing work?

- A. When it is created
- B. When the component initializes
- C. When pipe() is called
- D. When it is subscribed to

**Answer:** D

**Explanation:** Observables execute only on subscribe. Creating one or adding operators with pipe() does not start the request.

### 20. [RxJS] Which of the following are RxJS operators? (Select all that apply.)

- A. map
- B. ngOnInit
- C. tap
- D. filter

**Answer:** A, C, D

**Explanation:** map, filter and tap are operators used inside pipe(). ngOnInit is an Angular lifecycle hook.

### 21. [NgModules] In a classic NgModule, what is the purpose of the declarations array?

- A. List components, directives and pipes that belong to the module
- B. List services to inject
- C. List modules to import
- D. List routes

**Answer:** A

**Explanation:** declarations registers the module's components, directives and pipes. Services go in providers, other modules go in imports.

### 22. [Components] Which are valid ways to declare a component input? (Select all that apply.)

- A. title = input<string>();
- B. @Input() title = '';
- C. @Output() title = '';
- D. title = output<string>();

**Answer:** A, B

**Explanation:** @Input() and the input() function both declare inputs. @Output and output() declare events emitted to the parent.

### 23. [Components] Which combination lets a child component send an event to its parent?

- A. @Output() with EventEmitter
- B. @Input() with a callback signal
- C. @Injectable with providedIn
- D. @ViewChild with ngOnInit

**Answer:** A

**Explanation:** An @Output EventEmitter (or the output() function) emits events the parent listens to with (event) binding. @Input flows data downward.

### 24. [Change detection] Which snippet configures a component to use the OnPush change detection strategy?

- A. @Component({ detection: ChangeDetectionStrategy.Default })
- B. @Component({ changeDetection: ChangeDetectionStrategy.OnPush })
- C. @Component({ onPush: true })
- D. @Component({ strategy: 'OnPush' })

**Answer:** B

**Explanation:** changeDetection: ChangeDetectionStrategy.OnPush opts into OnPush checks. The other property names do not exist or select Default.

### 25. [Testing] Which Angular utility configures and creates a testing module for unit tests?

- A. TestBed
- B. ComponentFactory
- C. TestRunner
- D. NgTest

**Answer:** A

**Explanation:** TestBed.configureTestingModule sets up providers and imports for tests. The other names are not Angular testing APIs for this purpose.

### 26. [Deferrable views] What is the purpose of the @defer block?

```
@defer (on viewport) {
  <app-chart />
} @placeholder {
  <p>Chart</p>
}
```

- A. To lazy load the template dependencies it contains
- B. To debounce user input
- C. To defer HTTP requests
- D. To delay a component's lifecycle hooks

**Answer:** A

**Explanation:** @defer splits the enclosed standalone components, directives and pipes into separate chunks loaded on a trigger. It does not debounce or delay HTTP.

### 27. [Tooling] Which Angular CLI command generates a new component?

- A. ng build component
- B. ng new component
- C. ng add component
- D. ng generate component hero

**Answer:** D

**Explanation:** ng generate component hero (or ng g c hero) scaffolds a component. ng new creates a workspace, ng build compiles, ng add installs packages.

### 28. [Pipes] Which of these are built-in Angular pipes? (Select all that apply.)

- A. currency
- B. uppercase
- C. reverse
- D. date

**Answer:** A, B, D

**Explanation:** date, currency and uppercase are built in. There is no built-in reverse pipe.

### 29. [DI] What does @Injectable({ providedIn: 'root' }) do?

- A. Makes the service available only in AppModule providers
- B. Registers the service in the root injector as a tree-shakable singleton
- C. Prevents the service from being injected
- D. Creates a new instance per component

**Answer:** B

**Explanation:** providedIn: 'root' registers one shared instance in the root environment injector and lets unused services be tree-shaken. A new instance per component requires component-level providers.

### 30. [Control flow] Which built-in control flow block replaces *ngIf in Angular 17+?

```
@if (user) {
  <p>{{ user.name }}</p>
} @else {
  <p>Guest</p>
}
```

- A. @when
- B. @if
- C. @show
- D. @check

**Answer:** B

**Explanation:** @if (condition) { } @else { } is the built-in conditional. The other names do not exist.


## Medium

### 31. [Change detection] For a component with OnPush change detection, which situations cause it to be checked? (Select all that apply.)

- A. An input receives a new object reference
- B. A DOM event handler in its template runs
- C. A field changes inside an unrelated service timer
- D. A parent mutates a property of an object passed as input

**Answer:** A, B

**Explanation:** OnPush checks on input reference changes, events from the component's template, async pipe emissions, signal changes or markForCheck. In-place mutation and unrelated timer changes are not triggers.

### 32. [Change detection] A parent does this.items.push(newItem) and passes items to an OnPush child's @Input. The child's template does not update. Which fix is best?

- A. Change the child to ChangeDetectionStrategy.Default only in production
- B. Call ngOnInit manually on the child
- C. Pass a new array such as this.items = [...this.items, newItem]
- D. Wrap the push in setTimeout

**Answer:** C

**Explanation:** OnPush only sees input changes when the reference changes, so creating a new array triggers a check. Calling ngOnInit or setTimeout does not alter reference comparison.

### 33. [Signals] Which statements about computed() signals are true? (Select all that apply.)

- A. It is read-only
- B. Its value is lazily evaluated
- C. It can be updated with set()
- D. Its result is memoized until dependencies change

**Answer:** A, B, D

**Explanation:** computed signals are lazy, cached, and read-only. There is no set() on them.

### 34. [Signals] What is effect() best suited for?

- A. Deriving a value from other signals
- B. Creating HTTP requests on every render
- C. Replacing all template bindings
- D. Running side effects such as logging or syncing to localStorage when signals change

**Answer:** D

**Explanation:** effect() runs side effects when the signals it reads change. Deriving values is the job of computed().

### 35. [Signals] Which line correctly increments a writable signal count based on its previous value?

- A. count.update(c => c + 1)
- B. count = count() + 1
- C. count(count() + 1)
- D. count++

**Answer:** A

**Explanation:** count.update(c => c + 1) is the idiomatic form. count++ and reassignment break the signal, and count(x) is a call that reads, not writes.

### 36. [Signals] What happens if you try to call set() on a signal created with computed()?

- A. It resets the dependencies
- B. It overrides the derived value until dependencies change
- C. It works only inside effect()
- D. It is a compile-time error because computed signals are read-only

**Answer:** D

**Explanation:** computed returns a read-only Signal<T> without set or update. The value can only change via its dependencies.

### 37. [RxJS] A search box fires a request per keystroke and stale responses must be discarded. Which operator fits?

```
this.term$.pipe(
  debounceTime(300),
  distinctUntilChanged(),
  switchMap(t => this.api.search(t))
)
```

- A. mergeMap
- B. switchMap
- C. forkJoin
- D. concatMap

**Answer:** B

**Explanation:** switchMap unsubscribes from the previous inner Observable when a new value arrives, so only the latest response counts. mergeMap and concatMap would keep older requests running.

### 38. [RxJS] You must run save requests one after another in the order triggered. Which operator is appropriate?

- A. exhaustMap
- B. switchMap
- C. mergeMap
- D. concatMap

**Answer:** D

**Explanation:** concatMap waits for each inner Observable to complete before starting the next. mergeMap runs concurrently, switchMap cancels, exhaustMap ignores new ones.

### 39. [RxJS] A login button may be clicked many times quickly; you want to ignore clicks while a request is in flight. Which operator?

- A. exhaustMap
- B. concatMap
- C. mergeMap
- D. switchMap

**Answer:** A

**Explanation:** exhaustMap ignores outer emissions while its current inner Observable is active. switchMap would cancel the in-flight request and concatMap would queue them.

### 40. [RxJS] How does combineLatest behave?

- A. Emits an array of latest values whenever any source emits, once each has emitted at least once
- B. Emits only the first source value
- C. Emits sources one after another
- D. Emits after all sources complete

**Answer:** A

**Explanation:** combineLatest emits the combined latest values after every input has emitted once, and again on every later emission. Waiting for completion describes forkJoin.

### 41. [RxJS] What does forkJoin do when given several HTTP request Observables?

- A. Cancels all but the fastest
- B. Runs them in sequence
- C. Emits each response as it arrives
- D. Runs them in parallel and emits the last values once all complete

**Answer:** D

**Explanation:** forkJoin subscribes to all sources concurrently and emits one array of final values after all complete. Emitting as they arrive is closer to merge; the fastest wins with race.

### 42. [HttpClient] Two components each subscribe to the same this.http.get(url) Observable stored in a variable. How many HTTP requests are made?

- A. Zero until the component renders
- B. One per second
- C. One, because the Observable is shared automatically
- D. Two, because the Observable is cold

**Answer:** D

**Explanation:** Each subscription to an HttpClient Observable triggers its own request. Use shareReplay or a signal/store to share one response.

### 43. [RxJS] How does BehaviorSubject differ from Subject?

- A. It is unicast
- B. It replays all past values
- C. It requires an initial value and emits the current value to new subscribers
- D. It cannot be completed

**Answer:** C

**Explanation:** BehaviorSubject holds a current value, requires an initial one, and immediately emits it to new subscribers. ReplaySubject can replay many values; Subject emits only future ones.

### 44. [Memory management] You want an Observable subscription to auto-unsubscribe when the component is destroyed, inside a field initializer. Which approach fits?

```
private destroyRef = inject(DestroyRef);
ngOnInit() {
  this.ticks$.pipe(takeUntilDestroyed(this.destroyRef)).subscribe();
}
```

- A. Use first() always
- B. Pipe through takeUntilDestroyed()
- C. Call unsubscribe in ngOnInit
- D. Use takeUntil(this.ngOnDestroy)

**Answer:** B

**Explanation:** takeUntilDestroyed() completes the stream when the owning context is destroyed. The others do not tie to destruction.

### 45. [Error handling] What must the selector function of catchError return?

- A. An Observable
- B. A Promise only
- C. void
- D. A plain value

**Answer:** A

**Explanation:** catchError returns an ObservableInput, e.g. of([]) or EMPTY, or rethrows via throwError. A plain value is not valid.

### 46. [Memory management] Which subscriptions typically need manual cleanup in a component? (Select all that apply.)

- A. http.get(url).subscribe(...)
- B. An Observable consumed with the async pipe
- C. fromEvent(document, 'click').subscribe(...)
- D. interval(1000).subscribe(...)

**Answer:** C, D

**Explanation:** interval and DOM event streams never complete. HttpClient requests complete after a response and the async pipe unsubscribes itself.

### 47. [DI] A service is listed in a component's providers array. What is the effect?

- A. It is shared with all lazy modules
- B. Each component instance gets its own service instance
- C. It is ignored
- D. It is a singleton across the app

**Answer:** B

**Explanation:** Providing at component level creates a new instance per component instance, also visible to its children. Root-level providers are shared.

### 48. [DI] Why use an InjectionToken?

```
export const API_URL = new InjectionToken<string>('API_URL');
providers: [{ provide: API_URL, useValue: '/api' }]
```

- A. To speed up bootstrapping
- B. To replace @Injectable
- C. To make services lazy
- D. To inject non-class values such as config objects or primitives

**Answer:** D

**Explanation:** Types and interfaces have no runtime identity, so a token identifies the dependency. It does not replace @Injectable for classes.

### 49. [DI] Which provider form supplies a ready-made constant object for a token?

- A. useValue
- B. useFactory with deps only
- C. useExisting
- D. useClass

**Answer:** A

**Explanation:** useValue provides the literal value. useClass instantiates a class, useExisting aliases another token, and useFactory runs a function.

### 50. [DI] What does inject(Logger, { optional: true }) return if no provider exists?

- A. A new Logger
- B. Throws NullInjectorError
- C. undefined
- D. null

**Answer:** D

**Explanation:** With optional: true, a missing provider yields null instead of an error.

### 51. [DI] Where does Angular's injector first look for a dependency requested by a component?

- A. Only the NgModule
- B. The component's own element injector, then up the element tree, then environment injectors
- C. Root environment injector
- D. The browser's global scope

**Answer:** B

**Explanation:** Angular checks the element injector hierarchy (component and directive providers, viewProviders) and then falls back to environment injectors such as root. It is not global.

### 52. [DI] Where is calling inject() valid? (Select all that apply.)

- A. The constructor
- B. Inside a setTimeout callback
- C. Inside ngOnInit
- D. A field initializer in a component

**Answer:** A, D

**Explanation:** inject() works during construction (constructor and field initializers) and in factory functions, not in later lifecycle methods or async callbacks.

### 53. [HttpClient] Why must an interceptor call req.clone({...}) to add a header?

```
export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const r = req.clone({ setHeaders: { Authorization: 'Bearer x' } });
  return next(r);
};
```

- A. clone is faster
- B. HttpRequest objects are immutable
- C. Headers cannot be set otherwise in Angular
- D. It triggers a new subscription

**Answer:** B

**Explanation:** HttpRequest is immutable, so you create a modified copy with clone and pass it to next(). The reason is immutability, not performance.

### 54. [HttpClient] How do you register a functional interceptor?

- A. provideHttpClient(withInterceptors([authInterceptor]))
- B. providers: [{ provide: INTERCEPTOR, useValue: authInterceptor }]
- C. HttpClient.use(authInterceptor)
- D. imports: [InterceptorModule]

**Answer:** A

**Explanation:** withInterceptors takes an array of functional interceptors. The other forms are not valid APIs.

### 55. [Routing] Which values may a CanActivateFn return? (Select all that apply.)

```
export const authGuard: CanActivateFn = () => {
  return inject(AuthService).loggedIn() || inject(Router).parseUrl('/login');
};
```

- A. An Observable of boolean or UrlTree
- B. A string route name
- C. UrlTree
- D. boolean

**Answer:** A, C, D

**Explanation:** Guards can return boolean, UrlTree (to redirect), or Observable/Promise of those. Strings are not accepted.

### 56. [Routing] Which route properties enable lazy loading? (Select all that apply.)

```
{ path: 'admin', loadChildren: () => import('./admin/routes').then(m => m.ADMIN_ROUTES) }
```

- A. lazy: true
- B. loadChildren
- C. loadComponent
- D. import

**Answer:** B, C

**Explanation:** loadComponent lazy loads a standalone component and loadChildren a routes array or module. lazy and import are not route properties.

### 57. [Routing] A route /user/:id navigates from /user/1 to /user/2, reusing the same component instance. How do you reliably see the new id? (Select all that apply.)

- A. Read route.snapshot.paramMap in ngOnInit only
- B. Use withComponentInputBinding and an input named id
- C. Subscribe to route.paramMap
- D. Rely on ngOnInit running again

**Answer:** B, C

**Explanation:** Observable params and bound inputs update. The snapshot read once in ngOnInit is stale and ngOnInit does not run again for a reused instance.

### 58. [Routing] What problem does withComponentInputBinding() solve?

- A. It enables SSR
- B. It binds route params, query params and data to component inputs
- C. It binds two components together
- D. It makes guards synchronous

**Answer:** B

**Explanation:** With it, route parameters and data are set directly on matching inputs, removing the need to inject ActivatedRoute.

### 59. [Routing] What is a route resolver used for?

- A. Lazy loading modules
- B. Rendering 404 pages
- C. Blocking unauthenticated users
- D. Prefetching data before the route activates

**Answer:** D

**Explanation:** Resolvers fetch data before activation, exposing it via route data. Guards handle access, and loadChildren handles lazy loading.

### 60. [Routing] Why is pathMatch: 'full' needed on { path: '', redirectTo: 'home', pathMatch: 'full' }?

- A. Without it, the empty path prefix matches every URL and causes redirect loops
- B. It enables lazy loading
- C. It makes the route case-sensitive
- D. It improves SEO

**Answer:** A

**Explanation:** An empty path is a prefix of every URL, so with the default 'prefix' strategy everything would redirect. 'full' matches only an empty URL.

### 61. [Forms] Which form control state flags exist in Angular forms? (Select all that apply.)

- A. dirty
- B. pristine
- C. touched
- D. visited

**Answer:** A, B, C

**Explanation:** touched, dirty and pristine are properties on controls. visited is not.

### 62. [Forms] How do you react to value changes of a reactive FormControl?

- A. Listen for the ngChange event
- B. Subscribe to control.valueChanges
- C. Poll control.value in ngDoCheck only
- D. Use @Output on the control

**Answer:** B

**Explanation:** valueChanges emits each time the value changes. ngChange and @Output on controls do not exist.

### 63. [Forms] What should a synchronous custom validator function return when the value is valid?

```
const noSpaces: ValidatorFn = c =>
  /\s/.test(c.value) ? { spaces: true } : null;
```

- A. undefined
- B. true
- C. null
- D. An empty string

**Answer:** C

**Explanation:** A ValidatorFn returns null for valid and a ValidationErrors object like { forbidden: true } for invalid.

### 64. [Forms] What is the difference between setValue and patchValue on a FormGroup?

- A. patchValue allows a partial object while setValue requires all controls
- B. setValue allows partial objects
- C. patchValue only works for FormArray
- D. They are identical

**Answer:** A

**Explanation:** setValue throws if any control is missing, while patchValue updates only the supplied properties.

### 65. [Forms] Which statements about reactive forms are true? (Select all that apply.)

- A. They are generally easier to unit test than template-driven forms
- B. The form model is defined in the component class
- C. Values can be read synchronously
- D. They require ngModel on every input

**Answer:** A, B, C

**Explanation:** Reactive forms make the model explicit, synchronous and testable. They use formControlName/formControl, not ngModel.

### 66. [Forms] What is the purpose of implementing ControlValueAccessor?

- A. To validate asynchronously
- B. To lazy load a form
- C. To let a custom component work with Angular forms directives like formControl or ngModel
- D. To intercept HTTP calls

**Answer:** C

**Explanation:** ControlValueAccessor defines writeValue and change/touch callbacks so custom components integrate with form controls. Validation uses Validators.

### 67. [Control flow] Which contextual variables are available inside @for? (Select all that apply.)

```
@for (u of users; track u.id; let i = $index) {
  <li>{{ i }} {{ u.name }}</li>
} @empty {
  <li>No users</li>
}
```

- A. $key
- B. $first
- C. $item
- D. $index

**Answer:** B, D

**Explanation:** @for provides $index, $first, $last, $even, $odd and $count. $key and $item do not exist.

### 68. [Control flow] In a standalone component, what is a practical difference between @if and *ngIf?

- A. @if needs no import of NgIf or CommonModule
- B. @if works only in NgModules
- C. @if is slower
- D. *ngIf supports @else but @if does not

**Answer:** A

**Explanation:** The new blocks are built into the compiler and require no imports, whereas *ngIf requires NgIf. @if fully supports @else.

### 69. [Control flow] Why is track important in @for?

- A. It lets Angular reuse DOM nodes for unchanged items when the list changes
- B. It filters null items
- C. It subscribes to the array
- D. It sorts the list

**Answer:** A

**Explanation:** A stable identity like track item.id lets Angular move and reuse nodes instead of recreating them. It does not sort or filter.

### 70. [Deferrable views] Which are valid @defer triggers? (Select all that apply.)

- A. on idle
- B. on hover
- C. on scroll
- D. on viewport

**Answer:** A, B, D

**Explanation:** on idle, on viewport, on hover, on interaction, on immediate and on timer are supported, as is when condition. There is no on scroll trigger.

### 71. [Deferrable views] Which @defer sub-block displays content while the deferred dependencies are being fetched?

- A. @fallback
- B. @error
- C. @placeholder
- D. @loading

**Answer:** D

**Explanation:** @loading shows during loading, @placeholder before the trigger, and @error on failure. @fallback is not a defer block.

### 72. [Deferrable views] A component inside @defer still loads eagerly. What is a likely cause?

- A. The route is not lazy
- B. The component lacks @Input
- C. @defer only works with NgModules
- D. It is also referenced outside the @defer block, such as in the imports usage elsewhere in the template

**Answer:** D

**Explanation:** Deferred dependencies must be standalone and not used eagerly elsewhere in the same file, otherwise they are in the main bundle.

### 73. [Standalone] What does bootstrapApplication(AppComponent, { providers: [...] }) replace?

- A. RouterModule.forRoot
- B. platformBrowserDynamic().bootstrapModule(AppModule)
- C. TestBed
- D. ng serve

**Answer:** B

**Explanation:** bootstrapApplication starts a standalone root component directly and takes app-wide providers, replacing bootstrapModule with an AppModule.

### 74. [Standalone] What can a standalone component list in its imports array? (Select all that apply.)

- A. Route definitions
- B. Other standalone components and pipes
- C. Injectable services
- D. NgModules

**Answer:** B, D

**Explanation:** imports accepts standalone components, directives, pipes and NgModules. Services use providers and routes are given to the router.

### 75. [Standalone] Which are valid provider functions in a standalone application? (Select all that apply.)

- A. provideModule()
- B. provideHttpClient()
- C. provideRouter(routes)
- D. provideComponent()

**Answer:** B, C

**Explanation:** provideRouter and provideHttpClient configure the router and HttpClient. provideModule and provideComponent do not exist.

### 76. [NgModules] What is the purpose of the forRoot/forChild convention in modules such as RouterModule?

- A. To define two components
- B. To replace declarations
- C. To make modules lazy
- D. To provide singleton services once in the root while child modules only add configuration or routes

**Answer:** D

**Explanation:** forRoot returns a ModuleWithProviders with app-wide services, while forChild registers only extra routes without re-providing services.

### 77. [NgModules] You declare the same component in two NgModules. What happens?

- A. It becomes a singleton
- B. Angular merges them
- C. The second is ignored silently
- D. Compilation error: a component can be declared in only one module

**Answer:** D

**Explanation:** Each non-standalone component belongs to exactly one NgModule. To reuse it, export it from that module or make it standalone.

### 78. [NgModules] A SharedModule declares AppButtonComponent. A FeatureModule imports SharedModule but cannot use <app-button>. What is missing?

- A. AppButtonComponent needs providedIn root
- B. FeatureModule must provide it
- C. SharedModule must export AppButtonComponent
- D. bootstrap must include it

**Answer:** C

**Explanation:** Only exported declarations are usable by importing modules. providers and bootstrap are unrelated to template visibility.

### 79. [Pipes] When does a pure pipe re-run its transform?

- A. Only when its input value or parameters change by reference or primitive value
- B. On every change detection cycle
- C. Only on route change
- D. Only once

**Answer:** A

**Explanation:** Pure pipes are re-executed only when their input changes (primitive value or new reference), so mutating an array in place will not retrigger them.

### 80. [Pipes] What is the main drawback of setting pure: false on a custom pipe?

- A. It cannot be used with the async pipe
- B. It is not allowed with standalone pipes
- C. It runs on every change detection cycle, which may hurt performance
- D. It cannot take arguments

**Answer:** C

**Explanation:** Impure pipes run every cycle, so expensive transforms can slow the app. They can take arguments and be standalone.

### 81. [Pipes] A template uses (user$ | async)?.name and (user$ | async)?.email. What is the problem?

```
@if (user$ | async; as user) {
  <p>{{ user.name }} {{ user.email }}</p>
}
```

- A. Each async pipe creates its own subscription, possibly duplicating requests
- B. The optional chaining operator is invalid
- C. It leaks memory in all cases
- D. async cannot be used twice

**Answer:** A

**Explanation:** Each use subscribes separately, which can fire multiple HTTP calls for cold Observables. Use @if (user$ | async; as user) once instead.

### 82. [Directives] Which decorators are used in an attribute directive to listen for host events and bind host properties? (Select all that apply.)

- A. @HostListener
- B. @ViewChild
- C. @Output
- D. @HostBinding

**Answer:** A, D

**Explanation:** @HostListener subscribes to host events and @HostBinding sets host properties or attributes. @ViewChild queries the template and @Output emits events.

### 83. [Directives] What does <ng-content></ng-content> do inside a component template?

- A. Projects content supplied between the component's tags
- B. Lazy loads the content
- C. Renders content in a different route
- D. Creates a new component

**Answer:** A

**Explanation:** ng-content marks where parent-supplied child content is rendered. It does not create components or load anything lazily.

### 84. [Lifecycle] A @ViewChild({ static: false }) query (default) is first reliably available in which hook?

- A. constructor
- B. ngOnInit
- C. ngOnChanges
- D. ngAfterViewInit

**Answer:** D

**Explanation:** Dynamic view queries are resolved by ngAfterViewInit. At constructor time and ngOnInit they may be undefined (unless static: true).

### 85. [Lifecycle] A parent changes a property of an object bound to a child's @Input without replacing the reference. Will the child's ngOnChanges fire?

- A. No, ngOnChanges fires only when the input binding value or reference changes
- B. Yes, always
- C. Only in production mode
- D. Only if OnPush is used

**Answer:** A

**Explanation:** ngOnChanges compares binding values using identity, so in-place mutation is not detected. Use a new reference or ngDoCheck.

### 86. [Testing] Which methods of HttpTestingController are commonly used in tests? (Select all that apply.)

- A. expectOne
- B. flush on the returned TestRequest
- C. verify
- D. mockResponse

**Answer:** A, B, C

**Explanation:** expectOne finds a pending request, flush supplies a response, and verify asserts none are left. mockResponse does not exist.

### 87. [Testing] Why call fixture.detectChanges() in a component test?

- A. To compile the module
- B. To run change detection so bindings render and ngOnInit runs for the first time
- C. To restart the test runner
- D. To clear the DOM

**Answer:** B

**Explanation:** The first detectChanges triggers ngOnInit and updates the view. Without it the template shows initial, unrendered state.

### 88. [Testing] How do you replace a real service with a fake in a TestBed?

- A. declarations: [fakeService]
- B. providers: [{ provide: DataService, useValue: fakeService }]
- C. Call new DataService() in the component
- D. imports: [fakeService]

**Answer:** B

**Explanation:** Providing the same token with useValue (or useClass) swaps the implementation. imports and declarations are for modules and view classes.

### 89. [Signals] How do you declare a required signal input in a component?

- A. name = input.required<string>();
- B. name = signal.required<string>();
- C. @Input({ signal: true }) name!: string;
- D. name = required(input<string>());

**Answer:** A

**Explanation:** input.required<T>() declares a required signal input read as name(). The other forms are not valid APIs.

### 90. [Signals] What does toSignal() from @angular/core/rxjs-interop do?

```
users = toSignal(this.http.get<User[]>('/api/users'), { initialValue: [] });
```

- A. Converts a signal into a Promise
- B. Converts an Observable into a signal that holds its latest value
- C. Creates a Subject
- D. Subscribes without cleanup

**Answer:** B

**Explanation:** toSignal subscribes to the Observable and exposes the latest value as a read-only signal, unsubscribing automatically when its context is destroyed.


## Hard

### 91. [RxJS operators] Given the code, when does the subscriber receive values?

```
const source$ = merge(of('A'), of('B').pipe(delay(50)));
source$
  .pipe(switchMap(v => timer(100).pipe(map(() => v))))
  .subscribe(console.log);
```

- A. 'A' at about 100 ms and 'B' at about 150 ms
- B. 'A' and 'B' both at about 150 ms
- C. Only 'B', about 150 ms after subscribing
- D. Only 'A', at about 100 ms

**Answer:** C

**Explanation:** At t=50ms 'B' arrives while the inner timer for 'A' (due at 100ms) is still pending, so switchMap unsubscribes from it and 'A' is never emitted. The new inner timer for 'B' fires at 50+100=150ms. mergeMap or concatMap would have produced both values.

### 92. [RxJS operators] What is logged by this code?

```
of(1, 2, 3)
  .pipe(mergeMap(n => timer((4 - n) * 100).pipe(map(() => n))))
  .subscribe(console.log);
```

- A. 1, 2, 3
- B. 3, 2, 1
- C. Only 3
- D. Only 1

**Answer:** B

**Explanation:** mergeMap subscribes to all inner observables concurrently, and emits as each inner emits. The timers are 300ms, 200ms and 100ms for 1, 2 and 3, so the output is 3, 2, 1. concatMap would queue them and log 1, 2, 3.

### 93. [RxJS operators] Which statements about concatMap are true? (Select all that apply.)

- A. It unsubscribes from the active inner observable when a new source value arrives.
- B. It queues source values and subscribes to each inner observable only after the previous one completes.
- C. It drops source values that arrive while an inner observable is still active.
- D. Output order follows source order even if a later inner observable would finish faster.
- E. It behaves like mergeMap with a concurrency limit of 1.

**Answer:** B, D, E

**Explanation:** concatMap buffers outer values and runs inner observables strictly one at a time, so ordering is preserved and it equals mergeMap(fn, 1). Cancelling the active inner is switchMap's behavior, and dropping values while busy is exhaustMap's.

### 94. [RxJS operators] A Save button's click$ stream must ignore further clicks while a save request is still in flight, without cancelling that request. Which operator fits best?

- A. switchMap
- B. concatMap
- C. exhaustMap
- D. mergeMap

**Answer:** C

**Explanation:** exhaustMap ignores source values while its current inner observable is active, which prevents double submits. switchMap would cancel the first request, concatMap would queue and send duplicates afterwards, and mergeMap would send them all concurrently.

### 95. [RxJS operators] Which statements about source$.pipe(withLatestFrom(other$)) are true? (Select all that apply.)

- A. It emits only when source$ emits, paired with the latest value of other$.
- B. It completes as soon as other$ completes.
- C. It emits whenever either source$ or other$ emits, like combineLatest.
- D. Source emissions that occur before other$ has emitted for the first time are dropped.
- E. It subscribes to other$ only after source$ emits its first value.

**Answer:** A, D

**Explanation:** withLatestFrom is driven by the source: it subscribes to other$ at subscription time and emits only on source emissions once other$ has a value. Earlier source values are silently lost. Completion of other$ does not complete the result, and it is not combineLatest.

### 96. [RxJS operators] Which describes forkJoin([a$, b$])?

- A. It emits every time either source emits, using the latest values.
- B. It emits pairs of values by index, waiting for both at each index.
- C. It emits the first value of each source as soon as both have emitted.
- D. It emits one array of each source's last value after all sources complete; if any completes without emitting, it completes without emitting.

**Answer:** D

**Explanation:** forkJoin waits for every source to complete and then emits the last value from each exactly once. The first option is combineLatest, the second is zip, and the third is not an RxJS operator behavior. A source that never completes keeps forkJoin from emitting.

### 97. [RxJS operators] Which statements about debounceTime(300), throttleTime(300) and auditTime(300) are true? (Select all that apply.)

- A. debounceTime emits the most recent value only after 300 ms pass with no new source values.
- B. debounceTime emits the first value immediately and then silences the stream for 300 ms.
- C. auditTime emits the first value of each window immediately when it arrives.
- D. throttleTime by default emits the first value of a window and ignores the others in that window.

**Answer:** A, D

**Explanation:** debounce is trailing and resets on each value; throttleTime defaults to leading edge. auditTime is trailing: it emits the latest value when the window ends, not the first immediately. The third option describes a leading throttle, not debounce.

### 98. [RxJS operators] What is the problem with this typeahead pipeline?

```
this.search$.pipe(
  switchMap(q => this.http.get<Item[]>(`/api?q=${q}`)),
  catchError(() => of([]))
).subscribe(items => this.items = items);
```

- A. After the first HTTP error the outer stream is terminated; catchError should be placed inside the switchMap's inner pipe.
- B. catchError never runs because HttpClient errors are not delivered as observable errors.
- C. switchMap swallows errors, so catchError is unreachable.
- D. of([]) emits asynchronously, which reorders results.

**Answer:** A

**Explanation:** An error propagates to the outer pipeline, catchError then replaces it with of([]) which completes, so no further searches are processed. Putting catchError on the inner request keeps the outer search$ alive. HttpClient does emit errors via the error channel and switchMap does not swallow them.

### 99. [RxJS multicasting] In RxJS 7, what does source$.pipe(shareReplay(1)) do when all subscribers unsubscribe before the source completes?

- A. The source subscription is torn down immediately.
- B. It resets and re-subscribes to the source when a new subscriber arrives.
- C. It throws an unsubscription error on the next subscribe.
- D. The source stays subscribed (refCount is false by default) and the latest value is replayed to future subscribers.

**Answer:** D

**Explanation:** shareReplay(1) with default config keeps the underlying subscription alive after subscribers leave, which can leak long-lived sources. Use shareReplay({ bufferSize: 1, refCount: true }) to tear down when subscribers reach zero. It does not throw or reset by default.

### 100. [RxJS multicasting] What is logged?

```
const s = new Subject<number>();
s.next(1);
s.subscribe(v => console.log('A', v));
s.next(2);
s.subscribe(v => console.log('B', v));
s.next(3);
```

- A. A 1, A 2, A 3, B 3
- B. A 2, A 3, B 2, B 3
- C. A 2, A 3, B 3
- D. A 1, A 2, B 2, A 3, B 3

**Answer:** C

**Explanation:** A Subject is hot and has no replay: A misses 1 because it subscribed after next(1), and B misses 1 and 2. A receives 2 and 3, B receives only 3. A ReplaySubject or BehaviorSubject would behave differently.

### 101. [RxJS multicasting] Where should takeUntil(destroy$) be placed to avoid leaking inner subscriptions in a pipe that uses switchMap?

- A. Immediately after the source, before switchMap.
- B. Anywhere; operator order never matters for takeUntil.
- C. Only inside the inner observable.
- D. As the last operator, after switchMap/mergeMap.

**Answer:** D

**Explanation:** If takeUntil precedes switchMap, completing the outer does not unsubscribe a still-active inner observable, which can keep emitting. Placing it last unsubscribes from the whole upstream chain including inners. Order does matter.

### 102. [RxJS multicasting] A template uses `data$ | async` twice for `data$ = this.http.get<Item[]>('/api/items')`. Which statements are true? (Select all that apply.)

- A. Adding shareReplay({ bufferSize: 1, refCount: true }) to data$ makes both pipes share one request.
- B. Setting the component to OnPush deduplicates the request.
- C. Two HTTP requests are sent because the observable is cold and each async pipe subscribes separately.
- D. Using `@if (data$ | async; as data)` once and referencing `data` reduces it to one subscription.

**Answer:** A, C, D

**Explanation:** HttpClient observables are cold, so each subscription triggers a request. Multicasting with shareReplay or subscribing once with an alias fixes it. OnPush only affects when views are checked, not subscriptions.

### 103. [RxJS multicasting] Why does this distinctUntilChanged() not suppress duplicate emissions when the form values are identical?

```
this.form.valueChanges.pipe(
  distinctUntilChanged()
).subscribe(v => this.save(v));
```

- A. Each valueChanges emission is a new object, and the default comparison uses reference equality; supply a comparator.
- B. distinctUntilChanged only works on primitive streams created with of().
- C. valueChanges is a Subject so distinct operators are ignored.
- D. distinctUntilChanged needs a debounceTime before it to work.

**Answer:** A

**Explanation:** The default comparator is ===, so two different objects with the same content are considered distinct. Pass a comparator such as (a, b) => JSON.stringify(a) === JSON.stringify(b) or use a field-level comparison. The operator works on any type; it is just reference-based by default.

### 104. [RxJS interop] What does this log?

```
count = signal(0);
constructor() {
  toObservable(this.count).subscribe(console.log);
  this.count.set(1);
  this.count.set(2);
  this.count.set(3);
}
```

- A. 0, 1, 2, 3
- B. 3
- C. 0 and then 3
- D. 1, 2, 3

**Answer:** B

**Explanation:** toObservable emits via an effect that runs during change detection, so the three synchronous sets are coalesced and the subscriber sees the latest value only. It does not emit the intermediate values or the stale initial one.

### 105. [RxJS interop] What happens when takeUntilDestroyed() is called without arguments inside ngOnInit?

```
ngOnInit() {
  this.data$.pipe(takeUntilDestroyed()).subscribe();
}
```

- A. It works because ngOnInit runs in the component's injection context.
- B. It unsubscribes at the next change detection.
- C. It throws because it is not in an injection context; pass a DestroyRef instead.
- D. It silently does nothing and the subscription leaks.

**Answer:** C

**Explanation:** takeUntilDestroyed() calls inject(DestroyRef) when no argument is given, which fails outside an injection context such as ngOnInit. Capture destroyRef = inject(DestroyRef) in a field and pass it: takeUntilDestroyed(this.destroyRef). It does not silently leak; it throws.

### 106. [RxJS interop] Which statements about toSignal() are true? (Select all that apply.)

- A. Without initialValue, the resulting signal's type includes undefined until the first emission.
- B. It subscribes lazily on the first read of the signal.
- C. It subscribes immediately and unsubscribes automatically when the calling injection context is destroyed.
- D. It can be called anywhere, such as inside a click handler, with no injector.
- E. requireSync: true is valid for sources that emit synchronously on subscribe, such as BehaviorSubject.

**Answer:** A, C, E

**Explanation:** toSignal subscribes eagerly, ties cleanup to the injection context, and adds undefined to the type unless initialValue or requireSync is set. It must be called in an injection context (or given an injector), and it is not lazy.

### 107. [Signals] Which statements about this computed are true? (Select all that apply.)

```
flag = signal(true);
a = signal(1);
b = signal(2);
value = computed(() => {
  console.log('run');
  return this.flag() ? this.a() : this.b();
});
```

- A. While flag() is true, changing b() does not invalidate value.
- B. After a.set(5), the callback re-executes immediately even if nobody reads value().
- C. It is lazy: the callback does not run until value() is first read.
- D. Reading value() twice with no dependency changes runs the callback once.

**Answer:** A, C, D

**Explanation:** computed runs only on demand, caches its result, and tracks just the signals read in the last execution; b is not read when flag is true. A change to a dependency only marks it dirty, and recomputation waits for the next read.

### 108. [Signals] What happens with the effect after this code runs?

```
user = signal({ name: 'A' });
constructor() {
  effect(() => console.log(this.user().name));
}
rename() {
  const u = this.user();
  u.name = 'B';
  this.user.set(u);
}
```

- A. The effect does not re-run because the same object reference is set, so signal equality (Object.is) sees no change.
- B. The effect re-runs and logs 'B'.
- C. The effect re-runs only on the next change detection tick.
- D. set() throws because mutating signal values is not allowed.

**Answer:** A

**Explanation:** The object was mutated in place and set with the same reference, so the signal considers the value unchanged and notifies no consumers. Use update(u => ({...u, name: 'B'})) to create a new reference. Signals do not throw on mutation but they do not detect it.

### 109. [Signals] Which signal change causes this effect to re-run?

```
effect(() => {
  const q = this.query();
  untracked(() => this.log.record(q, this.user()));
});
```

- A. Only changes to query()
- B. Changes to either query() or user()
- C. Only changes to user()
- D. Neither; effects never re-run

**Answer:** A

**Explanation:** user() is read inside untracked(), so it is not recorded as a dependency; only query() is tracked. Effects do re-run when tracked dependencies change.

### 110. [Signals] What happens when this component is created?

```
name = input.required<string>();
constructor() {
  console.log(this.name());
}
```

- A. It logs undefined.
- B. It throws NG0950 because the required input has no value yet during construction.
- C. It logs an empty string.
- D. It logs the parent's bound value.

**Answer:** B

**Explanation:** A required signal input throws if read before the parent binding has been set, and the constructor runs before inputs are assigned. Read it in a computed, effect or later lifecycle hook instead.

### 111. [Signals] Which statements about model() are true? (Select all that apply.)

- A. The child can call .set() on it and a parent bound with [(value)] receives the update.
- B. It cannot be declared as required.
- C. It declares an input and a matching output named <name>Change.
- D. [(value)] on the parent side can bind to a writable signal.
- E. It is read-only like input().

**Answer:** A, C, D

**Explanation:** model() combines an input with a change output and is writable by the child. Parent two-way binding works with writable signals or property expressions. It is not read-only, and model.required() exists.

### 112. [Signals] What does selected() return at the end?

```
options = signal(['a', 'b']);
selected = linkedSignal(() => this.options()[0]);

this.selected.set('b');
this.options.set(['x', 'y']);
console.log(this.selected());
```

- A. 'b'
- B. 'x'
- C. 'y'
- D. undefined

**Answer:** B

**Explanation:** linkedSignal is writable, but when its source (options) changes it recomputes, discarding the manual 'b'. The recomputation yields options()[0], which is 'x'.

### 113. [Signals] An OnPush component reads count() in its template. A service calls count.set() inside a setTimeout. What happens?

- A. The view is stale until a parent input changes.
- B. The view is stale until markForCheck() is called.
- C. An ExpressionChangedAfterItHasBeenChecked error is thrown.
- D. The view updates because signal reads in the template mark the view for refresh when the value changes.

**Answer:** D

**Explanation:** A template that reads a signal becomes a reactive consumer; when the signal changes, Angular marks the view for refresh even under OnPush. No manual markForCheck is needed, and no NG0100 error occurs since the change happens outside a CD pass.

### 114. [Signals] What does reading the view query signal in the constructor log?

```
chart = viewChild<ElementRef>('chart');
constructor() {
  console.log(this.chart());
}
```

- A. The ElementRef of the canvas.
- B. null
- C. undefined, because the query result is not available during construction; use an effect or afterNextRender to read it.
- D. It throws NG0950.

**Answer:** C

**Explanation:** Signal-based queries return undefined until the view is created; the constructor runs before that. Read them in effect(), afterNextRender() or later hooks. They do not throw for an optional viewChild and do not return null.

### 115. [Signals] When is the cleanup function registered with onCleanup invoked?

```
effect(onCleanup => {
  const id = setInterval(() => this.tick(), this.ms());
  onCleanup(() => clearInterval(id));
});
```

- A. Only when the component is destroyed.
- B. Before the effect re-runs and when the effect is destroyed.
- C. After every change detection pass.
- D. Only if the effect throws.

**Answer:** B

**Explanation:** Cleanup runs before each subsequent execution of the effect and when it is destroyed, which suits timers and subscriptions that depend on the signal value. It is not tied to CD passes or errors.

### 116. [Signals] How many times, and with what value, does this effect log?

```
count = signal(0);
constructor() {
  effect(() => console.log('count', this.count()));
  this.count.set(1);
  this.count.set(2);
}
```

- A. Three times: 0, 1, 2
- B. Twice: 0, 2
- C. Once: 'count 2'
- D. Never, since effects only run after user events

**Answer:** C

**Explanation:** A component effect is scheduled to run during change detection, so by its first execution count is already 2, and intermediate values are never observed. Effects are asynchronous and batched, unlike RxJS subscriptions.

### 117. [Change detection] Which of these cause an OnPush component to be checked? (Select all that apply.)

- A. A setTimeout inside the component changes a plain field.
- B. The parent binds a new object reference to one of its @Input()s.
- C. A DOM event handler declared in its own template fires.
- D. An observable bound with the async pipe in its template emits.
- E. The parent mutates a property of the same object passed to the @Input().

**Answer:** B, C, D

**Explanation:** OnPush views are checked on input reference changes, template event handlers, async pipe emissions (which call markForCheck) and signals. Mutating an input object in place or changing a plain field from a timer does not mark the view dirty.

### 118. [Change detection] Why does the child list not update after add() is called?

```
// child
@Component({
  selector: 'app-list',
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `@for (i of items; track i) { <li>{{ i }}</li> }`
})
class ListComponent { @Input() items: string[] = []; }

// parent
add() { this.names.push('x'); }
```

- A. push() mutates the array in place, so the OnPush child's input reference is unchanged; use a new array.
- B. OnPush components cannot render arrays.
- C. The @for block requires trackBy to render new items.
- D. Parent change detection is disabled once a child is OnPush.

**Answer:** A

**Explanation:** The child only re-checks when the bound reference changes; push() keeps the same array. Assigning this.names = [...this.names, 'x'] works. OnPush does not block rendering arrays or the parent's own CD.

### 119. [Change detection] What happens in development mode when this component is first rendered?

```
@Component({ selector: 'app-x', template: `{{ title }}` })
class X implements AfterViewInit {
  title = 'Initial';
  ngAfterViewInit() { this.title = 'Loaded'; }
}
```

- A. It throws ExpressionChangedAfterItHasBeenChecked (NG0100) because a binding changed after it was checked.
- B. No error; the view shows 'Loaded' immediately.
- C. The error only occurs in production builds.
- D. It causes an infinite change detection loop.

**Answer:** A

**Explanation:** ngAfterViewInit runs after the view's bindings were evaluated, so the dev-mode check pass sees title differing from the previously rendered value and throws NG0100. It does not occur only in production and does not loop.

### 120. [Change detection] A field bound in the template is set from a @ViewChild value in ngAfterViewInit, causing NG0100. Which fixes work? (Select all that apply.)

- A. Move the assignment to ngAfterViewChecked.
- B. Call markForCheck() after assigning.
- C. Defer the assignment with Promise.resolve().then(...) so a later CD pass renders it.
- D. Inject ChangeDetectorRef and call detectChanges() right after assigning.

**Answer:** C, D

**Explanation:** detectChanges() re-evaluates the view immediately, and a microtask schedules a subsequent CD pass, so the verification pass does not see a stale value. markForCheck only schedules future checks and the dev-mode check still fails, while ngAfterViewChecked is subject to the same problem.

### 121. [Change detection] Which statements about markForCheck() and detectChanges() are true? (Select all that apply.)

- A. detectChanges() runs change detection synchronously on the view and its children.
- B. markForCheck() runs change detection synchronously on the component.
- C. detectChanges() marks ancestors up to the root as dirty.
- D. markForCheck() marks the view and its ancestors as dirty so they are checked in the next CD cycle; it does not run CD itself.

**Answer:** A, D

**Explanation:** markForCheck is a flag-setting operation that relies on a later tick, which is why it is used with OnPush. detectChanges performs an immediate check of that subtree and does not touch ancestors' dirty state.

### 122. [Change detection] Why would you register a mousemove listener inside ngZone.runOutsideAngular()?

- A. It makes the handler run faster than native listeners.
- B. So the handler is not patched and never runs.
- C. It avoids triggering an application-wide change detection per event; re-enter the zone or notify Angular when the UI actually needs updating.
- D. It lets the handler update templates without any change detection.

**Answer:** C

**Explanation:** Events registered within the Angular zone trigger CD after each invocation; outside it, they don't. You must call ngZone.run, markForCheck, or set a signal when something visible needs to change. It does not make the handler itself faster and the handler still runs.

### 123. [Zone.js] In a zone.js-based app, which of these cause Angular to run change detection after they complete? (Select all that apply.)

- A. An XHR or fetch response handled in the Angular zone
- B. A field changed by code running in runOutsideAngular
- C. A setTimeout callback running in the Angular zone
- D. Reading a signal in a plain TypeScript function
- E. A Promise.then callback running in the Angular zone

**Answer:** A, C, E

**Explanation:** NgZone emits onMicrotaskEmpty after patched async tasks run inside the zone, which drives ApplicationRef.tick. Code outside the zone does not notify Angular, and merely reading a signal triggers nothing.

### 124. [Zoneless] In a zoneless app (provideZonelessChangeDetection), which of these schedule change detection? (Select all that apply.)

- A. A signal read in a template changes.
- B. A Promise resolution mutates a plain field.
- C. markForCheck() is called.
- D. A setTimeout callback mutates a plain field.
- E. A template event listener fires.

**Answer:** A, C, E

**Explanation:** Zoneless scheduling reacts to signals, markForCheck, async pipe, and template listener events. Mutating plain fields in timers or promises is not detected, so those would require signals or markForCheck.

### 125. [Change detection] The parent runs change detection but passes no new inputs to an OnPush child. What is true for the child?

- A. Neither its hooks nor its template are touched.
- B. Its template is re-checked but ngDoCheck is skipped.
- C. ngDoCheck is still called, but its template is not re-checked unless marked dirty.
- D. Its template is checked only in production mode.

**Answer:** C

**Explanation:** ngDoCheck runs as part of the parent's check of the child directive, regardless of OnPush; the child's own view is skipped unless dirty. That is why ngDoCheck can be used to call markForCheck manually.

### 126. [Change detection] How often is getTotal() evaluated in this default (non-OnPush) component template?

```
<p>{{ getTotal() }}</p>
```

- A. Only once when the view is created.
- B. Only when its dependencies change.
- C. Only on events from the template.
- D. On every change detection cycle that checks this view, regardless of whether inputs changed.

**Answer:** D

**Explanation:** Template expressions with method calls are re-evaluated on every check of that view. Use a computed signal, a pure pipe or precomputed fields to avoid repeated work; Angular does not track what the method depends on.

### 127. [Pipes] What happens in the template after toggleFirst() runs?

```
@Pipe({ name: 'active' })
class ActivePipe {
  transform(users: User[]) { return users.filter(u => u.active); }
}
// template: @for (u of users | active; track u.id) { ... }
toggleFirst() { this.users[0].active = false; }
```

- A. The list updates because pipes always re-run.
- B. Pure pipes are re-run only when the input reference changes, so the mutation is not reflected.
- C. Angular throws an error for mutating bound arrays.
- D. The pipe re-runs only if it is marked impure through OnPush.

**Answer:** B

**Explanation:** A pure pipe is re-executed only when its input value (by reference for objects) or arguments change; mutating an object inside the array doesn't qualify. Replace the array immutably or use an impure pipe (with performance cost).

### 128. [DI] CounterService is providedIn: 'root', and a component also declares providers: [CounterService]. Which instance does that component (and its children) receive?

- A. The root singleton.
- B. A new instance created for that component's element injector, shared with its children but not with other component instances.
- C. A new instance shared by all instances of the component.
- D. An error for duplicate providers.

**Answer:** B

**Explanation:** Component-level providers register on the element injector, so each component instance gets its own service, visible to its view children and content. The root provider is shadowed rather than conflicting.

### 129. [DI] In what order does Angular resolve a dependency requested by a component?

- A. Root environment injector first, then element injectors.
- B. Platform injector, then module injector, then component.
- C. The element injector hierarchy (self and ancestors) first, then the environment injector chain, then the platform.
- D. Only the nearest component's providers are considered.

**Answer:** C

**Explanation:** Resolution walks up the element injector tree and then continues to the environment injector hierarchy (route/lazy, root) and finally the platform, ending at NullInjector. Starting from root would defeat component-level overrides.

### 130. [DI] Which statements about injection flags and options are true? (Select all that apply.)

```
constructor(@Optional() @SkipSelf() parent: ParentService | null) {}
// or
parent = inject(ParentService, { optional: true, skipSelf: true });
```

- A. self restricts lookup to the current node's own injector.
- B. With optional, a missing dependency yields null instead of throwing NullInjectorError.
- C. skipSelf starts resolution at the parent injector instead of the current one.
- D. host searches all the way up to the root injector.

**Answer:** A, B, C

**Explanation:** skipSelf, optional and self behave as described and combine, as in inject(Parent, { optional: true, skipSelf: true }). host limits the search to the host element boundary, it does not extend to the root.

### 131. [DI] Which statements about multi providers are true? (Select all that apply.)

- A. A later non-multi provider silently overrides earlier multi providers.
- B. Injecting a multi token returns an array of all provided values.
- C. Mixing multi and non-multi providers for the same token is an error.
- D. Values are collected in the order they were registered.

**Answer:** B, C, D

**Explanation:** multi: true collects values into an array in provision order. Mixing with non-multi providers throws an error rather than overriding silently.

### 132. [DI] What is the difference in this setup between inject(Logger) and inject(LoggerService)?

```
providers: [
  LoggerService,
  { provide: Logger, useClass: LoggerService }
]
```

- A. They are the same instance.
- B. inject(Logger) throws since Logger is abstract.
- C. inject(LoggerService) is undefined.
- D. They are two separate instances because useClass creates a new instance; use useExisting to alias.

**Answer:** D

**Explanation:** useClass instantiates its own object for the Logger token, separate from the LoggerService provider. useExisting aliases the token to the existing provider so a single instance is shared.

### 133. [DI] Where is inject() allowed? (Select all that apply.)

- A. Inside a setTimeout callback created in the constructor
- B. In a constructor body
- C. Synchronously inside a functional CanActivateFn
- D. Inside ngOnInit
- E. In a field initializer of a component or service

**Answer:** B, C, E

**Explanation:** Injection contexts exist during construction, field initialization, factory functions and framework-invoked functional guards. Lifecycle hooks and later async callbacks are not injection contexts unless wrapped with runInInjectionContext.

### 134. [DI] A service is listed in providers of a lazy-loaded NgModule (classic loadChildren). What is the effect?

- A. It becomes a root singleton.
- B. The lazy module gets its own child environment injector with its own instance of the service, separate from any root provider.
- C. It is available only to the lazy module's components, never services.
- D. Angular throws a duplicate provider error.

**Answer:** B

**Explanation:** Providers in a lazy-loaded NgModule are registered on a child environment injector, so code in that subtree sees its own instance, shadowing any root-level provider. This is a common source of 'two instances' bugs.

### 135. [DI] How do viewProviders differ from providers in a component?

- A. viewProviders are not visible to content projected into the component via ng-content.
- B. viewProviders are visible only to the component class itself.
- C. viewProviders are tree-shaken.
- D. viewProviders are visible to the parent component.

**Answer:** A

**Explanation:** viewProviders are visible to the component's view children only; projected content queries the injector tree of its declaring context and cannot see them. providers are visible to both.

### 136. [Routing] What happens when a user who is not logged in navigates to a route protected by this guard?

```
export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  const router = inject(Router);
  return auth.isLoggedIn() ? true : router.createUrlTree(['/login']);
};
```

- A. The navigation is cancelled and the router redirects to /login.
- B. The navigation is blocked and the user stays on the current page silently.
- C. An error is thrown because guards cannot return UrlTree.
- D. The route activates and the login page shows as an overlay.

**Answer:** A

**Explanation:** Returning a UrlTree cancels the current navigation and starts a new one to the tree's URL, which is cleaner than calling router.navigate inside the guard. Returning false would block silently.

### 137. [Routing] Which statements about route resolvers are true? (Select all that apply.)

- A. If a resolver's observable completes without emitting, the navigation is cancelled.
- B. Navigation waits for resolvers to produce a value before activating the route.
- C. Resolvers run after the target component's constructor.
- D. Resolved data can be read from ActivatedRoute.data or bound to inputs with withComponentInputBinding().

**Answer:** A, B, D

**Explanation:** The router resolves data before activation and exposes it via data. An empty observable results in cancelled navigation. Since resolution precedes activation, the component is not constructed first.

### 138. [Routing] How does canMatch differ from canActivate?

- A. canMatch runs after the component is created.
- B. canMatch can only return booleans.
- C. canMatch is evaluated during route matching; if it returns false the route is skipped, other matching routes are considered, and a lazy bundle is not loaded.
- D. They are identical aside from naming.

**Answer:** C

**Explanation:** canMatch participates in matching, so a false result lets the router try the next route with the same path and avoids downloading lazy code. canActivate runs after a route has matched and blocks the navigation instead.

### 139. [Routing] Navigating from /user/1 to /user/2 on the same route config with the same component. What happens?

- A. The component is reused; ngOnInit does not run again, so read params through paramMap observable or input binding.
- B. The component is destroyed and recreated.
- C. ngOnInit runs again but the constructor does not.
- D. Navigation is ignored.

**Answer:** A

**Explanation:** The default RouteReuseStrategy reuses the component instance if the route config is the same, updating ActivatedRoute observables. Snapshot reads in ngOnInit then go stale. Subscribe to paramMap or use component input binding.

### 140. [Routing] Which statements about lazy loading with standalone routes are true? (Select all that apply.)

- A. loadChildren can point to a file exporting a Routes array.
- B. A static import of the same component elsewhere in eager code can pull it into the main bundle, defeating the lazy split.
- C. loadComponent: () => import('./a').then(m => m.A) lazily loads a standalone component.
- D. Lazy loading requires NgModules.

**Answer:** A, B, C

**Explanation:** Dynamic import() is the split point for both loadComponent and loadChildren. If the class is also statically imported in eagerly loaded code, it ends up in the main chunk. NgModules are not required.

### 141. [Routing] A route is declared with providers: [AdminService] and children. Where does AdminService live?

- A. On the root injector, shared app-wide.
- B. In a route environment injector shared by that route and its children, separate from root.
- C. On the injector of each routed component individually.
- D. Providers are not allowed on routes.

**Answer:** B

**Explanation:** Route-level providers create an environment injector for that route and its descendants, so the service is created lazily when the route is activated and is shared within the subtree.

### 142. [Reactive forms] Given this group, which statements are true? (Select all that apply.)

```
form = this.fb.group({
  a: ['x', Validators.required],
  b: [{ value: 'y', disabled: true }, Validators.required]
});
```

- A. form.valid ignores b's validators.
- B. form.value includes b.
- C. form.value omits b.
- D. form.getRawValue() includes b.

**Answer:** A, C, D

**Explanation:** Disabled controls are excluded from the parent's value and from validity calculations, but getRawValue() returns all controls. Thus form.value omits b.

### 143. [Reactive forms] Which statements about setValue and patchValue on a FormGroup are true? (Select all that apply.)

- A. patchValue accepts partial objects and ignores unknown keys.
- B. patchValue throws when a key is missing.
- C. setValue requires an object matching the group's structure and throws on missing controls.
- D. setValue silently ignores unknown keys.

**Answer:** A, C

**Explanation:** setValue is strict about structure and throws for missing or unknown controls, while patchValue is lenient and ignores keys without matching controls.

### 144. [Reactive forms] What happens when a control has both a sync validator and an async validator, and the sync validator fails?

- A. Both run in parallel.
- B. The async validator is invoked first.
- C. Only the async validator result is reported.
- D. The async validator is not invoked; status is INVALID from the sync errors.

**Answer:** D

**Explanation:** Angular runs async validators only when sync validators produce no errors; status then becomes PENDING while it runs. This avoids unnecessary calls such as server requests for obviously invalid input.

### 145. [Reactive forms] What does { updateOn: 'blur' } do on a FormControl?

```
name = new FormControl('', { updateOn: 'blur' });
```

- A. It only delays validation messages.
- B. It makes the control disabled until blur.
- C. It runs async validators on blur only.
- D. The control's value, validity and valueChanges update on blur instead of on each input event.

**Answer:** D

**Explanation:** updateOn controls when the control's value updates and validation runs; with 'blur' these occur when the element loses focus. It is not limited to messages or async validators.

### 146. [Reactive forms] What does form.reset() do to this control, and what is its type?

```
const c = new FormControl('a');
c.reset();
```

- A. Resets to 'a' and the type is string.
- B. Resets to '' and the type is string.
- C. Throws because no reset value was supplied.
- D. Sets it to null and the type is string | null.

**Answer:** D

**Explanation:** A typed FormControl('a') resets to null and is typed string | null. new FormControl('a', { nonNullable: true }) resets to its initial value and is typed string.

### 147. [Reactive forms] A cross-field validator is attached to the FormGroup. Where can the mismatch error be read?

```
form = new FormGroup(
  { pw: new FormControl(''), confirm: new FormControl('') },
  { validators: matchValidator }
);
```

- A. On the group via form.errors / form.hasError('mismatch'), not on the child controls.
- B. On form.get('confirm')?.errors.
- C. On every control in the group.
- D. Nowhere; group validators cannot produce errors.

**Answer:** A

**Explanation:** The validator runs against the group so errors are on the group. To show them on a child you must set errors there manually or check the group's error in the template.

### 148. [Reactive forms] Which are true when building a custom ControlValueAccessor? (Select all that apply.)

- A. setDisabledState is optional.
- B. You implement writeValue, registerOnChange and registerOnTouched.
- C. Calling the registered onChange is unnecessary since Angular watches inner DOM events.
- D. You provide NG_VALUE_ACCESSOR with multi: true, usually via useExisting and forwardRef.
- E. The class must extend FormControl.

**Answer:** A, B, D

**Explanation:** The three core methods and the NG_VALUE_ACCESSOR provider are required, while setDisabledState is optional. You must call onChange yourself to push values to the form model, and the class does not extend FormControl.

### 149. [HttpClient/interceptors] With provideHttpClient(withInterceptors([a, b, c])), what is the order?

- A. Requests pass c, b, a; responses pass a, b, c.
- B. Both requests and responses pass a, b, c.
- C. Requests pass a, b, c; responses pass c, b, a.
- D. Order is arbitrary.

**Answer:** C

**Explanation:** Interceptors form a chain: a wraps b wraps c. Requests go through them in array order and responses come back through in reverse order.

### 150. [HttpClient/interceptors] Why does this interceptor fail to add the header?

```
export const auth: HttpInterceptorFn = (req, next) => {
  req.headers.set('Authorization', 'Bearer x');
  return next(req);
};
```

- A. next(req) cannot be called synchronously.
- B. Headers cannot be set in interceptors.
- C. HttpHeaders and HttpRequest are immutable; set() returns a new instance, so use req.clone({ setHeaders: ... }).
- D. Interceptors must return a Promise.

**Answer:** C

**Explanation:** HttpRequest and HttpHeaders are immutable, and set() returns a new HttpHeaders that is discarded here. The original req is passed on unchanged. Clone the request with the new header.

### 151. [HttpClient/interceptors] A class-based interceptor is registered via HTTP_INTERCEPTORS but the app uses provideHttpClient() with no features. What happens?

- A. It is ignored unless withInterceptorsFromDi() is added.
- B. It runs first, before functional interceptors.
- C. Angular throws at startup.
- D. It runs but only for POST requests.

**Answer:** A

**Explanation:** provideHttpClient doesn't pick up legacy DI interceptors by default; you must include withInterceptorsFromDi(). It's not an error, but the interceptor never runs.

### 152. [HttpClient/interceptors] Which statements about HttpClient observables are true? (Select all that apply.)

- A. Subscribing twice to the same cold observable sends two requests.
- B. Unsubscribing before the response arrives cancels the underlying request.
- C. They emit once and complete for a normal response.
- D. You must unsubscribe after completion to prevent a memory leak.

**Answer:** A, B, C

**Explanation:** HttpClient returns cold observables that complete after the response; unsubscribing early aborts the request, and each subscription triggers its own call. Unsubscribing after completion is unnecessary.

### 153. [Deferrable views] Which statements about @defer are true? (Select all that apply.)

- A. Dependencies of @placeholder are loaded lazily with the deferred content.
- B. Components, directives and pipes used inside the block must be standalone to be deferred.
- C. If a deferred dependency is also used eagerly outside the block in the same component, it is not lazily loaded.
- D. @loading content is shown before the trigger fires.
- E. The default trigger is on idle.

**Answer:** B, C, E

**Explanation:** Only standalone dependencies referenced solely inside the block are split out, and default trigger is idle. @placeholder dependencies are eager since they render first, and @loading shows only once loading started.

### 154. [Content projection] app-card renders <ng-content /> inside @if (open). With open === false, what about the projected <heavy-cmp />?

```
<app-card>
  <heavy-cmp />
</app-card>

<!-- app-card template -->
@if (open) { <ng-content /> }
```

- A. It is not created until open becomes true.
- B. It is created by the parent regardless but not attached to the DOM while the ng-content isn't rendered.
- C. Angular throws an error.
- D. It is created lazily like @defer.

**Answer:** B

**Explanation:** Content projection is evaluated in the declaring parent's context, so projected components are instantiated even if the slot is not rendered. Use @defer or ng-template with a structural directive to defer creation.

### 155. [Lifecycle] Which statement about first availability of queries is correct?

- A. Both @ViewChild and @ContentChild are available in ngOnInit.
- B. Non-static @ContentChild is available in ngAfterContentInit and @ViewChild in ngAfterViewInit (static queries earlier).
- C. @ContentChild is available only in ngAfterViewInit.
- D. Both are available only after ngOnDestroy.

**Answer:** B

**Explanation:** Content queries resolve before view queries: ngAfterContentInit runs before ngAfterViewInit. Static view queries can be available in ngOnInit, but dynamic ones need ngAfterViewInit.

### 156. [Lifecycle] Which statements about ngOnChanges are true? (Select all that apply.)

- A. It is not called when the parent mutates a property of the same object reference passed in.
- B. It is called whenever any field of the component changes.
- C. It is not called for changes the component makes to its own @Input property from inside.
- D. It is called before ngOnInit when the component has bound @Input()s.

**Answer:** A, C, D

**Explanation:** ngOnChanges receives SimpleChanges for bindings updated by the parent, based on reference checks. Internal assignments and in-place mutations do not trigger it, and it is not a general field watcher.

### 157. [Standalone] A standalone component uses <app-child /> in its template but does not list ChildComponent in its imports. What happens?

- A. It works because all standalone components are globally registered.
- B. It works at runtime but warns in the console.
- C. It compiles because Angular auto-imports from the file.
- D. The compiler reports an unknown element error (NG8001); the component must be imported.

**Answer:** D

**Explanation:** A standalone component's template scope consists of its own imports; unknown elements cause a compile error under AOT. No global registration or auto-import exists.

### 158. [Testing] In a test for an OnPush component, setting componentInstance.name = 'X' followed by fixture.detectChanges() works the first time but not afterwards. What is the proper fix?

```
fixture.componentInstance.name = 'X';
fixture.detectChanges();
```

- A. Use fixture.componentRef.setInput('name', 'X') then detectChanges().
- B. Call fixture.autoDetectChanges(false).
- C. Remove OnPush in the test with overrideComponent only.
- D. Call tick() inside the test.

**Answer:** A

**Explanation:** OnPush views are checked on the first detectChanges but afterwards only when marked dirty; setInput goes through the input binding path and marks it dirty. Setting a property directly bypasses that. Overriding strategy changes behavior under test.

### 159. [Testing] A fakeAsync test calls component.search('a') where search uses debounceTime(300) and ends without further calls. What happens?

```
it('searches', fakeAsync(() => {
  component.search('a');
}));
```

- A. It passes; timers are discarded.
- B. It fails with an error about 1 timer(s) still in the queue; use tick(300) or flush().
- C. It hangs forever.
- D. It passes but the subscription is not executed.

**Answer:** B

**Explanation:** fakeAsync throws if pending timers exist at test end. Advance virtual time with tick(300) or run all with flush(). It does not hang, since time is virtual.

### 160. [RxJS state] What does the subscriber of this pipeline receive when the user clicks the button three times?

```
fromEvent(button, 'click')
  .pipe(reduce(count => count + 1, 0))
  .subscribe(console.log);
```

- A. 1, 2, 3 as the clicks happen
- B. 3 once, after the third click
- C. Nothing, because reduce emits only when the source completes and fromEvent never completes
- D. 0, 1, 2, 3

**Answer:** C

**Explanation:** reduce accumulates silently and emits the final value only on source completion, and a DOM event stream never completes, so nothing is emitted. scan emits each intermediate accumulation, which is what is wanted for running counts.


## Expert

### 161. [Zone.js] A component registers a high-frequency mousemove listener inside ngOnInit. Which approach avoids an application-wide change detection pass per event while still allowing selective updates?

```
ngOnInit() {
  this.zone.runOutsideAngular(() => {
    window.addEventListener('mousemove', this.onMove);
  });
}
```

- A. Mark the component OnPush so Zone.js stops patching addEventListener
- B. Use setTimeout inside the handler to defer the tick
- C. Call ChangeDetectorRef.detach() in the constructor, which also unpatches the listener
- D. Wrap the registration in NgZone.runOutsideAngular and re-enter with ngZone.run only when state must update

**Answer:** D

**Explanation:** Listeners registered in the Angular zone trigger ApplicationRef.tick after each event. Registering in runOutsideAngular avoids that, and ngZone.run re-enters when needed. OnPush does not change zone patching, and detach only affects one view, not the global tick.

### 162. [Zoneless] In a zoneless application (provideZonelessChangeDetection), which of the following schedule a change detection run? (Select all that apply.)

- A. An async pipe receiving a new emission
- B. Calling ChangeDetectorRef.markForCheck()
- C. Setting a signal that is read in a component template
- D. A Promise.then callback that mutates a plain field
- E. Updating a plain class field inside a setTimeout callback

**Answer:** A, B, C

**Explanation:** Signals read in templates, markForCheck, async pipe emissions and template event listeners notify the scheduler. Plain field mutations in timers or promises produce no notification without Zone.js, so the view stays stale.

### 163. [OnPush] Which of the following mark an OnPush component view as dirty? (Select all that apply.)

- A. A DOM event handler bound in the component's own template runs
- B. An async pipe in its template receives a new value
- C. An @Input receives a new object reference
- D. A property of an input object is mutated in place by the parent
- E. A plain field is changed by a setTimeout callback in the component

**Answer:** A, B, C

**Explanation:** New input references, template-bound events, and async pipe emissions (via markForCheck) dirty the view. In-place mutation keeps the same reference, and a timer changing a field does not mark the view dirty.

### 164. [Signals] What happens when signal.set() is called with a value equal (Object.is) to the current value using the default equality?

- A. Computed signals recompute but templates are not refreshed
- B. The signal version increments and consumers are marked dirty
- C. Dependents are not notified and no recomputation occurs
- D. Effects re-run once but computed signals are skipped

**Answer:** C

**Explanation:** The signal compares with Object.is and, if equal, does nothing, so no consumers are dirtied. Effects and computeds are consumers and are not notified either.

### 165. [Signals] How does a computed() signal behave with respect to evaluation?

- A. It recomputes eagerly on every dependency change
- B. It recomputes on every change detection pass
- C. It recomputes on every read regardless of dependency changes
- D. It is lazy and memoized: it recomputes only when read after a dependency changed

**Answer:** D

**Explanation:** Computeds are lazily evaluated and cached until a dependency marks them stale. They are not eager, and they do not recompute on each read when dependencies are unchanged.

### 166. [Signals] Which statements about effect() in Angular are true? (Select all that apply.)

```
effect((onCleanup) => {
  const id = setInterval(() => log(this.count()), 1000);
  onCleanup(() => clearInterval(id));
});
```

- A. Setting a signal always runs dependent effects immediately before set() returns
- B. Effects must always be destroyed manually with destroy() or they leak, even in components
- C. The onCleanup callback runs before the next execution and on destroy
- D. Signals read inside untracked() do not become dependencies of the effect
- E. Effects are scheduled and flushed asynchronously, not synchronously when a signal is set

**Answer:** C, D, E

**Explanation:** Effects are batched and run during change detection or the scheduler flush, with cleanups between runs, and untracked reads add no dependency. They do not run synchronously inside set(). Effects created in an injection context are destroyed automatically with their owner, so manual destroy is not required.

### 167. [Dependency Injection] A component declares a service in viewProviders. Which consumer can NOT inject it?

- A. The component itself
- B. A component projected through <ng-content> into this component's template
- C. A directive on an element inside this component's template
- D. A child component declared in this component's template

**Answer:** B

**Explanation:** viewProviders are visible to the component and nodes in its own view but hidden from projected content, which belongs to the parent's declaration. Providers in 'providers' are visible to content children too.

### 168. [Dependency Injection] A component provides FormStateService in its providers and a child component needs the parent component's instance, while the child itself also provides FormStateService. How does the child obtain the parent's instance?

- A. inject(FormStateService, { host: true, self: true })
- B. inject(FormStateService, { optional: true })
- C. inject(FormStateService, { skipSelf: true })
- D. inject(FormStateService, { self: true })

**Answer:** C

**Explanation:** skipSelf starts resolution at the parent element injector. self restricts to the node itself and would return the child's own instance, and optional only changes failure behavior.

### 169. [Dependency Injection] Which statements about providedIn: 'root' services are true? (Select all that apply.)

- A. A lazy-loaded route that injects one gets a new instance per route by default
- B. They are tree-shakable if never injected
- C. They are registered by listing them in AppModule providers
- D. A lazy route's providers array can override them for that subtree
- E. They are singletons in the root environment injector unless overridden

**Answer:** B, D, E

**Explanation:** providedIn root registers a tree-shakable factory in the root injector, so one instance is shared, including lazy routes, unless a route's providers override it. No per-route instance is created unless the route provides its own.

### 170. [Routing] Services listed in a Route's providers array are scoped how?

- A. To an environment injector created for that route and its child routes
- B. To the root injector globally
- C. To the component rendered by the route only
- D. To the router-outlet element injector

**Answer:** A

**Explanation:** Route providers create a route-level EnvironmentInjector shared by the route and its children. They are not global, and they are not element-level providers of the component.

### 171. [Forms] Which are required or correct when implementing a custom ControlValueAccessor? (Select all that apply.)

```
@Component({
  selector: 'app-rating',
  providers: [{
    provide: NG_VALUE_ACCESSOR,
    useExisting: forwardRef(() => RatingComponent),
    multi: true
  }]
})
export class RatingComponent implements ControlValueAccessor { }
```

- A. writeValue is called by the forms API to push model values into the view
- B. registerOnChange stores a function to call when the user changes the value
- C. Provide NG_VALUE_ACCESSOR with useExisting (forwardRef) and multi: true
- D. writeValue should call onChange so the model stays in sync
- E. Call the registered onTouched callback when the control is blurred

**Answer:** A, B, C, E

**Explanation:** The token provider, writeValue (model to view), onTouched, and onChange (view to model) are all part of the contract. Calling onChange inside writeValue would echo the change back and incorrectly mark the control dirty.

### 172. [Forms] When is the optional ControlValueAccessor.setDisabledState called?

- A. Whenever writeValue is called
- B. When the control becomes invalid
- C. When the bound control's disabled status changes, for example via control.disable()
- D. Only once when the form is first created

**Answer:** C

**Explanation:** Forms calls setDisabledState to reflect enable/disable calls on the control. It is unrelated to validity or to value writes.

### 173. [Dynamic Components] After ViewContainerRef.createComponent for an OnPush component, how should a parent supply an input so ngOnChanges and the view update correctly?

```
const ref = vcr.createComponent(CardComponent);
ref.setInput('name', 'Ada');
```

- A. componentRef.instance.name = value
- B. Object.assign(componentRef.instance, { name: value })
- C. componentRef.changeDetectorRef.detach()
- D. componentRef.setInput('name', value)

**Answer:** D

**Explanation:** setInput marks the view dirty and triggers input handling like a binding. Assigning to the instance bypasses ngOnChanges and does not mark an OnPush view for check.

### 174. [Dynamic Components] A component is created with createComponent(Comp, { environmentInjector, hostElement }) outside any view container. What is needed for it to be change-detected?

```
const ref = createComponent(Toast, { environmentInjector: this.envInjector, hostElement: el });
this.appRef.attachView(ref.hostView);
```

- A. appRef.attachView(ref.hostView), and destroy it when done
- B. Nothing; it is automatically attached to the ApplicationRef
- C. Call NgZone.run once at creation
- D. Add it to the declarations of the root module

**Answer:** A

**Explanation:** A component created standalone is not part of any tree until its host view is attached to ApplicationRef; it must also be destroyed manually. It is not auto-attached, and zone runs or declarations do not attach it.

### 175. [SSR and Hydration] Which statements about Angular hydration are true? (Select all that apply.)

- A. ngSkipHydration opts a component out of hydration
- B. It requires ngSkipHydration on every component
- C. Manual DOM manipulation of Angular-owned nodes can cause hydration mismatches
- D. It reuses server-rendered DOM instead of recreating it
- E. Hydration discards the server HTML and re-renders everything

**Answer:** A, C, D

**Explanation:** Hydration reuses existing DOM and requires structure to match, so direct manipulation can break it; ngSkipHydration opts out. It does not discard the server output, and ngSkipHydration is only an opt-out, not a requirement.

### 176. [SSR and Hydration] How does withHttpTransferCache help an SSR app?

- A. It disables HTTP requests on the server
- B. It converts HttpClient to the fetch API
- C. Server HttpClient responses are serialized into the page and reused by the client, avoiding duplicate requests
- D. It caches all responses in localStorage permanently

**Answer:** C

**Explanation:** Responses made on the server are stored in TransferState and replayed on the client for matching requests. It is not persistent browser storage and does not stop server requests.

### 177. [SSR and Hydration] Which practices keep code safe for server-side rendering? (Select all that apply.)

- A. Inject DOCUMENT instead of using the global document
- B. Assume ngOnInit only runs in the browser
- C. Avoid unbounded timers that keep the server render from stabilizing
- D. Guard browser-only APIs with isPlatformBrowser or run them in afterNextRender
- E. Access window or document directly in constructors

**Answer:** A, C, D

**Explanation:** Platform guards, afterNextRender (browser only), and DOCUMENT injection keep code portable, and pending macrotasks delay stability. Constructors and ngOnInit run on the server too, so global browser access breaks there.

### 178. [Lazy Loading] How is a custom preloading strategy implemented to preload only routes flagged in data?

```
export class FlagPreload implements PreloadingStrategy {
  preload(route: Route, load: () => Observable<any>) {
    return route.data?.['preload'] ? load() : of(null);
  }
}
```

- A. Implement PreloadingStrategy.preload(route, load) returning load() or of(null) based on route.data
- B. Override Router.navigate to prefetch chunks
- C. Add providedIn: 'root' to the lazy route's component
- D. Use canMatch to return true for flagged routes

**Answer:** A

**Explanation:** preload receives the route and a loader function; returning load() fetches the chunk and of(null) skips it. canMatch gates matching, not background preloading.

### 179. [Lazy Loading] Which statements about @defer blocks are true? (Select all that apply.)

- A. A standalone component also referenced eagerly elsewhere is still split out into the lazy chunk
- B. on viewport triggers loading when the placeholder enters the viewport
- C. Dependencies used only within the block can be split into a separate lazy chunk
- D. @defer works with NgModule-declared (non-standalone) components in all cases
- E. The @placeholder content is shown before the trigger fires

**Answer:** B, C, E

**Explanation:** Standalone dependencies referenced only inside the block are lazily loaded, but eager use elsewhere keeps them in the main bundle. Placeholders and the viewport trigger work as described. Non-standalone dependencies are not deferrable by default.

### 180. [Bundle Performance] What does setting "sideEffects": false in a library's package.json allow bundlers to do?

```
{
  "name": "my-lib",
  "sideEffects": false
}
```

- A. Skip type checking during the build
- B. Make the library load lazily at runtime
- C. Drop unused modules/exports during tree shaking
- D. Disable zone patching in the library

**Answer:** C

**Explanation:** The flag tells the bundler that unused imports can be removed safely, improving tree shaking. It has nothing to do with zones, typing, or runtime lazy loading.

### 181. [RxJS] What is the difference between shareReplay(1) and shareReplay({ bufferSize: 1, refCount: true })?

- A. refCount makes the replayed value expire after one second
- B. Without refCount, values are never replayed
- C. refCount makes the observable hot, otherwise it is cold
- D. Without refCount the source subscription stays open after all subscribers leave; with it the source is unsubscribed at zero subscribers

**Answer:** D

**Explanation:** Plain shareReplay keeps the upstream subscription alive, which can leak with long-lived sources. With refCount true it unsubscribes at zero subscribers, though replay buffers behave normally in both.

### 182. [RxJS] Which of these help prevent subscription leaks in components? (Select all that apply.)

- A. takeUntilDestroyed() inside an injection context, or with a passed DestroyRef elsewhere
- B. Using the async pipe in the template
- C. Subscribing to HttpClient calls always leaks unless unsubscribed
- D. Calling takeUntilDestroyed() with no argument inside ngOnInit
- E. Storing Subscriptions and unsubscribing in ngOnDestroy

**Answer:** A, B, E

**Explanation:** takeUntilDestroyed with DestroyRef, async pipe, and manual unsubscription all release subscriptions. Without an argument outside an injection context it throws, and HttpClient observables complete after the response.

### 183. [RxJS] By default, what does the share() operator do when the subscriber count falls to zero and a new subscriber arrives later?

```
const shared$ = source$.pipe(share());
```

- A. It keeps the source subscribed forever
- B. It resets and resubscribes to the source, because resetOnRefCountZero is true by default
- C. It replays the last value without resubscribing
- D. It throws an error

**Answer:** B

**Explanation:** share() uses a Subject connector and resets on refCount zero, error, and complete, so late subscribers trigger a new source subscription. Replay behavior needs shareReplay or explicit config.

### 184. [Testing] Which approaches are appropriate when testing components in a modern Angular app? (Select all that apply.)

```
fixture.componentRef.setInput('title', 'Hi');
fixture.detectChanges();
http.expectOne('/api').flush([]);
```

- A. Use HttpTestingController and call verify() in afterEach
- B. Use component harnesses to decouple tests from DOM structure
- C. Use fixture.componentRef.setInput to set signal inputs
- D. Assign directly to a signal input property on the instance
- E. Use real timers and sleep() to wait for async work

**Answer:** A, B, C

**Explanation:** setInput works with signal inputs, HttpTestingController.verify checks outstanding requests, and harnesses abstract DOM. Real sleeps make tests slow and flaky; use fakeAsync or whenStable instead. Signal inputs cannot be assigned directly.

### 185. [State Management] Which are sound NgRx-style state design principles? (Select all that apply.)

- A. Duplicate derived data in the store for convenience
- B. Mutate state objects in place for performance
- C. Reducers must be pure functions
- D. Normalize entity collections and derive view data through selectors
- E. Keep side effects like HTTP calls in effects, not reducers

**Answer:** C, D, E

**Explanation:** Pure reducers, normalized state with derived selectors, and side effects in effects keep state predictable. Duplicated derived data goes stale and in-place mutation breaks change detection.

### 186. [State Management] When does a memoized createSelector recompute its projector?

- A. When any input selector returns a result that is not reference-equal to the previous one
- B. On every store emission
- C. On every change detection cycle
- D. Only when the whole state reference changes

**Answer:** A

**Explanation:** A createSelector reruns the projector only if its input selectors' results changed by reference. A new state object alone is not enough if the slices it reads are unchanged.

### 187. [Micro-frontends] In a Module Federation setup, which configuration choices reduce duplicate Angular runtimes? (Select all that apply.)

- A. Declare @angular/core as shared with singleton: true
- B. Give each remote its own bundled copy of Angular
- C. Use strictVersion to fail loudly on incompatible versions
- D. Share the same Router and Injector instance automatically without configuration
- E. Align the Angular versions across host and remotes

**Answer:** A, C, E

**Explanation:** Singleton sharing, strict versions, and aligned versions avoid duplicate runtimes. Bundling separate copies defeats this, and shared packages do not auto-share injectors.

### 188. [Templates] In @for, what does `track item.id` achieve compared with `track $index` when a list is reordered?

```
@for (item of items(); track item.id) {
  <app-row [item]="item" />
} @empty {
  <p>None</p>
}
```

- A. It sorts the list by id
- B. It makes the iteration lazy
- C. DOM nodes and component instances are moved with their items instead of being rebound to different data
- D. It disables DOM updates entirely

**Answer:** C

**Explanation:** Tracking by a stable id lets the diff move existing views, preserving state. Tracking by index reuses views by position and rebinds them to different items.

### 189. [Templates] Which statements about the @for block are true? (Select all that apply.)

- A. Contextual variables such as $index, $first, $last and $count are available
- B. It only accepts arrays, never other iterables
- C. An @empty block renders when the collection is empty
- D. track is optional and defaults to object identity
- E. The track expression is required

**Answer:** A, C, E

**Explanation:** track is mandatory, context variables and @empty exist, and it works with any iterable, not only arrays. There is no optional default tracking.

### 190. [Routing] A route is lazy-loaded with loadChildren. Which guard prevents the lazy chunk from being downloaded for unauthorized users?

```
{
  path: 'admin',
  canMatch: [() => inject(Auth).isAdmin()],
  loadChildren: () => import('./admin/routes')
}
```

- A. canMatch
- B. canActivate
- C. canDeactivate
- D. resolve

**Answer:** A

**Explanation:** canMatch runs during route matching, so a false result skips the route and its lazy loading. canActivate runs after the route has matched and the chunk loaded; resolve and canDeactivate come later.

### 191. [Routing] Which statements about functional route guards are true? (Select all that apply.)

- A. Returning false cancels navigation without redirecting
- B. They can call inject() to obtain services
- C. Returning a UrlTree redirects navigation
- D. They are skipped for lazy-loaded routes
- E. They must be classes implementing CanActivate

**Answer:** A, B, C

**Explanation:** Guard functions run in an injection context, may be async, and results are boolean or UrlTree (sync or async). Class-based guards are not required.

### 192. [Routing] When are route resolvers executed relative to guards?

- A. After the component is rendered
- B. In parallel with canDeactivate
- C. After guards pass, before the route is activated
- D. Before canMatch

**Answer:** C

**Explanation:** Resolvers run once guards have allowed navigation and complete before activation. They do not run before matching or after rendering.

### 193. [Standalone Migration] Which are correct when migrating an NgModule app to standalone? (Select all that apply.)

```
bootstrapApplication(AppComponent, {
  providers: [importProvidersFrom(LegacyModule)]
});
```

- A. All NgModules must be deleted before any component can be standalone
- B. NgModule providers can be brought in with importProvidersFrom
- C. Standalone components cannot import any NgModule
- D. The migration schematic can convert declarations stepwise
- E. Standalone components can import NgModules and other standalone items

**Answer:** B, D, E

**Explanation:** Standalone components may import NgModules, importProvidersFrom bridges module providers, and the schematic runs in steps. The cannot-import and must-delete claims are false.

### 194. [Change Detection] The ExpressionChangedAfterItHasBeenCheckedError occurs because:

- A. In dev mode, a second verification pass finds a binding value that changed during the first pass
- B. Change detection ran twice in production
- C. The component was OnPush
- D. A subscription was left open

**Answer:** A

**Explanation:** Angular re-checks bindings in dev mode and throws if a value changed after being checked, typically due to child-to-parent state changes. It is not produced in production builds.

### 195. [Change Detection] What does ChangeDetectorRef.markForCheck() do?

- A. Marks only this view and not its ancestors
- B. Marks the view and its ancestors for checking at the next tick without running change detection itself
- C. Runs change detection immediately on this view
- D. Detaches the view from the tree

**Answer:** B

**Explanation:** markForCheck marks the path to the root dirty so the next tick checks it. detectChanges is the call that runs it immediately.

### 196. [Signals] Which are true of signal-based inputs and model()? (Select all that apply.)

- A. Signal inputs can be updated with .set() inside the child
- B. Signal inputs are read-only in the component
- C. input.required() must be provided by the parent or compilation fails
- D. model() enables two-way binding with [(value)]
- E. Signal inputs cannot be read inside computed()

**Answer:** B, C, D

**Explanation:** Inputs are read-only, model is writable and bindable two-way, and required inputs are compile-checked. Inputs are normal signals and work in computed(). .set() exists on model, not input.

### 197. [Signals] Which statements about converting Observables with toSignal() in a large application are true? (Select all that apply.)

- A. It must be called in ngOnInit
- B. If the observable errors, reading the signal throws that error
- C. It never unsubscribes automatically
- D. Without initialValue, the signal's type includes undefined until the first emission
- E. It subscribes immediately and unsubscribes when the owning context is destroyed

**Answer:** B, D, E

**Explanation:** toSignal subscribes eagerly with automatic cleanup, includes undefined without an initial value, and rethrows errors on read. It needs an injection context, not ngOnInit.

### 198. [Zone.js] Why does making every component OnPush not stop Zone.js from triggering ApplicationRef.tick on each async event?

- A. Zone.js notifies on task completion regardless; OnPush only skips unchanged views during the pass
- B. OnPush components are never skipped
- C. Zone.js ignores OnPush components
- D. OnPush disables Zone.js patches

**Answer:** A

**Explanation:** Zone triggers a tick whenever microtasks drain, and OnPush only prunes which views are checked. The tick still happens.

### 199. [Dependency Injection] What is the difference between { provide: A, useClass: B } and { provide: A, useExisting: B }?

```
providers: [
  { provide: Logger, useClass: ConsoleLogger },
  { provide: Alias, useExisting: ConsoleLogger }
]
```

- A. useClass requires providedIn root
- B. useClass creates a separate B instance for A; useExisting aliases A to the existing B instance
- C. They are identical
- D. useExisting creates a new instance each time

**Answer:** B

**Explanation:** useExisting points the token at the same provider's instance so A and B share state, while useClass instantiates its own.

### 200. [HTTP] Which are true about functional HTTP interceptors registered with provideHttpClient(withInterceptors([...]))? (Select all that apply.)

```
export const authInterceptor: HttpInterceptorFn = (req, next) =>
  next(req.clone({ setHeaders: { Authorization: inject(Auth).token() } }));
```

- A. Request handling runs in array order and responses flow back in reverse
- B. They cannot modify the outgoing request
- C. They must return an Observable of HttpEvent
- D. They run in a different order than registered for requests
- E. They can use inject() to access services

**Answer:** A, C, E

**Explanation:** Functional interceptors have an injection context, form a chain in order, and return an event stream. Requests are immutable but can be cloned and modified. Claiming that request order differs from registration is false.

