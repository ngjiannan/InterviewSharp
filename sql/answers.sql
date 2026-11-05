USE PracticeDB;
GO

PRINT 'Q1';
SELECT * FROM Departments;
GO

PRINT 'Q2';
SELECT FirstName, LastName, Salary
FROM Employees
WHERE Salary > 100000;
GO

PRINT 'Q3';
SELECT FirstName, LastName, HireDate
FROM Employees
ORDER BY HireDate DESC;
GO

PRINT 'Q4';
SELECT TOP 5 FirstName, LastName, Salary
FROM Employees
ORDER BY Salary DESC;
GO

PRINT 'Q5';
SELECT DISTINCT JobTitle
FROM Employees
ORDER BY JobTitle;
GO

PRINT 'Q6';
SELECT CustomerId, CustomerName
FROM Customers
WHERE CustomerName LIKE 'S%';
GO

PRINT 'Q7';
SELECT OrderId, CustomerId, OrderDate, Status
FROM Orders
WHERE OrderDate >= '2024-01-01' AND OrderDate < '2025-01-01';
GO

PRINT 'Q8';
SELECT CustomerName, City, Country
FROM Customers
WHERE Country IN ('USA', 'UK');
GO

PRINT 'Q9';
SELECT EmployeeId, FirstName, LastName, JobTitle
FROM Employees
WHERE ManagerId IS NULL;
GO

PRINT 'Q10';
SELECT FirstName, LastName, CommissionPct
FROM Employees
WHERE CommissionPct IS NOT NULL;
GO

PRINT 'Q11';
SELECT CONCAT(FirstName, ' ', LastName) AS FullName,
       Salary * 1.10 AS SalaryWithBonus
FROM Employees;
GO

PRINT 'Q12';
SELECT COUNT(*) AS TotalOrders FROM Orders;
GO

PRINT 'Q13';
SELECT ProductName, UnitPrice, Stock
FROM Products
WHERE Stock = 0 OR UnitPrice > 1000;
GO

PRINT 'Q14';
SELECT ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice DESC, ProductId
OFFSET 5 ROWS FETCH NEXT 5 ROWS ONLY;
GO

PRINT 'Q15';
SELECT CustomerName, COALESCE(Email, 'N/A') AS Email
FROM Customers;
GO

PRINT 'Q16';
SELECT FirstName, LastName, JobTitle
FROM Employees
WHERE DepartmentId = 3;
GO

PRINT 'Q17';
SELECT ProductName, UnitPrice
FROM Products
WHERE Category = 'Electronics'
ORDER BY UnitPrice DESC;
GO

PRINT 'Q18';
SELECT CustomerId, CustomerName, City
FROM Customers
WHERE Country = 'Singapore';
GO

PRINT 'Q19';
SELECT FirstName, LastName, HireDate
FROM Employees
WHERE HireDate >= '2021-01-01'
ORDER BY HireDate;
GO

PRINT 'Q20';
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice BETWEEN 50 AND 200;
GO

PRINT 'Q21';
SELECT OrderId, CustomerId, OrderDate
FROM Orders
WHERE Status = 'Pending';
GO

PRINT 'Q22';
SELECT UPPER(DepartmentName) AS DeptUpper, LEN(DepartmentName) AS NameLength
FROM Departments;
GO

PRINT 'Q23';
SELECT FirstName, LastName
FROM Employees
WHERE LastName LIKE '%ng';
GO

PRINT 'Q24';
SELECT MIN(UnitPrice) AS CheapestPrice FROM Products;
GO

PRINT 'Q25';
SELECT SUM(Stock) AS TotalStock FROM Products;
GO

PRINT 'Q26';
SELECT AVG(UnitPrice) AS AvgPrice
FROM Products
WHERE Category = 'Accessories';
GO

PRINT 'Q27';
SELECT CustomerName, Country
FROM Customers
WHERE Country <> 'USA';
GO

PRINT 'Q28';
SELECT TOP 3 CustomerName, SignupDate
FROM Customers
ORDER BY SignupDate DESC;
GO

PRINT 'Q29';
SELECT EmployeeId, FirstName, LastName
FROM Employees
WHERE Email IS NULL;
GO

PRINT 'Q30';
SELECT COUNT(DISTINCT Country) AS Countries FROM Customers;
GO

PRINT 'Q31';
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
INNER JOIN Departments d ON d.DepartmentId = e.DepartmentId;
GO

PRINT 'Q32';
SELECT d.DepartmentName
FROM Departments d
LEFT JOIN Employees e ON e.DepartmentId = d.DepartmentId
WHERE e.EmployeeId IS NULL;
GO

PRINT 'Q33';
SELECT e.FirstName + ' ' + e.LastName AS Employee,
       COALESCE(m.FirstName + ' ' + m.LastName, 'None') AS Manager
FROM Employees e
LEFT JOIN Employees m ON m.EmployeeId = e.ManagerId;
GO

PRINT 'Q34';
SELECT d.DepartmentName, COUNT(e.EmployeeId) AS EmployeeCount
FROM Departments d
LEFT JOIN Employees e ON e.DepartmentId = d.DepartmentId
GROUP BY d.DepartmentName
ORDER BY EmployeeCount DESC;
GO

PRINT 'Q35';
SELECT d.DepartmentName, ROUND(AVG(e.Salary), 2) AS AvgSalary
FROM Employees e
JOIN Departments d ON d.DepartmentId = e.DepartmentId
GROUP BY d.DepartmentName
ORDER BY AvgSalary DESC;
GO

PRINT 'Q36';
SELECT d.DepartmentName, COUNT(*) AS EmployeeCount
FROM Employees e
JOIN Departments d ON d.DepartmentId = e.DepartmentId
GROUP BY d.DepartmentName
HAVING COUNT(*) > 5;
GO

PRINT 'Q37';
SELECT p.Category,
       SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
FROM OrderItems oi
JOIN Products p ON p.ProductId = oi.ProductId
GROUP BY p.Category
ORDER BY Revenue DESC;
GO

PRINT 'Q38';
SELECT c.CustomerId, c.CustomerName
FROM Customers c
WHERE NOT EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerId = c.CustomerId);
GO

PRINT 'Q39';
SELECT p.ProductId, p.ProductName
FROM Products p
LEFT JOIN OrderItems oi ON oi.ProductId = p.ProductId
WHERE oi.OrderItemId IS NULL;
GO

PRINT 'Q40';
SELECT YEAR(OrderDate) AS Yr, MONTH(OrderDate) AS Mth, COUNT(*) AS Orders
FROM Orders
WHERE OrderDate >= '2024-01-01' AND OrderDate < '2025-01-01'
GROUP BY YEAR(OrderDate), MONTH(OrderDate)
ORDER BY Yr, Mth;
GO

