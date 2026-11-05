import json, os

OUT = os.path.dirname(os.path.abspath(__file__))
Q = []

def q(level, topic, text, hints, sql, why):
    Q.append(dict(level=level, topic=topic, text=text, hints=hints, answer=sql.strip(), explanation=why))

E, M, H, X = "Easy", "Medium", "Hard", "Expert"

# ---------------- EASY ----------------
q(E, "SELECT", "List all columns and rows from the Departments table.",
  ["Use SELECT with a wildcard.", "The table name is Departments."],
  "SELECT * FROM Departments;",
  "SELECT * returns every column. Fine for exploration; in production list columns explicitly.")
q(E, "WHERE", "Show the first name, last name and salary of employees who earn more than 100,000.",
  ["Filter rows with WHERE.", "Compare Salary with > 100000."],
  "SELECT FirstName, LastName, Salary\nFROM Employees\nWHERE Salary > 100000;",
  "WHERE filters rows before they are returned.")
q(E, "ORDER BY", "List all employees (first name, last name, hire date) from the most recently hired to the earliest.",
  ["ORDER BY sorts results.", "Use DESC for newest first."],
  "SELECT FirstName, LastName, HireDate\nFROM Employees\nORDER BY HireDate DESC;",
  "Default sort is ASC; DESC reverses it.")
q(E, "TOP", "Find the 5 highest paid employees (first name, last name, salary).",
  ["TOP limits rows in SQL Server.", "Sort by Salary descending first, then take TOP 5."],
  "SELECT TOP 5 FirstName, LastName, Salary\nFROM Employees\nORDER BY Salary DESC;",
  "TOP (n) combined with ORDER BY gives the top-N. Use TOP (5) WITH TIES if ties should be included.")
q(E, "DISTINCT", "List the distinct job titles in the company, alphabetically.",
  ["DISTINCT removes duplicate rows.", "Add ORDER BY JobTitle."],
  "SELECT DISTINCT JobTitle\nFROM Employees\nORDER BY JobTitle;",
  "DISTINCT applies to the whole selected row, not just the first column.")
q(E, "LIKE", "Find customers whose name starts with the letter 'S'.",
  ["Use LIKE with a wildcard.", "'S%' matches anything starting with S."],
  "SELECT CustomerId, CustomerName\nFROM Customers\nWHERE CustomerName LIKE 'S%';",
  "% matches any number of characters, _ matches exactly one.")
q(E, "BETWEEN", "List all orders placed during 2024.",
  ["Use BETWEEN with two dates, or >= and <.", "Prefer a half-open range: >= '2024-01-01' AND < '2025-01-01'."],
  "SELECT OrderId, CustomerId, OrderDate, Status\nFROM Orders\nWHERE OrderDate >= '2024-01-01' AND OrderDate < '2025-01-01';",
  "A half-open range is safe for DATE and DATETIME columns alike and can use an index.")
q(E, "IN", "List customers located in the USA or the UK.",
  ["IN replaces multiple ORs.", "WHERE Country IN ('USA','UK')."],
  "SELECT CustomerName, City, Country\nFROM Customers\nWHERE Country IN ('USA', 'UK');",
  "IN is shorthand for OR-ed equality checks.")
q(E, "NULL", "Find employees who have no manager.",
  ["NULL cannot be compared with =.", "Use IS NULL."],
  "SELECT EmployeeId, FirstName, LastName, JobTitle\nFROM Employees\nWHERE ManagerId IS NULL;",
  "NULL means unknown; = NULL is never true. Always use IS NULL / IS NOT NULL.")
q(E, "NULL", "List employees who earn a commission (CommissionPct is not null), with their commission percentage.",
  ["Use IS NOT NULL."],
  "SELECT FirstName, LastName, CommissionPct\nFROM Employees\nWHERE CommissionPct IS NOT NULL;",
  "IS NOT NULL keeps only rows with a value.")
q(E, "Expressions", "Show each employee's full name (as FullName) and their annual salary plus a 10% bonus (as SalaryWithBonus).",
  ["Concatenate with CONCAT or +.", "Multiply Salary by 1.10 and give it an alias with AS."],
  "SELECT CONCAT(FirstName, ' ', LastName) AS FullName,\n       Salary * 1.10 AS SalaryWithBonus\nFROM Employees;",
  "CONCAT treats NULL as an empty string, unlike the + operator.")
