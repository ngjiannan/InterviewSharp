# SQL Server Interview Practice Answers


## Easy

### 1. [SELECT] List all columns and rows from the Departments table.

Hints:
1. Use SELECT with a wildcard.
2. The table name is Departments.

```sql
SELECT * FROM Departments;
```

**Explanation:** SELECT * returns every column. Fine for exploration; in production list columns explicitly.

### 2. [WHERE] Show the first name, last name and salary of employees who earn more than 100,000.

Hints:
1. Filter rows with WHERE.
2. Compare Salary with > 100000.

```sql
SELECT FirstName, LastName, Salary
FROM Employees
WHERE Salary > 100000;
```

**Explanation:** WHERE filters rows before they are returned.

### 3. [ORDER BY] List all employees (first name, last name, hire date) from the most recently hired to the earliest.

Hints:
1. ORDER BY sorts results.
2. Use DESC for newest first.

```sql
SELECT FirstName, LastName, HireDate
FROM Employees
ORDER BY HireDate DESC;
```

**Explanation:** Default sort is ASC; DESC reverses it.

### 4. [TOP] Find the 5 highest paid employees (first name, last name, salary).

Hints:
1. TOP limits rows in SQL Server.
2. Sort by Salary descending first, then take TOP 5.

```sql
SELECT TOP 5 FirstName, LastName, Salary
FROM Employees
ORDER BY Salary DESC;
```

**Explanation:** TOP (n) combined with ORDER BY gives the top-N. Use TOP (5) WITH TIES if ties should be included.

### 5. [DISTINCT] List the distinct job titles in the company, alphabetically.

Hints:
1. DISTINCT removes duplicate rows.
2. Add ORDER BY JobTitle.

```sql
SELECT DISTINCT JobTitle
FROM Employees
ORDER BY JobTitle;
```

**Explanation:** DISTINCT applies to the whole selected row, not just the first column.

### 6. [LIKE] Find customers whose name starts with the letter 'S'.

Hints:
1. Use LIKE with a wildcard.
2. 'S%' matches anything starting with S.

```sql
SELECT CustomerId, CustomerName
FROM Customers
WHERE CustomerName LIKE 'S%';
```

**Explanation:** % matches any number of characters, _ matches exactly one.

### 7. [BETWEEN] List all orders placed during 2024.

Hints:
1. Use BETWEEN with two dates, or >= and <.
2. Prefer a half-open range: >= '2024-01-01' AND < '2025-01-01'.

```sql
SELECT OrderId, CustomerId, OrderDate, Status
FROM Orders
WHERE OrderDate >= '2024-01-01' AND OrderDate < '2025-01-01';
```

**Explanation:** A half-open range is safe for DATE and DATETIME columns alike and can use an index.

### 8. [IN] List customers located in the USA or the UK.

Hints:
1. IN replaces multiple ORs.
2. WHERE Country IN ('USA','UK').

```sql
SELECT CustomerName, City, Country
FROM Customers
WHERE Country IN ('USA', 'UK');
```

**Explanation:** IN is shorthand for OR-ed equality checks.

### 9. [NULL] Find employees who have no manager.

Hints:
1. NULL cannot be compared with =.
2. Use IS NULL.

```sql
SELECT EmployeeId, FirstName, LastName, JobTitle
FROM Employees
WHERE ManagerId IS NULL;
```

**Explanation:** NULL means unknown; = NULL is never true. Always use IS NULL / IS NOT NULL.

### 10. [NULL] List employees who earn a commission (CommissionPct is not null), with their commission percentage.

Hints:
1. Use IS NOT NULL.

```sql
SELECT FirstName, LastName, CommissionPct
FROM Employees
WHERE CommissionPct IS NOT NULL;
```

**Explanation:** IS NOT NULL keeps only rows with a value.

### 11. [Expressions] Show each employee's full name (as FullName) and their annual salary plus a 10% bonus (as SalaryWithBonus).

Hints:
1. Concatenate with CONCAT or +.
2. Multiply Salary by 1.10 and give it an alias with AS.

```sql
SELECT CONCAT(FirstName, ' ', LastName) AS FullName,
       Salary * 1.10 AS SalaryWithBonus
FROM Employees;
```

**Explanation:** CONCAT treats NULL as an empty string, unlike the + operator.

### 12. [COUNT] How many orders are in the Orders table?

Hints:
1. Use an aggregate function.
2. COUNT(*) counts rows.

```sql
SELECT COUNT(*) AS TotalOrders FROM Orders;
```

**Explanation:** COUNT(*) counts all rows; COUNT(col) skips NULLs.

### 13. [AND / OR] Find products that are out of stock (Stock = 0) or priced above 1000.

Hints:
1. Combine conditions with OR.

```sql
SELECT ProductName, UnitPrice, Stock
FROM Products
WHERE Stock = 0 OR UnitPrice > 1000;
```

**Explanation:** Use parentheses when mixing AND and OR - AND binds tighter.

### 14. [OFFSET FETCH] Page through products ordered by price (highest first): skip the first 5 and return the next 5.

Hints:
1. OFFSET ... FETCH works with ORDER BY.
2. OFFSET 5 ROWS FETCH NEXT 5 ROWS ONLY.

```sql
SELECT ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice DESC, ProductId
OFFSET 5 ROWS FETCH NEXT 5 ROWS ONLY;
```

**Explanation:** OFFSET/FETCH is the standard pagination syntax. Add a unique tie-breaker column for deterministic pages.

### 15. [COALESCE] List customers' names and emails, showing 'N/A' where the email is missing.

Hints:
1. COALESCE / ISNULL replace NULL values.

```sql
SELECT CustomerName, COALESCE(Email, 'N/A') AS Email
FROM Customers;
```

**Explanation:** COALESCE returns its first non-NULL argument and is ANSI standard; ISNULL is T-SQL specific.

### 16. [WHERE] List all employees in the Sales department (DepartmentId = 3): first name, last name and job title.

Hints:
1. Filter Employees by DepartmentId.

```sql
SELECT FirstName, LastName, JobTitle
FROM Employees
WHERE DepartmentId = 3;
```

**Explanation:** A simple equality filter on a foreign key column.

### 17. [ORDER BY] List Electronics products (name and price) from the most expensive to the cheapest.

Hints:
1. Filter on Category, then ORDER BY UnitPrice DESC.

```sql
SELECT ProductName, UnitPrice
FROM Products
WHERE Category = 'Electronics'
ORDER BY UnitPrice DESC;
```

**Explanation:** WHERE is applied before ORDER BY.

### 18. [WHERE] List the customers located in Singapore.

Hints:
1. Filter on the Country column.

```sql
SELECT CustomerId, CustomerName, City
FROM Customers
WHERE Country = 'Singapore';
```

**Explanation:** String comparisons are case-insensitive under the default collation.

### 19. [Dates] List employees hired on or after 1 January 2021 (name and hire date), earliest first.

Hints:
1. Compare HireDate with a date literal.
2. Use ORDER BY HireDate.

```sql
SELECT FirstName, LastName, HireDate
FROM Employees
WHERE HireDate >= '2021-01-01'
ORDER BY HireDate;
```

**Explanation:** ISO date literals (yyyy-mm-dd) are language-independent for the DATE type.

### 20. [BETWEEN] Find products priced between 50 and 200 (inclusive), showing name and price.

Hints:
1. BETWEEN is inclusive on both ends.

```sql
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice BETWEEN 50 AND 200;
```

**Explanation:** BETWEEN a AND b is equivalent to >= a AND <= b.

### 21. [WHERE] List all orders that are currently Pending.

Hints:
1. Filter Orders on Status.

```sql
SELECT OrderId, CustomerId, OrderDate
FROM Orders
WHERE Status = 'Pending';
```

**Explanation:** Straightforward equality filter on a status column.

### 22. [String functions] Show department names in upper case together with the length of each name.

Hints:
1. UPPER() and LEN().

```sql
SELECT UPPER(DepartmentName) AS DeptUpper, LEN(DepartmentName) AS NameLength
FROM Departments;
```

**Explanation:** LEN ignores trailing spaces; DATALENGTH counts bytes.

### 23. [LIKE] Find employees whose last name ends with 'ng'.

Hints:
1. Put the wildcard at the start of the pattern.

```sql
SELECT FirstName, LastName
FROM Employees
WHERE LastName LIKE '%ng';
```

**Explanation:** A leading wildcard prevents index seeks - fine for small tables, costly on big ones.

### 24. [MIN] What is the lowest product price?

Hints:
1. Use an aggregate function.

```sql
SELECT MIN(UnitPrice) AS CheapestPrice FROM Products;
```

**Explanation:** MIN/MAX ignore NULLs.

### 25. [SUM] What is the total number of units in stock across all products?

Hints:
1. SUM over the Stock column.

```sql
SELECT SUM(Stock) AS TotalStock FROM Products;
```

**Explanation:** SUM returns NULL if there are no rows; wrap with COALESCE if you need 0.

### 26. [AVG] What is the average unit price of products in the Accessories category?

Hints:
1. AVG with a WHERE filter.

```sql
SELECT AVG(UnitPrice) AS AvgPrice
FROM Products
WHERE Category = 'Accessories';
```

**Explanation:** WHERE filters rows before the aggregate is calculated.

### 27. [NOT] List customers who are not in the USA (name and country).

Hints:
1. Use <> or NOT IN.

```sql
SELECT CustomerName, Country
FROM Customers
WHERE Country <> 'USA';
```

**Explanation:** <> and != are equivalent in T-SQL; <> is ANSI standard.

### 28. [TOP] Show the 3 most recently signed-up customers (name and signup date).

Hints:
1. TOP 3 with ORDER BY SignupDate DESC.

```sql
SELECT TOP 3 CustomerName, SignupDate
FROM Customers
ORDER BY SignupDate DESC;
```

**Explanation:** Dates in this table are unique enough that there is no tie at the cut-off.

### 29. [NULL] List employees who have no email address recorded.

Hints:
1. IS NULL.

```sql
SELECT EmployeeId, FirstName, LastName
FROM Employees
WHERE Email IS NULL;
```

**Explanation:** NULL checks need IS NULL.

### 30. [DISTINCT] How many different countries do our customers come from?

Hints:
1. COUNT(DISTINCT column).

```sql
SELECT COUNT(DISTINCT Country) AS Countries FROM Customers;
```

**Explanation:** COUNT(DISTINCT x) ignores NULLs and duplicates.


## Medium

### 31. [INNER JOIN] List each employee's full name with their department name. (Employees without a department should not appear.)

Hints:
1. Join Employees to Departments on DepartmentId.
2. INNER JOIN keeps only matching rows.

```sql
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
INNER JOIN Departments d ON d.DepartmentId = e.DepartmentId;
```

**Explanation:** Iris (no department) is excluded by the inner join.

### 32. [LEFT JOIN] Find departments that have no employees.

Hints:
1. Start from Departments and LEFT JOIN Employees.
2. Look for rows where the employee side is NULL.

```sql
SELECT d.DepartmentName
FROM Departments d
LEFT JOIN Employees e ON e.DepartmentId = d.DepartmentId
WHERE e.EmployeeId IS NULL;
```

**Explanation:** The anti-join pattern: LEFT JOIN then filter on NULL from the right table's key. NOT EXISTS is an equivalent alternative.

### 33. [Self join] List each employee with their manager's name (show NULL / 'None' when there is no manager).

Hints:
1. Join Employees to itself using two aliases.
2. Use LEFT JOIN so employees without a manager are kept.

```sql
SELECT e.FirstName + ' ' + e.LastName AS Employee,
       COALESCE(m.FirstName + ' ' + m.LastName, 'None') AS Manager
FROM Employees e
LEFT JOIN Employees m ON m.EmployeeId = e.ManagerId;
```

**Explanation:** A self join treats one table as two roles (employee and manager).

### 34. [GROUP BY] Count the number of employees in each department (show the department name).

Hints:
1. JOIN to get names, then GROUP BY the department name.
2. COUNT(*) per group.

```sql
SELECT d.DepartmentName, COUNT(e.EmployeeId) AS EmployeeCount
FROM Departments d
LEFT JOIN Employees e ON e.DepartmentId = d.DepartmentId
GROUP BY d.DepartmentName
ORDER BY EmployeeCount DESC;
```

**Explanation:** LEFT JOIN + COUNT(e.EmployeeId) keeps empty departments with 0 (COUNT(*) would give 1).

### 35. [AVG] Show the average salary per department (rounded to 2 decimals), highest first.

Hints:
1. AVG with GROUP BY.
2. ROUND(AVG(Salary), 2).

```sql
SELECT d.DepartmentName, ROUND(AVG(e.Salary), 2) AS AvgSalary
FROM Employees e
JOIN Departments d ON d.DepartmentId = e.DepartmentId
GROUP BY d.DepartmentName
ORDER BY AvgSalary DESC;
```

**Explanation:** Every non-aggregated column in SELECT must appear in GROUP BY.

### 36. [HAVING] List departments with more than 5 employees.

Hints:
1. WHERE filters rows, HAVING filters groups.
2. HAVING COUNT(*) > 5.

```sql
SELECT d.DepartmentName, COUNT(*) AS EmployeeCount
FROM Employees e
JOIN Departments d ON d.DepartmentId = e.DepartmentId
GROUP BY d.DepartmentName
HAVING COUNT(*) > 5;
```

**Explanation:** HAVING runs after grouping so it can use aggregates; WHERE cannot.

### 37. [SUM] Calculate total revenue per product category. Revenue = Quantity * UnitPrice * (1 - Discount) from OrderItems. Highest first.

Hints:
1. Join OrderItems to Products for Category.
2. SUM the revenue expression and GROUP BY Category.

```sql
SELECT p.Category,
       SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
FROM OrderItems oi
JOIN Products p ON p.ProductId = oi.ProductId
GROUP BY p.Category
ORDER BY Revenue DESC;
```

**Explanation:** Aggregate an expression, not just a column. Use the price stored on the order line (historical price).

### 38. [Anti join] Find customers who have never placed an order.