PRINT 'Q41';
SELECT d.DepartmentName,
       COUNT(*) AS Headcount,
       MIN(e.Salary) AS MinSalary,
       MAX(e.Salary) AS MaxSalary,
       AVG(e.Salary) AS AvgSalary
FROM Employees e
JOIN Departments d ON d.DepartmentId = e.DepartmentId
GROUP BY d.DepartmentName;
GO

PRINT 'Q42';
SELECT CASE WHEN Salary < 70000 THEN 'Low'
            WHEN Salary < 120000 THEN 'Mid'
            ELSE 'High' END AS Band,
       COUNT(*) AS Employees
FROM Employees
GROUP BY CASE WHEN Salary < 70000 THEN 'Low'
              WHEN Salary < 120000 THEN 'Mid'
              ELSE 'High' END;
GO

PRINT 'Q43';
SELECT TOP 3 c.CustomerName,
       SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
FROM Customers c
JOIN Orders o ON o.CustomerId = c.CustomerId
JOIN OrderItems oi ON oi.OrderId = o.OrderId
GROUP BY c.CustomerId, c.CustomerName
ORDER BY Revenue DESC;
GO

PRINT 'Q44';
SELECT Status,
       COUNT(*) AS Orders,
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM Orders), 1) AS Pct
FROM Orders
GROUP BY Status;
GO

PRINT 'Q45';
SELECT FirstName, LastName, Salary
FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees);
GO

PRINT 'Q46';
SELECT c.Category, s.Status
FROM (SELECT DISTINCT Category FROM Products) c
CROSS JOIN (SELECT DISTINCT Status FROM Orders) s
ORDER BY c.Category, s.Status;
GO

PRINT 'Q47';
SELECT FirstName, LastName, HireDate,
       DATEDIFF(YEAR, HireDate, '2025-12-31') AS TenureYearsApprox
FROM Employees
WHERE DATEADD(YEAR, 5, HireDate) <= '2025-12-31'
ORDER BY HireDate;
GO

PRINT 'Q48';
SELECT e.FirstName, e.LastName, d.Location
FROM Employees e
JOIN Departments d ON d.DepartmentId = e.DepartmentId
WHERE d.Location = 'Singapore';
GO

PRINT 'Q49';
SELECT c.CustomerName, COUNT(o.OrderId) AS OrderCount
FROM Customers c
LEFT JOIN Orders o ON o.CustomerId = c.CustomerId
GROUP BY c.CustomerId, c.CustomerName;
GO

PRINT 'Q50';
SELECT TOP 5 p.ProductName, SUM(oi.Quantity) AS UnitsSold
FROM OrderItems oi
JOIN Products p ON p.ProductId = oi.ProductId
GROUP BY p.ProductId, p.ProductName
ORDER BY UnitsSold DESC;
GO

PRINT 'Q51';
SELECT p.Category, AVG(oi.Discount) AS AvgDiscount
FROM OrderItems oi
JOIN Products p ON p.ProductId = oi.ProductId
GROUP BY p.Category;
GO

PRINT 'Q52';
SELECT YEAR(HireDate) AS HireYear, COUNT(*) AS Hires
FROM Employees
GROUP BY YEAR(HireDate)
ORDER BY HireYear;
GO

PRINT 'Q53';
SELECT Country, COUNT(*) AS Customers
FROM Customers
GROUP BY Country
HAVING COUNT(*) >= 3;
GO

PRINT 'Q54';
SELECT e.FirstName, e.LastName, COUNT(*) AS Orders
FROM Orders o
JOIN Employees e ON e.EmployeeId = o.EmployeeId
GROUP BY e.EmployeeId, e.FirstName, e.LastName;
GO

PRINT 'Q55';
SELECT Status, COUNT(*) AS Orders
FROM Orders
WHERE EmployeeId IS NULL
GROUP BY Status;
GO

PRINT 'Q56';
SELECT e.FirstName, e.LastName, e.DepartmentId, e.Salary
FROM Employees e
WHERE e.Salary = (SELECT MAX(e2.Salary) FROM Employees e2 WHERE e2.DepartmentId = e.DepartmentId);
GO

PRINT 'Q57';
SELECT City FROM Customers
UNION
SELECT Location FROM Departments;
GO

PRINT 'Q58';
SELECT City FROM Customers
INTERSECT
SELECT Location FROM Departments;
GO

PRINT 'Q59';
SELECT City FROM Customers
EXCEPT
SELECT Location FROM Departments;
GO

PRINT 'Q60';
SELECT EmployeeId, LEFT(FirstName, 1) + LEFT(LastName, 1) AS Initials
FROM Employees;
GO

PRINT 'Q61';
SELECT EmployeeId, LEFT(Email, CHARINDEX('@', Email) - 1) AS UserName
FROM Employees
WHERE Email IS NOT NULL;
GO

PRINT 'Q62';
SELECT ProductName, REPLACE(ProductName, ' ', '_') AS Slug
FROM Products;
GO

PRINT 'Q63';
SELECT DATEPART(QUARTER, OrderDate) AS Quarter, COUNT(*) AS Orders
FROM Orders
WHERE OrderDate >= '2024-01-01' AND OrderDate < '2025-01-01'
GROUP BY DATEPART(QUARTER, OrderDate)
ORDER BY Quarter;
GO

PRINT 'Q64';
SELECT DATENAME(WEEKDAY, OrderDate) AS Weekday, COUNT(*) AS Orders
FROM Orders
GROUP BY DATENAME(WEEKDAY, OrderDate);
GO

PRINT 'Q65';
SELECT o.OrderId, c.CustomerName, o.OrderDate, o.Status
FROM Orders o
JOIN Customers c ON c.CustomerId = o.CustomerId
WHERE o.OrderDate >= '2024-12-01' AND o.OrderDate < '2025-01-01';
GO

PRINT 'Q66';
SELECT TOP (3) WITH TIES ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice DESC;
GO

PRINT 'Q67';
SELECT FirstName, LastName, Salary * (1 + COALESCE(CommissionPct, 0)) AS TotalComp
FROM Employees
WHERE DepartmentId = 3;
GO

PRINT 'Q68';
SELECT Category, SUM(Stock * UnitPrice) AS StockValue
FROM Products
GROUP BY Category
HAVING SUM(Stock * UnitPrice) > 50000;
GO

PRINT 'Q69';
SELECT ProductName, IIF(Stock > 0, 'In stock', 'Out of stock') AS Availability
FROM Products;
GO

PRINT 'Q70';
SELECT TOP 10 oi.OrderId, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS OrderTotal
FROM OrderItems oi
GROUP BY oi.OrderId
ORDER BY OrderTotal DESC;
GO

PRINT 'Q71';
SELECT c.CustomerName, COUNT(*) AS Orders
FROM Customers c
JOIN Orders o ON o.CustomerId = c.CustomerId
GROUP BY c.CustomerId, c.CustomerName
HAVING COUNT(*) > 10;
GO