q(E, "COUNT", "How many orders are in the Orders table?",
  ["Use an aggregate function.", "COUNT(*) counts rows."],
  "SELECT COUNT(*) AS TotalOrders FROM Orders;",
  "COUNT(*) counts all rows; COUNT(col) skips NULLs.")
q(E, "AND / OR", "Find products that are out of stock (Stock = 0) or priced above 1000.",
  ["Combine conditions with OR."],
  "SELECT ProductName, UnitPrice, Stock\nFROM Products\nWHERE Stock = 0 OR UnitPrice > 1000;",
  "Use parentheses when mixing AND and OR - AND binds tighter.")
q(E, "OFFSET FETCH", "Page through products ordered by price (highest first): skip the first 5 and return the next 5.",
  ["OFFSET ... FETCH works with ORDER BY.", "OFFSET 5 ROWS FETCH NEXT 5 ROWS ONLY."],
  "SELECT ProductName, UnitPrice\nFROM Products\nORDER BY UnitPrice DESC, ProductId\nOFFSET 5 ROWS FETCH NEXT 5 ROWS ONLY;",
  "OFFSET/FETCH is the standard pagination syntax. Add a unique tie-breaker column for deterministic pages.")
q(E, "COALESCE", "List customers' names and emails, showing 'N/A' where the email is missing.",
  ["COALESCE / ISNULL replace NULL values."],
  "SELECT CustomerName, COALESCE(Email, 'N/A') AS Email\nFROM Customers;",
  "COALESCE returns its first non-NULL argument and is ANSI standard; ISNULL is T-SQL specific.")

# ---------------- MEDIUM ----------------
q(M, "INNER JOIN", "List each employee's full name with their department name. (Employees without a department should not appear.)",
  ["Join Employees to Departments on DepartmentId.", "INNER JOIN keeps only matching rows."],
  "SELECT e.FirstName, e.LastName, d.DepartmentName\nFROM Employees e\nINNER JOIN Departments d ON d.DepartmentId = e.DepartmentId;",
  "Iris (no department) is excluded by the inner join.")
q(M, "LEFT JOIN", "Find departments that have no employees.",
  ["Start from Departments and LEFT JOIN Employees.", "Look for rows where the employee side is NULL."],
  "SELECT d.DepartmentName\nFROM Departments d\nLEFT JOIN Employees e ON e.DepartmentId = d.DepartmentId\nWHERE e.EmployeeId IS NULL;",
  "The anti-join pattern: LEFT JOIN then filter on NULL from the right table's key. NOT EXISTS is an equivalent alternative.")
q(M, "Self join", "List each employee with their manager's name (show NULL / 'None' when there is no manager).",
  ["Join Employees to itself using two aliases.", "Use LEFT JOIN so employees without a manager are kept."],
  "SELECT e.FirstName + ' ' + e.LastName AS Employee,\n       COALESCE(m.FirstName + ' ' + m.LastName, 'None') AS Manager\nFROM Employees e\nLEFT JOIN Employees m ON m.EmployeeId = e.ManagerId;",
  "A self join treats one table as two roles (employee and manager).")
q(M, "GROUP BY", "Count the number of employees in each department (show the department name).",
  ["JOIN to get names, then GROUP BY the department name.", "COUNT(*) per group."],
  "SELECT d.DepartmentName, COUNT(e.EmployeeId) AS EmployeeCount\nFROM Departments d\nLEFT JOIN Employees e ON e.DepartmentId = d.DepartmentId\nGROUP BY d.DepartmentName\nORDER BY EmployeeCount DESC;",
  "LEFT JOIN + COUNT(e.EmployeeId) keeps empty departments with 0 (COUNT(*) would give 1).")
q(M, "AVG", "Show the average salary per department (rounded to 2 decimals), highest first.",
  ["AVG with GROUP BY.", "ROUND(AVG(Salary), 2)."],
  "SELECT d.DepartmentName, ROUND(AVG(e.Salary), 2) AS AvgSalary\nFROM Employees e\nJOIN Departments d ON d.DepartmentId = e.DepartmentId\nGROUP BY d.DepartmentName\nORDER BY AvgSalary DESC;",
  "Every non-aggregated column in SELECT must appear in GROUP BY.")
