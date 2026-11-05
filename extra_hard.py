REV = "oi.Quantity * oi.UnitPrice * (1 - oi.Discount)"
# Order-level totals reused by many answers
OT = "SELECT o.OrderId, o.CustomerId, o.OrderDate, o.Status, SUM(" + REV + ") AS Total\n    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId\n    GROUP BY o.OrderId, o.CustomerId, o.OrderDate, o.Status"
MONTHLY = ("SELECT DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1) AS MonthStart, SUM(" + REV + ") AS Revenue\n"
           "    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId\n    WHERE o.Status <> 'Cancelled'\n"
           "    GROUP BY DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1)")


def add(q0):
    def q(l, t, x, h, s, w):
        q0(l, t, x, h, s.replace("@R@", REV).replace("@OT@", OT).replace("@MONTHLY@", MONTHLY), w)

    H = "Hard"
    q(H, "NTILE", "Split employees into 4 salary quartiles (1 = highest paid). Show name, salary and quartile. Break salary ties by EmployeeId.",
      ["NTILE(4) OVER (ORDER BY Salary DESC, EmployeeId)."],
      "SELECT FirstName, LastName, Salary,\n       NTILE(4) OVER (ORDER BY Salary DESC, EmployeeId) AS Quartile\nFROM Employees;",
      "NTILE distributes rows into near-equal buckets; with 40 rows each bucket has 10.")
    q(H, "LEAD", "For customer 1, list each order date and the number of days until their next order (NULL for the last).",
      ["LEAD(OrderDate) OVER (ORDER BY OrderDate)."],
      "SELECT OrderId, OrderDate,\n       DATEDIFF(DAY, OrderDate, LEAD(OrderDate) OVER (ORDER BY OrderDate)) AS DaysToNext\nFROM Orders\nWHERE CustomerId = 1;",
      "The WHERE clause is applied before the window function, so LEAD sees only customer 1's rows.")
    q(H, "FIRST_VALUE", "Show every employee with the name of the highest-paid person in their department (employees with a department only).",
      ["FIRST_VALUE(name) OVER (PARTITION BY DepartmentId ORDER BY Salary DESC)."],
      "SELECT FirstName, LastName, DepartmentId, Salary,\n       FIRST_VALUE(FirstName) OVER (PARTITION BY DepartmentId ORDER BY Salary DESC, EmployeeId) AS TopEarner\nFROM Employees\nWHERE DepartmentId IS NOT NULL;",
      "Add a tie-breaker to the window ORDER BY so the result is deterministic.")
    q(H, "Running total", "For customer 5, list orders with a running count of orders so far and a running total of order value (by order date).",
      ["Build order totals in a CTE, then use SUM() OVER with ROWS."],
      "WITH OT AS (\n    @OT@\n)\nSELECT OrderId, OrderDate, Total,\n       ROW_NUMBER() OVER (ORDER BY OrderDate) AS OrderNo,\n       SUM(Total) OVER (ORDER BY OrderDate ROWS UNBOUNDED PRECEDING) AS RunningTotal\nFROM OT\nWHERE CustomerId = 5;",
      "Dates are unique per order, so the running window is unambiguous.")
    q(H, "Window SUM", "Show each employee's salary as a percentage of their department's total salary (2 decimals). Only employees with a department.",
      ["SUM(Salary) OVER (PARTITION BY DepartmentId)."],
      "SELECT FirstName, LastName, DepartmentId, Salary,\n       ROUND(100.0 * Salary / SUM(Salary) OVER (PARTITION BY DepartmentId), 2) AS PctOfDept\nFROM Employees\nWHERE DepartmentId IS NOT NULL;",
      "Window aggregates avoid a self join with a GROUP BY subquery.")
    q(H, "PERCENT_RANK", "Show each employee's PERCENT_RANK of salary across the company (rounded to 3 decimals).",
      ["PERCENT_RANK() OVER (ORDER BY Salary)."],
      "SELECT FirstName, LastName, Salary,\n       ROUND(PERCENT_RANK() OVER (ORDER BY Salary), 3) AS PctRank\nFROM Employees;",
      "PERCENT_RANK = (rank - 1) / (rows - 1); the lowest value is 0.")
    q(H, "CUME_DIST", "Show each employee's cumulative distribution of salary (rounded to 3 decimals) across the company.",
      ["CUME_DIST() OVER (ORDER BY Salary)."],
      "SELECT FirstName, LastName, Salary,\n       ROUND(CUME_DIST() OVER (ORDER BY Salary), 3) AS CumeDist\nFROM Employees;",
      "CUME_DIST = share of rows with value <= current, so the maximum is 1.")
    q(H, "Window AVG", "Show each employee's salary, their department average and the difference from it (employees with a department).",
      ["AVG(Salary) OVER (PARTITION BY DepartmentId)."],
      "SELECT FirstName, LastName, DepartmentId, Salary,\n       AVG(Salary) OVER (PARTITION BY DepartmentId) AS DeptAvg,\n       Salary - AVG(Salary) OVER (PARTITION BY DepartmentId) AS Diff\nFROM Employees\nWHERE DepartmentId IS NOT NULL;",
      "You cannot reference the alias DeptAvg in the same SELECT list.")
    q(H, "CTE", "Using a CTE, list customers whose total revenue is above the average customer revenue.",
      ["CTE of revenue per customer, compare to its AVG."],
      "WITH CustRev AS (\n    SELECT o.CustomerId, SUM(@R@) AS Revenue\n    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId\n    GROUP BY o.CustomerId\n)\nSELECT c.CustomerName, cr.Revenue\nFROM CustRev cr JOIN Customers c ON c.CustomerId = cr.CustomerId\nWHERE cr.Revenue > (SELECT AVG(Revenue) FROM CustRev);",
      "Customers without orders are not in the average, which is usually what is wanted.")
    q(H, "DENSE_RANK", "Return the top 5 revenue-ranked products (DENSE_RANK on total revenue, highest = 1).",
      ["CTE with SUM then DENSE_RANK; filter <= 5."],
      "WITH P AS (\n    SELECT p.ProductName, SUM(@R@) AS Revenue\n    FROM OrderItems oi JOIN Products p ON p.ProductId = oi.ProductId\n    GROUP BY p.ProductId, p.ProductName\n)\nSELECT ProductName, Revenue, DENSE_RANK() OVER (ORDER BY Revenue DESC) AS Rnk\nFROM P\nORDER BY Rnk\nOFFSET 0 ROWS FETCH NEXT 5 ROWS ONLY;",
      "Revenue totals are distinct so DENSE_RANK equals ROW_NUMBER here; you can filter in an outer query too.")
    q(H, "Recursive CTE", "Generate the numbers 1 to 10 with a recursive CTE.",
      ["Anchor SELECT 1, recursive part n + 1 WHERE n < 10."],
      "WITH Nums AS (\n    SELECT 1 AS n\n    UNION ALL\n    SELECT n + 1 FROM Nums WHERE n < 10\n)\nSELECT n FROM Nums;",
      "Always include a termination condition; MAXRECURSION defaults to 100.")
    q(H, "Recursive CTE", "List every direct and indirect subordinate of Grace Ong (EmployeeId 7): id, name and level below Grace.",
      ["Anchor: direct reports of 7 at level 1."],
      "WITH Sub AS (\n    SELECT EmployeeId, FirstName, LastName, 1 AS Level FROM Employees WHERE ManagerId = 7\n    UNION ALL\n    SELECT e.EmployeeId, e.FirstName, e.LastName, s.Level + 1\n    FROM Employees e JOIN Sub s ON e.ManagerId = s.EmployeeId\n)\nSELECT EmployeeId, FirstName + ' ' + LastName AS Name, Level FROM Sub;",
      "Grace's team has no managers below her, so all rows are at level 1.")
    q(H, "Recursive CTE", "How many people (direct and indirect) report up to Carol Wong (EmployeeId 3)?",
      ["Recursive CTE from ManagerId = 3, then COUNT(*)."],
      "WITH Sub AS (\n    SELECT EmployeeId FROM Employees WHERE ManagerId = 3\n    UNION ALL\n    SELECT e.EmployeeId FROM Employees e JOIN Sub s ON e.ManagerId = s.EmployeeId\n)\nSELECT COUNT(*) AS TotalReports FROM Sub;",
      "Counts the whole subtree below the root.")
    q(H, "Recursive CTE", "Produce one row per day of January 2024 with the number of orders on that day (0 if none).",
      ["Generate dates recursively, then LEFT JOIN Orders."],
      "WITH D AS (\n    SELECT CAST('2024-01-01' AS DATE) AS d\n    UNION ALL\n    SELECT DATEADD(DAY, 1, d) FROM D WHERE d < '2024-01-31'\n)\nSELECT D.d AS OrderDay, COUNT(o.OrderId) AS Orders\nFROM D LEFT JOIN Orders o ON o.OrderDate = D.d\nGROUP BY D.d\nORDER BY D.d;",
      "A calendar CTE fills gaps that a plain GROUP BY would miss.")
    q(H, "Recursive CTE", "What is the maximum depth (levels below the CEO) of the organisation hierarchy, and how many employees are at each level?",
      ["Recursive CTE from the CEO with a Level column, then GROUP BY Level."],
      "WITH Org AS (\n    SELECT EmployeeId, 0 AS Level FROM Employees WHERE ManagerId IS NULL AND EmployeeId = 1\n    UNION ALL\n    SELECT e.EmployeeId, o.Level + 1 FROM Employees e JOIN Org o ON e.ManagerId = o.EmployeeId\n)\nSELECT Level, COUNT(*) AS Employees FROM Org GROUP BY Level ORDER BY Level;",
      "The maximum depth is the highest Level value returned.")
    q(H, "CROSS APPLY", "For each customer, show their 2 most recent orders (customer, order id, order date).",
      ["CROSS APPLY (SELECT TOP 2 ... ORDER BY OrderDate DESC)."],
      "SELECT c.CustomerName, x.OrderId, x.OrderDate\nFROM Customers c\nCROSS APPLY (SELECT TOP 2 o.OrderId, o.OrderDate FROM Orders o WHERE o.CustomerId = c.CustomerId ORDER BY o.OrderDate DESC) x;",
      "CROSS APPLY drops customers with no orders; OUTER APPLY keeps them.")
    q(H, "OUTER APPLY", "List all customers with the date of their most recent order (NULL if none).",
      ["OUTER APPLY with TOP 1."],
      "SELECT c.CustomerName, x.OrderDate AS LastOrderDate\nFROM Customers c\nOUTER APPLY (SELECT TOP 1 o.OrderDate FROM Orders o WHERE o.CustomerId = c.CustomerId ORDER BY o.OrderDate DESC) x;",
      "A simpler alternative is LEFT JOIN with MAX(OrderDate).")
    q(H, "PIVOT", "Show the number of orders per year (rows) split by Status (columns Delivered, Shipped, Pending, Cancelled).",
      ["Select Year and Status first, then PIVOT(COUNT(Status) FOR Status IN (...))."],
      "SELECT Yr, [Delivered], [Shipped], [Pending], [Cancelled]\nFROM (SELECT YEAR(OrderDate) AS Yr, Status FROM Orders) s\nPIVOT (COUNT(Status) FOR Status IN ([Delivered], [Shipped], [Pending], [Cancelled])) p\nORDER BY Yr;",
      "Non-pivoted columns in the source become the grouping columns.")
    q(H, "UNPIVOT", "Show the salary statistics (minimum, maximum, average) of Employees as three rows: Stat and Value.",
      ["Compute the stats in one row, cast them to one type, and UNPIVOT."],
      "SELECT Stat, Value\nFROM (SELECT CAST(MIN(Salary) AS DECIMAL(12,2)) AS Minimum, CAST(MAX(Salary) AS DECIMAL(12,2)) AS Maximum, CAST(AVG(Salary) AS DECIMAL(12,2)) AS Average FROM Employees) s\nUNPIVOT (Value FOR Stat IN (Minimum, Maximum, Average)) u;",
      "UNPIVOT requires all columns to share one data type.")
    q(H, "Conditional aggregation", "For each department show the number of employees earning at least 100,000 and the number earning less.",
      ["SUM(CASE WHEN ... THEN 1 ELSE 0 END)."],
      "SELECT d.DepartmentName,\n       SUM(CASE WHEN e.Salary >= 100000 THEN 1 ELSE 0 END) AS HighEarners,\n       SUM(CASE WHEN e.Salary <  100000 THEN 1 ELSE 0 END) AS Others\nFROM Departments d JOIN Employees e ON e.DepartmentId = d.DepartmentId\nGROUP BY d.DepartmentName;",
      "Conditional aggregation produces several counts in one scan.")
    q(H, "Relational division", "Which customers have bought products from every product category?",
      ["Count distinct categories per customer and compare with the total number of categories."],
      "SELECT c.CustomerName\nFROM Customers c\nJOIN Orders o ON o.CustomerId = c.CustomerId\nJOIN OrderItems oi ON oi.OrderId = o.OrderId\nJOIN Products p ON p.ProductId = oi.ProductId\nGROUP BY c.CustomerId, c.CustomerName\nHAVING COUNT(DISTINCT p.Category) = (SELECT COUNT(DISTINCT Category) FROM Products);",
      "This 'for all' pattern is called relational division.")
    q(H, "INTERSECT", "Which customers placed orders in both 2023 and 2025? (customer id)",
      ["INTERSECT two queries filtered by year."],
      "SELECT CustomerId FROM Orders WHERE YEAR(OrderDate) = 2023\nINTERSECT\nSELECT CustomerId FROM Orders WHERE YEAR(OrderDate) = 2025;",
      "Could also use two EXISTS clauses.")
    q(H, "EXCEPT", "Using EXCEPT, which customers (CustomerId) have never placed an order?",
      ["EXCEPT between all customer ids and customer ids that appear in Orders."],
      "SELECT CustomerId FROM Customers\nEXCEPT\nSELECT CustomerId FROM Orders;",
      "EXCEPT returns distinct rows from the left set not found in the right set; NOT EXISTS is an equivalent alternative.")
    q(H, "LAG", "Show monthly revenue (non-cancelled orders) with the previous month's revenue and the % change (2 decimals).",
      ["Monthly CTE then LAG(Revenue) OVER (ORDER BY MonthStart)."],
      "WITH M AS (\n    @MONTHLY@\n)\nSELECT MonthStart, Revenue,\n       LAG(Revenue) OVER (ORDER BY MonthStart) AS PrevRevenue,\n       ROUND(100.0 * (Revenue - LAG(Revenue) OVER (ORDER BY MonthStart)) / LAG(Revenue) OVER (ORDER BY MonthStart), 2) AS PctChange\nFROM M\nORDER BY MonthStart;",
      "'Previous' means the previous month that has data, not necessarily the previous calendar month.")
    q(H, "LAG", "Show revenue per product category per year together with the previous year's revenue for the same category.",
      ["PARTITION BY Category ORDER BY Yr in LAG."],
      "WITH CY AS (\n    SELECT p.Category, YEAR(o.OrderDate) AS Yr, SUM(@R@) AS Revenue\n    FROM OrderItems oi\n    JOIN Orders o ON o.OrderId = oi.OrderId\n    JOIN Products p ON p.ProductId = oi.ProductId\n    GROUP BY p.Category, YEAR(o.OrderDate)\n)\nSELECT Category, Yr, Revenue,\n       LAG(Revenue) OVER (PARTITION BY Category ORDER BY Yr) AS PrevYearRevenue\nFROM CY;",
      "PARTITION BY restarts the LAG for each category.")
    q(H, "Self join", "List employees who earn at least 80% of their manager's salary.",
      ["Self join and compare e.Salary with 0.8 * m.Salary."],
      "SELECT e.FirstName, e.LastName, e.Salary, m.FirstName AS Manager, m.Salary AS ManagerSalary\nFROM Employees e JOIN Employees m ON m.EmployeeId = e.ManagerId\nWHERE e.Salary >= 0.8 * m.Salary;",
      "Self joins compare an employee to their manager; employees without a manager drop out of the inner join.")
    q(H, "ALL", "List employees who earn more than every employee in the Marketing department (DepartmentId 4).",
      ["> ALL (subquery) or > (SELECT MAX(...))."],
      "SELECT FirstName, LastName, Salary\nFROM Employees\nWHERE Salary > ALL (SELECT Salary FROM Employees WHERE DepartmentId = 4);",
      "ALL compares against every value; if the subquery is empty the condition is true.")
    q(H, "HAVING", "List departments whose average salary is higher than the company-wide average salary.",
      ["HAVING AVG(...) > (SELECT AVG(...))."],
      "SELECT d.DepartmentName, AVG(e.Salary) AS AvgSalary\nFROM Departments d JOIN Employees e ON e.DepartmentId = d.DepartmentId\nGROUP BY d.DepartmentName\nHAVING AVG(e.Salary) > (SELECT AVG(Salary) FROM Employees);",
      "A subquery is allowed inside HAVING.")
    q(H, "CTE", "List orders whose total value is higher than the average order value.",
      ["Order totals CTE and a scalar AVG subquery."],
      "WITH OT AS (\n    @OT@\n)\nSELECT OrderId, Total\nFROM OT\nWHERE Total > (SELECT AVG(Total) FROM OT);",
      "Reusing a CTE twice avoids repeating the aggregation text (though it is still evaluated twice).")
    q(H, "ROW_NUMBER", "Show each customer's second most recent order (customer, order id, order date).",
      ["ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY OrderDate DESC) = 2."],
      "WITH R AS (\n    SELECT CustomerId, OrderId, OrderDate,\n           ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY OrderDate DESC) AS rn\n    FROM Orders\n)\nSELECT c.CustomerName, R.OrderId, R.OrderDate\nFROM R JOIN Customers c ON c.CustomerId = R.CustomerId\nWHERE R.rn = 2;",
      "Customers with fewer than 2 orders do not appear.")
    q(H, "DATEDIFF", "For each customer show the number of days between their first and last order.",
      ["MIN and MAX of OrderDate with DATEDIFF."],
      "SELECT c.CustomerName, DATEDIFF(DAY, MIN(o.OrderDate), MAX(o.OrderDate)) AS SpanDays\nFROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId\nGROUP BY c.CustomerId, c.CustomerName;",
      "Aggregates can be nested inside scalar functions like DATEDIFF.")
    q(H, "LAG", "For each customer, compute the average number of days between consecutive orders (1 decimal).",
      ["LAG in a CTE to compute gaps, then AVG by customer."],
      "WITH G AS (\n    SELECT CustomerId, DATEDIFF(DAY, LAG(OrderDate) OVER (PARTITION BY CustomerId ORDER BY OrderDate), OrderDate) AS Gap\n    FROM Orders\n)\nSELECT c.CustomerName, ROUND(AVG(G.Gap * 1.0), 1) AS AvgGapDays\nFROM G JOIN Customers c ON c.CustomerId = G.CustomerId\nGROUP BY c.CustomerId, c.CustomerName;",
      "AVG ignores the NULL gap of each customer's first order.")
    q(H, "Running total", "Show employees ordered by hire date (EmployeeId as tie-break) with a running headcount.",
      ["COUNT(*) OVER (ORDER BY HireDate, EmployeeId ROWS UNBOUNDED PRECEDING)."],
      "SELECT FirstName, LastName, HireDate,\n       COUNT(*) OVER (ORDER BY HireDate, EmployeeId ROWS UNBOUNDED PRECEDING) AS Headcount\nFROM Employees;",
      "Equivalent to ROW_NUMBER in this case.")
    q(H, "DENSE_RANK", "Within each customer country, show the customer(s) with the highest total revenue.",
      ["CTE of revenue per customer, then RANK partitioned by Country."],
      "WITH CR AS (\n    SELECT c.CustomerName, c.Country, SUM(@R@) AS Revenue\n    FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId\n    GROUP BY c.CustomerId, c.CustomerName, c.Country\n), R AS (\n    SELECT *, RANK() OVER (PARTITION BY Country ORDER BY Revenue DESC) AS rnk FROM CR\n)\nSELECT Country, CustomerName, Revenue FROM R WHERE rnk = 1;",
      "RANK keeps ties; ROW_NUMBER would drop them.")
    q(H, "Cumulative share", "List products by revenue (highest first) with each product's share of total revenue and the cumulative share (2 decimals).",
      ["SUM(Revenue) OVER () for the total and a running SUM for cumulative."],
      "WITH P AS (\n    SELECT p.ProductId, p.ProductName, SUM(@R@) AS Revenue\n    FROM OrderItems oi JOIN Products p ON p.ProductId = oi.ProductId\n    GROUP BY p.ProductId, p.ProductName\n)\nSELECT ProductName, Revenue,\n       ROUND(100.0 * Revenue / SUM(Revenue) OVER (), 2) AS SharePct,\n       ROUND(100.0 * SUM(Revenue) OVER (ORDER BY Revenue DESC, ProductId ROWS UNBOUNDED PRECEDING) / SUM(Revenue) OVER (), 2) AS CumulativePct\nFROM P\nORDER BY Revenue DESC;",
      "This is the basis of a Pareto (80/20) analysis.")
    q(H, "Window SUM", "For each product, show its revenue and its percentage of its own category's revenue (2 decimals).",
      ["SUM(Revenue) OVER (PARTITION BY Category)."],
      "WITH P AS (\n    SELECT p.Category, p.ProductName, SUM(@R@) AS Revenue\n    FROM OrderItems oi JOIN Products p ON p.ProductId = oi.ProductId\n    GROUP BY p.ProductId, p.Category, p.ProductName\n)\nSELECT Category, ProductName, Revenue,\n       ROUND(100.0 * Revenue / SUM(Revenue) OVER (PARTITION BY Category), 2) AS PctOfCategory\nFROM P;",
      "A window function can aggregate over the grouped result of the CTE.")
    q(H, "Subquery", "For each customer country, show total revenue and the revenue of its single biggest order.",
      ["Order totals CTE joined to customers."],
      "WITH OT AS (\n    @OT@\n)\nSELECT c.Country, SUM(OT.Total) AS Revenue, MAX(OT.Total) AS BiggestOrder\nFROM OT JOIN Customers c ON c.CustomerId = OT.CustomerId\nGROUP BY c.Country;",
      "Aggregate in layers: order totals first, then by country.")
    q(H, "RANK", "Rank sales reps by total revenue of their orders (RANK, highest = 1). Ignore orders without a rep.",
      ["Join Orders to Employees and RANK() OVER (ORDER BY SUM(...) DESC)."],
      "SELECT e.FirstName, e.LastName, SUM(@R@) AS Revenue,\n       RANK() OVER (ORDER BY SUM(@R@) DESC) AS Rnk\nFROM Orders o\nJOIN OrderItems oi ON oi.OrderId = o.OrderId\nJOIN Employees e ON e.EmployeeId = o.EmployeeId\nGROUP BY e.EmployeeId, e.FirstName, e.LastName;",
      "Window functions can be applied on top of aggregates in the same SELECT.")
    q(H, "Conditional aggregation", "Show revenue per year (rows) with columns Q1, Q2, Q3, Q4 (non-cancelled orders).",
      ["SUM(CASE WHEN DATEPART(QUARTER, OrderDate) = 1 THEN ... END)."],
      "SELECT YEAR(o.OrderDate) AS Yr,\n       SUM(CASE WHEN DATEPART(QUARTER, o.OrderDate) = 1 THEN @R@ ELSE 0 END) AS Q1,\n       SUM(CASE WHEN DATEPART(QUARTER, o.OrderDate) = 2 THEN @R@ ELSE 0 END) AS Q2,\n       SUM(CASE WHEN DATEPART(QUARTER, o.OrderDate) = 3 THEN @R@ ELSE 0 END) AS Q3,\n       SUM(CASE WHEN DATEPART(QUARTER, o.OrderDate) = 4 THEN @R@ ELSE 0 END) AS Q4\nFROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId\nWHERE o.Status <> 'Cancelled'\nGROUP BY YEAR(o.OrderDate)\nORDER BY Yr;",
      "A manual pivot is more flexible than PIVOT when you need computed values.")
    q(H, "ROW_NUMBER", "For each employee, show their first and their latest salary from SalaryHistory and the percentage growth (1 decimal).",
      ["MIN/MAX with first/last rows, or FIRST_VALUE with a window frame."],
      "WITH S AS (\n    SELECT EmployeeId, Salary,\n           ROW_NUMBER() OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate) AS rn_asc,\n           ROW_NUMBER() OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate DESC) AS rn_desc\n    FROM SalaryHistory\n)\nSELECT a.EmployeeId, a.Salary AS FirstSalary, d.Salary AS LatestSalary,\n       ROUND(100.0 * (d.Salary - a.Salary) / a.Salary, 1) AS GrowthPct\nFROM S a JOIN S d ON d.EmployeeId = a.EmployeeId AND d.rn_desc = 1\nWHERE a.rn_asc = 1;",
      "Two row numbers (ascending and descending) pick the first and last rows.")
    q(H, "Window COUNT", "List all employees whose last name is shared with at least one other employee (show all of them).",
      ["COUNT(*) OVER (PARTITION BY LastName) > 1 in a CTE."],
      "WITH L AS (\n    SELECT EmployeeId, FirstName, LastName, COUNT(*) OVER (PARTITION BY LastName) AS Cnt FROM Employees\n)\nSELECT EmployeeId, FirstName, LastName FROM L WHERE Cnt > 1;",
      "Unlike GROUP BY, the window approach keeps the detail rows.")
    q(H, "ROW_NUMBER", "Show the employees that would be removed when de-duplicating on (Salary, HireDate), keeping the lowest EmployeeId of each group.",
      ["ROW_NUMBER() OVER (PARTITION BY Salary, HireDate ORDER BY EmployeeId) > 1."],
      "WITH D AS (\n    SELECT EmployeeId, FirstName, LastName, Salary, HireDate,\n           ROW_NUMBER() OVER (PARTITION BY Salary, HireDate ORDER BY EmployeeId) AS rn\n    FROM Employees\n)\nSELECT EmployeeId, FirstName, LastName FROM D WHERE rn > 1;",
      "To actually delete, DELETE directly from the CTE.")
    q(H, "PERCENTILE_CONT", "What is the median salary of all employees?",
      ["PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Salary) OVER ()."],
      "SELECT DISTINCT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Salary) OVER () AS MedianSalary\nFROM Employees;",
      "In T-SQL PERCENTILE_CONT is an analytic function and needs OVER; DISTINCT collapses the repeated value.")
    q(H, "PERCENTILE_CONT", "What is the median salary in each department (employees with a department)?",
      ["PARTITION BY DepartmentId inside OVER."],
      "SELECT DISTINCT DepartmentId,\n       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Salary) OVER (PARTITION BY DepartmentId) AS MedianSalary\nFROM Employees\nWHERE DepartmentId IS NOT NULL;",
      "For an even number of rows the median is the average of the two middle values.")
    q(H, "LAG", "What is the longest gap in days between two consecutive orders of the same customer? Show customer name and gap for each customer's longest gap.",
      ["LAG for gaps, MAX per customer."],
      "WITH G AS (\n    SELECT CustomerId, DATEDIFF(DAY, LAG(OrderDate) OVER (PARTITION BY CustomerId ORDER BY OrderDate), OrderDate) AS Gap\n    FROM Orders\n)\nSELECT c.CustomerName, MAX(G.Gap) AS LongestGap\nFROM G JOIN Customers c ON c.CustomerId = G.CustomerId\nGROUP BY c.CustomerId, c.CustomerName;",
      "MAX ignores the first-order NULL.")
    q(H, "STRING_AGG", "For each department list the distinct job titles as a comma-separated, alphabetical string.",
      ["Get DISTINCT pairs in a subquery, then STRING_AGG."],
      "SELECT d.DepartmentName, STRING_AGG(t.JobTitle, ', ') WITHIN GROUP (ORDER BY t.JobTitle) AS Titles\nFROM Departments d\nJOIN (SELECT DISTINCT DepartmentId, JobTitle FROM Employees) t ON t.DepartmentId = d.DepartmentId\nGROUP BY d.DepartmentName;",
      "STRING_AGG has no DISTINCT option, hence the derived table.")
    q(H, "Window AVG", "For each customer show their total revenue and the average revenue of customers in the same country.",
      ["AVG(Revenue) OVER (PARTITION BY Country)."],
      "WITH CR AS (\n    SELECT c.CustomerName, c.Country, SUM(@R@) AS Revenue\n    FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId\n    GROUP BY c.CustomerId, c.CustomerName, c.Country\n)\nSELECT CustomerName, Country, Revenue,\n       AVG(Revenue) OVER (PARTITION BY Country) AS CountryAvg\nFROM CR;",
      "Window functions run after GROUP BY, so they can use the grouped result.")
    q(H, "GROUP BY", "How many orders did customers place in the same year they signed up? Show customer name and count (customers with at least one).",
      ["Join on YEAR(OrderDate) = YEAR(SignupDate)."],
      "SELECT c.CustomerName, COUNT(*) AS Orders\nFROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId AND YEAR(o.OrderDate) = YEAR(c.SignupDate)\nGROUP BY c.CustomerId, c.CustomerName;",
      "Join conditions may contain expressions, not only column equality.")
    q(H, "ROW_NUMBER", "For every order show its most expensive line item (product name and unit price).",
      ["ROW_NUMBER() OVER (PARTITION BY OrderId ORDER BY UnitPrice DESC) = 1."],
      "WITH R AS (\n    SELECT oi.OrderId, oi.ProductId, oi.UnitPrice,\n           ROW_NUMBER() OVER (PARTITION BY oi.OrderId ORDER BY oi.UnitPrice DESC) AS rn\n    FROM OrderItems oi\n)\nSELECT R.OrderId, p.ProductName, R.UnitPrice\nFROM R JOIN Products p ON p.ProductId = R.ProductId\nWHERE R.rn = 1;",
      "Top-1 per group is one of the most common window function patterns.")
    q(H, "HAVING", "Which customers spent more in total than 'Acme Corp'?",
      ["HAVING SUM(...) > (subquery for Acme)."],
      "SELECT c.CustomerName, SUM(@R@) AS Revenue\nFROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId\nGROUP BY c.CustomerId, c.CustomerName\nHAVING SUM(@R@) > (\n    SELECT SUM(@R@) FROM Customers c2 JOIN Orders o ON o.CustomerId = c2.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId\n    WHERE c2.CustomerName = 'Acme Corp');",
      "The inner query reuses the aliases because it is not correlated.")
    q(H, "EXISTS", "Find customers who have both a Cancelled order and a Delivered order.",
      ["Two EXISTS conditions."],
      "SELECT c.CustomerName\nFROM Customers c\nWHERE EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerId = c.CustomerId AND o.Status = 'Cancelled')\n  AND EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerId = c.CustomerId AND o.Status = 'Delivered');",
      "Each EXISTS is independent, so there is no row multiplication.")
    q(H, "HAVING", "Which sales reps sold to more than 5 distinct customers?",
      ["COUNT(DISTINCT CustomerId) in HAVING."],
      "SELECT e.FirstName, e.LastName, COUNT(DISTINCT o.CustomerId) AS Customers\nFROM Orders o JOIN Employees e ON e.EmployeeId = o.EmployeeId\nGROUP BY e.EmployeeId, e.FirstName, e.LastName\nHAVING COUNT(DISTINCT o.CustomerId) > 5;",
      "Same pattern with a threshold.")
    q(H, "Self join", "Find pairs of products that appear together in at least 3 orders (product names, number of shared orders).",
      ["Self join OrderItems on OrderId with a.ProductId < b.ProductId."],
      "SELECT p1.ProductName AS ProductA, p2.ProductName AS ProductB, COUNT(*) AS Together\nFROM OrderItems a\nJOIN OrderItems b ON b.OrderId = a.OrderId AND a.ProductId < b.ProductId\nJOIN Products p1 ON p1.ProductId = a.ProductId\nJOIN Products p2 ON p2.ProductId = b.ProductId\nGROUP BY p1.ProductName, p2.ProductName\nHAVING COUNT(*) >= 3;",
      "Basket analysis / market-basket pairs.")
    q(H, "ROW_NUMBER", "For each year, which month had the highest non-cancelled revenue? (year, month start, revenue)",
      ["Monthly CTE, ROW_NUMBER() OVER (PARTITION BY YEAR(MonthStart) ORDER BY Revenue DESC)."],
      "WITH M AS (\n    @MONTHLY@\n), R AS (\n    SELECT *, ROW_NUMBER() OVER (PARTITION BY YEAR(MonthStart) ORDER BY Revenue DESC) AS rn FROM M\n)\nSELECT YEAR(MonthStart) AS Yr, MonthStart, Revenue FROM R WHERE rn = 1;",
      "Partitioning by a year expression is allowed.")
    q(H, "PERCENTILE_CONT", "List employees who earn above the 90th percentile of salaries.",
      ["Compute PERCENTILE_CONT(0.9) in a CTE and compare."],
      "WITH P AS (\n    SELECT DISTINCT PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY Salary) OVER () AS P90 FROM Employees\n)\nSELECT e.FirstName, e.LastName, e.Salary\nFROM Employees e CROSS JOIN P\nWHERE e.Salary > P.P90;",
      "Continuous percentiles interpolate between values.")
    q(H, "OFFSET FETCH", "Return the 3rd to 6th most expensive products (use OFFSET/FETCH).",
      ["ORDER BY UnitPrice DESC OFFSET 2 ROWS FETCH NEXT 4 ROWS ONLY."],
      "SELECT ProductName, UnitPrice\nFROM Products\nORDER BY UnitPrice DESC\nOFFSET 2 ROWS FETCH NEXT 4 ROWS ONLY;",
      "OFFSET skips rows, FETCH limits the rest.")
    q(H, "CASE", "Show for each employee whether they are a 'Manager' (has direct reports) or 'Individual Contributor', using a single query without GROUP BY.",
      ["CASE WHEN EXISTS (...) THEN ... END."],
      "SELECT e.FirstName, e.LastName,\n       CASE WHEN EXISTS (SELECT 1 FROM Employees r WHERE r.ManagerId = e.EmployeeId) THEN 'Manager' ELSE 'Individual Contributor' END AS Role\nFROM Employees e;",
      "EXISTS can be used inside a CASE expression.")
    q(H, "Window MAX", "For each order, show the total and the customer's largest order total for comparison, only for orders that are the customer's largest.",
      ["MAX(Total) OVER (PARTITION BY CustomerId) = Total."],
      "WITH OT AS (\n    @OT@\n), M AS (\n    SELECT *, MAX(Total) OVER (PARTITION BY CustomerId) AS MaxTotal FROM OT\n)\nSELECT OrderId, CustomerId, Total FROM M WHERE Total = MaxTotal;",
      "Equivalent to a top-1 per group but keeps ties.")
    q(H, "Subquery", "List products whose average ordered quantity per line is above the overall average quantity per line.",
      ["Compare AVG(Quantity) per product with a scalar AVG subquery."],
      "SELECT p.ProductName, AVG(oi.Quantity * 1.0) AS AvgQty\nFROM OrderItems oi JOIN Products p ON p.ProductId = oi.ProductId\nGROUP BY p.ProductId, p.ProductName\nHAVING AVG(oi.Quantity * 1.0) > (SELECT AVG(Quantity * 1.0) FROM OrderItems);",
      "Multiply by 1.0 to avoid integer AVG.")
    q(H, "NOT EXISTS", "Which sales reps (employees with orders) have never handled a Cancelled order?",
      ["Reps appear in Orders; NOT EXISTS for cancelled ones."],
      "SELECT e.FirstName, e.LastName\nFROM Employees e\nWHERE EXISTS (SELECT 1 FROM Orders o WHERE o.EmployeeId = e.EmployeeId)\n  AND NOT EXISTS (SELECT 1 FROM Orders o WHERE o.EmployeeId = e.EmployeeId AND o.Status = 'Cancelled');",
      "Combine EXISTS and NOT EXISTS for 'has X but never Y'.")
