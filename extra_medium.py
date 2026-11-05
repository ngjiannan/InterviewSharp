REV = "oi.Quantity * oi.UnitPrice * (1 - oi.Discount)"


def add(q0):
    def q(l, t, x, h, s, w):
        q0(l, t, x, h, s.replace("@R@", REV), w)

    M = "Medium"
    q(M, "INNER JOIN", "List first name, last name and department location for employees whose department is located in Singapore.",
      ["Join Employees to Departments, filter on Location."],
      "SELECT e.FirstName, e.LastName, d.Location\nFROM Employees e\nJOIN Departments d ON d.DepartmentId = e.DepartmentId\nWHERE d.Location = 'Singapore';",
      "JOIN defaults to INNER JOIN.")
    q(M, "LEFT JOIN", "Show every customer with their number of orders, including customers with none (0).",
      ["LEFT JOIN Orders, then COUNT a column from Orders, not *."],
      "SELECT c.CustomerName, COUNT(o.OrderId) AS OrderCount\nFROM Customers c\nLEFT JOIN Orders o ON o.CustomerId = c.CustomerId\nGROUP BY c.CustomerId, c.CustomerName;",
      "COUNT(o.OrderId) ignores the NULLs produced for unmatched customers.")
    q(M, "SUM", "Show the total quantity sold per product (product name and units), for the 5 best-selling products.",
      ["Join OrderItems to Products and SUM(Quantity).", "ORDER BY the sum DESC with TOP 5."],
      "SELECT TOP 5 p.ProductName, SUM(oi.Quantity) AS UnitsSold\nFROM OrderItems oi\nJOIN Products p ON p.ProductId = oi.ProductId\nGROUP BY p.ProductId, p.ProductName\nORDER BY UnitsSold DESC;",
      "Group by the product key plus name; ORDER BY can use the alias.")
    q(M, "AVG", "Show the average discount (as a fraction) per product category.",
      ["Join OrderItems to Products, AVG(Discount) by Category."],
      "SELECT p.Category, AVG(oi.Discount) AS AvgDiscount\nFROM OrderItems oi\nJOIN Products p ON p.ProductId = oi.ProductId\nGROUP BY p.Category;",
      "Discount is DECIMAL(4,2) so AVG keeps decimal precision.")
    q(M, "GROUP BY", "How many employees were hired in each year? (year, count), oldest year first.",
      ["YEAR(HireDate)."],
      "SELECT YEAR(HireDate) AS HireYear, COUNT(*) AS Hires\nFROM Employees\nGROUP BY YEAR(HireDate)\nORDER BY HireYear;",
      "You must repeat the expression in GROUP BY (aliases are not allowed there).")
    q(M, "HAVING", "List countries that have at least 3 customers, with the customer count.",
      ["GROUP BY Country with HAVING COUNT(*) >= 3."],
      "SELECT Country, COUNT(*) AS Customers\nFROM Customers\nGROUP BY Country\nHAVING COUNT(*) >= 3;",
      "HAVING filters groups after aggregation.")
    q(M, "GROUP BY", "For each sales rep (employee who owns orders), show their name and number of orders. Ignore orders without a rep.",
      ["INNER JOIN Orders to Employees removes the NULL EmployeeId rows."],
      "SELECT e.FirstName, e.LastName, COUNT(*) AS Orders\nFROM Orders o\nJOIN Employees e ON e.EmployeeId = o.EmployeeId\nGROUP BY e.EmployeeId, e.FirstName, e.LastName;",
      "NULL never equals anything, so unassigned orders drop out of the inner join.")
    q(M, "NULL", "How many orders of each Status have no sales rep assigned?",
      ["Filter EmployeeId IS NULL then GROUP BY Status."],
      "SELECT Status, COUNT(*) AS Orders\nFROM Orders\nWHERE EmployeeId IS NULL\nGROUP BY Status;",
      "WHERE runs before grouping.")
    q(M, "Subquery", "List the employees who earn the highest salary in their own department (include ties).",
      ["Compare Salary to MAX(Salary) of the same department."],
      "SELECT e.FirstName, e.LastName, e.DepartmentId, e.Salary\nFROM Employees e\nWHERE e.Salary = (SELECT MAX(e2.Salary) FROM Employees e2 WHERE e2.DepartmentId = e.DepartmentId);",
      "Correlated subquery; employees with NULL department are excluded.")
    q(M, "UNION", "Produce a single distinct list of cities that appear either as a customer city or as a department location.",
      ["UNION removes duplicates."],
      "SELECT City FROM Customers\nUNION\nSELECT Location FROM Departments;",
      "Column names come from the first SELECT; types must be compatible.")
    q(M, "INTERSECT", "Which cities are both a customer city and a department location?",
      ["INTERSECT returns rows present in both queries."],
      "SELECT City FROM Customers\nINTERSECT\nSELECT Location FROM Departments;",
      "INTERSECT also removes duplicates.")
    q(M, "EXCEPT", "Which customer cities are NOT department locations? (distinct)",
      ["EXCEPT returns rows from the first query not found in the second."],
      "SELECT City FROM Customers\nEXCEPT\nSELECT Location FROM Departments;",
      "Order matters for EXCEPT.")
    q(M, "String functions", "Show each employee's initials (e.g. 'AT' for Alice Tan) together with their EmployeeId.",
      ["LEFT(string, 1) and concatenation."],
      "SELECT EmployeeId, LEFT(FirstName, 1) + LEFT(LastName, 1) AS Initials\nFROM Employees;",
      "LEFT/RIGHT extract the first/last n characters.")
    q(M, "String functions", "Extract the username part of each employee's email (text before '@'). Skip employees without an email.",
      ["CHARINDEX('@', Email) finds the position.", "LEFT(Email, position - 1)."],
      "SELECT EmployeeId, LEFT(Email, CHARINDEX('@', Email) - 1) AS UserName\nFROM Employees\nWHERE Email IS NOT NULL;",
      "CHARINDEX returns 0 when not found, which would make LEFT fail - hence the NULL filter.")
    q(M, "String functions", "Show product names with spaces replaced by underscores.",
      ["REPLACE(string, old, new)."],
      "SELECT ProductName, REPLACE(ProductName, ' ', '_') AS Slug\nFROM Products;",
      "REPLACE is case-insensitive under the default collation.")
    q(M, "Date functions", "How many orders were placed in each quarter of 2024? (quarter, orders)",
      ["DATEPART(QUARTER, OrderDate)."],
      "SELECT DATEPART(QUARTER, OrderDate) AS Quarter, COUNT(*) AS Orders\nFROM Orders\nWHERE OrderDate >= '2024-01-01' AND OrderDate < '2025-01-01'\nGROUP BY DATEPART(QUARTER, OrderDate)\nORDER BY Quarter;",
      "DATEPART returns an int; DATENAME returns text.")
    q(M, "Date functions", "How many orders were placed on each day of the week (name of the weekday)?",
      ["DATENAME(WEEKDAY, date)."],
      "SELECT DATENAME(WEEKDAY, OrderDate) AS Weekday, COUNT(*) AS Orders\nFROM Orders\nGROUP BY DATENAME(WEEKDAY, OrderDate);",
      "Weekday names depend on the session language (English here).")
    q(M, "JOIN", "List orders placed in December 2024 with the customer name, order date and status.",
      ["Join Orders to Customers and filter the date range."],
      "SELECT o.OrderId, c.CustomerName, o.OrderDate, o.Status\nFROM Orders o\nJOIN Customers c ON c.CustomerId = o.CustomerId\nWHERE o.OrderDate >= '2024-12-01' AND o.OrderDate < '2025-01-01';",
      "Half-open date ranges avoid end-of-month edge cases.")
    q(M, "TOP WITH TIES", "List the 3 highest-priced products, including any products tied with the 3rd price.",
      ["TOP (3) WITH TIES requires ORDER BY."],
      "SELECT TOP (3) WITH TIES ProductName, UnitPrice\nFROM Products\nORDER BY UnitPrice DESC;",
      "WITH TIES returns extra rows that tie on the ORDER BY value of the last row.")
    q(M, "ISNULL", "For Sales employees (DepartmentId 3) show total compensation = Salary * (1 + commission), treating a missing commission as 0.",
      ["COALESCE/ISNULL(CommissionPct, 0)."],
      "SELECT FirstName, LastName, Salary * (1 + COALESCE(CommissionPct, 0)) AS TotalComp\nFROM Employees\nWHERE DepartmentId = 3;",
      "Any arithmetic with NULL yields NULL, so replace NULL first.")
    q(M, "GROUP BY", "For each product category show the stock value (SUM of Stock * UnitPrice). Only show categories above 50,000.",
      ["Aggregate an expression and filter with HAVING."],
      "SELECT Category, SUM(Stock * UnitPrice) AS StockValue\nFROM Products\nGROUP BY Category\nHAVING SUM(Stock * UnitPrice) > 50000;",
      "HAVING must repeat the aggregate expression (or wrap in a CTE).")
    q(M, "IIF", "Label each product 'In stock' or 'Out of stock' based on Stock.",
      ["IIF(condition, a, b) or CASE."],
      "SELECT ProductName, IIF(Stock > 0, 'In stock', 'Out of stock') AS Availability\nFROM Products;",
      "IIF is shorthand for a two-branch CASE.")
    q(M, "SUM", "Show the 10 orders with the highest total value (OrderId and total).",
      ["SUM revenue per OrderId, TOP 10."],
      "SELECT TOP 10 oi.OrderId, SUM(@R@) AS OrderTotal\nFROM OrderItems oi\nGROUP BY oi.OrderId\nORDER BY OrderTotal DESC;",
      "Order totals are computed from order lines.")
    q(M, "HAVING", "List customers who placed more than 10 orders (name and count).",
      ["JOIN, GROUP BY, HAVING COUNT(*) > 10."],
      "SELECT c.CustomerName, COUNT(*) AS Orders\nFROM Customers c\nJOIN Orders o ON o.CustomerId = c.CustomerId\nGROUP BY c.CustomerId, c.CustomerName\nHAVING COUNT(*) > 10;",
      "HAVING works on the grouped result.")
    q(M, "NOT EXISTS", "Which products were not ordered at all in 2025?",
      ["NOT EXISTS with a join between OrderItems and Orders inside."],
      "SELECT p.ProductId, p.ProductName\nFROM Products p\nWHERE NOT EXISTS (\n    SELECT 1 FROM OrderItems oi\n    JOIN Orders o ON o.OrderId = oi.OrderId\n    WHERE oi.ProductId = p.ProductId AND o.OrderDate >= '2025-01-01' AND o.OrderDate < '2026-01-01');",
      "NOT EXISTS handles the 'never ordered' and 'not ordered in period' cases uniformly.")
    q(M, "Derived table", "What is the average number of line items per order?",
      ["Count lines per order in a derived table, then AVG."],
      "SELECT AVG(Lines * 1.0) AS AvgLines\nFROM (SELECT OrderId, COUNT(*) AS Lines FROM OrderItems GROUP BY OrderId) x;",
      "Multiply by 1.0 to avoid integer averaging.")
    q(M, "HAVING", "Which job titles are held by more than one employee? (title, count)",
      ["GROUP BY JobTitle HAVING COUNT(*) > 1."],
      "SELECT JobTitle, COUNT(*) AS Employees\nFROM Employees\nGROUP BY JobTitle\nHAVING COUNT(*) > 1;",
      "A classic duplicate-detection pattern.")
    q(M, "Self join", "List each manager's name with their number of direct reports (managers only).",
      ["Join Employees to itself on ManagerId, group by the manager."],
      "SELECT m.FirstName, m.LastName, COUNT(*) AS DirectReports\nFROM Employees e\nJOIN Employees m ON m.EmployeeId = e.ManagerId\nGROUP BY m.EmployeeId, m.FirstName, m.LastName;",
      "The inner join drops employees without a manager (the CEO and Iris), and only people with at least one report appear.")
    q(M, "NOT EXISTS", "List employees who do not manage anyone.",
      ["NOT EXISTS on Employees.ManagerId."],
      "SELECT e.EmployeeId, e.FirstName, e.LastName\nFROM Employees e\nWHERE NOT EXISTS (SELECT 1 FROM Employees r WHERE r.ManagerId = e.EmployeeId);",
      "Anti-join pattern again.")
    q(M, "Self join", "Find pairs of different employees in the same department who earn exactly the same salary (each pair once).",
      ["Self join with e1.EmployeeId < e2.EmployeeId."],
      "SELECT e1.FirstName + ' ' + e1.LastName AS Employee1, e2.FirstName + ' ' + e2.LastName AS Employee2, e1.Salary\nFROM Employees e1\nJOIN Employees e2 ON e1.DepartmentId = e2.DepartmentId AND e1.Salary = e2.Salary AND e1.EmployeeId < e2.EmployeeId;",
      "The < condition removes mirrored and self pairs.")
    q(M, "GROUP BY", "How many customers signed up in each year?",
      ["GROUP BY YEAR(SignupDate)."],
      "SELECT YEAR(SignupDate) AS SignupYear, COUNT(*) AS Customers\nFROM Customers\nGROUP BY YEAR(SignupDate)\nORDER BY SignupYear;",
      "Same pattern as hires per year.")
    q(M, "SUM", "Show total revenue per calendar year.",
      ["Join Orders and OrderItems, group by YEAR(OrderDate)."],
      "SELECT YEAR(o.OrderDate) AS Yr, SUM(@R@) AS Revenue\nFROM Orders o\nJOIN OrderItems oi ON oi.OrderId = o.OrderId\nGROUP BY YEAR(o.OrderDate)\nORDER BY Yr;",
      "Revenue = Quantity * UnitPrice * (1 - Discount).")
    q(M, "Multi-table JOIN", "Show total revenue per customer country.",
      ["Customers -> Orders -> OrderItems."],
      "SELECT c.Country, SUM(@R@) AS Revenue\nFROM Customers c\nJOIN Orders o ON o.CustomerId = c.CustomerId\nJOIN OrderItems oi ON oi.OrderId = o.OrderId\nGROUP BY c.Country\nORDER BY Revenue DESC;",
      "Chain joins along foreign keys.")
    q(M, "SUM", "Which 3 customers lost the most revenue to Cancelled orders? (customer name, cancelled revenue)",
      ["Filter Status = 'Cancelled' before aggregating."],
      "SELECT TOP 3 c.CustomerName, SUM(@R@) AS CancelledRevenue\nFROM Customers c\nJOIN Orders o ON o.CustomerId = c.CustomerId\nJOIN OrderItems oi ON oi.OrderId = o.OrderId\nWHERE o.Status = 'Cancelled'\nGROUP BY c.CustomerId, c.CustomerName\nORDER BY CancelledRevenue DESC;",
      "Filtering in WHERE keeps only cancelled orders.")
    q(M, "HAVING", "For job titles held by at least 2 employees, show the average salary.",
      ["HAVING COUNT(*) >= 2 together with AVG."],
      "SELECT JobTitle, AVG(Salary) AS AvgSalary\nFROM Employees\nGROUP BY JobTitle\nHAVING COUNT(*) >= 2;",
      "Multiple aggregates may appear in SELECT and HAVING.")
    q(M, "Date functions", "List employees whose hire date was a Monday.",
      ["DATENAME(WEEKDAY, HireDate) = 'Monday'."],
      "SELECT FirstName, LastName, HireDate\nFROM Employees\nWHERE DATENAME(WEEKDAY, HireDate) = 'Monday';",
      "Avoid DATEPART(WEEKDAY) here because its numbering depends on DATEFIRST.")
    q(M, "Correlated subquery", "List products priced above the average price of their own category.",
      ["Correlated AVG subquery on Category."],
      "SELECT p.ProductName, p.Category, p.UnitPrice\nFROM Products p\nWHERE p.UnitPrice > (SELECT AVG(p2.UnitPrice) FROM Products p2 WHERE p2.Category = p.Category);",
      "The subquery is re-evaluated (logically) per outer row.")
    q(M, "COUNT DISTINCT", "For each sales rep, how many distinct customers have they sold to?",
      ["COUNT(DISTINCT CustomerId)."],
      "SELECT e.FirstName, e.LastName, COUNT(DISTINCT o.CustomerId) AS Customers\nFROM Orders o\nJOIN Employees e ON e.EmployeeId = o.EmployeeId\nGROUP BY e.EmployeeId, e.FirstName, e.LastName;",
      "COUNT(DISTINCT) vs COUNT(*) is a frequent interview trap.")
    q(M, "HAVING", "Which employees have exactly 3 records in SalaryHistory?",
      ["GROUP BY EmployeeId HAVING COUNT(*) = 3."],
      "SELECT EmployeeId, COUNT(*) AS Records\nFROM SalaryHistory\nGROUP BY EmployeeId\nHAVING COUNT(*) = 3;",
      "Employees hired recently have fewer history rows.")
    q(M, "SUM", "Which products gave away more than 1,000 in total discounts (Quantity * UnitPrice * Discount)?",
      ["SUM the discount amount and HAVING > 1000."],
      "SELECT p.ProductName, SUM(oi.Quantity * oi.UnitPrice * oi.Discount) AS DiscountGiven\nFROM OrderItems oi\nJOIN Products p ON p.ProductId = oi.ProductId\nGROUP BY p.ProductId, p.ProductName\nHAVING SUM(oi.Quantity * oi.UnitPrice * oi.Discount) > 1000;",
      "Discount value = list value minus net revenue.")
    q(M, "Self join", "List employees whose manager works in a different department (employee, employee dept, manager dept).",
      ["Self join then compare DepartmentId."],
      "SELECT e.FirstName, e.LastName, e.DepartmentId AS EmpDept, m.DepartmentId AS MgrDept\nFROM Employees e\nJOIN Employees m ON m.EmployeeId = e.ManagerId\nWHERE e.DepartmentId <> m.DepartmentId;",
      "Rows with NULL in either department are excluded because NULL <> x is unknown.")
    q(M, "COUNT DISTINCT", "For each customer, how many distinct products have they ever ordered?",
      ["Join Orders and OrderItems."],
      "SELECT c.CustomerName, COUNT(DISTINCT oi.ProductId) AS Products\nFROM Customers c\nJOIN Orders o ON o.CustomerId = c.CustomerId\nJOIN OrderItems oi ON oi.OrderId = o.OrderId\nGROUP BY c.CustomerId, c.CustomerName;",
      "Distinct is needed because a product can repeat across orders.")
    q(M, "STRING_AGG", "For each department, list its employees' first names as one comma-separated string sorted alphabetically.",
      ["STRING_AGG(FirstName, ',') WITHIN GROUP (ORDER BY FirstName)."],
      "SELECT d.DepartmentName, STRING_AGG(e.FirstName, ',') WITHIN GROUP (ORDER BY e.FirstName) AS Employees\nFROM Departments d\nJOIN Employees e ON e.DepartmentId = d.DepartmentId\nGROUP BY d.DepartmentName;",
      "STRING_AGG needs WITHIN GROUP for deterministic order.")
    q(M, "Metadata", "List each table in the database with its number of columns (use INFORMATION_SCHEMA.COLUMNS).",
      ["GROUP BY TABLE_NAME."],
      "SELECT TABLE_NAME, COUNT(*) AS ColumnCount\nFROM INFORMATION_SCHEMA.COLUMNS\nGROUP BY TABLE_NAME;",
      "INFORMATION_SCHEMA views are ANSI-standard metadata.")
    q(M, "Metadata", "List all foreign key constraints with the table that owns them (sys.foreign_keys and OBJECT_NAME(parent_object_id)).",
      ["sys.foreign_keys has name and parent_object_id."],
      "SELECT name AS ForeignKey, OBJECT_NAME(parent_object_id) AS TableName\nFROM sys.foreign_keys;",
      "System catalog views describe the schema.")
    q(M, "FORMAT", "Show employee IDs formatted as 'EMP0001' style codes with the employee's full name.",
      ["FORMAT(number, 'EMP0000') or RIGHT('0000' + ...)."],
      "SELECT 'EMP' + RIGHT('0000' + CAST(EmployeeId AS VARCHAR(10)), 4) AS Code, FirstName + ' ' + LastName AS FullName\nFROM Employees;",
      "RIGHT-padding is faster than FORMAT, which is CLR based.")
    q(M, "CASE", "Count orders per Status, showing a friendly label: Delivered/Shipped as 'Completed or on the way', others by their own name.",
      ["CASE in SELECT and GROUP BY (or a derived table)."],
      "SELECT x.Label, COUNT(*) AS Orders\nFROM (SELECT CASE WHEN Status IN ('Delivered','Shipped') THEN 'Completed or on the way' ELSE Status END AS Label FROM Orders) x\nGROUP BY x.Label;",
      "A derived table lets you group by the CASE alias.")