q(M, "HAVING", "List departments with more than 5 employees.",
  ["WHERE filters rows, HAVING filters groups.", "HAVING COUNT(*) > 5."],
  "SELECT d.DepartmentName, COUNT(*) AS EmployeeCount\nFROM Employees e\nJOIN Departments d ON d.DepartmentId = e.DepartmentId\nGROUP BY d.DepartmentName\nHAVING COUNT(*) > 5;",
  "HAVING runs after grouping so it can use aggregates; WHERE cannot.")
q(M, "SUM", "Calculate total revenue per product category. Revenue = Quantity * UnitPrice * (1 - Discount) from OrderItems. Highest first.",
  ["Join OrderItems to Products for Category.", "SUM the revenue expression and GROUP BY Category."],
  "SELECT p.Category,\n       SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue\nFROM OrderItems oi\nJOIN Products p ON p.ProductId = oi.ProductId\nGROUP BY p.Category\nORDER BY Revenue DESC;",
  "Aggregate an expression, not just a column. Use the price stored on the order line (historical price).")
q(M, "Anti join", "Find customers who have never placed an order.",
  ["LEFT JOIN Orders and test for NULL, or use NOT EXISTS.", "Avoid NOT IN if the subquery column can contain NULLs."],
  "SELECT c.CustomerId, c.CustomerName\nFROM Customers c\nWHERE NOT EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerId = c.CustomerId);",
  "NOT EXISTS is NULL-safe and usually optimises well.")
q(M, "Anti join", "Find products that have never been ordered.",
  ["Same pattern as the previous question, on OrderItems."],
  "SELECT p.ProductId, p.ProductName\nFROM Products p\nLEFT JOIN OrderItems oi ON oi.ProductId = p.ProductId\nWHERE oi.OrderItemId IS NULL;",
  "LEFT JOIN ... IS NULL on the right table's primary key.")
q(M, "Date functions", "Show the number of orders per month for 2024 (year, month, order count), in calendar order.",
  ["Use YEAR() and MONTH() or DATEPART.", "Group by both and order by them."],
  "SELECT YEAR(OrderDate) AS Yr, MONTH(OrderDate) AS Mth, COUNT(*) AS Orders\nFROM Orders\nWHERE OrderDate >= '2024-01-01' AND OrderDate < '2025-01-01'\nGROUP BY YEAR(OrderDate), MONTH(OrderDate)\nORDER BY Yr, Mth;",
  "Group by the same expressions you select. EOMONTH or FORMAT could also be used.")
q(M, "MIN / MAX", "For each department show headcount, minimum, maximum and average salary.",
  ["Several aggregates can be used in one query."],
  "SELECT d.DepartmentName,\n       COUNT(*) AS Headcount,\n       MIN(e.Salary) AS MinSalary,\n       MAX(e.Salary) AS MaxSalary,\n       AVG(e.Salary) AS AvgSalary\nFROM Employees e\nJOIN Departments d ON d.DepartmentId = e.DepartmentId\nGROUP BY d.DepartmentName;",
  "Multiple aggregates over the same grouping is a single pass over the data.")
q(M, "CASE", "Classify employees into salary bands: 'Low' (< 70,000), 'Mid' (70,000-119,999), 'High' (>= 120,000) and count employees in each band.",
  ["Use CASE to build the band.", "GROUP BY the CASE expression (or wrap it in a subquery/CTE)."],
  "SELECT CASE WHEN Salary < 70000 THEN 'Low'\n            WHEN Salary < 120000 THEN 'Mid'\n            ELSE 'High' END AS Band,\n       COUNT(*) AS Employees\nFROM Employees\nGROUP BY CASE WHEN Salary < 70000 THEN 'Low'\n              WHEN Salary < 120000 THEN 'Mid'\n              ELSE 'High' END;",
  "CASE evaluates top to bottom and returns the first match.")
q(M, "Multi-table JOIN", "Find the top 3 customers by total revenue (customer name and revenue).",
  ["Customers -> Orders -> OrderItems.", "SUM revenue, GROUP BY customer, ORDER BY DESC, TOP 3."],
  "SELECT TOP 3 c.CustomerName,\n       SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue\nFROM Customers c\nJOIN Orders o ON o.CustomerId = c.CustomerId\nJOIN OrderItems oi ON oi.OrderId = o.OrderId\nGROUP BY c.CustomerId, c.CustomerName\nORDER BY Revenue DESC;",
  "Group by the key (CustomerId) as well as the name in case two customers share a name.")
