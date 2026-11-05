REV = "oi.Quantity * oi.UnitPrice * (1 - oi.Discount)"
OT = "SELECT o.OrderId, o.CustomerId, o.OrderDate, o.Status, SUM(" + REV + ") AS Total\n    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId\n    GROUP BY o.OrderId, o.CustomerId, o.OrderDate, o.Status"
MONTHLY = ("SELECT DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1) AS MonthStart, SUM(" + REV + ") AS Revenue\n"
           "    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId\n    WHERE o.Status <> 'Cancelled'\n"
           "    GROUP BY DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1)")


def add(q0):
    def q(l, t, x, h, s, w):
        q0(l, t, x, h, s.replace("@R@", REV).replace("@OT@", OT).replace("@MONTHLY@", MONTHLY), w)

    X = "Expert"
    q(X, "Calendar gaps", "List every date in Q1 2024 (1 Jan - 31 Mar) on which no order was placed.",
      ["Build a calendar with a recursive CTE.", "Anti-join to Orders."],
      "WITH D AS (\n    SELECT CAST('2024-01-01' AS DATE) AS d\n    UNION ALL\n    SELECT DATEADD(DAY, 1, d) FROM D WHERE d < '2024-03-31'\n)\nSELECT d AS EmptyDay\nFROM D\nWHERE NOT EXISTS (SELECT 1 FROM Orders o WHERE o.OrderDate = D.d)\nOPTION (MAXRECURSION 400);",
      "Finding missing dates requires generating the full list first.")
    q(X, "Gaps and islands", "Find runs of consecutive calendar days that all have at least one order. Return start date, end date and length for runs of 2 or more days.",
      ["Distinct dates, then date minus ROW_NUMBER days gives a constant per island."],
      "WITH Dd AS (SELECT DISTINCT OrderDate AS d FROM Orders),\nG AS (\n    SELECT d, DATEADD(DAY, -ROW_NUMBER() OVER (ORDER BY d), d) AS grp FROM Dd\n)\nSELECT MIN(d) AS StartDate, MAX(d) AS EndDate, COUNT(*) AS Days\nFROM G\nGROUP BY grp\nHAVING COUNT(*) >= 2;",
      "Subtracting the row number from the date makes consecutive days share the same value.")
    q(X, "Window SUM", "For each customer and year, list their orders with a running total of order value that restarts every year.",
      ["Order totals CTE; SUM() OVER (PARTITION BY CustomerId, YEAR(OrderDate) ORDER BY OrderDate ROWS UNBOUNDED PRECEDING)."],
      "WITH OT AS (\n    @OT@\n)\nSELECT CustomerId, OrderId, OrderDate, Total,\n       SUM(Total) OVER (PARTITION BY CustomerId, YEAR(OrderDate) ORDER BY OrderDate ROWS UNBOUNDED PRECEDING) AS YtdTotal\nFROM OT;",
      "PARTITION BY resets the running window, here per customer per year.")
    q(X, "Retention", "How many customers ordered in 2023 and again in 2024 (retained), and what percentage of 2023 customers is that (1 decimal)?",
      ["Sets of customers by year; COUNT the intersection."],
      "WITH A AS (SELECT DISTINCT CustomerId FROM Orders WHERE YEAR(OrderDate) = 2023),\n     B AS (SELECT DISTINCT CustomerId FROM Orders WHERE YEAR(OrderDate) = 2024)\nSELECT COUNT(B.CustomerId) AS Retained,\n       ROUND(100.0 * COUNT(B.CustomerId) / COUNT(A.CustomerId), 1) AS RetentionPct\nFROM A LEFT JOIN B ON B.CustomerId = A.CustomerId;",
      "COUNT(column) only counts matched rows from the LEFT JOIN.")
    q(X, "ROW_NUMBER", "For each customer show the first order they ever placed: order id, date and order total.",
      ["Order totals CTE then ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY OrderDate)."],
      "WITH OT AS (\n    @OT@\n), R AS (\n    SELECT *, ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY OrderDate) AS rn FROM OT\n)\nSELECT CustomerId, OrderId, OrderDate, Total FROM R WHERE rn = 1;",
      "Top-1 per group again, here chronological.")
    q(X, "Bottom N per group", "For each product category, list the 2 products with the lowest stock (category, product, stock).",
      ["ROW_NUMBER() OVER (PARTITION BY Category ORDER BY Stock) <= 2."],
      "WITH R AS (\n    SELECT Category, ProductName, Stock, ROW_NUMBER() OVER (PARTITION BY Category ORDER BY Stock) AS rn FROM Products\n)\nSELECT Category, ProductName, Stock FROM R WHERE rn <= 2;",
      "Ordering ascending gives bottom-N.")
    q(X, "Recursive CTE", "For every manager, compute the total salary cost of their entire team (all direct and indirect reports, excluding the manager). Show manager name and team cost.",
      ["Make every employee the root of their own subtree, then SUM descendants."],
      "WITH T AS (\n    SELECT EmployeeId AS RootId, EmployeeId AS MemberId FROM Employees\n    UNION ALL\n    SELECT t.RootId, e.EmployeeId FROM T t JOIN Employees e ON e.ManagerId = t.MemberId\n)\nSELECT r.FirstName + ' ' + r.LastName AS Manager, SUM(m.Salary) AS TeamCost\nFROM T\nJOIN Employees r ON r.EmployeeId = T.RootId\nJOIN Employees m ON m.EmployeeId = T.MemberId\nWHERE T.RootId <> T.MemberId\nGROUP BY r.EmployeeId, r.FirstName, r.LastName;",
      "Starting a recursive CTE from all rows computes every subtree at once.")
    q(X, "PERCENTILE_CONT", "What is the median order value (using order totals)?",
      ["Order totals CTE then PERCENTILE_CONT(0.5)."],
      "WITH OT AS (\n    @OT@\n)\nSELECT DISTINCT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Total) OVER () AS MedianOrder\nFROM OT;",
      "The median is robust to very large orders, unlike the mean.")
    q(X, "LAG", "For each employee, find their largest single percentage raise from SalaryHistory (1 decimal).",
      ["LAG to get the previous salary, MAX of the % change."],
      "WITH C AS (\n    SELECT EmployeeId,\n           100.0 * (Salary - LAG(Salary) OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate)) / LAG(Salary) OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate) AS Pct\n    FROM SalaryHistory\n)\nSELECT EmployeeId, ROUND(MAX(Pct), 1) AS BiggestRaisePct\nFROM C\nGROUP BY EmployeeId\nHAVING MAX(Pct) IS NOT NULL;",
      "Employees with a single record have no raise, so HAVING removes them.")
    q(X, "Point in time", "What salary was each employee earning on 2024-06-30 according to SalaryHistory? (EmployeeId, Salary). Exclude employees who had no record by then.",
      ["Latest record with EffectiveDate <= the date; ROW_NUMBER DESC."],
      "WITH S AS (\n    SELECT EmployeeId, Salary,\n           ROW_NUMBER() OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate DESC) AS rn\n    FROM SalaryHistory\n    WHERE EffectiveDate <= '2024-06-30'\n)\nSELECT EmployeeId, Salary FROM S WHERE rn = 1;",
      "Slowly-changing-dimension 'as of' lookup.")
    q(X, "Point in time", "What was the total payroll on 2024-06-30 (sum of each employee's then-current salary)?",
      ["Same as the previous question then SUM."],
      "WITH S AS (\n    SELECT EmployeeId, Salary,\n           ROW_NUMBER() OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate DESC) AS rn\n    FROM SalaryHistory\n    WHERE EffectiveDate <= '2024-06-30'\n)\nSELECT SUM(Salary) AS Payroll FROM S WHERE rn = 1;",
      "Summing all history rows would massively overcount.")
    q(X, "NTILE", "Find customers in the top revenue quartile (NTILE(4) = 1). Show customer name and revenue.",
      ["Revenue per customer CTE then NTILE(4) OVER (ORDER BY Revenue DESC)."],
      "WITH CR AS (\n    SELECT c.CustomerName, SUM(@R@) AS Revenue\n    FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId\n    GROUP BY c.CustomerId, c.CustomerName\n), N AS (\n    SELECT *, NTILE(4) OVER (ORDER BY Revenue DESC) AS Q FROM CR\n)\nSELECT CustomerName, Revenue FROM N WHERE Q = 1;",
      "NTILE splits ordered rows into equal-count groups.")
    q(X, "New customers", "For each month, count the customers placing their first-ever order, with a running total of acquired customers.",
      ["MIN(OrderDate) per customer, group by month, running SUM."],
      "WITH F AS (\n    SELECT CustomerId, DATEFROMPARTS(YEAR(MIN(OrderDate)), MONTH(MIN(OrderDate)), 1) AS FirstMonth\n    FROM Orders GROUP BY CustomerId\n), M AS (\n    SELECT FirstMonth, COUNT(*) AS NewCustomers FROM F GROUP BY FirstMonth\n)\nSELECT FirstMonth, NewCustomers,\n       SUM(NewCustomers) OVER (ORDER BY FirstMonth ROWS UNBOUNDED PRECEDING) AS CumulativeCustomers\nFROM M;",
      "Aggregate twice: customer level first, then month level.")
    q(X, "Basket analysis", "Which products are most often ordered together with 'Laptop Pro 15'? Show product and number of shared orders for products shared in at least 3 orders.",
      ["Self join OrderItems on OrderId with one side fixed to the laptop."],
      "SELECT p.ProductName, COUNT(*) AS SharedOrders\nFROM OrderItems a\nJOIN Products lp ON lp.ProductId = a.ProductId AND lp.ProductName = 'Laptop Pro 15'\nJOIN OrderItems b ON b.OrderId = a.OrderId AND b.ProductId <> a.ProductId\nJOIN Products p ON p.ProductId = b.ProductId\nGROUP BY p.ProductId, p.ProductName\nHAVING COUNT(*) >= 3;",
      "Association-rule style questions rely on self joins.")
    q(X, "Window SUM", "Find order lines that account for more than 50% of their order's value. Show OrderId, ProductId and the share (2 decimals).",
      ["SUM(line value) OVER (PARTITION BY OrderId)."],
      "WITH L AS (\n    SELECT oi.OrderId, oi.ProductId, @R@ AS LineValue,\n           SUM(@R@) OVER (PARTITION BY oi.OrderId) AS OrderValue\n    FROM OrderItems oi\n)\nSELECT OrderId, ProductId, ROUND(100.0 * LineValue / OrderValue, 2) AS SharePct\nFROM L\nWHERE LineValue > 0.5 * OrderValue;",
      "Window functions let you compare each row to its group total without a self join.")
    q(X, "Day of week", "Which weekday generates the most revenue (non-cancelled)? Return the weekday name and revenue.",
      ["Group by DATENAME(WEEKDAY) and take the top row."],
      "SELECT TOP 1 DATENAME(WEEKDAY, o.OrderDate) AS Weekday, SUM(@R@) AS Revenue\nFROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId\nWHERE o.Status <> 'Cancelled'\nGROUP BY DATENAME(WEEKDAY, o.OrderDate)\nORDER BY Revenue DESC;",
      "Remember to sort on the aggregate, not the weekday name.")
    q(X, "Year to date", "Show 2024 monthly non-cancelled revenue with a year-to-date running total.",
      ["Monthly CTE filtered to 2024, SUM OVER with ROWS."],
      "WITH M AS (\n    @MONTHLY@\n)\nSELECT MonthStart, Revenue,\n       SUM(Revenue) OVER (ORDER BY MonthStart ROWS UNBOUNDED PRECEDING) AS YtdRevenue\nFROM M\nWHERE MonthStart >= '2024-01-01' AND MonthStart < '2025-01-01';",
      "WHERE is applied before the window function, so the running total starts at the first 2024 month - that is what makes it year-to-date.")
    q(X, "Year-over-year", "For each month show revenue and the revenue of the same month one year earlier (NULL if none) and the difference.",
      ["LEFT JOIN the monthly CTE to itself on DATEADD(YEAR, -1, MonthStart)."],
      "WITH M AS (\n    @MONTHLY@\n)\nSELECT cur.MonthStart, cur.Revenue, prev.Revenue AS PrevYearRevenue, cur.Revenue - prev.Revenue AS Diff\nFROM M cur\nLEFT JOIN M prev ON prev.MonthStart = DATEADD(YEAR, -1, cur.MonthStart);",
      "Self-joining on shifted dates is more robust than LAG(12) when months are missing.")
    q(X, "Recursive CTE", "Show the chain of command above Jon Tan (EmployeeId 36) up to the CEO: name and level above Jon (0 = Jon).",
      ["Recursive CTE walking ManagerId upwards."],
      "WITH Up AS (\n    SELECT EmployeeId, FirstName, LastName, ManagerId, 0 AS Level FROM Employees WHERE EmployeeId = 36\n    UNION ALL\n    SELECT e.EmployeeId, e.FirstName, e.LastName, e.ManagerId, u.Level + 1\n    FROM Employees e JOIN Up u ON e.EmployeeId = u.ManagerId\n)\nSELECT FirstName + ' ' + LastName AS Name, Level FROM Up ORDER BY Level;",
      "Walking up joins on the manager's id rather than the employee's.")
    q(X, "Cross tab", "Show headcount per department (rows) and salary band (columns Low < 70000, Mid 70000-119999, High >= 120000). Only employees with a department.",
      ["Conditional aggregation with CASE."],
      "SELECT d.DepartmentName,\n       SUM(CASE WHEN e.Salary < 70000 THEN 1 ELSE 0 END) AS Low,\n       SUM(CASE WHEN e.Salary >= 70000 AND e.Salary < 120000 THEN 1 ELSE 0 END) AS Mid,\n       SUM(CASE WHEN e.Salary >= 120000 THEN 1 ELSE 0 END) AS High\nFROM Departments d JOIN Employees e ON e.DepartmentId = d.DepartmentId\nGROUP BY d.DepartmentName;",
      "A cross tab is just GROUP BY with CASE-based aggregates.")
    q(X, "DATEDIFF", "For every customer who has ordered, show how many days passed between signing up and their first order.",
      ["MIN(OrderDate) then DATEDIFF with SignupDate."],
      "SELECT c.CustomerName, DATEDIFF(DAY, c.SignupDate, MIN(o.OrderDate)) AS DaysToFirstOrder\nFROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId\nGROUP BY c.CustomerId, c.CustomerName, c.SignupDate;",
      "Negative values would reveal orders placed before signup (data quality!).")
    q(X, "LAG", "List orders whose Status is the same as that customer's previous order's status (customer, order id, status).",
      ["LAG(Status) OVER (PARTITION BY CustomerId ORDER BY OrderDate)."],
      "WITH S AS (\n    SELECT CustomerId, OrderId, Status,\n           LAG(Status) OVER (PARTITION BY CustomerId ORDER BY OrderDate) AS PrevStatus\n    FROM Orders\n)\nSELECT CustomerId, OrderId, Status FROM S WHERE Status = PrevStatus;",
      "LAG returns NULL for the first row so it never matches.")
    q(X, "Self join", "List employees who manage at least one person who is themselves a manager (i.e. managers of managers).",
      ["Self join twice or nested EXISTS."],
      "SELECT m.EmployeeId, m.FirstName, m.LastName\nFROM Employees m\nWHERE EXISTS (\n    SELECT 1 FROM Employees r\n    WHERE r.ManagerId = m.EmployeeId\n      AND EXISTS (SELECT 1 FROM Employees rr WHERE rr.ManagerId = r.EmployeeId));",
      "Nested EXISTS checks two levels of the hierarchy.")
    q(X, "PIVOT", "Show a cohort matrix: rows = customer signup year, columns = order year 2023, 2024, 2025, values = number of orders.",
      ["Join Customers to Orders, then PIVOT on order year."],
      "SELECT SignupYear, [2023], [2024], [2025]\nFROM (SELECT YEAR(c.SignupDate) AS SignupYear, YEAR(o.OrderDate) AS OrderYear, o.OrderId\n      FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId) s\nPIVOT (COUNT(OrderId) FOR OrderYear IN ([2023], [2024], [2025])) p\nORDER BY SignupYear;",
      "Cohort tables are PIVOTs of counts by a cohort key and a time key.")
    q(X, "Distribution", "How many customers placed 1-5 orders, 6-10 orders, and 11+ orders? (bucket, customers). Include only customers with orders.",
      ["Count orders per customer first, then bucket with CASE."],
      "WITH C AS (SELECT CustomerId, COUNT(*) AS Orders FROM Orders GROUP BY CustomerId)\nSELECT CASE WHEN Orders <= 5 THEN '1-5' WHEN Orders <= 10 THEN '6-10' ELSE '11+' END AS Bucket,\n       COUNT(*) AS Customers\nFROM C\nGROUP BY CASE WHEN Orders <= 5 THEN '1-5' WHEN Orders <= 10 THEN '6-10' ELSE '11+' END;",
      "A histogram is an aggregate of an aggregate.")
    q(X, "ROW_NUMBER", "Find customers whose most recent order was Cancelled.",
      ["ROW_NUMBER by OrderDate DESC and check Status of row 1."],
      "WITH R AS (\n    SELECT CustomerId, Status, ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY OrderDate DESC) AS rn FROM Orders\n)\nSELECT c.CustomerName\nFROM R JOIN Customers c ON c.CustomerId = R.CustomerId\nWHERE R.rn = 1 AND R.Status = 'Cancelled';",
      "Filter on the status after picking the latest row, not before.")
    q(X, "FIRST_VALUE", "For each department show the highest and lowest paid employee names (one row per department, employees with a department).",
      ["FIRST_VALUE with ASC and DESC ordering, DISTINCT."],
      "SELECT DISTINCT d.DepartmentName,\n       FIRST_VALUE(e.FirstName) OVER (PARTITION BY e.DepartmentId ORDER BY e.Salary DESC, e.EmployeeId) AS HighestPaid,\n       FIRST_VALUE(e.FirstName) OVER (PARTITION BY e.DepartmentId ORDER BY e.Salary ASC, e.EmployeeId) AS LowestPaid\nFROM Employees e JOIN Departments d ON d.DepartmentId = e.DepartmentId;",
      "Two FIRST_VALUEs with opposite orderings avoid the LAST_VALUE frame trap.")
    q(X, "Anniversary", "For each employee compute their next work anniversary date on or after 2026-01-01.",
      ["Add whole years to HireDate until it is >= the reference date."],
      "SELECT EmployeeId, FirstName, LastName, HireDate,\n       CASE WHEN DATEADD(YEAR, DATEDIFF(YEAR, HireDate, '2026-01-01'), HireDate) >= '2026-01-01'\n            THEN DATEADD(YEAR, DATEDIFF(YEAR, HireDate, '2026-01-01'), HireDate)\n            ELSE DATEADD(YEAR, DATEDIFF(YEAR, HireDate, '2026-01-01') + 1, HireDate) END AS NextAnniversary\nFROM Employees;",
      "DATEDIFF(YEAR) counts boundaries, so the result may need one more year.")
    q(X, "Budgeting", "Starting from the highest-paid employee (ties by EmployeeId) and going down, which employees fit within a cumulative salary budget of 1,000,000? Show name, salary and running total.",
      ["Running SUM ordered by Salary DESC, EmployeeId; filter <= 1,000,000."],
      "WITH R AS (\n    SELECT FirstName, LastName, Salary,\n           SUM(Salary) OVER (ORDER BY Salary DESC, EmployeeId ROWS UNBOUNDED PRECEDING) AS RunningTotal\n    FROM Employees\n)\nSELECT FirstName, LastName, Salary, RunningTotal FROM R WHERE RunningTotal <= 1000000;",
      "Filter in an outer query because window functions are not allowed in WHERE.")
    q(X, "Metadata", "List every table with its row count using sys.tables and sys.partitions.",
      ["Join on object_id and filter index_id IN (0,1)."],
      "SELECT t.name AS TableName, SUM(p.rows) AS TotalRows\nFROM sys.tables t JOIN sys.partitions p ON p.object_id = t.object_id AND p.index_id IN (0, 1)\nGROUP BY t.name;",
      "Heap (0) and clustered index (1) partitions hold the base rows; counting other indexes would double count.")
    q(X, "Dynamic ranking", "Rank customers by revenue within each year (DENSE_RANK, highest = 1) and return the top 3 per year with year, customer, revenue and rank.",
      ["Revenue per customer per year, then DENSE_RANK partitioned by Yr."],
      "WITH CR AS (\n    SELECT YEAR(o.OrderDate) AS Yr, c.CustomerName, SUM(@R@) AS Revenue\n    FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId\n    GROUP BY YEAR(o.OrderDate), c.CustomerId, c.CustomerName\n), R AS (\n    SELECT *, DENSE_RANK() OVER (PARTITION BY Yr ORDER BY Revenue DESC) AS Rnk FROM CR\n)\nSELECT Yr, CustomerName, Revenue, Rnk FROM R WHERE Rnk <= 3;",
      "Top-N per group with ties handled by DENSE_RANK.")
    q(X, "Anti join", "Find employees who never appear as the sales rep on any order and are in the Sales department.",
      ["Sales dept = 3; NOT EXISTS on Orders.EmployeeId."],
      "SELECT e.EmployeeId, e.FirstName, e.LastName\nFROM Employees e\nWHERE e.DepartmentId = 3\n  AND NOT EXISTS (SELECT 1 FROM Orders o WHERE o.EmployeeId = e.EmployeeId);",
      "Reps 16-21 are assigned orders in the seed data, so remaining Sales staff show up here.")
    q(X, "Moving average", "Show each month's non-cancelled revenue and the average of the previous 2 months only (excluding the current month), rounded to 2 decimals.",
      ["Frame: ROWS BETWEEN 2 PRECEDING AND 1 PRECEDING."],
      "WITH M AS (\n    @MONTHLY@\n)\nSELECT MonthStart, Revenue,\n       ROUND(AVG(Revenue) OVER (ORDER BY MonthStart ROWS BETWEEN 2 PRECEDING AND 1 PRECEDING), 2) AS PrevTwoAvg\nFROM M;",
      "Frames can exclude the current row; the first month has NULL.")
    q(X, "Orders vs average", "List each customer's orders whose value is above that customer's own average order value (customer, order id, total, customer average).",
      ["Order totals CTE with AVG OVER (PARTITION BY CustomerId)."],
      "WITH OT AS (\n    @OT@\n), A AS (\n    SELECT *, AVG(Total) OVER (PARTITION BY CustomerId) AS CustAvg FROM OT\n)\nSELECT CustomerId, OrderId, Total, CustAvg FROM A WHERE Total > CustAvg;",
      "Three layers: order lines, order totals, then per-customer window.")
    q(X, "Pivot from CTE", "Show total revenue per product category (rows) per Status (columns Delivered, Shipped, Pending, Cancelled).",
      ["Join Orders, OrderItems, Products; PIVOT on Status."],
      "SELECT Category, [Delivered], [Shipped], [Pending], [Cancelled]\nFROM (\n    SELECT p.Category, o.Status, @R@ AS Revenue\n    FROM OrderItems oi JOIN Orders o ON o.OrderId = oi.OrderId JOIN Products p ON p.ProductId = oi.ProductId\n) s\nPIVOT (SUM(Revenue) FOR Status IN ([Delivered], [Shipped], [Pending], [Cancelled])) pv;",
      "PIVOT can aggregate any measure.")