Hints:
1. LEFT JOIN Orders and test for NULL, or use NOT EXISTS.
2. Avoid NOT IN if the subquery column can contain NULLs.

```sql
SELECT c.CustomerId, c.CustomerName
FROM Customers c
WHERE NOT EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerId = c.CustomerId);
```

**Explanation:** NOT EXISTS is NULL-safe and usually optimises well.

### 39. [Anti join] Find products that have never been ordered.

Hints:
1. Same pattern as the previous question, on OrderItems.

```sql
SELECT p.ProductId, p.ProductName
FROM Products p
LEFT JOIN OrderItems oi ON oi.ProductId = p.ProductId
WHERE oi.OrderItemId IS NULL;
```

**Explanation:** LEFT JOIN ... IS NULL on the right table's primary key.

### 40. [Date functions] Show the number of orders per month for 2024 (year, month, order count), in calendar order.

Hints:
1. Use YEAR() and MONTH() or DATEPART.
2. Group by both and order by them.

```sql
SELECT YEAR(OrderDate) AS Yr, MONTH(OrderDate) AS Mth, COUNT(*) AS Orders
FROM Orders
WHERE OrderDate >= '2024-01-01' AND OrderDate < '2025-01-01'
GROUP BY YEAR(OrderDate), MONTH(OrderDate)
ORDER BY Yr, Mth;
```

**Explanation:** Group by the same expressions you select. EOMONTH or FORMAT could also be used.

### 41. [MIN / MAX] For each department show headcount, minimum, maximum and average salary.

Hints:
1. Several aggregates can be used in one query.

```sql
SELECT d.DepartmentName,
       COUNT(*) AS Headcount,
       MIN(e.Salary) AS MinSalary,
       MAX(e.Salary) AS MaxSalary,
       AVG(e.Salary) AS AvgSalary
FROM Employees e
JOIN Departments d ON d.DepartmentId = e.DepartmentId
GROUP BY d.DepartmentName;
```

**Explanation:** Multiple aggregates over the same grouping is a single pass over the data.

### 42. [CASE] Classify employees into salary bands: 'Low' (< 70,000), 'Mid' (70,000-119,999), 'High' (>= 120,000) and count employees in each band.

Hints:
1. Use CASE to build the band.
2. GROUP BY the CASE expression (or wrap it in a subquery/CTE).

```sql
SELECT CASE WHEN Salary < 70000 THEN 'Low'
            WHEN Salary < 120000 THEN 'Mid'
            ELSE 'High' END AS Band,
       COUNT(*) AS Employees
FROM Employees
GROUP BY CASE WHEN Salary < 70000 THEN 'Low'
              WHEN Salary < 120000 THEN 'Mid'
              ELSE 'High' END;
```

**Explanation:** CASE evaluates top to bottom and returns the first match.

### 43. [Multi-table JOIN] Find the top 3 customers by total revenue (customer name and revenue).

Hints:
1. Customers -> Orders -> OrderItems.
2. SUM revenue, GROUP BY customer, ORDER BY DESC, TOP 3.

```sql
SELECT TOP 3 c.CustomerName,
       SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
FROM Customers c
JOIN Orders o ON o.CustomerId = c.CustomerId
JOIN OrderItems oi ON oi.OrderId = o.OrderId
GROUP BY c.CustomerId, c.CustomerName
ORDER BY Revenue DESC;
```

**Explanation:** Group by the key (CustomerId) as well as the name in case two customers share a name.

### 44. [GROUP BY] Show the number of orders per Status and what percentage of all orders each status represents (1 decimal).

Hints:
1. A scalar subquery (SELECT COUNT(*) FROM Orders) gives the total.
2. Multiply by 100.0 to avoid integer division.

```sql
SELECT Status,
       COUNT(*) AS Orders,
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM Orders), 1) AS Pct
FROM Orders
GROUP BY Status;
```

**Explanation:** Integer / integer is integer division in T-SQL, so use 100.0.

### 45. [Subquery] List employees who earn more than the company-wide average salary.

Hints:
1. Compare Salary with a subquery that returns AVG(Salary).

```sql
SELECT FirstName, LastName, Salary
FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees);
```

**Explanation:** A scalar subquery returns one value and can be used in a WHERE comparison.

### 46. [CROSS JOIN] Produce a grid of every product Category combined with every order Status (distinct values only).

Hints:
1. CROSS JOIN pairs every row of one set with every row of another.
2. Use two DISTINCT subqueries.

```sql
SELECT c.Category, s.Status
FROM (SELECT DISTINCT Category FROM Products) c
CROSS JOIN (SELECT DISTINCT Status FROM Orders) s
ORDER BY c.Category, s.Status;
```

**Explanation:** CROSS JOIN creates the Cartesian product - useful for building report skeletons that are later LEFT JOINed with facts.

### 47. [DATEDIFF] Show each employee's tenure in whole years as of 2025-12-31, for employees with at least 5 years of service.

Hints:
1. DATEDIFF(YEAR, start, end) counts year boundaries, not full years.
2. For full years compare against DATEADD(YEAR, 5, HireDate).

```sql
SELECT FirstName, LastName, HireDate,
       DATEDIFF(YEAR, HireDate, '2025-12-31') AS TenureYearsApprox
FROM Employees
WHERE DATEADD(YEAR, 5, HireDate) <= '2025-12-31'
ORDER BY HireDate;
```

**Explanation:** DATEDIFF(YEAR) counts calendar boundaries crossed (2024-12-31 to 2025-01-01 = 1). The DATEADD filter guarantees full 5 years.

### 48. [INNER JOIN] List first name, last name and department location for employees whose department is located in Singapore.

Hints:
1. Join Employees to Departments, filter on Location.

```sql
SELECT e.FirstName, e.LastName, d.Location
FROM Employees e
JOIN Departments d ON d.DepartmentId = e.DepartmentId
WHERE d.Location = 'Singapore';
```

**Explanation:** JOIN defaults to INNER JOIN.

### 49. [LEFT JOIN] Show every customer with their number of orders, including customers with none (0).

Hints:
1. LEFT JOIN Orders, then COUNT a column from Orders, not *.

```sql
SELECT c.CustomerName, COUNT(o.OrderId) AS OrderCount
FROM Customers c
LEFT JOIN Orders o ON o.CustomerId = c.CustomerId
GROUP BY c.CustomerId, c.CustomerName;
```

**Explanation:** COUNT(o.OrderId) ignores the NULLs produced for unmatched customers.

### 50. [SUM] Show the total quantity sold per product (product name and units), for the 5 best-selling products.

Hints:
1. Join OrderItems to Products and SUM(Quantity).
2. ORDER BY the sum DESC with TOP 5.

```sql
SELECT TOP 5 p.ProductName, SUM(oi.Quantity) AS UnitsSold
FROM OrderItems oi
JOIN Products p ON p.ProductId = oi.ProductId
GROUP BY p.ProductId, p.ProductName
ORDER BY UnitsSold DESC;
```

**Explanation:** Group by the product key plus name; ORDER BY can use the alias.

### 51. [AVG] Show the average discount (as a fraction) per product category.

Hints:
1. Join OrderItems to Products, AVG(Discount) by Category.

```sql
SELECT p.Category, AVG(oi.Discount) AS AvgDiscount
FROM OrderItems oi
JOIN Products p ON p.ProductId = oi.ProductId
GROUP BY p.Category;
```

**Explanation:** Discount is DECIMAL(4,2) so AVG keeps decimal precision.

### 52. [GROUP BY] How many employees were hired in each year? (year, count), oldest year first.

Hints:
1. YEAR(HireDate).

```sql
SELECT YEAR(HireDate) AS HireYear, COUNT(*) AS Hires
FROM Employees
GROUP BY YEAR(HireDate)
ORDER BY HireYear;
```

**Explanation:** You must repeat the expression in GROUP BY (aliases are not allowed there).

### 53. [HAVING] List countries that have at least 3 customers, with the customer count.

Hints:
1. GROUP BY Country with HAVING COUNT(*) >= 3.

```sql
SELECT Country, COUNT(*) AS Customers
FROM Customers
GROUP BY Country
HAVING COUNT(*) >= 3;
```

**Explanation:** HAVING filters groups after aggregation.

### 54. [GROUP BY] For each sales rep (employee who owns orders), show their name and number of orders. Ignore orders without a rep.

Hints:
1. INNER JOIN Orders to Employees removes the NULL EmployeeId rows.

```sql
SELECT e.FirstName, e.LastName, COUNT(*) AS Orders
FROM Orders o
JOIN Employees e ON e.EmployeeId = o.EmployeeId
GROUP BY e.EmployeeId, e.FirstName, e.LastName;
```

**Explanation:** NULL never equals anything, so unassigned orders drop out of the inner join.

### 55. [NULL] How many orders of each Status have no sales rep assigned?

Hints:
1. Filter EmployeeId IS NULL then GROUP BY Status.

```sql
SELECT Status, COUNT(*) AS Orders
FROM Orders
WHERE EmployeeId IS NULL
GROUP BY Status;
```

**Explanation:** WHERE runs before grouping.

### 56. [Subquery] List the employees who earn the highest salary in their own department (include ties).

Hints:
1. Compare Salary to MAX(Salary) of the same department.

```sql
SELECT e.FirstName, e.LastName, e.DepartmentId, e.Salary
FROM Employees e
WHERE e.Salary = (SELECT MAX(e2.Salary) FROM Employees e2 WHERE e2.DepartmentId = e.DepartmentId);
```

**Explanation:** Correlated subquery; employees with NULL department are excluded.

### 57. [UNION] Produce a single distinct list of cities that appear either as a customer city or as a department location.

Hints:
1. UNION removes duplicates.

```sql
SELECT City FROM Customers
UNION
SELECT Location FROM Departments;
```

**Explanation:** Column names come from the first SELECT; types must be compatible.

### 58. [INTERSECT] Which cities are both a customer city and a department location?

Hints:
1. INTERSECT returns rows present in both queries.

```sql
SELECT City FROM Customers
INTERSECT
SELECT Location FROM Departments;
```

**Explanation:** INTERSECT also removes duplicates.

### 59. [EXCEPT] Which customer cities are NOT department locations? (distinct)

Hints:
1. EXCEPT returns rows from the first query not found in the second.

```sql
SELECT City FROM Customers
EXCEPT
SELECT Location FROM Departments;
```

**Explanation:** Order matters for EXCEPT.

### 60. [String functions] Show each employee's initials (e.g. 'AT' for Alice Tan) together with their EmployeeId.

Hints:
1. LEFT(string, 1) and concatenation.

```sql
SELECT EmployeeId, LEFT(FirstName, 1) + LEFT(LastName, 1) AS Initials
FROM Employees;
```

**Explanation:** LEFT/RIGHT extract the first/last n characters.

### 61. [String functions] Extract the username part of each employee's email (text before '@'). Skip employees without an email.

Hints:
1. CHARINDEX('@', Email) finds the position.
2. LEFT(Email, position - 1).

```sql
SELECT EmployeeId, LEFT(Email, CHARINDEX('@', Email) - 1) AS UserName
FROM Employees
WHERE Email IS NOT NULL;
```

**Explanation:** CHARINDEX returns 0 when not found, which would make LEFT fail - hence the NULL filter.

### 62. [String functions] Show product names with spaces replaced by underscores.

Hints:
1. REPLACE(string, old, new).

```sql
SELECT ProductName, REPLACE(ProductName, ' ', '_') AS Slug
FROM Products;
```

**Explanation:** REPLACE is case-insensitive under the default collation.

### 63. [Date functions] How many orders were placed in each quarter of 2024? (quarter, orders)

Hints:
1. DATEPART(QUARTER, OrderDate).

```sql
SELECT DATEPART(QUARTER, OrderDate) AS Quarter, COUNT(*) AS Orders
FROM Orders
WHERE OrderDate >= '2024-01-01' AND OrderDate < '2025-01-01'
GROUP BY DATEPART(QUARTER, OrderDate)
ORDER BY Quarter;
```

**Explanation:** DATEPART returns an int; DATENAME returns text.

### 64. [Date functions] How many orders were placed on each day of the week (name of the weekday)?

Hints:
1. DATENAME(WEEKDAY, date).

```sql
SELECT DATENAME(WEEKDAY, OrderDate) AS Weekday, COUNT(*) AS Orders
FROM Orders
GROUP BY DATENAME(WEEKDAY, OrderDate);
```

**Explanation:** Weekday names depend on the session language (English here).

### 65. [JOIN] List orders placed in December 2024 with the customer name, order date and status.

Hints:
1. Join Orders to Customers and filter the date range.

```sql
SELECT o.OrderId, c.CustomerName, o.OrderDate, o.Status
FROM Orders o
JOIN Customers c ON c.CustomerId = o.CustomerId
WHERE o.OrderDate >= '2024-12-01' AND o.OrderDate < '2025-01-01';
```

**Explanation:** Half-open date ranges avoid end-of-month edge cases.

### 66. [TOP WITH TIES] List the 3 highest-priced products, including any products tied with the 3rd price.

Hints:
1. TOP (3) WITH TIES requires ORDER BY.

```sql
SELECT TOP (3) WITH TIES ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice DESC;
```

**Explanation:** WITH TIES returns extra rows that tie on the ORDER BY value of the last row.

### 67. [ISNULL] For Sales employees (DepartmentId 3) show total compensation = Salary * (1 + commission), treating a missing commission as 0.

Hints:
1. COALESCE/ISNULL(CommissionPct, 0).

```sql
SELECT FirstName, LastName, Salary * (1 + COALESCE(CommissionPct, 0)) AS TotalComp
FROM Employees
WHERE DepartmentId = 3;
```

**Explanation:** Any arithmetic with NULL yields NULL, so replace NULL first.

### 68. [GROUP BY] For each product category show the stock value (SUM of Stock * UnitPrice). Only show categories above 50,000.

Hints:
1. Aggregate an expression and filter with HAVING.