PRINT 'Q72';
SELECT p.ProductId, p.ProductName
FROM Products p
WHERE NOT EXISTS (
    SELECT 1 FROM OrderItems oi
    JOIN Orders o ON o.OrderId = oi.OrderId
    WHERE oi.ProductId = p.ProductId AND o.OrderDate >= '2025-01-01' AND o.OrderDate < '2026-01-01');
GO

PRINT 'Q73';
SELECT AVG(Lines * 1.0) AS AvgLines
FROM (SELECT OrderId, COUNT(*) AS Lines FROM OrderItems GROUP BY OrderId) x;
GO

PRINT 'Q74';
SELECT JobTitle, COUNT(*) AS Employees
FROM Employees
GROUP BY JobTitle
HAVING COUNT(*) > 1;
GO

PRINT 'Q75';
SELECT m.FirstName, m.LastName, COUNT(*) AS DirectReports
FROM Employees e
JOIN Employees m ON m.EmployeeId = e.ManagerId
GROUP BY m.EmployeeId, m.FirstName, m.LastName;
GO

PRINT 'Q76';
SELECT e.EmployeeId, e.FirstName, e.LastName
FROM Employees e
WHERE NOT EXISTS (SELECT 1 FROM Employees r WHERE r.ManagerId = e.EmployeeId);
GO

PRINT 'Q77';
SELECT e1.FirstName + ' ' + e1.LastName AS Employee1, e2.FirstName + ' ' + e2.LastName AS Employee2, e1.Salary
FROM Employees e1
JOIN Employees e2 ON e1.DepartmentId = e2.DepartmentId AND e1.Salary = e2.Salary AND e1.EmployeeId < e2.EmployeeId;
GO

PRINT 'Q78';
SELECT YEAR(SignupDate) AS SignupYear, COUNT(*) AS Customers
FROM Customers
GROUP BY YEAR(SignupDate)
ORDER BY SignupYear;
GO

PRINT 'Q79';
SELECT YEAR(o.OrderDate) AS Yr, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
FROM Orders o
JOIN OrderItems oi ON oi.OrderId = o.OrderId
GROUP BY YEAR(o.OrderDate)
ORDER BY Yr;
GO

PRINT 'Q80';
SELECT c.Country, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
FROM Customers c
JOIN Orders o ON o.CustomerId = c.CustomerId
JOIN OrderItems oi ON oi.OrderId = o.OrderId
GROUP BY c.Country
ORDER BY Revenue DESC;
GO

PRINT 'Q81';
SELECT TOP 3 c.CustomerName, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS CancelledRevenue
FROM Customers c
JOIN Orders o ON o.CustomerId = c.CustomerId
JOIN OrderItems oi ON oi.OrderId = o.OrderId
WHERE o.Status = 'Cancelled'
GROUP BY c.CustomerId, c.CustomerName
ORDER BY CancelledRevenue DESC;
GO

PRINT 'Q82';
SELECT JobTitle, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY JobTitle
HAVING COUNT(*) >= 2;
GO

PRINT 'Q83';
SELECT p.ProductName, p.Category, p.UnitPrice
FROM Products p
WHERE p.UnitPrice > (SELECT AVG(p2.UnitPrice) FROM Products p2 WHERE p2.Category = p.Category);
GO

PRINT 'Q84';
SELECT e.FirstName, e.LastName, COUNT(DISTINCT o.CustomerId) AS Customers
FROM Orders o
JOIN Employees e ON e.EmployeeId = o.EmployeeId
GROUP BY e.EmployeeId, e.FirstName, e.LastName;
GO

PRINT 'Q85';
SELECT EmployeeId, COUNT(*) AS Records
FROM SalaryHistory
GROUP BY EmployeeId
HAVING COUNT(*) = 3;
GO

PRINT 'Q86';
SELECT p.ProductName, SUM(oi.Quantity * oi.UnitPrice * oi.Discount) AS DiscountGiven
FROM OrderItems oi
JOIN Products p ON p.ProductId = oi.ProductId
GROUP BY p.ProductId, p.ProductName
HAVING SUM(oi.Quantity * oi.UnitPrice * oi.Discount) > 1000;
GO

PRINT 'Q87';
SELECT e.FirstName, e.LastName, e.DepartmentId AS EmpDept, m.DepartmentId AS MgrDept
FROM Employees e
JOIN Employees m ON m.EmployeeId = e.ManagerId
WHERE e.DepartmentId <> m.DepartmentId;
GO

PRINT 'Q88';
SELECT c.CustomerName, COUNT(DISTINCT oi.ProductId) AS Products
FROM Customers c
JOIN Orders o ON o.CustomerId = c.CustomerId
JOIN OrderItems oi ON oi.OrderId = o.OrderId
GROUP BY c.CustomerId, c.CustomerName;
GO

PRINT 'Q89';
SELECT d.DepartmentName, STRING_AGG(e.FirstName, ',') WITHIN GROUP (ORDER BY e.FirstName) AS Employees
FROM Departments d
JOIN Employees e ON e.DepartmentId = d.DepartmentId
GROUP BY d.DepartmentName;
GO

PRINT 'Q90';
SELECT TABLE_NAME, COUNT(*) AS ColumnCount
FROM INFORMATION_SCHEMA.COLUMNS
GROUP BY TABLE_NAME;
GO

PRINT 'Q91';
SELECT FirstName + ' ' + LastName AS Name, 'Employee' AS Type FROM Employees
UNION ALL
SELECT CustomerName, 'Customer' FROM Customers;
GO

PRINT 'Q92';
SELECT e.FirstName, e.LastName, e.DepartmentId, e.Salary
FROM Employees e
WHERE e.Salary > (SELECT AVG(e2.Salary)
                  FROM Employees e2
                  WHERE e2.DepartmentId = e.DepartmentId);
GO

PRINT 'Q93';
SELECT c.CustomerId, c.CustomerName
FROM Customers c
WHERE EXISTS (SELECT 1 FROM Orders o
              WHERE o.CustomerId = c.CustomerId AND o.Status = 'Cancelled');
GO

PRINT 'Q94';
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
GO

PRINT 'Q95';
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
GO

PRINT 'Q96';
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
GO

PRINT 'Q97';
WITH Chain AS (
    SELECT EmployeeId, CAST(FirstName AS NVARCHAR(400)) AS Path
    FROM Employees WHERE EmployeeId = 1
    UNION ALL
    SELECT e.EmployeeId, CAST(c.Path + N' > ' + e.FirstName AS NVARCHAR(400))
    FROM Employees e
    JOIN Chain c ON e.ManagerId = c.EmployeeId
)
SELECT EmployeeId, Path FROM Chain ORDER BY Path;
GO