q(M, "GROUP BY", "Show the number of orders per Status and what percentage of all orders each status represents (1 decimal).",
  ["A scalar subquery (SELECT COUNT(*) FROM Orders) gives the total.", "Multiply by 100.0 to avoid integer division."],
  "SELECT Status,\n       COUNT(*) AS Orders,\n       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM Orders), 1) AS Pct\nFROM Orders\nGROUP BY Status;",
  "Integer / integer is integer division in T-SQL, so use 100.0.")
q(M, "Subquery", "List employees who earn more than the company-wide average salary.",
  ["Compare Salary with a subquery that returns AVG(Salary)."],
  "SELECT FirstName, LastName, Salary\nFROM Employees\nWHERE Salary > (SELECT AVG(Salary) FROM Employees);",
  "A scalar subquery returns one value and can be used in a WHERE comparison.")
q(M, "CROSS JOIN", "Produce a grid of every product Category combined with every order Status (distinct values only).",
  ["CROSS JOIN pairs every row of one set with every row of another.", "Use two DISTINCT subqueries."],
  "SELECT c.Category, s.Status\nFROM (SELECT DISTINCT Category FROM Products) c\nCROSS JOIN (SELECT DISTINCT Status FROM Orders) s\nORDER BY c.Category, s.Status;",
  "CROSS JOIN creates the Cartesian product - useful for building report skeletons that are later LEFT JOINed with facts.")
q(M, "DATEDIFF", "Show each employee's tenure in whole years as of 2025-12-31, for employees with at least 5 years of service.",
  ["DATEDIFF(YEAR, start, end) counts year boundaries, not full years.", "For full years compare against DATEADD(YEAR, 5, HireDate)."],
  "SELECT FirstName, LastName, HireDate,\n       DATEDIFF(YEAR, HireDate, '2025-12-31') AS TenureYearsApprox\nFROM Employees\nWHERE DATEADD(YEAR, 5, HireDate) <= '2025-12-31'\nORDER BY HireDate;",
  "DATEDIFF(YEAR) counts calendar boundaries crossed (2024-12-31 to 2025-01-01 = 1). The DATEADD filter guarantees full 5 years.")

# ---------------- HARD ----------------
q(H, "UNION", "Create a single list of names with a Type column: all employees (Type='Employee') and all customers (Type='Customer').",
  ["UNION ALL stacks result sets with matching column counts/types.", "Use a literal for the Type column."],
  "SELECT FirstName + ' ' + LastName AS Name, 'Employee' AS Type FROM Employees\nUNION ALL\nSELECT CustomerName, 'Customer' FROM Customers;",
  "UNION removes duplicates (and sorts/hashes); UNION ALL keeps everything and is faster.")
q(H, "Correlated subquery", "Find employees who earn more than the average salary of their own department.",
  ["The subquery must reference the outer row.", "Or compute department averages with a window function."],
  "SELECT e.FirstName, e.LastName, e.DepartmentId, e.Salary\nFROM Employees e\nWHERE e.Salary > (SELECT AVG(e2.Salary)\n                  FROM Employees e2\n                  WHERE e2.DepartmentId = e.DepartmentId);",
  "Alternative: SELECT ..., AVG(Salary) OVER (PARTITION BY DepartmentId) in a CTE and filter on it. Employees with NULL department are excluded because NULL = NULL is not true.")
q(H, "EXISTS", "List customers who have at least one cancelled order.",
  ["EXISTS stops at the first match.", "Correlate the subquery on CustomerId."],
  "SELECT c.CustomerId, c.CustomerName\nFROM Customers c\nWHERE EXISTS (SELECT 1 FROM Orders o\n              WHERE o.CustomerId = c.CustomerId AND o.Status = 'Cancelled');",
  "EXISTS avoids duplicates that an INNER JOIN would produce for customers with several cancelled orders.")
q(H, "CTE", "Using a CTE, compute revenue per month (exclude Cancelled orders) and list only the months whose revenue is above the average monthly revenue.",
  ["Build monthly revenue in a CTE.", "Compare against (SELECT AVG(Revenue) FROM cte)."],
  "WITH Monthly AS (\n    SELECT DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1) AS MonthStart,\n           SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue\n    FROM Orders o\n    JOIN OrderItems oi ON oi.OrderId = o.OrderId\n    WHERE o.Status <> 'Cancelled'\n    GROUP BY DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1)\n)\nSELECT MonthStart, Revenue\nFROM Monthly\nWHERE Revenue > (SELECT AVG(Revenue) FROM Monthly)\nORDER BY MonthStart;",
  "A CTE names an intermediate result so it can be reused and read top-down. It is not materialised - it is inlined like a view.")