```sql
SELECT Category, SUM(Stock * UnitPrice) AS StockValue
FROM Products
GROUP BY Category
HAVING SUM(Stock * UnitPrice) > 50000;
```

**Explanation:** HAVING must repeat the aggregate expression (or wrap in a CTE).

### 69. [IIF] Label each product 'In stock' or 'Out of stock' based on Stock.

Hints:
1. IIF(condition, a, b) or CASE.

```sql
SELECT ProductName, IIF(Stock > 0, 'In stock', 'Out of stock') AS Availability
FROM Products;
```

**Explanation:** IIF is shorthand for a two-branch CASE.

### 70. [SUM] Show the 10 orders with the highest total value (OrderId and total).

Hints:
1. SUM revenue per OrderId, TOP 10.

```sql
SELECT TOP 10 oi.OrderId, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS OrderTotal
FROM OrderItems oi
GROUP BY oi.OrderId
ORDER BY OrderTotal DESC;
```

**Explanation:** Order totals are computed from order lines.

### 71. [HAVING] List customers who placed more than 10 orders (name and count).

Hints:
1. JOIN, GROUP BY, HAVING COUNT(*) > 10.

```sql
SELECT c.CustomerName, COUNT(*) AS Orders
FROM Customers c
JOIN Orders o ON o.CustomerId = c.CustomerId
GROUP BY c.CustomerId, c.CustomerName
HAVING COUNT(*) > 10;
```

**Explanation:** HAVING works on the grouped result.

### 72. [NOT EXISTS] Which products were not ordered at all in 2025?

Hints:
1. NOT EXISTS with a join between OrderItems and Orders inside.

```sql
SELECT p.ProductId, p.ProductName
FROM Products p
WHERE NOT EXISTS (
    SELECT 1 FROM OrderItems oi
    JOIN Orders o ON o.OrderId = oi.OrderId
    WHERE oi.ProductId = p.ProductId AND o.OrderDate >= '2025-01-01' AND o.OrderDate < '2026-01-01');
```

**Explanation:** NOT EXISTS handles the 'never ordered' and 'not ordered in period' cases uniformly.

### 73. [Derived table] What is the average number of line items per order?

Hints:
1. Count lines per order in a derived table, then AVG.

```sql
SELECT AVG(Lines * 1.0) AS AvgLines
FROM (SELECT OrderId, COUNT(*) AS Lines FROM OrderItems GROUP BY OrderId) x;
```

**Explanation:** Multiply by 1.0 to avoid integer averaging.

### 74. [HAVING] Which job titles are held by more than one employee? (title, count)

Hints:
1. GROUP BY JobTitle HAVING COUNT(*) > 1.

```sql
SELECT JobTitle, COUNT(*) AS Employees
FROM Employees
GROUP BY JobTitle
HAVING COUNT(*) > 1;
```

**Explanation:** A classic duplicate-detection pattern.

### 75. [Self join] List each manager's name with their number of direct reports (managers only).

Hints:
1. Join Employees to itself on ManagerId, group by the manager.

```sql
SELECT m.FirstName, m.LastName, COUNT(*) AS DirectReports
FROM Employees e
JOIN Employees m ON m.EmployeeId = e.ManagerId
GROUP BY m.EmployeeId, m.FirstName, m.LastName;
```

**Explanation:** The inner join drops employees without a manager (the CEO and Iris), and only people with at least one report appear.

### 76. [NOT EXISTS] List employees who do not manage anyone.

Hints:
1. NOT EXISTS on Employees.ManagerId.

```sql
SELECT e.EmployeeId, e.FirstName, e.LastName
FROM Employees e
WHERE NOT EXISTS (SELECT 1 FROM Employees r WHERE r.ManagerId = e.EmployeeId);
```

**Explanation:** Anti-join pattern again.

### 77. [Self join] Find pairs of different employees in the same department who earn exactly the same salary (each pair once).

Hints:
1. Self join with e1.EmployeeId < e2.EmployeeId.

```sql
SELECT e1.FirstName + ' ' + e1.LastName AS Employee1, e2.FirstName + ' ' + e2.LastName AS Employee2, e1.Salary
FROM Employees e1
JOIN Employees e2 ON e1.DepartmentId = e2.DepartmentId AND e1.Salary = e2.Salary AND e1.EmployeeId < e2.EmployeeId;
```

**Explanation:** The < condition removes mirrored and self pairs.

### 78. [GROUP BY] How many customers signed up in each year?

Hints:
1. GROUP BY YEAR(SignupDate).

```sql
SELECT YEAR(SignupDate) AS SignupYear, COUNT(*) AS Customers
FROM Customers
GROUP BY YEAR(SignupDate)
ORDER BY SignupYear;
```

**Explanation:** Same pattern as hires per year.

### 79. [SUM] Show total revenue per calendar year.

Hints:
1. Join Orders and OrderItems, group by YEAR(OrderDate).

```sql
SELECT YEAR(o.OrderDate) AS Yr, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
FROM Orders o
JOIN OrderItems oi ON oi.OrderId = o.OrderId
GROUP BY YEAR(o.OrderDate)
ORDER BY Yr;
```

**Explanation:** Revenue = Quantity * UnitPrice * (1 - Discount).

### 80. [Multi-table JOIN] Show total revenue per customer country.

Hints:
1. Customers -> Orders -> OrderItems.

```sql
SELECT c.Country, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
FROM Customers c
JOIN Orders o ON o.CustomerId = c.CustomerId
JOIN OrderItems oi ON oi.OrderId = o.OrderId
GROUP BY c.Country
ORDER BY Revenue DESC;
```

**Explanation:** Chain joins along foreign keys.

### 81. [SUM] Which 3 customers lost the most revenue to Cancelled orders? (customer name, cancelled revenue)

Hints:
1. Filter Status = 'Cancelled' before aggregating.

```sql
SELECT TOP 3 c.CustomerName, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS CancelledRevenue
FROM Customers c
JOIN Orders o ON o.CustomerId = c.CustomerId
JOIN OrderItems oi ON oi.OrderId = o.OrderId
WHERE o.Status = 'Cancelled'
GROUP BY c.CustomerId, c.CustomerName
ORDER BY CancelledRevenue DESC;
```

**Explanation:** Filtering in WHERE keeps only cancelled orders.

### 82. [HAVING] For job titles held by at least 2 employees, show the average salary.

Hints:
1. HAVING COUNT(*) >= 2 together with AVG.

```sql
SELECT JobTitle, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY JobTitle
HAVING COUNT(*) >= 2;
```

**Explanation:** Multiple aggregates may appear in SELECT and HAVING.

### 83. [Correlated subquery] List products priced above the average price of their own category.

Hints:
1. Correlated AVG subquery on Category.

```sql
SELECT p.ProductName, p.Category, p.UnitPrice
FROM Products p
WHERE p.UnitPrice > (SELECT AVG(p2.UnitPrice) FROM Products p2 WHERE p2.Category = p.Category);
```

**Explanation:** The subquery is re-evaluated (logically) per outer row.

### 84. [COUNT DISTINCT] For each sales rep, how many distinct customers have they sold to?

Hints:
1. COUNT(DISTINCT CustomerId).

```sql
SELECT e.FirstName, e.LastName, COUNT(DISTINCT o.CustomerId) AS Customers
FROM Orders o
JOIN Employees e ON e.EmployeeId = o.EmployeeId
GROUP BY e.EmployeeId, e.FirstName, e.LastName;
```

**Explanation:** COUNT(DISTINCT) vs COUNT(*) is a frequent interview trap.

### 85. [HAVING] Which employees have exactly 3 records in SalaryHistory?

Hints:
1. GROUP BY EmployeeId HAVING COUNT(*) = 3.

```sql
SELECT EmployeeId, COUNT(*) AS Records
FROM SalaryHistory
GROUP BY EmployeeId
HAVING COUNT(*) = 3;
```

**Explanation:** Employees hired recently have fewer history rows.

### 86. [SUM] Which products gave away more than 1,000 in total discounts (Quantity * UnitPrice * Discount)?

Hints:
1. SUM the discount amount and HAVING > 1000.

```sql
SELECT p.ProductName, SUM(oi.Quantity * oi.UnitPrice * oi.Discount) AS DiscountGiven
FROM OrderItems oi
JOIN Products p ON p.ProductId = oi.ProductId
GROUP BY p.ProductId, p.ProductName
HAVING SUM(oi.Quantity * oi.UnitPrice * oi.Discount) > 1000;
```

**Explanation:** Discount value = list value minus net revenue.

### 87. [Self join] List employees whose manager works in a different department (employee, employee dept, manager dept).

Hints:
1. Self join then compare DepartmentId.

```sql
SELECT e.FirstName, e.LastName, e.DepartmentId AS EmpDept, m.DepartmentId AS MgrDept
FROM Employees e
JOIN Employees m ON m.EmployeeId = e.ManagerId
WHERE e.DepartmentId <> m.DepartmentId;
```

**Explanation:** Rows with NULL in either department are excluded because NULL <> x is unknown.

### 88. [COUNT DISTINCT] For each customer, how many distinct products have they ever ordered?

Hints:
1. Join Orders and OrderItems.

```sql
SELECT c.CustomerName, COUNT(DISTINCT oi.ProductId) AS Products
FROM Customers c
JOIN Orders o ON o.CustomerId = c.CustomerId
JOIN OrderItems oi ON oi.OrderId = o.OrderId
GROUP BY c.CustomerId, c.CustomerName;
```

**Explanation:** Distinct is needed because a product can repeat across orders.

### 89. [STRING_AGG] For each department, list its employees' first names as one comma-separated string sorted alphabetically.

Hints:
1. STRING_AGG(FirstName, ',') WITHIN GROUP (ORDER BY FirstName).

```sql
SELECT d.DepartmentName, STRING_AGG(e.FirstName, ',') WITHIN GROUP (ORDER BY e.FirstName) AS Employees
FROM Departments d
JOIN Employees e ON e.DepartmentId = d.DepartmentId
GROUP BY d.DepartmentName;
```

**Explanation:** STRING_AGG needs WITHIN GROUP for deterministic order.

### 90. [Metadata] List each table in the database with its number of columns (use INFORMATION_SCHEMA.COLUMNS).

Hints:
1. GROUP BY TABLE_NAME.

```sql
SELECT TABLE_NAME, COUNT(*) AS ColumnCount
FROM INFORMATION_SCHEMA.COLUMNS
GROUP BY TABLE_NAME;
```

**Explanation:** INFORMATION_SCHEMA views are ANSI-standard metadata.


## Hard

### 91. [UNION] Create a single list of names with a Type column: all employees (Type='Employee') and all customers (Type='Customer').

Hints:
1. UNION ALL stacks result sets with matching column counts/types.
2. Use a literal for the Type column.

```sql
SELECT FirstName + ' ' + LastName AS Name, 'Employee' AS Type FROM Employees
UNION ALL
SELECT CustomerName, 'Customer' FROM Customers;
```

**Explanation:** UNION removes duplicates (and sorts/hashes); UNION ALL keeps everything and is faster.

### 92. [Correlated subquery] Find employees who earn more than the average salary of their own department.

Hints:
1. The subquery must reference the outer row.
2. Or compute department averages with a window function.

```sql
SELECT e.FirstName, e.LastName, e.DepartmentId, e.Salary
FROM Employees e
WHERE e.Salary > (SELECT AVG(e2.Salary)
                  FROM Employees e2
                  WHERE e2.DepartmentId = e.DepartmentId);
```

**Explanation:** Alternative: SELECT ..., AVG(Salary) OVER (PARTITION BY DepartmentId) in a CTE and filter on it. Employees with NULL department are excluded because NULL = NULL is not true.

### 93. [EXISTS] List customers who have at least one cancelled order.

Hints:
1. EXISTS stops at the first match.
2. Correlate the subquery on CustomerId.

```sql
SELECT c.CustomerId, c.CustomerName
FROM Customers c
WHERE EXISTS (SELECT 1 FROM Orders o
              WHERE o.CustomerId = c.CustomerId AND o.Status = 'Cancelled');
```

**Explanation:** EXISTS avoids duplicates that an INNER JOIN would produce for customers with several cancelled orders.

### 94. [CTE] Using a CTE, compute revenue per month (exclude Cancelled orders) and list only the months whose revenue is above the average monthly revenue.

Hints:
1. Build monthly revenue in a CTE.
2. Compare against (SELECT AVG(Revenue) FROM cte).

```sql
WITH Monthly AS (
    SELECT DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1) AS MonthStart,
           SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Orders o
    JOIN OrderItems oi ON oi.OrderId = o.OrderId
    WHERE o.Status <> 'Cancelled'
    GROUP BY DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1)
)
SELECT MonthStart, Revenue
FROM Monthly
WHERE Revenue > (SELECT AVG(Revenue) FROM Monthly)
ORDER BY MonthStart;
```

**Explanation:** A CTE names an intermediate result so it can be reused and read top-down. It is not materialised - it is inlined like a view.

### 95. [Multiple CTEs] For each customer show their total revenue and their share (%) of overall revenue, largest share first. Use two CTEs.

Hints:
1. CTE 1: revenue per customer.
2. CTE 2: total revenue; CROSS JOIN it to divide.

```sql
WITH CustRev AS (
    SELECT o.CustomerId,
           SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Orders o
    JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.CustomerId
), Total AS (
    SELECT SUM(Revenue) AS Total FROM CustRev
)
SELECT c.CustomerName,
       cr.Revenue,
       ROUND(100.0 * cr.Revenue / t.Total, 2) AS SharePct
FROM CustRev cr
JOIN Customers c ON c.CustomerId = cr.CustomerId
CROSS JOIN Total t
ORDER BY SharePct DESC;
```

**Explanation:** CTEs can reference earlier CTEs in the same WITH clause. Window alternative: SUM(Revenue) OVER ().

### 96. [Recursive CTE] Display the organisation hierarchy starting from the CEO (EmployeeId = 1): employee name, level (CEO = 0) and manager id.