PRINT 'Q98';
WITH Ranked AS (
    SELECT e.*, ROW_NUMBER() OVER (PARTITION BY e.DepartmentId ORDER BY e.Salary DESC, e.EmployeeId) AS rn
    FROM Employees e
    WHERE e.DepartmentId IS NOT NULL
)
SELECT d.DepartmentName, r.FirstName, r.LastName, r.Salary
FROM Ranked r
JOIN Departments d ON d.DepartmentId = r.DepartmentId
WHERE r.rn = 1;
GO

PRINT 'Q99';
SELECT FirstName, LastName, Salary,
       RANK()       OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS SalaryRank,
       DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS SalaryDenseRank
FROM Employees
WHERE DepartmentId = 2
ORDER BY Salary DESC;
GO

PRINT 'Q100';
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
GO

PRINT 'Q101';
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
GO

PRINT 'Q102';
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
GO

PRINT 'Q103';
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
GO

PRINT 'Q104';
SELECT FirstName, LastName, Salary,
       NTILE(4) OVER (ORDER BY Salary DESC, EmployeeId) AS Quartile
FROM Employees;
GO

PRINT 'Q105';
SELECT OrderId, OrderDate,
       DATEDIFF(DAY, OrderDate, LEAD(OrderDate) OVER (ORDER BY OrderDate)) AS DaysToNext
FROM Orders
WHERE CustomerId = 1;
GO

PRINT 'Q106';
SELECT FirstName, LastName, DepartmentId, Salary,
       FIRST_VALUE(FirstName) OVER (PARTITION BY DepartmentId ORDER BY Salary DESC, EmployeeId) AS TopEarner
FROM Employees
WHERE DepartmentId IS NOT NULL;
GO

PRINT 'Q107';
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
GO

PRINT 'Q108';
SELECT FirstName, LastName, DepartmentId, Salary,
       ROUND(100.0 * Salary / SUM(Salary) OVER (PARTITION BY DepartmentId), 2) AS PctOfDept
FROM Employees
WHERE DepartmentId IS NOT NULL;
GO

PRINT 'Q109';
SELECT FirstName, LastName, Salary,
       ROUND(PERCENT_RANK() OVER (ORDER BY Salary), 3) AS PctRank
FROM Employees;
GO

PRINT 'Q110';
SELECT FirstName, LastName, Salary,
       ROUND(CUME_DIST() OVER (ORDER BY Salary), 3) AS CumeDist
FROM Employees;
GO

PRINT 'Q111';
SELECT FirstName, LastName, DepartmentId, Salary,
       AVG(Salary) OVER (PARTITION BY DepartmentId) AS DeptAvg,
       Salary - AVG(Salary) OVER (PARTITION BY DepartmentId) AS Diff
FROM Employees
WHERE DepartmentId IS NOT NULL;
GO

PRINT 'Q112';
WITH CustRev AS (
    SELECT o.CustomerId, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.CustomerId
)
SELECT c.CustomerName, cr.Revenue
FROM CustRev cr JOIN Customers c ON c.CustomerId = cr.CustomerId
WHERE cr.Revenue > (SELECT AVG(Revenue) FROM CustRev);
GO

PRINT 'Q113';
WITH P AS (
    SELECT p.ProductName, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM OrderItems oi JOIN Products p ON p.ProductId = oi.ProductId
    GROUP BY p.ProductId, p.ProductName
)
SELECT ProductName, Revenue, DENSE_RANK() OVER (ORDER BY Revenue DESC) AS Rnk
FROM P
ORDER BY Rnk
OFFSET 0 ROWS FETCH NEXT 5 ROWS ONLY;
GO

PRINT 'Q114';
WITH Nums AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM Nums WHERE n < 10
)
SELECT n FROM Nums;
GO

PRINT 'Q115';
WITH Sub AS (
    SELECT EmployeeId, FirstName, LastName, 1 AS Level FROM Employees WHERE ManagerId = 7
    UNION ALL
    SELECT e.EmployeeId, e.FirstName, e.LastName, s.Level + 1
    FROM Employees e JOIN Sub s ON e.ManagerId = s.EmployeeId
)
SELECT EmployeeId, FirstName + ' ' + LastName AS Name, Level FROM Sub;
GO

PRINT 'Q116';
WITH Sub AS (
    SELECT EmployeeId FROM Employees WHERE ManagerId = 3
    UNION ALL
    SELECT e.EmployeeId FROM Employees e JOIN Sub s ON e.ManagerId = s.EmployeeId
)
SELECT COUNT(*) AS TotalReports FROM Sub;
GO

PRINT 'Q117';
WITH D AS (
    SELECT CAST('2024-01-01' AS DATE) AS d
    UNION ALL
    SELECT DATEADD(DAY, 1, d) FROM D WHERE d < '2024-01-31'
)
SELECT D.d AS OrderDay, COUNT(o.OrderId) AS Orders
FROM D LEFT JOIN Orders o ON o.OrderDate = D.d
GROUP BY D.d
ORDER BY D.d;
GO

PRINT 'Q118';
WITH Org AS (
    SELECT EmployeeId, 0 AS Level FROM Employees WHERE ManagerId IS NULL AND EmployeeId = 1
    UNION ALL
    SELECT e.EmployeeId, o.Level + 1 FROM Employees e JOIN Org o ON e.ManagerId = o.EmployeeId
)
SELECT Level, COUNT(*) AS Employees FROM Org GROUP BY Level ORDER BY Level;
GO

PRINT 'Q119';
SELECT c.CustomerName, x.OrderId, x.OrderDate
FROM Customers c
CROSS APPLY (SELECT TOP 2 o.OrderId, o.OrderDate FROM Orders o WHERE o.CustomerId = c.CustomerId ORDER BY o.OrderDate DESC) x;
GO

PRINT 'Q120';
SELECT c.CustomerName, x.OrderDate AS LastOrderDate
FROM Customers c
OUTER APPLY (SELECT TOP 1 o.OrderDate FROM Orders o WHERE o.CustomerId = c.CustomerId ORDER BY o.OrderDate DESC) x;
GO

PRINT 'Q121';
SELECT Yr, [Delivered], [Shipped], [Pending], [Cancelled]
FROM (SELECT YEAR(OrderDate) AS Yr, Status FROM Orders) s
PIVOT (COUNT(Status) FOR Status IN ([Delivered], [Shipped], [Pending], [Cancelled])) p
ORDER BY Yr;
GO

PRINT 'Q122';
SELECT Stat, Value
FROM (SELECT CAST(MIN(Salary) AS DECIMAL(12,2)) AS Minimum, CAST(MAX(Salary) AS DECIMAL(12,2)) AS Maximum, CAST(AVG(Salary) AS DECIMAL(12,2)) AS Average FROM Employees) s
UNPIVOT (Value FOR Stat IN (Minimum, Maximum, Average)) u;
GO

PRINT 'Q123';
SELECT d.DepartmentName,
       SUM(CASE WHEN e.Salary >= 100000 THEN 1 ELSE 0 END) AS HighEarners,
       SUM(CASE WHEN e.Salary <  100000 THEN 1 ELSE 0 END) AS Others