q(H, "Multiple CTEs", "For each customer show their total revenue and their share (%) of overall revenue, largest share first. Use two CTEs.",
  ["CTE 1: revenue per customer.", "CTE 2: total revenue; CROSS JOIN it to divide."],
  "WITH CustRev AS (\n    SELECT o.CustomerId,\n           SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue\n    FROM Orders o\n    JOIN OrderItems oi ON oi.OrderId = o.OrderId\n    GROUP BY o.CustomerId\n), Total AS (\n    SELECT SUM(Revenue) AS Total FROM CustRev\n)\nSELECT c.CustomerName,\n       cr.Revenue,\n       ROUND(100.0 * cr.Revenue / t.Total, 2) AS SharePct\nFROM CustRev cr\nJOIN Customers c ON c.CustomerId = cr.CustomerId\nCROSS JOIN Total t\nORDER BY SharePct DESC;",
  "CTEs can reference earlier CTEs in the same WITH clause. Window alternative: SUM(Revenue) OVER ().")
q(H, "Recursive CTE", "Display the organisation hierarchy starting from the CEO (EmployeeId = 1): employee name, level (CEO = 0) and manager id.",
  ["A recursive CTE has an anchor member and a recursive member joined with UNION ALL.", "Recursive part joins Employees to the CTE on ManagerId = cte.EmployeeId and adds 1 to the level."],
  "WITH Org AS (\n    SELECT EmployeeId, FirstName, LastName, ManagerId, 0 AS Level\n    FROM Employees\n    WHERE EmployeeId = 1\n    UNION ALL\n    SELECT e.EmployeeId, e.FirstName, e.LastName, e.ManagerId, o.Level + 1\n    FROM Employees e\n    JOIN Org o ON e.ManagerId = o.EmployeeId\n)\nSELECT EmployeeId, FirstName + ' ' + LastName AS Name, Level, ManagerId\nFROM Org\nORDER BY Level, EmployeeId;",
  "Default MAXRECURSION is 100; guard against cycles in real data. Employees such as Iris (no manager) are not reachable from the CEO, so they do not appear.")
q(H, "Recursive CTE", "For every employee in the CEO's hierarchy, build the reporting chain as text, e.g. 'Alice > Bob > Grace > Ivy'.",
  ["Carry a path string in the recursive CTE.", "Concatenate the parent path with ' > ' and the current first name."],
  "WITH Chain AS (\n    SELECT EmployeeId, CAST(FirstName AS NVARCHAR(400)) AS Path\n    FROM Employees WHERE EmployeeId = 1\n    UNION ALL\n    SELECT e.EmployeeId, CAST(c.Path + N' > ' + e.FirstName AS NVARCHAR(400))\n    FROM Employees e\n    JOIN Chain c ON e.ManagerId = c.EmployeeId\n)\nSELECT EmployeeId, Path FROM Chain ORDER BY Path;",
  "Both members of a recursive CTE must have identical column types, so CAST the anchor to the final width.")
q(H, "ROW_NUMBER", "Find the highest paid employee in each department (ignore employees without a department). Break ties by lowest EmployeeId.",
  ["ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...).", "Filter rn = 1 in an outer query or CTE - you cannot use a window function in WHERE."],
  "WITH Ranked AS (\n    SELECT e.*, ROW_NUMBER() OVER (PARTITION BY e.DepartmentId ORDER BY e.Salary DESC, e.EmployeeId) AS rn\n    FROM Employees e\n    WHERE e.DepartmentId IS NOT NULL\n)\nSELECT d.DepartmentName, r.FirstName, r.LastName, r.Salary\nFROM Ranked r\nJOIN Departments d ON d.DepartmentId = r.DepartmentId\nWHERE r.rn = 1;",
  "Window functions are evaluated after WHERE/GROUP BY, so filtering needs a CTE or subquery.")
q(H, "RANK / DENSE_RANK", "Rank employees by salary within their department showing both RANK and DENSE_RANK (call them SalaryRank and SalaryDenseRank). Show Engineering only (DepartmentId = 2).",
  ["Both functions use OVER (PARTITION BY ... ORDER BY Salary DESC).", "Look at how ties (equal salaries) are numbered."],
  "SELECT FirstName, LastName, Salary,\n       RANK()       OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS SalaryRank,\n       DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS SalaryDenseRank\nFROM Employees\nWHERE DepartmentId = 2\nORDER BY Salary DESC;",
  "RANK leaves gaps after ties (1,2,2,4); DENSE_RANK does not (1,2,2,3); ROW_NUMBER never ties.")