Hints:
1. A recursive CTE has an anchor member and a recursive member joined with UNION ALL.
2. Recursive part joins Employees to the CTE on ManagerId = cte.EmployeeId and adds 1 to the level.

```sql
WITH Org AS (
    SELECT EmployeeId, FirstName, LastName, ManagerId, 0 AS Level
    FROM Employees
    WHERE EmployeeId = 1
    UNION ALL
    SELECT e.EmployeeId, e.FirstName, e.LastName, e.ManagerId, o.Level + 1
    FROM Employees e
    JOIN Org o ON e.ManagerId = o.EmployeeId
)
SELECT EmployeeId, FirstName + ' ' + LastName AS Name, Level, ManagerId
FROM Org
ORDER BY Level, EmployeeId;
```

**Explanation:** Default MAXRECURSION is 100; guard against cycles in real data. Employees such as Iris (no manager) are not reachable from the CEO, so they do not appear.

### 97. [Recursive CTE] For every employee in the CEO's hierarchy, build the reporting chain as text, e.g. 'Alice > Bob > Grace > Ivy'.

Hints:
1. Carry a path string in the recursive CTE.
2. Concatenate the parent path with ' > ' and the current first name.

```sql
WITH Chain AS (
    SELECT EmployeeId, CAST(FirstName AS NVARCHAR(400)) AS Path
    FROM Employees WHERE EmployeeId = 1
    UNION ALL
    SELECT e.EmployeeId, CAST(c.Path + N' > ' + e.FirstName AS NVARCHAR(400))
    FROM Employees e
    JOIN Chain c ON e.ManagerId = c.EmployeeId
)
SELECT EmployeeId, Path FROM Chain ORDER BY Path;
```

**Explanation:** Both members of a recursive CTE must have identical column types, so CAST the anchor to the final width.

### 98. [ROW_NUMBER] Find the highest paid employee in each department (ignore employees without a department). Break ties by lowest EmployeeId.

Hints:
1. ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...).
2. Filter rn = 1 in an outer query or CTE - you cannot use a window function in WHERE.

```sql
WITH Ranked AS (
    SELECT e.*, ROW_NUMBER() OVER (PARTITION BY e.DepartmentId ORDER BY e.Salary DESC, e.EmployeeId) AS rn
    FROM Employees e
    WHERE e.DepartmentId IS NOT NULL
)
SELECT d.DepartmentName, r.FirstName, r.LastName, r.Salary
FROM Ranked r
JOIN Departments d ON d.DepartmentId = r.DepartmentId
WHERE r.rn = 1;
```

**Explanation:** Window functions are evaluated after WHERE/GROUP BY, so filtering needs a CTE or subquery.

### 99. [RANK / DENSE_RANK] Rank employees by salary within their department showing both RANK and DENSE_RANK (call them SalaryRank and SalaryDenseRank). Show Engineering only (DepartmentId = 2).

Hints:
1. Both functions use OVER (PARTITION BY ... ORDER BY Salary DESC).
2. Look at how ties (equal salaries) are numbered.

```sql
SELECT FirstName, LastName, Salary,
       RANK()       OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS SalaryRank,
       DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS SalaryDenseRank
FROM Employees
WHERE DepartmentId = 2
ORDER BY Salary DESC;
```

**Explanation:** RANK leaves gaps after ties (1,2,2,4); DENSE_RANK does not (1,2,2,3); ROW_NUMBER never ties.

### 100. [Running total] Show monthly revenue together with a running (cumulative) total, ordered by month. Exclude Cancelled orders.

Hints:
1. Aggregate by month first (CTE).
2. SUM(Revenue) OVER (ORDER BY MonthStart ROWS UNBOUNDED PRECEDING).

```sql
WITH Monthly AS (
    SELECT DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1) AS MonthStart,
           SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Orders o
    JOIN OrderItems oi ON oi.OrderId = o.OrderId
    WHERE o.Status <> 'Cancelled'
    GROUP BY DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1)
)
SELECT MonthStart, Revenue,
       SUM(Revenue) OVER (ORDER BY MonthStart ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS RunningTotal
FROM Monthly
ORDER BY MonthStart;
```

**Explanation:** Specify ROWS explicitly; the default RANGE frame is slower and treats ties differently.

### 101. [LAG] Using SalaryHistory, show each salary change per employee with the previous salary and the percentage increase (1 decimal). Only rows that have a previous salary, for employees 9, 10 and 11.

Hints:
1. LAG(Salary) OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate).
2. Filter on a non-NULL previous salary in an outer query.

```sql
WITH H AS (
    SELECT EmployeeId, EffectiveDate, Salary,
           LAG(Salary) OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate) AS PrevSalary
    FROM SalaryHistory
)
SELECT EmployeeId, EffectiveDate, PrevSalary, Salary,
       ROUND(100.0 * (Salary - PrevSalary) / PrevSalary, 1) AS PctIncrease
FROM H
WHERE PrevSalary IS NOT NULL AND EmployeeId IN (9, 10, 11)
ORDER BY EmployeeId, EffectiveDate;
```

**Explanation:** LAG/LEAD access previous/next rows without a self join. A third argument supplies a default instead of NULL.

### 102. [Conditional aggregation] Find customers whose 2024 revenue is higher than their 2023 revenue. Show both amounts.

Hints:
1. SUM(CASE WHEN YEAR(OrderDate)=2023 THEN ... END).
2. Use HAVING to compare the two conditional sums.

```sql
SELECT c.CustomerName,
       SUM(CASE WHEN YEAR(o.OrderDate) = 2023 THEN oi.Quantity * oi.UnitPrice * (1 - oi.Discount) ELSE 0 END) AS Rev2023,
       SUM(CASE WHEN YEAR(o.OrderDate) = 2024 THEN oi.Quantity * oi.UnitPrice * (1 - oi.Discount) ELSE 0 END) AS Rev2024
FROM Customers c
JOIN Orders o ON o.CustomerId = c.CustomerId
JOIN OrderItems oi ON oi.OrderId = o.OrderId
GROUP BY c.CustomerId, c.CustomerName
HAVING SUM(CASE WHEN YEAR(o.OrderDate) = 2024 THEN oi.Quantity * oi.UnitPrice * (1 - oi.Discount) ELSE 0 END)
     > SUM(CASE WHEN YEAR(o.OrderDate) = 2023 THEN oi.Quantity * oi.UnitPrice * (1 - oi.Discount) ELSE 0 END)
ORDER BY c.CustomerName;
```

**Explanation:** Conditional aggregation pivots rows to columns in a single scan.

### 103. [PIVOT] Show revenue by product Category (rows) and by year 2023, 2024, 2025 (columns).

Hints:
1. PIVOT needs the source rows shaped as (Category, Year, Revenue).
2. PIVOT(SUM(Revenue) FOR Yr IN ([2023],[2024],[2025])).

```sql
SELECT Category, [2023], [2024], [2025]
FROM (
    SELECT p.Category, YEAR(o.OrderDate) AS Yr,
           oi.Quantity * oi.UnitPrice * (1 - oi.Discount) AS Revenue
    FROM OrderItems oi
    JOIN Orders o   ON o.OrderId = oi.OrderId
    JOIN Products p ON p.ProductId = oi.ProductId
) src
PIVOT (SUM(Revenue) FOR Yr IN ([2023], [2024], [2025])) pvt
ORDER BY Category;
```

**Explanation:** The pivot columns must be hard-coded unless you build dynamic SQL. The CASE-based approach from the previous question is equivalent.

### 104. [NTILE] Split employees into 4 salary quartiles (1 = highest paid). Show name, salary and quartile. Break salary ties by EmployeeId.

Hints:
1. NTILE(4) OVER (ORDER BY Salary DESC, EmployeeId).

```sql
SELECT FirstName, LastName, Salary,
       NTILE(4) OVER (ORDER BY Salary DESC, EmployeeId) AS Quartile
FROM Employees;
```

**Explanation:** NTILE distributes rows into near-equal buckets; with 40 rows each bucket has 10.

### 105. [LEAD] For customer 1, list each order date and the number of days until their next order (NULL for the last).

Hints:
1. LEAD(OrderDate) OVER (ORDER BY OrderDate).

```sql
SELECT OrderId, OrderDate,
       DATEDIFF(DAY, OrderDate, LEAD(OrderDate) OVER (ORDER BY OrderDate)) AS DaysToNext
FROM Orders
WHERE CustomerId = 1;
```

**Explanation:** The WHERE clause is applied before the window function, so LEAD sees only customer 1's rows.

### 106. [FIRST_VALUE] Show every employee with the name of the highest-paid person in their department (employees with a department only).

Hints:
1. FIRST_VALUE(name) OVER (PARTITION BY DepartmentId ORDER BY Salary DESC).

```sql
SELECT FirstName, LastName, DepartmentId, Salary,
       FIRST_VALUE(FirstName) OVER (PARTITION BY DepartmentId ORDER BY Salary DESC, EmployeeId) AS TopEarner
FROM Employees
WHERE DepartmentId IS NOT NULL;
```

**Explanation:** Add a tie-breaker to the window ORDER BY so the result is deterministic.

### 107. [Running total] For customer 5, list orders with a running count of orders so far and a running total of order value (by order date).

Hints:
1. Build order totals in a CTE, then use SUM() OVER with ROWS.

```sql
WITH OT AS (
    SELECT o.OrderId, o.CustomerId, o.OrderDate, o.Status, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Total
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.OrderId, o.CustomerId, o.OrderDate, o.Status
)
SELECT OrderId, OrderDate, Total,
       ROW_NUMBER() OVER (ORDER BY OrderDate) AS OrderNo,
       SUM(Total) OVER (ORDER BY OrderDate ROWS UNBOUNDED PRECEDING) AS RunningTotal
FROM OT
WHERE CustomerId = 5;
```

**Explanation:** Dates are unique per order, so the running window is unambiguous.

### 108. [Window SUM] Show each employee's salary as a percentage of their department's total salary (2 decimals). Only employees with a department.

Hints:
1. SUM(Salary) OVER (PARTITION BY DepartmentId).

```sql
SELECT FirstName, LastName, DepartmentId, Salary,
       ROUND(100.0 * Salary / SUM(Salary) OVER (PARTITION BY DepartmentId), 2) AS PctOfDept
FROM Employees
WHERE DepartmentId IS NOT NULL;
```

**Explanation:** Window aggregates avoid a self join with a GROUP BY subquery.

### 109. [PERCENT_RANK] Show each employee's PERCENT_RANK of salary across the company (rounded to 3 decimals).

Hints:
1. PERCENT_RANK() OVER (ORDER BY Salary).

```sql
SELECT FirstName, LastName, Salary,
       ROUND(PERCENT_RANK() OVER (ORDER BY Salary), 3) AS PctRank
FROM Employees;
```

**Explanation:** PERCENT_RANK = (rank - 1) / (rows - 1); the lowest value is 0.

### 110. [CUME_DIST] Show each employee's cumulative distribution of salary (rounded to 3 decimals) across the company.

Hints:
1. CUME_DIST() OVER (ORDER BY Salary).

```sql
SELECT FirstName, LastName, Salary,
       ROUND(CUME_DIST() OVER (ORDER BY Salary), 3) AS CumeDist
FROM Employees;
```

**Explanation:** CUME_DIST = share of rows with value <= current, so the maximum is 1.

### 111. [Window AVG] Show each employee's salary, their department average and the difference from it (employees with a department).

Hints:
1. AVG(Salary) OVER (PARTITION BY DepartmentId).

```sql
SELECT FirstName, LastName, DepartmentId, Salary,
       AVG(Salary) OVER (PARTITION BY DepartmentId) AS DeptAvg,
       Salary - AVG(Salary) OVER (PARTITION BY DepartmentId) AS Diff
FROM Employees
WHERE DepartmentId IS NOT NULL;
```

**Explanation:** You cannot reference the alias DeptAvg in the same SELECT list.

### 112. [CTE] Using a CTE, list customers whose total revenue is above the average customer revenue.

Hints:
1. CTE of revenue per customer, compare to its AVG.

```sql
WITH CustRev AS (
    SELECT o.CustomerId, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.CustomerId
)
SELECT c.CustomerName, cr.Revenue
FROM CustRev cr JOIN Customers c ON c.CustomerId = cr.CustomerId
WHERE cr.Revenue > (SELECT AVG(Revenue) FROM CustRev);
```

**Explanation:** Customers without orders are not in the average, which is usually what is wanted.

### 113. [DENSE_RANK] Return the top 5 revenue-ranked products (DENSE_RANK on total revenue, highest = 1).

Hints:
1. CTE with SUM then DENSE_RANK; filter <= 5.

```sql
WITH P AS (
    SELECT p.ProductName, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM OrderItems oi JOIN Products p ON p.ProductId = oi.ProductId
    GROUP BY p.ProductId, p.ProductName
)
SELECT ProductName, Revenue, DENSE_RANK() OVER (ORDER BY Revenue DESC) AS Rnk
FROM P
ORDER BY Rnk
OFFSET 0 ROWS FETCH NEXT 5 ROWS ONLY;
```

**Explanation:** Revenue totals are distinct so DENSE_RANK equals ROW_NUMBER here; you can filter in an outer query too.

### 114. [Recursive CTE] Generate the numbers 1 to 10 with a recursive CTE.

Hints:
1. Anchor SELECT 1, recursive part n + 1 WHERE n < 10.

```sql
WITH Nums AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM Nums WHERE n < 10
)
SELECT n FROM Nums;
```

**Explanation:** Always include a termination condition; MAXRECURSION defaults to 100.

### 115. [Recursive CTE] List every direct and indirect subordinate of Grace Ong (EmployeeId 7): id, name and level below Grace.

Hints:
1. Anchor: direct reports of 7 at level 1.

```sql
WITH Sub AS (
    SELECT EmployeeId, FirstName, LastName, 1 AS Level FROM Employees WHERE ManagerId = 7
    UNION ALL
    SELECT e.EmployeeId, e.FirstName, e.LastName, s.Level + 1
    FROM Employees e JOIN Sub s ON e.ManagerId = s.EmployeeId
)
SELECT EmployeeId, FirstName + ' ' + LastName AS Name, Level FROM Sub;
```