FROM Departments d JOIN Employees e ON e.DepartmentId = d.DepartmentId
GROUP BY d.DepartmentName;
GO

PRINT 'Q124';
SELECT c.CustomerName
FROM Customers c
JOIN Orders o ON o.CustomerId = c.CustomerId
JOIN OrderItems oi ON oi.OrderId = o.OrderId
JOIN Products p ON p.ProductId = oi.ProductId
GROUP BY c.CustomerId, c.CustomerName
HAVING COUNT(DISTINCT p.Category) = (SELECT COUNT(DISTINCT Category) FROM Products);
GO

PRINT 'Q125';
SELECT CustomerId FROM Orders WHERE YEAR(OrderDate) = 2023
INTERSECT
SELECT CustomerId FROM Orders WHERE YEAR(OrderDate) = 2025;
GO

PRINT 'Q126';
SELECT CustomerId FROM Customers
EXCEPT
SELECT CustomerId FROM Orders;
GO

PRINT 'Q127';
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
GO

PRINT 'Q128';
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
GO

PRINT 'Q129';
SELECT e.FirstName, e.LastName, e.Salary, m.FirstName AS Manager, m.Salary AS ManagerSalary
FROM Employees e JOIN Employees m ON m.EmployeeId = e.ManagerId
WHERE e.Salary >= 0.8 * m.Salary;
GO

PRINT 'Q130';
SELECT d.DepartmentName, AVG(e.Salary) AS AvgSalary
FROM Departments d JOIN Employees e ON e.DepartmentId = d.DepartmentId
GROUP BY d.DepartmentName
HAVING AVG(e.Salary) > (SELECT AVG(Salary) FROM Employees);
GO

PRINT 'Q131';
WITH OT AS (
    SELECT o.OrderId, o.CustomerId, o.OrderDate, o.Status, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Total
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.OrderId, o.CustomerId, o.OrderDate, o.Status
)
SELECT OrderId, Total
FROM OT
WHERE Total > (SELECT AVG(Total) FROM OT);
GO

PRINT 'Q132';
WITH R AS (
    SELECT CustomerId, OrderId, OrderDate,
           ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY OrderDate DESC) AS rn
    FROM Orders
)
SELECT c.CustomerName, R.OrderId, R.OrderDate
FROM R JOIN Customers c ON c.CustomerId = R.CustomerId
WHERE R.rn = 2;
GO

PRINT 'Q133';
SELECT c.CustomerName, DATEDIFF(DAY, MIN(o.OrderDate), MAX(o.OrderDate)) AS SpanDays
FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId
GROUP BY c.CustomerId, c.CustomerName;
GO

PRINT 'Q134';
WITH G AS (
    SELECT CustomerId, DATEDIFF(DAY, LAG(OrderDate) OVER (PARTITION BY CustomerId ORDER BY OrderDate), OrderDate) AS Gap
    FROM Orders
)
SELECT c.CustomerName, ROUND(AVG(G.Gap * 1.0), 1) AS AvgGapDays
FROM G JOIN Customers c ON c.CustomerId = G.CustomerId
GROUP BY c.CustomerId, c.CustomerName;
GO

PRINT 'Q135';
SELECT FirstName, LastName, HireDate,
       COUNT(*) OVER (ORDER BY HireDate, EmployeeId ROWS UNBOUNDED PRECEDING) AS Headcount
FROM Employees;
GO

PRINT 'Q136';
WITH CR AS (
    SELECT c.CustomerName, c.Country, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY c.CustomerId, c.CustomerName, c.Country
), R AS (
    SELECT *, RANK() OVER (PARTITION BY Country ORDER BY Revenue DESC) AS rnk FROM CR
)
SELECT Country, CustomerName, Revenue FROM R WHERE rnk = 1;
GO

PRINT 'Q137';
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
GO

PRINT 'Q138';
WITH P AS (
    SELECT p.Category, p.ProductName, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM OrderItems oi JOIN Products p ON p.ProductId = oi.ProductId
    GROUP BY p.ProductId, p.Category, p.ProductName
)
SELECT Category, ProductName, Revenue,
       ROUND(100.0 * Revenue / SUM(Revenue) OVER (PARTITION BY Category), 2) AS PctOfCategory
FROM P;
GO

PRINT 'Q139';
WITH OT AS (
    SELECT o.OrderId, o.CustomerId, o.OrderDate, o.Status, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Total
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.OrderId, o.CustomerId, o.OrderDate, o.Status
)
SELECT c.Country, SUM(OT.Total) AS Revenue, MAX(OT.Total) AS BiggestOrder
FROM OT JOIN Customers c ON c.CustomerId = OT.CustomerId
GROUP BY c.Country;
GO

PRINT 'Q140';
SELECT e.FirstName, e.LastName, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue,
       RANK() OVER (ORDER BY SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) DESC) AS Rnk
FROM Orders o
JOIN OrderItems oi ON oi.OrderId = o.OrderId
JOIN Employees e ON e.EmployeeId = o.EmployeeId
GROUP BY e.EmployeeId, e.FirstName, e.LastName;
GO

PRINT 'Q141';
SELECT YEAR(o.OrderDate) AS Yr,
       SUM(CASE WHEN DATEPART(QUARTER, o.OrderDate) = 1 THEN oi.Quantity * oi.UnitPrice * (1 - oi.Discount) ELSE 0 END) AS Q1,
       SUM(CASE WHEN DATEPART(QUARTER, o.OrderDate) = 2 THEN oi.Quantity * oi.UnitPrice * (1 - oi.Discount) ELSE 0 END) AS Q2,
       SUM(CASE WHEN DATEPART(QUARTER, o.OrderDate) = 3 THEN oi.Quantity * oi.UnitPrice * (1 - oi.Discount) ELSE 0 END) AS Q3,
       SUM(CASE WHEN DATEPART(QUARTER, o.OrderDate) = 4 THEN oi.Quantity * oi.UnitPrice * (1 - oi.Discount) ELSE 0 END) AS Q4
FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
WHERE o.Status <> 'Cancelled'
GROUP BY YEAR(o.OrderDate)
ORDER BY Yr;
GO

PRINT 'Q142';
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
GO

PRINT 'Q143';
WITH L AS (
    SELECT EmployeeId, FirstName, LastName, COUNT(*) OVER (PARTITION BY LastName) AS Cnt FROM Employees
)
SELECT EmployeeId, FirstName, LastName FROM L WHERE Cnt > 1;
GO

PRINT 'Q144';
WITH D AS (
    SELECT EmployeeId, FirstName, LastName, Salary, HireDate,
           ROW_NUMBER() OVER (PARTITION BY Salary, HireDate ORDER BY EmployeeId) AS rn
    FROM Employees
)
SELECT EmployeeId, FirstName, LastName FROM D WHERE rn > 1;
GO