q(H, "Running total", "Show monthly revenue together with a running (cumulative) total, ordered by month. Exclude Cancelled orders.",
  ["Aggregate by month first (CTE).", "SUM(Revenue) OVER (ORDER BY MonthStart ROWS UNBOUNDED PRECEDING)."],
  "WITH Monthly AS (\n    SELECT DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1) AS MonthStart,\n           SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue\n    FROM Orders o\n    JOIN OrderItems oi ON oi.OrderId = o.OrderId\n    WHERE o.Status <> 'Cancelled'\n    GROUP BY DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1)\n)\nSELECT MonthStart, Revenue,\n       SUM(Revenue) OVER (ORDER BY MonthStart ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS RunningTotal\nFROM Monthly\nORDER BY MonthStart;",
  "Specify ROWS explicitly; the default RANGE frame is slower and treats ties differently.")
q(H, "LAG", "Using SalaryHistory, show each salary change per employee with the previous salary and the percentage increase (1 decimal). Only rows that have a previous salary, for employees 9, 10 and 11.",
  ["LAG(Salary) OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate).", "Filter on a non-NULL previous salary in an outer query."],
  "WITH H AS (\n    SELECT EmployeeId, EffectiveDate, Salary,\n           LAG(Salary) OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate) AS PrevSalary\n    FROM SalaryHistory\n)\nSELECT EmployeeId, EffectiveDate, PrevSalary, Salary,\n       ROUND(100.0 * (Salary - PrevSalary) / PrevSalary, 1) AS PctIncrease\nFROM H\nWHERE PrevSalary IS NOT NULL AND EmployeeId IN (9, 10, 11)\nORDER BY EmployeeId, EffectiveDate;",
  "LAG/LEAD access previous/next rows without a self join. A third argument supplies a default instead of NULL.")
q(H, "Conditional aggregation", "Find customers whose 2024 revenue is higher than their 2023 revenue. Show both amounts.",
  ["SUM(CASE WHEN YEAR(OrderDate)=2023 THEN ... END).", "Use HAVING to compare the two conditional sums."],
  "SELECT c.CustomerName,\n       SUM(CASE WHEN YEAR(o.OrderDate) = 2023 THEN oi.Quantity * oi.UnitPrice * (1 - oi.Discount) ELSE 0 END) AS Rev2023,\n       SUM(CASE WHEN YEAR(o.OrderDate) = 2024 THEN oi.Quantity * oi.UnitPrice * (1 - oi.Discount) ELSE 0 END) AS Rev2024\nFROM Customers c\nJOIN Orders o ON o.CustomerId = c.CustomerId\nJOIN OrderItems oi ON oi.OrderId = o.OrderId\nGROUP BY c.CustomerId, c.CustomerName\nHAVING SUM(CASE WHEN YEAR(o.OrderDate) = 2024 THEN oi.Quantity * oi.UnitPrice * (1 - oi.Discount) ELSE 0 END)\n     > SUM(CASE WHEN YEAR(o.OrderDate) = 2023 THEN oi.Quantity * oi.UnitPrice * (1 - oi.Discount) ELSE 0 END)\nORDER BY c.CustomerName;",
  "Conditional aggregation pivots rows to columns in a single scan.")
q(H, "PIVOT", "Show revenue by product Category (rows) and by year 2023, 2024, 2025 (columns).",
  ["PIVOT needs the source rows shaped as (Category, Year, Revenue).", "PIVOT(SUM(Revenue) FOR Yr IN ([2023],[2024],[2025]))."],
  "SELECT Category, [2023], [2024], [2025]\nFROM (\n    SELECT p.Category, YEAR(o.OrderDate) AS Yr,\n           oi.Quantity * oi.UnitPrice * (1 - oi.Discount) AS Revenue\n    FROM OrderItems oi\n    JOIN Orders o   ON o.OrderId = oi.OrderId\n    JOIN Products p ON p.ProductId = oi.ProductId\n) src\nPIVOT (SUM(Revenue) FOR Yr IN ([2023], [2024], [2025])) pvt\nORDER BY Category;",
  "The pivot columns must be hard-coded unless you build dynamic SQL. The CASE-based approach from the previous question is equivalent.")