**Explanation:** Grace's team has no managers below her, so all rows are at level 1.

### 116. [Recursive CTE] How many people (direct and indirect) report up to Carol Wong (EmployeeId 3)?

Hints:
1. Recursive CTE from ManagerId = 3, then COUNT(*).

```sql
WITH Sub AS (
    SELECT EmployeeId FROM Employees WHERE ManagerId = 3
    UNION ALL
    SELECT e.EmployeeId FROM Employees e JOIN Sub s ON e.ManagerId = s.EmployeeId
)
SELECT COUNT(*) AS TotalReports FROM Sub;
```

**Explanation:** Counts the whole subtree below the root.

### 117. [Recursive CTE] Produce one row per day of January 2024 with the number of orders on that day (0 if none).

Hints:
1. Generate dates recursively, then LEFT JOIN Orders.

```sql
WITH D AS (
    SELECT CAST('2024-01-01' AS DATE) AS d
    UNION ALL
    SELECT DATEADD(DAY, 1, d) FROM D WHERE d < '2024-01-31'
)
SELECT D.d AS OrderDay, COUNT(o.OrderId) AS Orders
FROM D LEFT JOIN Orders o ON o.OrderDate = D.d
GROUP BY D.d
ORDER BY D.d;
```

**Explanation:** A calendar CTE fills gaps that a plain GROUP BY would miss.

### 118. [Recursive CTE] What is the maximum depth (levels below the CEO) of the organisation hierarchy, and how many employees are at each level?

Hints:
1. Recursive CTE from the CEO with a Level column, then GROUP BY Level.

```sql
WITH Org AS (
    SELECT EmployeeId, 0 AS Level FROM Employees WHERE ManagerId IS NULL AND EmployeeId = 1
    UNION ALL
    SELECT e.EmployeeId, o.Level + 1 FROM Employees e JOIN Org o ON e.ManagerId = o.EmployeeId
)
SELECT Level, COUNT(*) AS Employees FROM Org GROUP BY Level ORDER BY Level;
```

**Explanation:** The maximum depth is the highest Level value returned.

### 119. [CROSS APPLY] For each customer, show their 2 most recent orders (customer, order id, order date).

Hints:
1. CROSS APPLY (SELECT TOP 2 ... ORDER BY OrderDate DESC).

```sql
SELECT c.CustomerName, x.OrderId, x.OrderDate
FROM Customers c
CROSS APPLY (SELECT TOP 2 o.OrderId, o.OrderDate FROM Orders o WHERE o.CustomerId = c.CustomerId ORDER BY o.OrderDate DESC) x;
```

**Explanation:** CROSS APPLY drops customers with no orders; OUTER APPLY keeps them.

### 120. [OUTER APPLY] List all customers with the date of their most recent order (NULL if none).

Hints:
1. OUTER APPLY with TOP 1.

```sql
SELECT c.CustomerName, x.OrderDate AS LastOrderDate
FROM Customers c
OUTER APPLY (SELECT TOP 1 o.OrderDate FROM Orders o WHERE o.CustomerId = c.CustomerId ORDER BY o.OrderDate DESC) x;
```

**Explanation:** A simpler alternative is LEFT JOIN with MAX(OrderDate).

### 121. [PIVOT] Show the number of orders per year (rows) split by Status (columns Delivered, Shipped, Pending, Cancelled).

Hints:
1. Select Year and Status first, then PIVOT(COUNT(Status) FOR Status IN (...)).

```sql
SELECT Yr, [Delivered], [Shipped], [Pending], [Cancelled]
FROM (SELECT YEAR(OrderDate) AS Yr, Status FROM Orders) s
PIVOT (COUNT(Status) FOR Status IN ([Delivered], [Shipped], [Pending], [Cancelled])) p
ORDER BY Yr;
```

**Explanation:** Non-pivoted columns in the source become the grouping columns.

### 122. [UNPIVOT] Show the salary statistics (minimum, maximum, average) of Employees as three rows: Stat and Value.

Hints:
1. Compute the stats in one row, cast them to one type, and UNPIVOT.

```sql
SELECT Stat, Value
FROM (SELECT CAST(MIN(Salary) AS DECIMAL(12,2)) AS Minimum, CAST(MAX(Salary) AS DECIMAL(12,2)) AS Maximum, CAST(AVG(Salary) AS DECIMAL(12,2)) AS Average FROM Employees) s
UNPIVOT (Value FOR Stat IN (Minimum, Maximum, Average)) u;
```

**Explanation:** UNPIVOT requires all columns to share one data type.

### 123. [Conditional aggregation] For each department show the number of employees earning at least 100,000 and the number earning less.

Hints:
1. SUM(CASE WHEN ... THEN 1 ELSE 0 END).

```sql
SELECT d.DepartmentName,
       SUM(CASE WHEN e.Salary >= 100000 THEN 1 ELSE 0 END) AS HighEarners,
       SUM(CASE WHEN e.Salary <  100000 THEN 1 ELSE 0 END) AS Others
FROM Departments d JOIN Employees e ON e.DepartmentId = d.DepartmentId
GROUP BY d.DepartmentName;
```

**Explanation:** Conditional aggregation produces several counts in one scan.

### 124. [Relational division] Which customers have bought products from every product category?

Hints:
1. Count distinct categories per customer and compare with the total number of categories.

```sql
SELECT c.CustomerName
FROM Customers c
JOIN Orders o ON o.CustomerId = c.CustomerId
JOIN OrderItems oi ON oi.OrderId = o.OrderId
JOIN Products p ON p.ProductId = oi.ProductId
GROUP BY c.CustomerId, c.CustomerName
HAVING COUNT(DISTINCT p.Category) = (SELECT COUNT(DISTINCT Category) FROM Products);
```

**Explanation:** This 'for all' pattern is called relational division.

### 125. [INTERSECT] Which customers placed orders in both 2023 and 2025? (customer id)

Hints:
1. INTERSECT two queries filtered by year.

```sql
SELECT CustomerId FROM Orders WHERE YEAR(OrderDate) = 2023
INTERSECT
SELECT CustomerId FROM Orders WHERE YEAR(OrderDate) = 2025;
```

**Explanation:** Could also use two EXISTS clauses.

### 126. [EXCEPT] Using EXCEPT, which customers (CustomerId) have never placed an order?

Hints:
1. EXCEPT between all customer ids and customer ids that appear in Orders.

```sql
SELECT CustomerId FROM Customers
EXCEPT
SELECT CustomerId FROM Orders;
```

**Explanation:** EXCEPT returns distinct rows from the left set not found in the right set; NOT EXISTS is an equivalent alternative.

### 127. [LAG] Show monthly revenue (non-cancelled orders) with the previous month's revenue and the % change (2 decimals).

Hints:
1. Monthly CTE then LAG(Revenue) OVER (ORDER BY MonthStart).

```sql
WITH M AS (
    SELECT DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1) AS MonthStart, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    WHERE o.Status <> 'Cancelled'
    GROUP BY DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1)
)
SELECT MonthStart, Revenue,
       LAG(Revenue) OVER (ORDER BY MonthStart) AS PrevRevenue,
       ROUND(100.0 * (Revenue - LAG(Revenue) OVER (ORDER BY MonthStart)) / LAG(Revenue) OVER (ORDER BY MonthStart), 2) AS PctChange
FROM M
ORDER BY MonthStart;
```

**Explanation:** 'Previous' means the previous month that has data, not necessarily the previous calendar month.

### 128. [LAG] Show revenue per product category per year together with the previous year's revenue for the same category.

Hints:
1. PARTITION BY Category ORDER BY Yr in LAG.

```sql
WITH CY AS (
    SELECT p.Category, YEAR(o.OrderDate) AS Yr, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM OrderItems oi
    JOIN Orders o ON o.OrderId = oi.OrderId
    JOIN Products p ON p.ProductId = oi.ProductId
    GROUP BY p.Category, YEAR(o.OrderDate)
)
SELECT Category, Yr, Revenue,
       LAG(Revenue) OVER (PARTITION BY Category ORDER BY Yr) AS PrevYearRevenue
FROM CY;
```

**Explanation:** PARTITION BY restarts the LAG for each category.

### 129. [Self join] List employees who earn at least 80% of their manager's salary.

Hints:
1. Self join and compare e.Salary with 0.8 * m.Salary.

```sql
SELECT e.FirstName, e.LastName, e.Salary, m.FirstName AS Manager, m.Salary AS ManagerSalary
FROM Employees e JOIN Employees m ON m.EmployeeId = e.ManagerId
WHERE e.Salary >= 0.8 * m.Salary;
```

**Explanation:** Self joins compare an employee to their manager; employees without a manager drop out of the inner join.

### 130. [HAVING] List departments whose average salary is higher than the company-wide average salary.

Hints:
1. HAVING AVG(...) > (SELECT AVG(...)).

```sql
SELECT d.DepartmentName, AVG(e.Salary) AS AvgSalary
FROM Departments d JOIN Employees e ON e.DepartmentId = d.DepartmentId
GROUP BY d.DepartmentName
HAVING AVG(e.Salary) > (SELECT AVG(Salary) FROM Employees);
```

**Explanation:** A subquery is allowed inside HAVING.

### 131. [CTE] List orders whose total value is higher than the average order value.

Hints:
1. Order totals CTE and a scalar AVG subquery.

```sql
WITH OT AS (
    SELECT o.OrderId, o.CustomerId, o.OrderDate, o.Status, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Total
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.OrderId, o.CustomerId, o.OrderDate, o.Status
)
SELECT OrderId, Total
FROM OT
WHERE Total > (SELECT AVG(Total) FROM OT);
```

**Explanation:** Reusing a CTE twice avoids repeating the aggregation text (though it is still evaluated twice).

### 132. [ROW_NUMBER] Show each customer's second most recent order (customer, order id, order date).

Hints:
1. ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY OrderDate DESC) = 2.

```sql
WITH R AS (
    SELECT CustomerId, OrderId, OrderDate,
           ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY OrderDate DESC) AS rn
    FROM Orders
)
SELECT c.CustomerName, R.OrderId, R.OrderDate
FROM R JOIN Customers c ON c.CustomerId = R.CustomerId
WHERE R.rn = 2;
```

**Explanation:** Customers with fewer than 2 orders do not appear.

### 133. [DATEDIFF] For each customer show the number of days between their first and last order.

Hints:
1. MIN and MAX of OrderDate with DATEDIFF.

```sql
SELECT c.CustomerName, DATEDIFF(DAY, MIN(o.OrderDate), MAX(o.OrderDate)) AS SpanDays
FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId
GROUP BY c.CustomerId, c.CustomerName;
```

**Explanation:** Aggregates can be nested inside scalar functions like DATEDIFF.

### 134. [LAG] For each customer, compute the average number of days between consecutive orders (1 decimal).

Hints:
1. LAG in a CTE to compute gaps, then AVG by customer.

```sql
WITH G AS (
    SELECT CustomerId, DATEDIFF(DAY, LAG(OrderDate) OVER (PARTITION BY CustomerId ORDER BY OrderDate), OrderDate) AS Gap
    FROM Orders
)
SELECT c.CustomerName, ROUND(AVG(G.Gap * 1.0), 1) AS AvgGapDays
FROM G JOIN Customers c ON c.CustomerId = G.CustomerId
GROUP BY c.CustomerId, c.CustomerName;
```

**Explanation:** AVG ignores the NULL gap of each customer's first order.

### 135. [Running total] Show employees ordered by hire date (EmployeeId as tie-break) with a running headcount.

Hints:
1. COUNT(*) OVER (ORDER BY HireDate, EmployeeId ROWS UNBOUNDED PRECEDING).

```sql
SELECT FirstName, LastName, HireDate,
       COUNT(*) OVER (ORDER BY HireDate, EmployeeId ROWS UNBOUNDED PRECEDING) AS Headcount
FROM Employees;
```

**Explanation:** Equivalent to ROW_NUMBER in this case.

### 136. [DENSE_RANK] Within each customer country, show the customer(s) with the highest total revenue.

Hints:
1. CTE of revenue per customer, then RANK partitioned by Country.

```sql
WITH CR AS (
    SELECT c.CustomerName, c.Country, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY c.CustomerId, c.CustomerName, c.Country
), R AS (
    SELECT *, RANK() OVER (PARTITION BY Country ORDER BY Revenue DESC) AS rnk FROM CR
)
SELECT Country, CustomerName, Revenue FROM R WHERE rnk = 1;
```

**Explanation:** RANK keeps ties; ROW_NUMBER would drop them.

### 137. [Cumulative share] List products by revenue (highest first) with each product's share of total revenue and the cumulative share (2 decimals).

Hints:
1. SUM(Revenue) OVER () for the total and a running SUM for cumulative.

```sql
WITH P AS (
    SELECT p.ProductId, p.ProductName, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM OrderItems oi JOIN Products p ON p.ProductId = oi.ProductId
    GROUP BY p.ProductId, p.ProductName
)
SELECT ProductName, Revenue,
       ROUND(100.0 * Revenue / SUM(Revenue) OVER (), 2) AS SharePct,
       ROUND(100.0 * SUM(Revenue) OVER (ORDER BY Revenue DESC, ProductId ROWS UNBOUNDED PRECEDING) / SUM(Revenue) OVER (), 2) AS CumulativePct
FROM P
ORDER BY Revenue DESC;
```

**Explanation:** This is the basis of a Pareto (80/20) analysis.

### 138. [Window SUM] For each product, show its revenue and its percentage of its own category's revenue (2 decimals).

Hints:
1. SUM(Revenue) OVER (PARTITION BY Category).

```sql
WITH P AS (
    SELECT p.Category, p.ProductName, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM OrderItems oi JOIN Products p ON p.ProductId = oi.ProductId
    GROUP BY p.ProductId, p.Category, p.ProductName
)
SELECT Category, ProductName, Revenue,
       ROUND(100.0 * Revenue / SUM(Revenue) OVER (PARTITION BY Category), 2) AS PctOfCategory
FROM P;
```