PRINT 'Q145';
SELECT DISTINCT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Salary) OVER () AS MedianSalary
FROM Employees;
GO

PRINT 'Q146';
SELECT DISTINCT DepartmentId,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Salary) OVER (PARTITION BY DepartmentId) AS MedianSalary
FROM Employees
WHERE DepartmentId IS NOT NULL;
GO

PRINT 'Q147';
WITH G AS (
    SELECT CustomerId, DATEDIFF(DAY, LAG(OrderDate) OVER (PARTITION BY CustomerId ORDER BY OrderDate), OrderDate) AS Gap
    FROM Orders
)
SELECT c.CustomerName, MAX(G.Gap) AS LongestGap
FROM G JOIN Customers c ON c.CustomerId = G.CustomerId
GROUP BY c.CustomerId, c.CustomerName;
GO

PRINT 'Q148';
SELECT d.DepartmentName, STRING_AGG(t.JobTitle, ', ') WITHIN GROUP (ORDER BY t.JobTitle) AS Titles
FROM Departments d
JOIN (SELECT DISTINCT DepartmentId, JobTitle FROM Employees) t ON t.DepartmentId = d.DepartmentId
GROUP BY d.DepartmentName;
GO

PRINT 'Q149';
WITH CR AS (
    SELECT c.CustomerName, c.Country, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY c.CustomerId, c.CustomerName, c.Country
)
SELECT CustomerName, Country, Revenue,
       AVG(Revenue) OVER (PARTITION BY Country) AS CountryAvg
FROM CR;
GO

PRINT 'Q150';
SELECT c.CustomerName, COUNT(*) AS Orders
FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId AND YEAR(o.OrderDate) = YEAR(c.SignupDate)
GROUP BY c.CustomerId, c.CustomerName;
GO

PRINT 'Q151';
WITH R AS (
    SELECT oi.OrderId, oi.ProductId, oi.UnitPrice,
           ROW_NUMBER() OVER (PARTITION BY oi.OrderId ORDER BY oi.UnitPrice DESC) AS rn
    FROM OrderItems oi
)
SELECT R.OrderId, p.ProductName, R.UnitPrice
FROM R JOIN Products p ON p.ProductId = R.ProductId
WHERE R.rn = 1;
GO

PRINT 'Q152';
SELECT c.CustomerName, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId
GROUP BY c.CustomerId, c.CustomerName
HAVING SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) > (
    SELECT SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) FROM Customers c2 JOIN Orders o ON o.CustomerId = c2.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId
    WHERE c2.CustomerName = 'Acme Corp');
GO

PRINT 'Q153';
SELECT c.CustomerName
FROM Customers c
WHERE EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerId = c.CustomerId AND o.Status = 'Cancelled')
  AND EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerId = c.CustomerId AND o.Status = 'Delivered');
GO

PRINT 'Q154';
SELECT e.FirstName, e.LastName, COUNT(DISTINCT o.CustomerId) AS Customers
FROM Orders o JOIN Employees e ON e.EmployeeId = o.EmployeeId
GROUP BY e.EmployeeId, e.FirstName, e.LastName
HAVING COUNT(DISTINCT o.CustomerId) > 5;
GO

PRINT 'Q155';
SELECT p1.ProductName AS ProductA, p2.ProductName AS ProductB, COUNT(*) AS Together
FROM OrderItems a
JOIN OrderItems b ON b.OrderId = a.OrderId AND a.ProductId < b.ProductId
JOIN Products p1 ON p1.ProductId = a.ProductId
JOIN Products p2 ON p2.ProductId = b.ProductId
GROUP BY p1.ProductName, p2.ProductName
HAVING COUNT(*) >= 3;
GO

PRINT 'Q156';
WITH M AS (
    SELECT DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1) AS MonthStart, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    WHERE o.Status <> 'Cancelled'
    GROUP BY DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1)
), R AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY YEAR(MonthStart) ORDER BY Revenue DESC) AS rn FROM M
)
SELECT YEAR(MonthStart) AS Yr, MonthStart, Revenue FROM R WHERE rn = 1;
GO

PRINT 'Q157';
WITH P AS (
    SELECT DISTINCT PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY Salary) OVER () AS P90 FROM Employees
)
SELECT e.FirstName, e.LastName, e.Salary
FROM Employees e CROSS JOIN P
WHERE e.Salary > P.P90;
GO

PRINT 'Q158';
SELECT e.FirstName, e.LastName,
       CASE WHEN EXISTS (SELECT 1 FROM Employees r WHERE r.ManagerId = e.EmployeeId) THEN 'Manager' ELSE 'Individual Contributor' END AS Role
FROM Employees e;
GO

PRINT 'Q159';
WITH OT AS (
    SELECT o.OrderId, o.CustomerId, o.OrderDate, o.Status, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Total
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.OrderId, o.CustomerId, o.OrderDate, o.Status
), M AS (
    SELECT *, MAX(Total) OVER (PARTITION BY CustomerId) AS MaxTotal FROM OT
)
SELECT OrderId, CustomerId, Total FROM M WHERE Total = MaxTotal;
GO

PRINT 'Q160';
SELECT e.FirstName, e.LastName
FROM Employees e
WHERE EXISTS (SELECT 1 FROM Orders o WHERE o.EmployeeId = e.EmployeeId)
  AND NOT EXISTS (SELECT 1 FROM Orders o WHERE o.EmployeeId = e.EmployeeId AND o.Status = 'Cancelled');
GO

PRINT 'Q161';
WITH R AS (
    SELECT DepartmentId, FirstName, LastName, Salary,
           DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS rnk
    FROM Employees
    WHERE DepartmentId IS NOT NULL
)
SELECT d.DepartmentName, R.FirstName, R.LastName, R.Salary
FROM R JOIN Departments d ON d.DepartmentId = R.DepartmentId
WHERE R.rnk = 2;
GO

PRINT 'Q162';
SELECT Salary, HireDate, COUNT(*) AS Employees
FROM Employees
GROUP BY Salary, HireDate
HAVING COUNT(*) > 1;
GO

PRINT 'Q163';
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
GO

PRINT 'Q164';
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
GO

PRINT 'Q165';
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
GO

PRINT 'Q166';
WITH D AS (
    SELECT CAST('2024-01-01' AS DATE) AS d
    UNION ALL
    SELECT DATEADD(DAY, 1, d) FROM D WHERE d < '2024-03-31'
)
SELECT d AS EmptyDay
FROM D
WHERE NOT EXISTS (SELECT 1 FROM Orders o WHERE o.OrderDate = D.d)
OPTION (MAXRECURSION 400);
GO

