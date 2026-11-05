# Deploying InterviewSharp for free

Architecture: static PWA (Cloudflare Pages) -> small API (Azure App Service F1) -> Azure SQL Database (free offer).
MCQ tracks and study mode work with the PWA alone; only live Run/Check needs the API and database.

## 0. Push to GitHub
```powershell
cd InterviewSharp
git init; git add .; git commit -m "InterviewSharp"
# create an empty repo on github.com, then:
git remote add origin https://github.com/<you>/InterviewSharp.git
git push -u origin main
```
`.gitignore` already excludes `.env` and `appsettings.Development.json` (they hold the local SA password). Check `git status` before pushing.

## 1. Azure SQL Database (free offer)
1. Create a free Azure account (https://azure.microsoft.com/free; a card is needed for identity only).
2. Portal > Create > SQL Database > **Apply free offer** (serverless, 100,000 vCore-seconds + 32 GB/month). Name the database `PracticeDB`, choose SQL authentication and note the admin login/password. Set "behavior when free limit reached" to **Auto-pause**.
3. Networking: add your client IP and enable "Allow Azure services and resources to access this server".
4. Connect (Azure Data Studio, SSMS or `sqlcmd -S <server>.database.windows.net -d PracticeDB -U <admin> -P <pw>`) and run in order:
   `sql\azure\01_schema.sql`, `sql\azure\02_seed.sql`, `sql\azure\03_readonly_user.sql` (edit the password first).
   These were tested for all 200 answers.

## 2. API on Azure App Service F1 (free)
The API is the `InterviewSharp` server project (`/api/run`, `/api/check`, `/api/schema`, `/healthz`).
```powershell
az login
az webapp up --name <unique-api-name> --resource-group <rg> --runtime "dotnet:10" --sku F1 --location <region> --project-name InterviewSharp   # run from InterviewSharp\InterviewSharp
az webapp config connection-string set -g <rg> -n <unique-api-name> -t Custom --settings PracticeDb="Server=tcp:<server>.database.windows.net,1433;Database=PracticeDB;User ID=practice_reader;Password=<pw>;Encrypt=True;"
az webapp config appsettings set -g <rg> -n <unique-api-name> --settings Hosted__AllowReset=false "Cors__Origins__0=https://<pages-name>.pages.dev"
```
Check `https://<unique-api-name>.azurewebsites.net/healthz`. If the runtime string is not accepted, run `az webapp list-runtimes`. If .NET 10 is unavailable on F1 in your region, publish self-contained instead (`dotnet publish -r win-x86 --self-contained`) and zip-deploy.
F1 sleeps when idle (first request ~20s) and has a CPU quota; the UI shows a "waking up" message.

## 3. PWA on Cloudflare Pages (free)
Cloudflare dashboard > Workers & Pages > Create > Pages > Connect to Git, pick the repo:
- Build command: `curl -sSL https://dot.net/v1/dotnet-install.sh | bash -s -- --channel 10.0 && export PATH="$HOME/.dotnet:$PATH" && dotnet publish InterviewSharp.Pwa -c Release -o out`
- Build output directory: `out/wwwroot`
- Project name: `interviewsharp` -> https://interviewsharp.pages.dev

Then edit `InterviewSharp.Pwa/wwwroot/appsettings.json`:
```json
{ "ApiBaseUrl": "https://<unique-api-name>.azurewebsites.net" }
```
commit and push; Pages redeploys. Leave it empty for study-only mode. `_redirects` (SPA fallback) and `_headers` are already included.

## Free domain options
- `*.pages.dev` (included, easiest), `*.github.io` (GitHub Pages; needs base-href changes), `*.netlify.app`.
- A nicer free name: a subdomain from is-a.dev (PR to their GitHub repo) pointed at the Pages project via *Custom domains*. Free TLDs like .tk are unreliable.

## Install as an app
Open the site in Chrome/Edge > Install icon in the address bar (or Share > Add to Home Screen on iOS). It works offline after the first load.