**Explanation:** A window function can aggregate over the grouped result of the CTE.

### 139. [Subquery] For each customer country, show total revenue and the revenue of its single biggest order.

Hints:
1. Order totals CTE joined to customers.

```sql
WITH OT AS (
    SELECT o.OrderId, o.CustomerId, o.OrderDate, o.Status, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Total
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.OrderId, o.CustomerId, o.OrderDate, o.Status
)
SELECT c.Country, SUM(OT.Total) AS Revenue, MAX(OT.Total) AS BiggestOrder
FROM OT JOIN Customers c ON c.CustomerId = OT.CustomerId
GROUP BY c.Country;
```

**Explanation:** Aggregate in layers: order totals first, then by country.

### 140. [RANK] Rank sales reps by total revenue of their orders (RANK, highest = 1). Ignore orders without a rep.

Hints:
1. Join Orders to Employees and RANK() OVER (ORDER BY SUM(...) DESC).

```sql
SELECT e.FirstName, e.LastName, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue,
       RANK() OVER (ORDER BY SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) DESC) AS Rnk
FROM Orders o
JOIN OrderItems oi ON oi.OrderId = o.OrderId
JOIN Employees e ON e.EmployeeId = o.EmployeeId
GROUP BY e.EmployeeId, e.FirstName, e.LastName;
```

**Explanation:** Window functions can be applied on top of aggregates in the same SELECT.

### 141. [Conditional aggregation] Show revenue per year (rows) with columns Q1, Q2, Q3, Q4 (non-cancelled orders).

Hints:
1. SUM(CASE WHEN DATEPART(QUARTER, OrderDate) = 1 THEN ... END).

```sql
SELECT YEAR(o.OrderDate) AS Yr,
       SUM(CASE WHEN DATEPART(QUARTER, o.OrderDate) = 1 THEN oi.Quantity * oi.UnitPrice * (1 - oi.Discount) ELSE 0 END) AS Q1,
       SUM(CASE WHEN DATEPART(QUARTER, o.OrderDate) = 2 THEN oi.Quantity * oi.UnitPrice * (1 - oi.Discount) ELSE 0 END) AS Q2,
       SUM(CASE WHEN DATEPART(QUARTER, o.OrderDate) = 3 THEN oi.Quantity * oi.UnitPrice * (1 - oi.Discount) ELSE 0 END) AS Q3,
       SUM(CASE WHEN DATEPART(QUARTER, o.OrderDate) = 4 THEN oi.Quantity * oi.UnitPrice * (1 - oi.Discount) ELSE 0 END) AS Q4
FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
WHERE o.Status <> 'Cancelled'
GROUP BY YEAR(o.OrderDate)
ORDER BY Yr;
```

**Explanation:** A manual pivot is more flexible than PIVOT when you need computed values.

### 142. [ROW_NUMBER] For each employee, show their first and their latest salary from SalaryHistory and the percentage growth (1 decimal).

Hints:
1. MIN/MAX with first/last rows, or FIRST_VALUE with a window frame.

```sql
WITH S AS (
    SELECT EmployeeId, Salary,
           ROW_NUMBER() OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate) AS rn_asc,
           ROW_NUMBER() OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate DESC) AS rn_desc
    FROM SalaryHistory
)
SELECT a.EmployeeId, a.Salary AS FirstSalary, d.Salary AS LatestSalary,
       ROUND(100.0 * (d.Salary - a.Salary) / a.Salary, 1) AS GrowthPct
FROM S a JOIN S d ON d.EmployeeId = a.EmployeeId AND d.rn_desc = 1
WHERE a.rn_asc = 1;
```

**Explanation:** Two row numbers (ascending and descending) pick the first and last rows.

### 143. [Window COUNT] List all employees whose last name is shared with at least one other employee (show all of them).

Hints:
1. COUNT(*) OVER (PARTITION BY LastName) > 1 in a CTE.

```sql
WITH L AS (
    SELECT EmployeeId, FirstName, LastName, COUNT(*) OVER (PARTITION BY LastName) AS Cnt FROM Employees
)
SELECT EmployeeId, FirstName, LastName FROM L WHERE Cnt > 1;
```

**Explanation:** Unlike GROUP BY, the window approach keeps the detail rows.

### 144. [ROW_NUMBER] Show the employees that would be removed when de-duplicating on (Salary, HireDate), keeping the lowest EmployeeId of each group.

Hints:
1. ROW_NUMBER() OVER (PARTITION BY Salary, HireDate ORDER BY EmployeeId) > 1.

```sql
WITH D AS (
    SELECT EmployeeId, FirstName, LastName, Salary, HireDate,
           ROW_NUMBER() OVER (PARTITION BY Salary, HireDate ORDER BY EmployeeId) AS rn
    FROM Employees
)
SELECT EmployeeId, FirstName, LastName FROM D WHERE rn > 1;
```

**Explanation:** To actually delete, DELETE directly from the CTE.

### 145. [PERCENTILE_CONT] What is the median salary of all employees?

Hints:
1. PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Salary) OVER ().

```sql
SELECT DISTINCT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Salary) OVER () AS MedianSalary
FROM Employees;
```

**Explanation:** In T-SQL PERCENTILE_CONT is an analytic function and needs OVER; DISTINCT collapses the repeated value.

### 146. [PERCENTILE_CONT] What is the median salary in each department (employees with a department)?

Hints:
1. PARTITION BY DepartmentId inside OVER.

```sql
SELECT DISTINCT DepartmentId,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Salary) OVER (PARTITION BY DepartmentId) AS MedianSalary
FROM Employees
WHERE DepartmentId IS NOT NULL;
```

**Explanation:** For an even number of rows the median is the average of the two middle values.

### 147. [LAG] What is the longest gap in days between two consecutive orders of the same customer? Show customer name and gap for each customer's longest gap.

Hints:
1. LAG for gaps, MAX per customer.

```sql
WITH G AS (
    SELECT CustomerId, DATEDIFF(DAY, LAG(OrderDate) OVER (PARTITION BY CustomerId ORDER BY OrderDate), OrderDate) AS Gap
    FROM Orders
)
SELECT c.CustomerName, MAX(G.Gap) AS LongestGap
FROM G JOIN Customers c ON c.CustomerId = G.CustomerId
GROUP BY c.CustomerId, c.CustomerName;
```

**Explanation:** MAX ignores the first-order NULL.

### 148. [STRING_AGG] For each department list the distinct job titles as a comma-separated, alphabetical string.

Hints:
1. Get DISTINCT pairs in a subquery, then STRING_AGG.

```sql
SELECT d.DepartmentName, STRING_AGG(t.JobTitle, ', ') WITHIN GROUP (ORDER BY t.JobTitle) AS Titles
FROM Departments d
JOIN (SELECT DISTINCT DepartmentId, JobTitle FROM Employees) t ON t.DepartmentId = d.DepartmentId
GROUP BY d.DepartmentName;
```

**Explanation:** STRING_AGG has no DISTINCT option, hence the derived table.

### 149. [Window AVG] For each customer show their total revenue and the average revenue of customers in the same country.

Hints:
1. AVG(Revenue) OVER (PARTITION BY Country).

```sql
WITH CR AS (
    SELECT c.CustomerName, c.Country, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY c.CustomerId, c.CustomerName, c.Country
)
SELECT CustomerName, Country, Revenue,
       AVG(Revenue) OVER (PARTITION BY Country) AS CountryAvg
FROM CR;
```

**Explanation:** Window functions run after GROUP BY, so they can use the grouped result.

### 150. [GROUP BY] How many orders did customers place in the same year they signed up? Show customer name and count (customers with at least one).

Hints:
1. Join on YEAR(OrderDate) = YEAR(SignupDate).

```sql
SELECT c.CustomerName, COUNT(*) AS Orders
FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId AND YEAR(o.OrderDate) = YEAR(c.SignupDate)
GROUP BY c.CustomerId, c.CustomerName;
```

**Explanation:** Join conditions may contain expressions, not only column equality.

### 151. [ROW_NUMBER] For every order show its most expensive line item (product name and unit price).

Hints:
1. ROW_NUMBER() OVER (PARTITION BY OrderId ORDER BY UnitPrice DESC) = 1.

```sql
WITH R AS (
    SELECT oi.OrderId, oi.ProductId, oi.UnitPrice,
           ROW_NUMBER() OVER (PARTITION BY oi.OrderId ORDER BY oi.UnitPrice DESC) AS rn
    FROM OrderItems oi
)
SELECT R.OrderId, p.ProductName, R.UnitPrice
FROM R JOIN Products p ON p.ProductId = R.ProductId
WHERE R.rn = 1;
```

**Explanation:** Top-1 per group is one of the most common window function patterns.

### 152. [HAVING] Which customers spent more in total than 'Acme Corp'?

Hints:
1. HAVING SUM(...) > (subquery for Acme).

```sql
SELECT c.CustomerName, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId
GROUP BY c.CustomerId, c.CustomerName
HAVING SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) > (
    SELECT SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) FROM Customers c2 JOIN Orders o ON o.CustomerId = c2.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId
    WHERE c2.CustomerName = 'Acme Corp');
```

**Explanation:** The inner query reuses the aliases because it is not correlated.

### 153. [EXISTS] Find customers who have both a Cancelled order and a Delivered order.

Hints:
1. Two EXISTS conditions.

```sql
SELECT c.CustomerName
FROM Customers c
WHERE EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerId = c.CustomerId AND o.Status = 'Cancelled')
  AND EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerId = c.CustomerId AND o.Status = 'Delivered');
```

**Explanation:** Each EXISTS is independent, so there is no row multiplication.

### 154. [HAVING] Which sales reps sold to more than 5 distinct customers?

Hints:
1. COUNT(DISTINCT CustomerId) in HAVING.

```sql
SELECT e.FirstName, e.LastName, COUNT(DISTINCT o.CustomerId) AS Customers
FROM Orders o JOIN Employees e ON e.EmployeeId = o.EmployeeId
GROUP BY e.EmployeeId, e.FirstName, e.LastName
HAVING COUNT(DISTINCT o.CustomerId) > 5;
```

**Explanation:** Same pattern with a threshold.

### 155. [Self join] Find pairs of products that appear together in at least 3 orders (product names, number of shared orders).

Hints:
1. Self join OrderItems on OrderId with a.ProductId < b.ProductId.

```sql
SELECT p1.ProductName AS ProductA, p2.ProductName AS ProductB, COUNT(*) AS Together
FROM OrderItems a
JOIN OrderItems b ON b.OrderId = a.OrderId AND a.ProductId < b.ProductId
JOIN Products p1 ON p1.ProductId = a.ProductId
JOIN Products p2 ON p2.ProductId = b.ProductId
GROUP BY p1.ProductName, p2.ProductName
HAVING COUNT(*) >= 3;
```

**Explanation:** Basket analysis / market-basket pairs.

### 156. [ROW_NUMBER] For each year, which month had the highest non-cancelled revenue? (year, month start, revenue)

Hints:
1. Monthly CTE, ROW_NUMBER() OVER (PARTITION BY YEAR(MonthStart) ORDER BY Revenue DESC).

```sql
WITH M AS (
    SELECT DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1) AS MonthStart, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    WHERE o.Status <> 'Cancelled'
    GROUP BY DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1)
), R AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY YEAR(MonthStart) ORDER BY Revenue DESC) AS rn FROM M
)
SELECT YEAR(MonthStart) AS Yr, MonthStart, Revenue FROM R WHERE rn = 1;
```

**Explanation:** Partitioning by a year expression is allowed.

### 157. [PERCENTILE_CONT] List employees who earn above the 90th percentile of salaries.

Hints:
1. Compute PERCENTILE_CONT(0.9) in a CTE and compare.

```sql
WITH P AS (
    SELECT DISTINCT PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY Salary) OVER () AS P90 FROM Employees
)
SELECT e.FirstName, e.LastName, e.Salary
FROM Employees e CROSS JOIN P
WHERE e.Salary > P.P90;
```

**Explanation:** Continuous percentiles interpolate between values.

### 158. [CASE] Show for each employee whether they are a 'Manager' (has direct reports) or 'Individual Contributor', using a single query without GROUP BY.

Hints:
1. CASE WHEN EXISTS (...) THEN ... END.

```sql
SELECT e.FirstName, e.LastName,
       CASE WHEN EXISTS (SELECT 1 FROM Employees r WHERE r.ManagerId = e.EmployeeId) THEN 'Manager' ELSE 'Individual Contributor' END AS Role
FROM Employees e;
```

**Explanation:** EXISTS can be used inside a CASE expression.

### 159. [Window MAX] For each order, show the total and the customer's largest order total for comparison, only for orders that are the customer's largest.

Hints:
1. MAX(Total) OVER (PARTITION BY CustomerId) = Total.

```sql
WITH OT AS (
    SELECT o.OrderId, o.CustomerId, o.OrderDate, o.Status, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Total
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.OrderId, o.CustomerId, o.OrderDate, o.Status
), M AS (
    SELECT *, MAX(Total) OVER (PARTITION BY CustomerId) AS MaxTotal FROM OT
)
SELECT OrderId, CustomerId, Total FROM M WHERE Total = MaxTotal;
```

**Explanation:** Equivalent to a top-1 per group but keeps ties.

### 160. [NOT EXISTS] Which sales reps (employees with orders) have never handled a Cancelled order?

Hints:
1. Reps appear in Orders; NOT EXISTS for cancelled ones.

```sql
SELECT e.FirstName, e.LastName
FROM Employees e
WHERE EXISTS (SELECT 1 FROM Orders o WHERE o.EmployeeId = e.EmployeeId)
  AND NOT EXISTS (SELECT 1 FROM Orders o WHERE o.EmployeeId = e.EmployeeId AND o.Status = 'Cancelled');
```

**Explanation:** Combine EXISTS and NOT EXISTS for 'has X but never Y'.