PRINT 'Q167';
WITH Dd AS (SELECT DISTINCT OrderDate AS d FROM Orders),
G AS (
    SELECT d, DATEADD(DAY, -ROW_NUMBER() OVER (ORDER BY d), d) AS grp FROM Dd
)
SELECT MIN(d) AS StartDate, MAX(d) AS EndDate, COUNT(*) AS Days
FROM G
GROUP BY grp
HAVING COUNT(*) >= 2;
GO

PRINT 'Q168';
WITH OT AS (
    SELECT o.OrderId, o.CustomerId, o.OrderDate, o.Status, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Total
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.OrderId, o.CustomerId, o.OrderDate, o.Status
)
SELECT CustomerId, OrderId, OrderDate, Total,
       SUM(Total) OVER (PARTITION BY CustomerId, YEAR(OrderDate) ORDER BY OrderDate ROWS UNBOUNDED PRECEDING) AS YtdTotal
FROM OT;
GO

PRINT 'Q169';
WITH A AS (SELECT DISTINCT CustomerId FROM Orders WHERE YEAR(OrderDate) = 2023),
     B AS (SELECT DISTINCT CustomerId FROM Orders WHERE YEAR(OrderDate) = 2024)
SELECT COUNT(B.CustomerId) AS Retained,
       ROUND(100.0 * COUNT(B.CustomerId) / COUNT(A.CustomerId), 1) AS RetentionPct
FROM A LEFT JOIN B ON B.CustomerId = A.CustomerId;
GO

PRINT 'Q170';
WITH OT AS (
    SELECT o.OrderId, o.CustomerId, o.OrderDate, o.Status, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Total
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.OrderId, o.CustomerId, o.OrderDate, o.Status
), R AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY OrderDate) AS rn FROM OT
)
SELECT CustomerId, OrderId, OrderDate, Total FROM R WHERE rn = 1;
GO

PRINT 'Q171';
WITH R AS (
    SELECT Category, ProductName, Stock, ROW_NUMBER() OVER (PARTITION BY Category ORDER BY Stock) AS rn FROM Products
)
SELECT Category, ProductName, Stock FROM R WHERE rn <= 2;
GO

PRINT 'Q172';
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
GO

PRINT 'Q173';
WITH OT AS (
    SELECT o.OrderId, o.CustomerId, o.OrderDate, o.Status, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Total
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.OrderId, o.CustomerId, o.OrderDate, o.Status
)
SELECT DISTINCT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Total) OVER () AS MedianOrder
FROM OT;
GO

PRINT 'Q174';
WITH C AS (
    SELECT EmployeeId,
           100.0 * (Salary - LAG(Salary) OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate)) / LAG(Salary) OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate) AS Pct
    FROM SalaryHistory
)
SELECT EmployeeId, ROUND(MAX(Pct), 1) AS BiggestRaisePct
FROM C
GROUP BY EmployeeId
HAVING MAX(Pct) IS NOT NULL;
GO

PRINT 'Q175';
WITH S AS (
    SELECT EmployeeId, Salary,
           ROW_NUMBER() OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate DESC) AS rn
    FROM SalaryHistory
    WHERE EffectiveDate <= '2024-06-30'
)
SELECT EmployeeId, Salary FROM S WHERE rn = 1;
GO

PRINT 'Q176';
WITH S AS (
    SELECT EmployeeId, Salary,
           ROW_NUMBER() OVER (PARTITION BY EmployeeId ORDER BY EffectiveDate DESC) AS rn
    FROM SalaryHistory
    WHERE EffectiveDate <= '2024-06-30'
)
SELECT SUM(Salary) AS Payroll FROM S WHERE rn = 1;
GO

PRINT 'Q177';
WITH CR AS (
    SELECT c.CustomerName, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY c.CustomerId, c.CustomerName
), N AS (
    SELECT *, NTILE(4) OVER (ORDER BY Revenue DESC) AS Q FROM CR
)
SELECT CustomerName, Revenue FROM N WHERE Q = 1;
GO

PRINT 'Q178';
WITH F AS (
    SELECT CustomerId, DATEFROMPARTS(YEAR(MIN(OrderDate)), MONTH(MIN(OrderDate)), 1) AS FirstMonth
    FROM Orders GROUP BY CustomerId
), M AS (
    SELECT FirstMonth, COUNT(*) AS NewCustomers FROM F GROUP BY FirstMonth
)
SELECT FirstMonth, NewCustomers,
       SUM(NewCustomers) OVER (ORDER BY FirstMonth ROWS UNBOUNDED PRECEDING) AS CumulativeCustomers
FROM M;
GO

PRINT 'Q179';
SELECT p.ProductName, COUNT(*) AS SharedOrders
FROM OrderItems a
JOIN Products lp ON lp.ProductId = a.ProductId AND lp.ProductName = 'Laptop Pro 15'
JOIN OrderItems b ON b.OrderId = a.OrderId AND b.ProductId <> a.ProductId
JOIN Products p ON p.ProductId = b.ProductId
GROUP BY p.ProductId, p.ProductName
HAVING COUNT(*) >= 3;
GO

PRINT 'Q180';
WITH L AS (
    SELECT oi.OrderId, oi.ProductId, oi.Quantity * oi.UnitPrice * (1 - oi.Discount) AS LineValue,
           SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) OVER (PARTITION BY oi.OrderId) AS OrderValue
    FROM OrderItems oi
)
SELECT OrderId, ProductId, ROUND(100.0 * LineValue / OrderValue, 2) AS SharePct
FROM L
WHERE LineValue > 0.5 * OrderValue;
GO

PRINT 'Q181';
SELECT TOP 1 DATENAME(WEEKDAY, o.OrderDate) AS Weekday, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
WHERE o.Status <> 'Cancelled'
GROUP BY DATENAME(WEEKDAY, o.OrderDate)
ORDER BY Revenue DESC;
GO

PRINT 'Q182';
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
GO

PRINT 'Q183';
WITH M AS (
    SELECT DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1) AS MonthStart, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    WHERE o.Status <> 'Cancelled'
    GROUP BY DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1)
)
SELECT cur.MonthStart, cur.Revenue, prev.Revenue AS PrevYearRevenue, cur.Revenue - prev.Revenue AS Diff
FROM M cur
LEFT JOIN M prev ON prev.MonthStart = DATEADD(YEAR, -1, cur.MonthStart);
GO

PRINT 'Q184';
WITH Up AS (
    SELECT EmployeeId, FirstName, LastName, ManagerId, 0 AS Level FROM Employees WHERE EmployeeId = 36
    UNION ALL
    SELECT e.EmployeeId, e.FirstName, e.LastName, e.ManagerId, u.Level + 1
    FROM Employees e JOIN Up u ON e.EmployeeId = u.ManagerId
)
SELECT FirstName + ' ' + LastName AS Name, Level FROM Up ORDER BY Level;
GO