# ---------------- EXPERT ----------------
q(X, "DENSE_RANK", "Find the employee(s) with the second-highest salary in each department (departments with fewer than two distinct salaries should not appear).",
  ["DENSE_RANK handles ties properly.", "Filter DENSE_RANK = 2 in an outer query."],
  "WITH R AS (\n    SELECT DepartmentId, FirstName, LastName, Salary,\n           DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS rnk\n    FROM Employees\n    WHERE DepartmentId IS NOT NULL\n)\nSELECT d.DepartmentName, R.FirstName, R.LastName, R.Salary\nFROM R JOIN Departments d ON d.DepartmentId = R.DepartmentId\nWHERE R.rnk = 2;",
  "The classic 'Nth highest' question. ROW_NUMBER would wrongly pick one of several people tied for first.")
q(X, "Duplicates", "Find groups of employees that share the same Salary and HireDate, listing the salary, hire date and how many employees are in each such group.",
  ["Group by the columns that define a duplicate.", "HAVING COUNT(*) > 1."],
  "SELECT Salary, HireDate, COUNT(*) AS Employees\nFROM Employees\nGROUP BY Salary, HireDate\nHAVING COUNT(*) > 1;",
  "Duplicate detection is GROUP BY + HAVING COUNT(*) > 1. To delete duplicates use ROW_NUMBER() and delete rn > 1.")
q(X, "Top N per group", "Find the top 2 products by revenue in each product category (category, product, revenue, rank).",
  ["Aggregate revenue per product first.", "Then ROW_NUMBER/RANK partitioned by Category and filter <= 2."],
  "WITH ProdRev AS (\n    SELECT p.Category, p.ProductName,\n           SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue\n    FROM OrderItems oi\n    JOIN Products p ON p.ProductId = oi.ProductId\n    GROUP BY p.Category, p.ProductId, p.ProductName\n), Ranked AS (\n    SELECT *, ROW_NUMBER() OVER (PARTITION BY Category ORDER BY Revenue DESC) AS rn\n    FROM ProdRev\n)\nSELECT Category, ProductName, Revenue, rn AS Rnk\nFROM Ranked\nWHERE rn <= 2\nORDER BY Category, rn;",
  "Alternative: CROSS APPLY (SELECT TOP 2 ...) per category.")
q(X, "Gaps and islands", "For each customer, find their longest streak of consecutive calendar months in which they placed at least one order. Return the top 5 customers by streak length (customer name, streak length in months, streak start month).",
  ["Reduce to distinct (CustomerId, month number) first.", "Subtract ROW_NUMBER() from the month number - consecutive months share the same difference (the 'island' key)."],
  "WITH M AS (\n    SELECT DISTINCT CustomerId, DATEDIFF(MONTH, '2000-01-01', OrderDate) AS Mn\n    FROM Orders\n), Grp AS (\n    SELECT CustomerId, Mn,\n           Mn - ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY Mn) AS Island\n    FROM M\n), Streaks AS (\n    SELECT CustomerId, Island, COUNT(*) AS StreakLen, MIN(Mn) AS StartMn\n    FROM Grp\n    GROUP BY CustomerId, Island\n), Best AS (\n    SELECT *, ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY StreakLen DESC, StartMn) AS rn\n    FROM Streaks\n)\nSELECT TOP 5 c.CustomerName, b.StreakLen,\n       DATEADD(MONTH, b.StartMn, '2000-01-01') AS StreakStart\nFROM Best b\nJOIN Customers c ON c.CustomerId = b.CustomerId\nWHERE b.rn = 1\nORDER BY b.StreakLen DESC, c.CustomerName;",
  "Gaps-and-islands: value minus row number is constant inside a run of consecutive values.")
q(X, "Moving average", "Show monthly revenue (excluding Cancelled orders) with a 3-month moving average (current month and the 2 previous months), rounded to 2 decimals.",
  ["Aggregate to months in a CTE.", "AVG(Revenue) OVER (ORDER BY MonthStart ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)."],
  "WITH Monthly AS (\n    SELECT DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1) AS MonthStart,\n           SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue\n    FROM Orders o\n    JOIN OrderItems oi ON oi.OrderId = o.OrderId\n    WHERE o.Status <> 'Cancelled'\n    GROUP BY DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1)\n)\nSELECT MonthStart, Revenue,\n       ROUND(AVG(Revenue) OVER (ORDER BY MonthStart ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2) AS MovingAvg3\nFROM Monthly\nORDER BY MonthStart;",
  "The first two months average fewer than 3 rows. Months without orders would be missing - join to a calendar table if that matters.")