## Expert

### 161. [DENSE_RANK] Find the employee(s) with the second-highest salary in each department (departments with fewer than two distinct salaries should not appear).

Hints:
1. DENSE_RANK handles ties properly.
2. Filter DENSE_RANK = 2 in an outer query.

```sql
WITH R AS (
    SELECT DepartmentId, FirstName, LastName, Salary,
           DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS rnk
    FROM Employees
    WHERE DepartmentId IS NOT NULL
)
SELECT d.DepartmentName, R.FirstName, R.LastName, R.Salary
FROM R JOIN Departments d ON d.DepartmentId = R.DepartmentId
WHERE R.rnk = 2;
```

**Explanation:** The classic 'Nth highest' question. ROW_NUMBER would wrongly pick one of several people tied for first.

### 162. [Duplicates] Find groups of employees that share the same Salary and HireDate, listing the salary, hire date and how many employees are in each such group.

Hints:
1. Group by the columns that define a duplicate.
2. HAVING COUNT(*) > 1.

```sql
SELECT Salary, HireDate, COUNT(*) AS Employees
FROM Employees
GROUP BY Salary, HireDate
HAVING COUNT(*) > 1;
```

**Explanation:** Duplicate detection is GROUP BY + HAVING COUNT(*) > 1. To delete duplicates use ROW_NUMBER() and delete rn > 1.

### 163. [Top N per group] Find the top 2 products by revenue in each product category (category, product, revenue, rank).

Hints:
1. Aggregate revenue per product first.
2. Then ROW_NUMBER/RANK partitioned by Category and filter <= 2.

```sql
WITH ProdRev AS (
    SELECT p.Category, p.ProductName,
           SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM OrderItems oi
    JOIN Products p ON p.ProductId = oi.ProductId
    GROUP BY p.Category, p.ProductId, p.ProductName
), Ranked AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY Category ORDER BY Revenue DESC) AS rn
    FROM ProdRev
)
SELECT Category, ProductName, Revenue, rn AS Rnk
FROM Ranked
WHERE rn <= 2
ORDER BY Category, rn;
```

**Explanation:** Alternative: CROSS APPLY (SELECT TOP 2 ...) per category.

### 164. [Gaps and islands] For each customer, find their longest streak of consecutive calendar months in which they placed at least one order. Return the top 5 customers by streak length (customer name, streak length in months, streak start month).

Hints:
1. Reduce to distinct (CustomerId, month number) first.
2. Subtract ROW_NUMBER() from the month number - consecutive months share the same difference (the 'island' key).

```sql
WITH M AS (
    SELECT DISTINCT CustomerId, DATEDIFF(MONTH, '2000-01-01', OrderDate) AS Mn
    FROM Orders
), Grp AS (
    SELECT CustomerId, Mn,
           Mn - ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY Mn) AS Island
    FROM M
), Streaks AS (
    SELECT CustomerId, Island, COUNT(*) AS StreakLen, MIN(Mn) AS StartMn
    FROM Grp
    GROUP BY CustomerId, Island
), Best AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY StreakLen DESC, StartMn) AS rn
    FROM Streaks
)
SELECT TOP 5 c.CustomerName, b.StreakLen,
       DATEADD(MONTH, b.StartMn, '2000-01-01') AS StreakStart
FROM Best b
JOIN Customers c ON c.CustomerId = b.CustomerId
WHERE b.rn = 1
ORDER BY b.StreakLen DESC, c.CustomerName;
```

**Explanation:** Gaps-and-islands: value minus row number is constant inside a run of consecutive values.

### 165. [Moving average] Show monthly revenue (excluding Cancelled orders) with a 3-month moving average (current month and the 2 previous months), rounded to 2 decimals.

Hints:
1. Aggregate to months in a CTE.
2. AVG(Revenue) OVER (ORDER BY MonthStart ROWS BETWEEN 2 PRECEDING AND CURRENT ROW).

```sql
WITH Monthly AS (
    SELECT DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1) AS MonthStart,
           SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Orders o
    JOIN OrderItems oi ON oi.OrderId = o.OrderId
    WHERE o.Status <> 'Cancelled'
    GROUP BY DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1)
)
SELECT MonthStart, Revenue,
       ROUND(AVG(Revenue) OVER (ORDER BY MonthStart ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2) AS MovingAvg3
FROM Monthly
ORDER BY MonthStart;
```

**Explanation:** The first two months average fewer than 3 rows. Months without orders would be missing - join to a calendar table if that matters.

### 166. [Calendar gaps] List every date in Q1 2024 (1 Jan - 31 Mar) on which no order was placed.

Hints:
1. Build a calendar with a recursive CTE.
2. Anti-join to Orders.

```sql
WITH D AS (
    SELECT CAST('2024-01-01' AS DATE) AS d
    UNION ALL
    SELECT DATEADD(DAY, 1, d) FROM D WHERE d < '2024-03-31'
)
SELECT d AS EmptyDay
FROM D
WHERE NOT EXISTS (SELECT 1 FROM Orders o WHERE o.OrderDate = D.d)
OPTION (MAXRECURSION 400);
```

**Explanation:** Finding missing dates requires generating the full list first.

### 167. [Gaps and islands] Find runs of consecutive calendar days that all have at least one order. Return start date, end date and length for runs of 2 or more days.

Hints:
1. Distinct dates, then date minus ROW_NUMBER days gives a constant per island.

```sql
WITH Dd AS (SELECT DISTINCT OrderDate AS d FROM Orders),
G AS (
    SELECT d, DATEADD(DAY, -ROW_NUMBER() OVER (ORDER BY d), d) AS grp FROM Dd
)
SELECT MIN(d) AS StartDate, MAX(d) AS EndDate, COUNT(*) AS Days
FROM G
GROUP BY grp
HAVING COUNT(*) >= 2;
```

**Explanation:** Subtracting the row number from the date makes consecutive days share the same value.

### 168. [Window SUM] For each customer and year, list their orders with a running total of order value that restarts every year.

Hints:
1. Order totals CTE; SUM() OVER (PARTITION BY CustomerId, YEAR(OrderDate) ORDER BY OrderDate ROWS UNBOUNDED PRECEDING).

```sql
WITH OT AS (
    SELECT o.OrderId, o.CustomerId, o.OrderDate, o.Status, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Total
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.OrderId, o.CustomerId, o.OrderDate, o.Status
)
SELECT CustomerId, OrderId, OrderDate, Total,
       SUM(Total) OVER (PARTITION BY CustomerId, YEAR(OrderDate) ORDER BY OrderDate ROWS UNBOUNDED PRECEDING) AS YtdTotal
FROM OT;
```

**Explanation:** PARTITION BY resets the running window, here per customer per year.

### 169. [Retention] How many customers ordered in 2023 and again in 2024 (retained), and what percentage of 2023 customers is that (1 decimal)?

Hints:
1. Sets of customers by year; COUNT the intersection.

```sql
WITH A AS (SELECT DISTINCT CustomerId FROM Orders WHERE YEAR(OrderDate) = 2023),
     B AS (SELECT DISTINCT CustomerId FROM Orders WHERE YEAR(OrderDate) = 2024)
SELECT COUNT(B.CustomerId) AS Retained,
       ROUND(100.0 * COUNT(B.CustomerId) / COUNT(A.CustomerId), 1) AS RetentionPct
FROM A LEFT JOIN B ON B.CustomerId = A.CustomerId;
```

**Explanation:** COUNT(column) only counts matched rows from the LEFT JOIN.

### 170. [ROW_NUMBER] For each customer show the first order they ever placed: order id, date and order total.

Hints:
1. Order totals CTE then ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY OrderDate).

```sql
WITH OT AS (
    SELECT o.OrderId, o.CustomerId, o.OrderDate, o.Status, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Total
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.OrderId, o.CustomerId, o.OrderDate, o.Status
), R AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY OrderDate) AS rn FROM OT
)
SELECT CustomerId, OrderId, OrderDate, Total FROM R WHERE rn = 1;
```

**Explanation:** Top-1 per group again, here chronological.

### 171. [Bottom N per group] For each product category, list the 2 products with the lowest stock (category, product, stock).

Hints:
1. ROW_NUMBER() OVER (PARTITION BY Category ORDER BY Stock) <= 2.

```sql
WITH R AS (
    SELECT Category, ProductName, Stock, ROW_NUMBER() OVER (PARTITION BY Category ORDER BY Stock) AS rn FROM Products
)
SELECT Category, ProductName, Stock FROM R WHERE rn <= 2;
```

**Explanation:** Ordering ascending gives bottom-N.

### 172. [Recursive CTE] For every manager, compute the total salary cost of their entire team (all direct and indirect reports, excluding the manager). Show manager name and team cost.

Hints:
1. Make every employee the root of their own subtree, then SUM descendants.

```sql
WITH T AS (
    SELECT EmployeeId AS RootId, EmployeeId AS MemberId FROM Employees
    UNION ALL
    SELECT t.RootId, e.EmployeeId FROM T t JOIN Employees e ON e.ManagerId = t.MemberId
)
SELECT r.FirstName + ' ' + r.LastName AS Manager, SUM(m.Salary) AS TeamCost
FROM T
JOIN Employees r ON r.EmployeeId = T.RootId
JOIN Employees m ON m.EmployeeId = T.MemberId
WHERE T.RootId <> T.MemberId
GROUP BY r.EmployeeId, r.FirstName, r.LastName;
```

**Explanation:** Starting a recursive CTE from all rows computes every subtree at once.

### 173. [PERCENTILE_CONT] What is the median order value (using order totals)?

Hints:
1. Order totals CTE then PERCENTILE_CONT(0.5).

```sql
WITH OT AS (
    SELECT o.OrderId, o.CustomerId, o.OrderDate, o.Status, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Total
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.OrderId, o.CustomerId, o.OrderDate, o.Status
)
SELECT DISTINCT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Total) OVER () AS MedianOrder
FROM OT;
```

**Explanation:** The median is robust to very large orders, unlike the mean.

### 174. [LAG] For each employee, find their largest single percentage raise from SalaryHistory (1 decimal).

Hints:
1. LAG to get the previous salary, MAX of the % change.

```sql
WITH C AS (
    SELECT EmployeeId,
           100.0 * (Salary - LAG(Salary) OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate)) / LAG(Salary) OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate) AS Pct
    FROM SalaryHistory
)
SELECT EmployeeId, ROUND(MAX(Pct), 1) AS BiggestRaisePct
FROM C
GROUP BY EmployeeId
HAVING MAX(Pct) IS NOT NULL;
```

**Explanation:** Employees with a single record have no raise, so HAVING removes them.

### 175. [Point in time] What salary was each employee earning on 2024-06-30 according to SalaryHistory? (EmployeeId, Salary). Exclude employees who had no record by then.

Hints:
1. Latest record with EffectiveDate <= the date; ROW_NUMBER DESC.

```sql
WITH S AS (
    SELECT EmployeeId, Salary,
           ROW_NUMBER() OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate DESC) AS rn
    FROM SalaryHistory
    WHERE EffectiveDate <= '2024-06-30'
)
SELECT EmployeeId, Salary FROM S WHERE rn = 1;
```

**Explanation:** Slowly-changing-dimension 'as of' lookup.

### 176. [Point in time] What was the total payroll on 2024-06-30 (sum of each employee's then-current salary)?

Hints:
1. Same as the previous question then SUM.

```sql
WITH S AS (
    SELECT EmployeeId, Salary,
           ROW_NUMBER() OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate DESC) AS rn
    FROM SalaryHistory
    WHERE EffectiveDate <= '2024-06-30'
)
SELECT SUM(Salary) AS Payroll FROM S WHERE rn = 1;
```

**Explanation:** Summing all history rows would massively overcount.

### 177. [NTILE] Find customers in the top revenue quartile (NTILE(4) = 1). Show customer name and revenue.

Hints:
1. Revenue per customer CTE then NTILE(4) OVER (ORDER BY Revenue DESC).

```sql
WITH CR AS (
    SELECT c.CustomerName, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY c.CustomerId, c.CustomerName
), N AS (
    SELECT *, NTILE(4) OVER (ORDER BY Revenue DESC) AS Q FROM CR
)
SELECT CustomerName, Revenue FROM N WHERE Q = 1;
```

**Explanation:** NTILE splits ordered rows into equal-count groups.

### 178. [New customers] For each month, count the customers placing their first-ever order, with a running total of acquired customers.

Hints:
1. MIN(OrderDate) per customer, group by month, running SUM.

```sql
WITH F AS (
    SELECT CustomerId, DATEFROMPARTS(YEAR(MIN(OrderDate)), MONTH(MIN(OrderDate)), 1) AS FirstMonth
    FROM Orders GROUP BY CustomerId
), M AS (
    SELECT FirstMonth, COUNT(*) AS NewCustomers FROM F GROUP BY FirstMonth
)
SELECT FirstMonth, NewCustomers,
       SUM(NewCustomers) OVER (ORDER BY FirstMonth ROWS UNBOUNDED PRECEDING) AS CumulativeCustomers
FROM M;
```

**Explanation:** Aggregate twice: customer level first, then month level.

### 179. [Basket analysis] Which products are most often ordered together with 'Laptop Pro 15'? Show product and number of shared orders for products shared in at least 3 orders.

Hints:
1. Self join OrderItems on OrderId with one side fixed to the laptop.

```sql
SELECT p.ProductName, COUNT(*) AS SharedOrders
FROM OrderItems a
JOIN Products lp ON lp.ProductId = a.ProductId AND lp.ProductName = 'Laptop Pro 15'
JOIN OrderItems b ON b.OrderId = a.OrderId AND b.ProductId <> a.ProductId
JOIN Products p ON p.ProductId = b.ProductId
GROUP BY p.ProductId, p.ProductName
HAVING COUNT(*) >= 3;
```

**Explanation:** Association-rule style questions rely on self joins.

### 180. [Window SUM] Find order lines that account for more than 50% of their order's value. Show OrderId, ProductId and the share (2 decimals).