PRINT 'Q185';
SELECT d.DepartmentName,
       SUM(CASE WHEN e.Salary < 70000 THEN 1 ELSE 0 END) AS Low,
       SUM(CASE WHEN e.Salary >= 70000 AND e.Salary < 120000 THEN 1 ELSE 0 END) AS Mid,
       SUM(CASE WHEN e.Salary >= 120000 THEN 1 ELSE 0 END) AS High
FROM Departments d JOIN Employees e ON e.DepartmentId = d.DepartmentId
GROUP BY d.DepartmentName;
GO

PRINT 'Q186';
SELECT c.CustomerName, DATEDIFF(DAY, c.SignupDate, MIN(o.OrderDate)) AS DaysToFirstOrder
FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId
GROUP BY c.CustomerId, c.CustomerName, c.SignupDate;
GO

PRINT 'Q187';
WITH S AS (
    SELECT CustomerId, OrderId, Status,
           LAG(Status) OVER (PARTITION BY CustomerId ORDER BY OrderDate) AS PrevStatus
    FROM Orders
)
SELECT CustomerId, OrderId, Status FROM S WHERE Status = PrevStatus;
GO

PRINT 'Q188';
SELECT m.EmployeeId, m.FirstName, m.LastName
FROM Employees m
WHERE EXISTS (
    SELECT 1 FROM Employees r
    WHERE r.ManagerId = m.EmployeeId
      AND EXISTS (SELECT 1 FROM Employees rr WHERE rr.ManagerId = r.EmployeeId));
GO

PRINT 'Q189';
SELECT SignupYear, [2023], [2024], [2025]
FROM (SELECT YEAR(c.SignupDate) AS SignupYear, YEAR(o.OrderDate) AS OrderYear, o.OrderId
      FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId) s
PIVOT (COUNT(OrderId) FOR OrderYear IN ([2023], [2024], [2025])) p
ORDER BY SignupYear;
GO

PRINT 'Q190';
WITH C AS (SELECT CustomerId, COUNT(*) AS Orders FROM Orders GROUP BY CustomerId)
SELECT CASE WHEN Orders <= 5 THEN '1-5' WHEN Orders <= 10 THEN '6-10' ELSE '11+' END AS Bucket,
       COUNT(*) AS Customers
FROM C
GROUP BY CASE WHEN Orders <= 5 THEN '1-5' WHEN Orders <= 10 THEN '6-10' ELSE '11+' END;
GO

PRINT 'Q191';
WITH R AS (
    SELECT CustomerId, Status, ROW_NUMBER() OVER (PARTITION BY CustomerId ORDER BY OrderDate DESC) AS rn FROM Orders
)
SELECT c.CustomerName
FROM R JOIN Customers c ON c.CustomerId = R.CustomerId
WHERE R.rn = 1 AND R.Status = 'Cancelled';
GO

PRINT 'Q192';
SELECT DISTINCT d.DepartmentName,
       FIRST_VALUE(e.FirstName) OVER (PARTITION BY e.DepartmentId ORDER BY e.Salary DESC, e.EmployeeId) AS HighestPaid,
       FIRST_VALUE(e.FirstName) OVER (PARTITION BY e.DepartmentId ORDER BY e.Salary ASC, e.EmployeeId) AS LowestPaid
FROM Employees e JOIN Departments d ON d.DepartmentId = e.DepartmentId;
GO

PRINT 'Q193';
SELECT EmployeeId, FirstName, LastName, HireDate,
       CASE WHEN DATEADD(YEAR, DATEDIFF(YEAR, HireDate, '2026-01-01'), HireDate) >= '2026-01-01'
            THEN DATEADD(YEAR, DATEDIFF(YEAR, HireDate, '2026-01-01'), HireDate)
            ELSE DATEADD(YEAR, DATEDIFF(YEAR, HireDate, '2026-01-01') + 1, HireDate) END AS NextAnniversary
FROM Employees;
GO

PRINT 'Q194';
WITH R AS (
    SELECT FirstName, LastName, Salary,
           SUM(Salary) OVER (ORDER BY Salary DESC, EmployeeId ROWS UNBOUNDED PRECEDING) AS RunningTotal
    FROM Employees
)
SELECT FirstName, LastName, Salary, RunningTotal FROM R WHERE RunningTotal <= 1000000;
GO

PRINT 'Q195';
SELECT t.name AS TableName, SUM(p.rows) AS TotalRows
FROM sys.tables t JOIN sys.partitions p ON p.object_id = t.object_id AND p.index_id IN (0, 1)
GROUP BY t.name;
GO

PRINT 'Q196';
WITH CR AS (
    SELECT YEAR(o.OrderDate) AS Yr, c.CustomerName, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Customers c JOIN Orders o ON o.CustomerId = c.CustomerId JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY YEAR(o.OrderDate), c.CustomerId, c.CustomerName
), R AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY Yr ORDER BY Revenue DESC) AS Rnk FROM CR
)
SELECT Yr, CustomerName, Revenue, Rnk FROM R WHERE Rnk <= 3;
GO

PRINT 'Q197';
SELECT e.EmployeeId, e.FirstName, e.LastName
FROM Employees e
WHERE e.DepartmentId = 3
  AND NOT EXISTS (SELECT 1 FROM Orders o WHERE o.EmployeeId = e.EmployeeId);
GO

PRINT 'Q198';
WITH M AS (
    SELECT DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1) AS MonthStart, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Revenue
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    WHERE o.Status <> 'Cancelled'
    GROUP BY DATEFROMPARTS(YEAR(o.OrderDate), MONTH(o.OrderDate), 1)
)
SELECT MonthStart, Revenue,
       ROUND(AVG(Revenue) OVER (ORDER BY MonthStart ROWS BETWEEN 2 PRECEDING AND 1 PRECEDING), 2) AS PrevTwoAvg
FROM M;
GO

PRINT 'Q199';
WITH OT AS (
    SELECT o.OrderId, o.CustomerId, o.OrderDate, o.Status, SUM(oi.Quantity * oi.UnitPrice * (1 - oi.Discount)) AS Total
    FROM Orders o JOIN OrderItems oi ON oi.OrderId = o.OrderId
    GROUP BY o.OrderId, o.CustomerId, o.OrderDate, o.Status
), A AS (
    SELECT *, AVG(Total) OVER (PARTITION BY CustomerId) AS CustAvg FROM OT
)
SELECT CustomerId, OrderId, Total, CustAvg FROM A WHERE Total > CustAvg;
GO

PRINT 'Q200';
SELECT Category, [Delivered], [Shipped], [Pending], [Cancelled]
FROM (
    SELECT p.Category, o.Status, oi.Quantity * oi.UnitPrice * (1 - oi.Discount) AS Revenue
    FROM OrderItems oi JOIN Orders o ON o.OrderId = oi.OrderId JOIN Products p ON p.ProductId = oi.ProductId
) s
PIVOT (SUM(Revenue) FOR Status IN ([Delivered], [Shipped], [Pending], [Cancelled])) pv;
GO