import importlib, hashlib, collections
for m in ("extra_easy", "extra_medium", "extra_hard", "extra_expert"):
    importlib.import_module(m).add(q)
DROP = ("List all foreign key constraints", "List employees whose hire date was a Monday", "Count orders per Status, showing a friendly label",
        "Show employee IDs formatted", "Return the 3rd to 6th", "List employees who earn more than every employee in the Marketing",
        "List products whose average ordered quantity")
Q[:] = [x for x in Q if not x["text"].startswith(DROP)]
order = {"Easy": 0, "Medium": 1, "Hard": 2, "Expert": 3}
Q.sort(key=lambda x: order[x["level"]])
assert len(Q) == 200, len(Q)
assert len({x["text"] for x in Q}) == 200
print(collections.Counter(x["level"] for x in Q))
for i, x in enumerate(Q, 1):
    x["id"] = i
    x["key"] = hashlib.sha1(x["answer"].encode("utf-8")).hexdigest()[:12]
assert len({x["key"] for x in Q}) == 200

_mp = os.path.join(OUT, "meta.json")
META = json.load(open(_mp, encoding="utf-8")) if os.path.exists(_mp) else {}
for x in Q:
    m = META.get(x["key"], {})
    x["tables"] = m.get("tables", [])
    x["returns"] = m.get("returns", [])
    x["ordering"] = m.get("ordering", "")

with open(os.path.join(OUT, "questions.json"), "w", encoding="utf-8") as f:
    json.dump(Q, f, indent=2, ensure_ascii=False)

schema = """## Database schema (PracticeDB)

| Table | Columns |
|---|---|
| Departments | DepartmentId, DepartmentName, Location |
| Employees | EmployeeId, FirstName, LastName, Email, DepartmentId, ManagerId, JobTitle, HireDate, Salary, CommissionPct |
| SalaryHistory | SalaryHistoryId, EmployeeId, EffectiveDate, Salary |
| Customers | CustomerId, CustomerName, Email, City, Country, SignupDate |
| Products | ProductId, ProductName, Category, UnitPrice, Stock |
| Orders | OrderId, CustomerId, EmployeeId (sales rep), OrderDate, Status |
| OrderItems | OrderItemId, OrderId, ProductId, Quantity, UnitPrice, Discount |

Revenue of a line = `Quantity * UnitPrice * (1 - Discount)`.
"""

def spec(x):
    s = ""
    if x.get("tables"):
        s += f"- Tables: {', '.join(x['tables'])}\n"
    if x.get("returns"):
        s += f"- Return columns (in this order): {', '.join(x['returns'])}\n"
    if x.get("ordering"):
        s += f"- Sorted by: {x['ordering']}\n"
    return s + "\n" if s else ""


with open(os.path.join(OUT, "questions.md"), "w", encoding="utf-8") as f:
    f.write("# SQL Server Interview Practice Questions\n\n" + schema + "\n")
    lvl = None
    for x in Q:
        if x["level"] != lvl:
            lvl = x["level"]; f.write(f"\n## {lvl}\n\n")
        f.write(f"**{x['id']}. [{x['topic']}]** {x['text']}\n\n")
        f.write(spec(x))

with open(os.path.join(OUT, "answers.md"), "w", encoding="utf-8") as f:
    f.write("# SQL Server Interview Practice Answers\n\n")
    lvl = None
    for x in Q:
        if x["level"] != lvl:
            lvl = x["level"]; f.write(f"\n## {lvl}\n\n")
        f.write(f"### {x['id']}. [{x['topic']}] {x['text']}\n\n")
        f.write("Hints:\n" + "".join(f"{i}. {h}\n" for i, h in enumerate(x["hints"], 1)) + "\n")
        f.write("```sql\n" + x["answer"] + "\n```\n\n")
        f.write(f"**Explanation:** {x['explanation']}\n\n")

with open(os.path.join(OUT, "sql", "answers.sql"), "w", encoding="utf-8") as f:
    f.write("USE PracticeDB;\nGO\n")
    for x in Q:
        f.write(f"\nPRINT 'Q{x['id']}';\n{x['answer']}\nGO\n")
print("ok", len(Q))