Hints:
1. SUM(line value) OVER (PARTITION BY OrderId).

```sql
WITH L AS (
    SELECT oi.OrderId, oi.ProductId, oi.Quantity * oi.UnitPrice * (1 - oi.Discount) AS LineValue,
           SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) OVER (PARTITION BY oi.OrderId) AS OrderValue
    FROM OrderItems oi
)
SELECT OrderId, ProductId, ROUND(100.0 * LineValue / OrderValue, 2) AS SharePct
FROM L
WHERE LineValue > 0.5 * OrderValue;
```

**Explanation:** Window functions let you compare each row to its group total without a self join.

### 181. [Day of week] Which weekday generates the most revenue (non-cancelled)? Return the weekday name and revenue.

Hints:
1. Group by DATENAME(WEEKDAY) and take the top row.

```sql
SELECT TOP 1 DATENAME(WEEKDAY, o.OrderDate) AS Weekday, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
WHERE o.Status <> 'Cancelled'
GROUP BY DATENAME(WEEKDAY, o.OrderDate)
ORDER BY Revenue DESC;
```

**Explanation:** Remember to sort on the aggregate, not the weekday name.

### 182. [Year to date] Show 2024 monthly non-cancelled revenue with a year-to-date running total.

Hints:
1. Monthly CTE filtered to 2024, SUM OVER with ROWS.

```sql
WITH M AS (
    SELECT DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1) AS MonthStart, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    WHERE o.Status <> 'Cancelled'
    GROUP BY DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1)
)
SELECT MonthStart, Revenue,
       SUM(Revenue) OVER (ORDER BY MonthStart ROWS UNBOUNDED PRECEDING) AS YtdRevenue
FROM M
WHERE MonthStart >= '2024-01-01' AND MonthStart < '2025-01-01';
```

**Explanation:** WHERE is applied before the window function, so the running total starts at the first 2024 month - that is what makes it year-to-date.

### 183. [Year-over-year] For each month show revenue and the revenue of the same month one year earlier (NULL if none) and the difference.

Hints:
1. LEFT JOIN the monthly CTE to itself on DATEADD(YEAR, -1, MonthStart).

```sql
WITH M AS (
    SELECT DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1) AS MonthStart, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    WHERE o.Status <> 'Cancelled'
    GROUP BY DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1)
)
SELECT cur.MonthStart, cur.Revenue, prev.Revenue AS PrevYearRevenue, cur.Revenue - prev.Revenue AS Diff
FROM M cur
LEFT JOIN M prev ON prev.MonthStart = DATEADD(YEAR, -1, cur.MonthStart);
```

**Explanation:** Self-joining on shifted dates is more robust than LAG(12) when months are missing.

### 184. [Recursive CTE] Show the chain of command above Jon Tan (EmployeeId 36) up to the CEO: name and level above Jon (0 = Jon).

Hints:
1. Recursive CTE walking ManagerId upwards.

```sql
WITH Up AS (
    SELECT EmployeeId, FirstName, LastName, ManagerId, 0 AS Level FROM Employees WHERE EmployeeId = 36
    UNION ALL
    SELECT e.EmployeeId, e.FirstName, e.LastName, e.ManagerId, u.Level + 1
    FROM Employees e JOIN Up u ON e.EmployeeId = u.ManagerId
)
SELECT FirstName + ' ' + LastName AS Name, Level FROM Up ORDER BY Level;
```

**Explanation:** Walking up joins on the manager's id rather than the employee's.

### 185. [Cross tab] Show headcount per department (rows) and salary band (columns Low < 70000, Mid 70000-119999, High >= 120000). Only employees with a department.

Hints:
1. Conditional aggregation with CASE.

```sql
SELECT d.DepartmentName,
       SUM(CASE WHEN e.Salary < 70000 THEN 1 ELSE 0 END) AS Low,
       SUM(CASE WHEN e.Salary >= 70000 AND e.Salary < 120000 THEN 1 ELSE 0 END) AS Mid,
       SUM(CASE WHEN e.Salary >= 120000 THEN 1 ELSE 0 END) AS High
FROM Departments d JOIN Employees e ON e.DepartmentId = d.DepartmentId
GROUP BY d.DepartmentName;
```

**Explanation:** A cross tab is just GROUP BY with CASE-based aggregates.

### 186. [DATEDIFF] For every customer who has ordered, show how many days passed between signing up and their first order.

Hints:
1. MIN(OrderDate) then DATEDIFF with SignupDate.

```sql
SELECT c.CustomerName, DATEDIFF(DAY, c.SignupDate, MIN(o.OrderDate)) AS DaysToFirstOrder
FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId
GROUP BY c.CustomerId, c.CustomerName, c.SignupDate;
```

**Explanation:** Negative values would reveal orders placed before signup (data quality!).

### 187. [LAG] List orders whose Status is the same as that customer's previous order's status (customer, order id, status).

Hints:
1. LAG(Status) OVER (PARTITION BY CustomerId ORDER BY OrderDate).

```sql
WITH S AS (
    SELECT CustomerId, OrderId, Status,
           LAG(Status) OVER (PARTITION BY CustomerId ORDER BY OrderDate) AS PrevStatus
    FROM Orders
)
SELECT CustomerId, OrderId, Status FROM S WHERE Status = PrevStatus;
```

**Explanation:** LAG returns NULL for the first row so it never matches.

### 188. [Self join] List employees who manage at least one person who is themselves a manager (i.e. managers of managers).

Hints:
1. Self join twice or nested EXISTS.

```sql
SELECT m.EmployeeId, m.FirstName, m.LastName
FROM Employees m
WHERE EXISTS (
    SELECT 1 FROM Employees r
    WHERE r.ManagerId = m.EmployeeId
      AND EXISTS (SELECT 1 FROM Employees rr WHERE rr.ManagerId = r.EmployeeId));
```

**Explanation:** Nested EXISTS checks two levels of the hierarchy.

### 189. [PIVOT] Show a cohort matrix: rows = customer signup year, columns = order year 2023, 2024, 2025, values = number of orders.

Hints:
1. Join Customers to Orders, then PIVOT on order year.

```sql
SELECT SignupYear, [2023], [2024], [2025]
FROM (SELECT YEAR(c.SignupDate) AS SignupYear, YEAR(o.OrderDate) AS OrderYear, o.OrderId
      FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId) s
PIVOT (COUNT(OrderId) FOR OrderYear IN ([2023], [2024], [2025])) p
ORDER BY SignupYear;
```

**Explanation:** Cohort tables are PIVOTs of counts by a cohort key and a time key.

### 190. [Distribution] How many customers placed 1-5 orders, 6-10 orders, and 11+ orders? (bucket, customers). Include only customers with orders.

Hints:
1. Count orders per customer first, then bucket with CASE.

```sql
WITH C AS (SELECT CustomerId, COUNT(*) AS Orders FROM Orders GROUP BY CustomerId)
SELECT CASE WHEN Orders <= 5 THEN '1-5' WHEN Orders <= 10 THEN '6-10' ELSE '11+' END AS Bucket,
       COUNT(*) AS Customers
FROM C
GROUP BY CASE WHEN Orders <= 5 THEN '1-5' WHEN Orders <= 10 THEN '6-10' ELSE '11+' END;
```

**Explanation:** A histogram is an aggregate of an aggregate.

### 191. [ROW_NUMBER] Find customers whose most recent order was Cancelled.

Hints:
1. ROW_NUMBER by OrderDate DESC and check Status of row 1.

```sql
WITH R AS (
    SELECT CustomerId, Status, ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY OrderDate DESC) AS rn FROM Orders
)
SELECT c.CustomerName
FROM R JOIN Customers c ON c.CustomerId = R.CustomerId
WHERE R.rn = 1 AND R.Status = 'Cancelled';
```

**Explanation:** Filter on the status after picking the latest row, not before.

### 192. [FIRST_VALUE] For each department show the highest and lowest paid employee names (one row per department, employees with a department).

Hints:
1. FIRST_VALUE with ASC and DESC ordering, DISTINCT.

```sql
SELECT DISTINCT d.DepartmentName,
       FIRST_VALUE(e.FirstName) OVER (PARTITION BY e.DepartmentId ORDER BY e.Salary DESC, e.EmployeeId) AS HighestPaid,
       FIRST_VALUE(e.FirstName) OVER (PARTITION BY e.DepartmentId ORDER BY e.Salary ASC, e.EmployeeId) AS LowestPaid
FROM Employees e JOIN Departments d ON d.DepartmentId = e.DepartmentId;
```

**Explanation:** Two FIRST_VALUEs with opposite orderings avoid the LAST_VALUE frame trap.

### 193. [Anniversary] For each employee compute their next work anniversary date on or after 2026-01-01.

Hints:
1. Add whole years to HireDate until it is >= the reference date.

```sql
SELECT EmployeeId, FirstName, LastName, HireDate,
       CASE WHEN DATEADD(YEAR, DATEDIFF(YEAR, HireDate, '2026-01-01'), HireDate) >= '2026-01-01'
            THEN DATEADD(YEAR, DATEDIFF(YEAR, HireDate, '2026-01-01'), HireDate)
            ELSE DATEADD(YEAR, DATEDIFF(YEAR, HireDate, '2026-01-01') + 1, HireDate) END AS NextAnniversary
FROM Employees;
```

**Explanation:** DATEDIFF(YEAR) counts boundaries, so the result may need one more year.

### 194. [Budgeting] Starting from the highest-paid employee (ties by EmployeeId) and going down, which employees fit within a cumulative salary budget of 1,000,000? Show name, salary and running total.

Hints:
1. Running SUM ordered by Salary DESC, EmployeeId; filter <= 1,000,000.

```sql
WITH R AS (
    SELECT FirstName, LastName, Salary,
           SUM(Salary) OVER (ORDER BY Salary DESC, EmployeeId ROWS UNBOUNDED PRECEDING) AS RunningTotal
    FROM Employees
)
SELECT FirstName, LastName, Salary, RunningTotal FROM R WHERE RunningTotal <= 1000000;
```

**Explanation:** Filter in an outer query because window functions are not allowed in WHERE.

### 195. [Metadata] List every table with its row count using sys.tables and sys.partitions.

Hints:
1. Join on object_id and filter index_id IN (0,1).

```sql
SELECT t.name AS TableName, SUM(p.rows) AS TotalRows
FROM sys.tables t JOIN sys.partitions p ON p.object_id = t.object_id AND p.index_id IN (0, 1)
GROUP BY t.name;
```

**Explanation:** Heap (0) and clustered index (1) partitions hold the base rows; counting other indexes would double count.

### 196. [Dynamic ranking] Rank customers by revenue within each year (DENSE_RANK, highest = 1) and return the top 3 per year with year, customer, revenue and rank.

Hints:
1. Revenue per customer per year, then DENSE_RANK partitioned by Yr.

```sql
WITH CR AS (
    SELECT YEAR(o.OrderDate) AS Yr, c.CustomerName, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY YEAR(o.OrderDate), c.CustomerId, c.CustomerName
), R AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY Yr ORDER BY Revenue DESC) AS Rnk FROM CR
)
SELECT Yr, CustomerName, Revenue, Rnk FROM R WHERE Rnk <= 3;
```

**Explanation:** Top-N per group with ties handled by DENSE_RANK.

### 197. [Anti join] Find employees who never appear as the sales rep on any order and are in the Sales department.

Hints:
1. Sales dept = 3; NOT EXISTS on Orders.EmployeeId.

```sql
SELECT e.EmployeeId, e.FirstName, e.LastName
FROM Employees e
WHERE e.DepartmentId = 3
  AND NOT EXISTS (SELECT 1 FROM Orders o WHERE o.EmployeeId = e.EmployeeId);
```

**Explanation:** Reps 16-21 are assigned orders in the seed data, so remaining Sales staff show up here.

### 198. [Moving average] Show each month's non-cancelled revenue and the average of the previous 2 months only (excluding the current month), rounded to 2 decimals.

Hints:
1. Frame: ROWS BETWEEN 2 PRECEDING AND 1 PRECEDING.

```sql
WITH M AS (
    SELECT DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1) AS MonthStart, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    WHERE o.Status <> 'Cancelled'
    GROUP BY DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1)
)
SELECT MonthStart, Revenue,
       ROUND(AVG(Revenue) OVER (ORDER BY MonthStart ROWS BETWEEN 2 PRECEDING AND 1 PRECEDING), 2) AS PrevTwoAvg
FROM M;
```

**Explanation:** Frames can exclude the current row; the first month has NULL.

### 199. [Orders vs average] List each customer's orders whose value is above that customer's own average order value (customer, order id, total, customer average).

Hints:
1. Order totals CTE with AVG OVER (PARTITION BY CustomerId).

```sql
WITH OT AS (
    SELECT o.OrderId, o.CustomerId, o.OrderDate, o.Status, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Total
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.OrderId, o.CustomerId, o.OrderDate, o.Status
), A AS (
    SELECT *, AVG(Total) OVER (PARTITION BY CustomerId) AS CustAvg FROM OT
)
SELECT CustomerId, OrderId, Total, CustAvg FROM A WHERE Total > CustAvg;
```

**Explanation:** Three layers: order lines, order totals, then per-customer window.

### 200. [Pivot from CTE] Show total revenue per product category (rows) per Status (columns Delivered, Shipped, Pending, Cancelled).

Hints:
1. Join Orders, OrderItems, Products; PIVOT on Status.

```sql
SELECT Category, [Delivered], [Shipped], [Pending], [Cancelled]
FROM (
    SELECT p.Category, o.Status, oi.Quantity * oi.UnitPrice * (1 - oi.Discount) AS Revenue
    FROM OrderItems oi JOIN Orders o ON o.OrderId = oi.OrderId JOIN Products p ON p.ProductId = oi.ProductId
) s
PIVOT (SUM(Revenue) FOR Status IN ([Delivered], [Shipped], [Pending], [Cancelled])) pv;
```

**Explanation:** PIVOT can aggregate any measure.

