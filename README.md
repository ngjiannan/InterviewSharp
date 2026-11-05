# InterviewSharp

Interview practice: SQL Server (hands-on), Angular and .NET/C# (MCQ).

| Item | Description |
|---|---|
| `sql\01_schema.sql`, `sql\02_seed.sql` | Create `PracticeDB` and load sample data (company / orders theme) |
| `questions.md` | 200 questions (30 Easy / 60 Medium / 70 Hard / 40 Expert) |
| `answers.md` | Hints, model answers and explanations for all 200 |
| `sql\answers.sql` | All model answers as a runnable script |
| `InterviewSharp\` | Blazor Web App (.NET 10): write queries, run, get hints, check answers |
| `build_content.py` + `extra_*.py` | Source of the questions/answers; regenerates `questions.json`, `questions.md`, `answers.md`, `sql\answers.sql` |

## 1. SQL Server (Docker)

The SA password is in `.env` (`MSSQL_SA_PASSWORD`) and in `InterviewSharp\appsettings.Development.json`.

```powershell
docker start sql-practice      # start (container already created)
docker stop sql-practice       # stop
```

Connect with SSMS / Azure Data Studio: `localhost,1433`, login `sa`, trust server certificate.

Re-create the container from scratch:

```powershell
docker run -d --name sql-practice -e ACCEPT_EULA=Y -e "MSSQL_SA_PASSWORD=<password>" -p 1433:1433 -v sqlpractice_data:/var/opt/mssql mcr.microsoft.com/mssql/server:2022-latest
```

Then use the app's **Schema & Database → Reset database** button (or run the two `.sql` files) to create `PracticeDB`.

## 2. Practice app

```powershell
cd InterviewSharp
$env:ASPNETCORE_ENVIRONMENT = "Development"
dotnet run --urls http://localhost:5000
```

Open http://localhost:5000. Pick a question, write a `SELECT`/`WITH` query, then:
**Run**, **Hint** (progressive), **Check my answer** (compares your result set with the model answer; row order and column names are ignored), **Show answer**.
The app has no login. Only single read-only `SELECT`/`WITH` statements are accepted, with a 10 s timeout and a 500-row cap.

After editing `build_content.py`, re-run it and copy `questions.json` to `InterviewSharp\`.

## Schema

Departments, Employees (self-referencing `ManagerId`), SalaryHistory, Customers, Products, Orders, OrderItems.
Sample data includes NULLs, ties, duplicates, a department without employees, customers/products without orders, and an employee with no department or manager.

## Progress
Solved questions (marked ✓ when **Check my answer** is correct) are saved in your browser's localStorage (key `sqlpractice.solved`), so nothing is stored on the server and they survive restarts and **Reset database**. Progress is per browser; clear site data to reset it. Use the *Unsolved only* toggle to hide solved ones.

## Question format
Each question lists the **tables** to use and the exact **return columns (in order)**; column aliases don't need to match. These are generated from the model answers by `enrich.py` (run it, then `build_content.py`, after changing any answer).

## Angular and .NET / C# MCQs
400 multiple-choice questions (200 each; 30 Easy / 60 Medium / 70 Hard / 40 Expert), mixing single-answer and *select all that apply* (graded all-or-nothing). Open **Angular** or **.NET / C#** in the top nav: optional hint, instant correct answer + explanation, solved tracking in localStorage (`sqlpractice.angular.solved` / `sqlpractice.dotnet.solved`). Sources are in `mcq\`; run `build_mcq.py` to validate and regenerate `mcq_*.json` / `mcq_*.md` (answers), then copy the JSON files into `InterviewSharp\`.

## PWA and free hosting
`InterviewSharp.Pwa` is an installable, offline-capable Blazor WebAssembly PWA built from the shared UI library `InterviewSharp.Shared` (the local server app uses the same pages). Content JSON is copied from the repo root at build time. Without an `ApiBaseUrl` (in `InterviewSharp.Pwa\wwwroot\appsettings.json`) the SQL page runs in study mode (hints, answers, manual "Mark solved"). Build with `dotnet publish InterviewSharp.Pwa -c Release -o out` (serve `out\wwwroot`). See **DEPLOY.md** for free hosting (Cloudflare Pages + Azure SQL free offer + App Service F1) and free domains. The server app also exposes `/api/run`, `/api/check`, `/api/schema`, `/healthz` with CORS (`Cors:Origins`) and rate limiting.
