"""Derives meta.json (tables, returned columns, ordering) for each question from its model answer.

Run after build_content.py: reads questions.json, asks SQL Server for each answer's result-set
column names, and writes meta.json keyed by question key. Then re-run build_content.py to merge.
"""
import json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
KNOWN = ["Departments", "Employees", "SalaryHistory", "Customers", "Products", "Orders", "OrderItems"]
pw = open(os.path.join(ROOT, ".env")).read().split("=", 1)[1].strip().splitlines()[0]

Q = json.load(open(os.path.join(ROOT, "questions.json"), encoding="utf-8"))


def tables_of(sql):
    s = re.sub(r"--[^\n]*", "", sql)
    found = []
    for m in re.finditer(r"\b(?:FROM|JOIN|APPLY)\s+(?:dbo\.)?(\w+)", s, re.I):
        n = next((k for k in KNOWN if k.lower() == m.group(1).lower()), None)
        if n and n not in found:
            found.append(n)
    return found


def final_order_by(sql):
    s = re.sub(r"--[^\n]*", "", sql).rstrip().rstrip(";")
    s = re.sub(r"OPTION\s*\(.*\)\s*$", "", s, flags=re.I | re.S).rstrip()
    depth, last = 0, None
    for m in re.finditer(r"\(|\)|\bORDER\s+BY\b", s, re.I):
        t = m.group(0)
        if t == "(":
            depth += 1
        elif t == ")":
            depth -= 1
        elif depth == 0:
            last = m
    if not last:
        return ""
    tail = s[last.end():]
    tail = re.sub(r"\s+OFFSET\b.*$", "", tail, flags=re.I | re.S)
    return re.sub(r"\s+", " ", tail).strip()


lines = ["SET NOCOUNT ON;", "USE PracticeDB;", "GO"]
for x in Q:
    t = x["answer"].replace("'", "''")
    lines.append(f"SELECT '###{x['key']}' AS k;")
    lines.append(f"SELECT name FROM sys.dm_exec_describe_first_result_set(N'{t}', NULL, 0) WHERE is_hidden = 0 ORDER BY column_ordinal;")
    lines.append("GO")
sql_path = os.path.join(ROOT, "sql", "_describe.sql")
open(sql_path, "w", encoding="utf-8").write("\n".join(lines))

subprocess.run(["docker", "cp", sql_path, "sql-practice:/tmp/sql/_describe.sql"], check=True)
r = subprocess.run(["docker", "exec", "sql-practice", "/opt/mssql-tools18/bin/sqlcmd", "-C", "-S", "localhost", "-U", "sa", "-P", pw,
                    "-i", "/tmp/sql/_describe.sql", "-h", "-1", "-W"], capture_output=True, text=True, encoding="utf-8")
os.remove(sql_path)

cols, cur = {}, None
for ln in r.stdout.splitlines():
    ln = ln.strip()
    if ln.startswith("###"):
        cur = ln[3:]
        cols[cur] = []
    elif ln and cur and not ln.startswith(("Msg", "(")):
        cols[cur].append(ln)
    elif ln.startswith("Msg"):
        print("ERR", cur, ln)

meta, bad = {}, 0
for x in Q:
    c = cols.get(x["key"], [])
    if not c:
        bad += 1
        print("no columns for", x["id"])
    meta[x["key"]] = {"tables": tables_of(x["answer"]), "returns": c, "ordering": final_order_by(x["answer"])}
json.dump(meta, open(os.path.join(ROOT, "meta.json"), "w", encoding="utf-8"), indent=1)
print("meta for", len(meta), "missing columns:", bad)
