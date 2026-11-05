# SQL Server Interview Practice Questions

## Database schema (PracticeDB)

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


## Easy

**1. [SELECT]** List all columns and rows from the Departments table.

- Tables: Departments
- Return columns (in this order): DepartmentId, DepartmentName, Location

**2. [WHERE]** Show the first name, last name and salary of employees who earn more than 100,000.

- Tables: Employees
- Return columns (in this order): FirstName, LastName, Salary

**3. [ORDER BY]** List all employees (first name, last name, hire date) from the most recently hired to the earliest.

- Tables: Employees
- Return columns (in this order): FirstName, LastName, HireDate
- Sorted by: HireDate DESC

**4. [TOP]** Find the 5 highest paid employees (first name, last name, salary).

- Tables: Employees
- Return columns (in this order): FirstName, LastName, Salary
- Sorted by: Salary DESC

**5. [DISTINCT]** List the distinct job titles in the company, alphabetically.

- Tables: Employees
- Return columns (in this order): JobTitle
- Sorted by: JobTitle

**6. [LIKE]** Find customers whose name starts with the letter 'S'.

- Tables: Customers
- Return columns (in this order): CustomerId, CustomerName

**7. [BETWEEN]** List all orders placed during 2024.

- Tables: Orders
- Return columns (in this order): OrderId, CustomerId, OrderDate, Status

**8. [IN]** List customers located in the USA or the UK.

- Tables: Customers
- Return columns (in this order): CustomerName, City, Country

**9. [NULL]** Find employees who have no manager.

- Tables: Employees
- Return columns (in this order): EmployeeId, FirstName, LastName, JobTitle

**10. [NULL]** List employees who earn a commission (CommissionPct is not null), with their commission percentage.

- Tables: Employees
- Return columns (in this order): FirstName, LastName, CommissionPct

**11. [Expressions]** Show each employee's full name (as FullName) and their annual salary plus a 10% bonus (as SalaryWithBonus).

- Tables: Employees
- Return columns (in this order): FullName, SalaryWithBonus

**12. [COUNT]** How many orders are in the Orders table?

- Tables: Orders
- Return columns (in this order): TotalOrders

**13. [AND / OR]** Find products that are out of stock (Stock = 0) or priced above 1000.

- Tables: Products
- Return columns (in this order): ProductName, UnitPrice, Stock

**14. [OFFSET FETCH]** Page through products ordered by price (highest first): skip the first 5 and return the next 5.

- Tables: Products
- Return columns (in this order): ProductName, UnitPrice
- Sorted by: UnitPrice DESC, ProductId

**15. [COALESCE]** List customers' names and emails, showing 'N/A' where the email is missing.

- Tables: Customers
- Return columns (in this order): CustomerName, Email

**16. [WHERE]** List all employees in the Sales department (DepartmentId = 3): first name, last name and job title.

- Tables: Employees
- Return columns (in this order): FirstName, LastName, JobTitle

**17. [ORDER BY]** List Electronics products (name and price) from the most expensive to the cheapest.

- Tables: Products
- Return columns (in this order): ProductName, UnitPrice
- Sorted by: UnitPrice DESC

**18. [WHERE]** List the customers located in Singapore.

- Tables: Customers
- Return columns (in this order): CustomerId, CustomerName, City

**19. [Dates]** List employees hired on or after 1 January 2021 (name and hire date), earliest first.

- Tables: Employees
- Return columns (in this order): FirstName, LastName, HireDate
- Sorted by: HireDate

**20. [BETWEEN]** Find products priced between 50 and 200 (inclusive), showing name and price.

- Tables: Products
- Return columns (in this order): ProductName, UnitPrice

**21. [WHERE]** List all orders that are currently Pending.

- Tables: Orders
- Return columns (in this order): OrderId, CustomerId, OrderDate

**22. [String functions]** Show department names in upper case together with the length of each name.

- Tables: Departments
- Return columns (in this order): DeptUpper, NameLength

**23. [LIKE]** Find employees whose last name ends with 'ng'.

- Tables: Employees
- Return columns (in this order): FirstName, LastName

**24. [MIN]** What is the lowest product price?

- Tables: Products
- Return columns (in this order): CheapestPrice

**25. [SUM]** What is the total number of units in stock across all products?

- Tables: Products
- Return columns (in this order): TotalStock

**26. [AVG]** What is the average unit price of products in the Accessories category?

- Tables: Products
- Return columns (in this order): AvgPrice

**27. [NOT]** List customers who are not in the USA (name and country).

- Tables: Customers
- Return columns (in this order): CustomerName, Country

**28. [TOP]** Show the 3 most recently signed-up customers (name and signup date).

- Tables: Customers
- Return columns (in this order): CustomerName, SignupDate
- Sorted by: SignupDate DESC

**29. [NULL]** List employees who have no email address recorded.

- Tables: Employees
- Return columns (in this order): EmployeeId, FirstName, LastName

**30. [DISTINCT]** How many different countries do our customers come from?

- Tables: Customers
- Return columns (in this order): Countries


## Medium

**31. [INNER JOIN]** List each employee's full name with their department name. (Employees without a department should not appear.)

- Tables: Employees, Departments
- Return columns (in this order): FirstName, LastName, DepartmentName

**32. [LEFT JOIN]** Find departments that have no employees.

- Tables: Departments, Employees
- Return columns (in this order): DepartmentName

**33. [Self join]** List each employee with their manager's name (show NULL / 'None' when there is no manager).

- Tables: Employees
- Return columns (in this order): Employee, Manager

**34. [GROUP BY]** Count the number of employees in each department (show the department name).

- Tables: Departments, Employees
- Return columns (in this order): DepartmentName, EmployeeCount
- Sorted by: EmployeeCount DESC

**35. [AVG]** Show the average salary per department (rounded to 2 decimals), highest first.

- Tables: Employees, Departments
- Return columns (in this order): DepartmentName, AvgSalary
- Sorted by: AvgSalary DESC

**36. [HAVING]** List departments with more than 5 employees.

- Tables: Employees, Departments
- Return columns (in this order): DepartmentName, EmployeeCount

**37. [SUM]** Calculate total revenue per product category. Revenue = Quantity * UnitPrice * (1 - Discount) from OrderItems. Highest first.

- Tables: OrderItems, Products
- Return columns (in this order): Category, Revenue
- Sorted by: Revenue DESC

**38. [Anti join]** Find customers who have never placed an order.

- Tables: Customers, Orders
- Return columns (in this order): CustomerId, CustomerName

**39. [Anti join]** Find products that have never been ordered.

- Tables: Products, OrderItems
- Return columns (in this order): ProductId, ProductName

**40. [Date functions]** Show the number of orders per month for 2024 (year, month, order count), in calendar order.

- Tables: Orders
- Return columns (in this order): Yr, Mth, Orders
- Sorted by: Yr, Mth

**41. [MIN / MAX]** For each department show headcount, minimum, maximum and average salary.

- Tables: Employees, Departments
- Return columns (in this order): DepartmentName, Headcount, MinSalary, MaxSalary, AvgSalary

**42. [CASE]** Classify employees into salary bands: 'Low' (< 70,000), 'Mid' (70,000-119,999), 'High' (>= 120,000) and count employees in each band.

- Tables: Employees
- Return columns (in this order): Band, Employees

**43. [Multi-table JOIN]** Find the top 3 customers by total revenue (customer name and revenue).

- Tables: Customers, Orders, OrderItems
- Return columns (in this order): CustomerName, Revenue
- Sorted by: Revenue DESC

**44. [GROUP BY]** Show the number of orders per Status and what percentage of all orders each status represents (1 decimal).

- Tables: Orders
- Return columns (in this order): Status, Orders, Pct

**45. [Subquery]** List employees who earn more than the company-wide average salary.

- Tables: Employees
- Return columns (in this order): FirstName, LastName, Salary

**46. [CROSS JOIN]** Produce a grid of every product Category combined with every order Status (distinct values only).

- Tables: Products, Orders
- Return columns (in this order): Category, Status
- Sorted by: c.Category, s.Status

**47. [DATEDIFF]** Show each employee's tenure in whole years as of 2025-12-31, for employees with at least 5 years of service.

- Tables: Employees
- Return columns (in this order): FirstName, LastName, HireDate, TenureYearsApprox
- Sorted by: HireDate

**48. [INNER JOIN]** List first name, last name and department location for employees whose department is located in Singapore.

- Tables: Employees, Departments
- Return columns (in this order): FirstName, LastName, Location

**49. [LEFT JOIN]** Show every customer with their number of orders, including customers with none (0).

- Tables: Customers, Orders
- Return columns (in this order): CustomerName, OrderCount

**50. [SUM]** Show the total quantity sold per product (product name and units), for the 5 best-selling products.

- Tables: OrderItems, Products
- Return columns (in this order): ProductName, UnitsSold
- Sorted by: UnitsSold DESC

**51. [AVG]** Show the average discount (as a fraction) per product category.

- Tables: OrderItems, Products
- Return columns (in this order): Category, AvgDiscount

**52. [GROUP BY]** How many employees were hired in each year? (year, count), oldest year first.

- Tables: Employees
- Return columns (in this order): HireYear, Hires
- Sorted by: HireYear

**53. [HAVING]** List countries that have at least 3 customers, with the customer count.

- Tables: Customers
- Return columns (in this order): Country, Customers

**54. [GROUP BY]** For each sales rep (employee who owns orders), show their name and number of orders. Ignore orders without a rep.

- Tables: Orders, Employees
- Return columns (in this order): FirstName, LastName, Orders

**55. [NULL]** How many orders of each Status have no sales rep assigned?

- Tables: Orders
- Return columns (in this order): Status, Orders

**56. [Subquery]** List the employees who earn the highest salary in their own department (include ties).

- Tables: Employees
- Return columns (in this order): FirstName, LastName, DepartmentId, Salary

**57. [UNION]** Produce a single distinct list of cities that appear either as a customer city or as a department location.

- Tables: Customers, Departments
- Return columns (in this order): City

**58. [INTERSECT]** Which cities are both a customer city and a department location?

- Tables: Customers, Departments
- Return columns (in this order): City

**59. [EXCEPT]** Which customer cities are NOT department locations? (distinct)

- Tables: Customers, Departments
- Return columns (in this order): City

**60. [String functions]** Show each employee's initials (e.g. 'AT' for Alice Tan) together with their EmployeeId.

- Tables: Employees
- Return columns (in this order): EmployeeId, Initials

**61. [String functions]** Extract the username part of each employee's email (text before '@'). Skip employees without an email.

- Tables: Employees
- Return columns (in this order): EmployeeId, UserName

**62. [String functions]** Show product names with spaces replaced by underscores.

- Tables: Products
- Return columns (in this order): ProductName, Slug

**63. [Date functions]** How many orders were placed in each quarter of 2024? (quarter, orders)

- Tables: Orders
- Return columns (in this order): Quarter, Orders
- Sorted by: Quarter

**64. [Date functions]** How many orders were placed on each day of the week (name of the weekday)?

- Tables: Orders
- Return columns (in this order): Weekday, Orders

**65. [JOIN]** List orders placed in December 2024 with the customer name, order date and status.

- Tables: Orders, Customers
- Return columns (in this order): OrderId, CustomerName, OrderDate, Status

**66. [TOP WITH TIES]** List the 3 highest-priced products, including any products tied with the 3rd price.

- Tables: Products
- Return columns (in this order): ProductName, UnitPrice
- Sorted by: UnitPrice DESC

**67. [ISNULL]** For Sales employees (DepartmentId 3) show total compensation = Salary * (1 + commission), treating a missing commission as 0.

- Tables: Employees
- Return columns (in this order): FirstName, LastName, TotalComp

**68. [GROUP BY]** For each product category show the stock value (SUM of Stock * UnitPrice). Only show categories above 50,000.

- Tables: Products
- Return columns (in this order): Category, StockValue

**69. [IIF]** Label each product 'In stock' or 'Out of stock' based on Stock.

- Tables: Products
- Return columns (in this order): ProductName, Availability

**70. [SUM]** Show the 10 orders with the highest total value (OrderId and total).

- Tables: OrderItems
- Return columns (in this order): OrderId, OrderTotal
- Sorted by: OrderTotal DESC

**71. [HAVING]** List customers who placed more than 10 orders (name and count).

- Tables: Customers, Orders
- Return columns (in this order): CustomerName, Orders

**72. [NOT EXISTS]** Which products were not ordered at all in 2025?

- Tables: Products, OrderItems, Orders
- Return columns (in this order): ProductId, ProductName

**73. [Derived table]** What is the average number of line items per order?

- Tables: OrderItems
- Return columns (in this order): AvgLines

**74. [HAVING]** Which job titles are held by more than one employee? (title, count)

- Tables: Employees
- Return columns (in this order): JobTitle, Employees

**75. [Self join]** List each manager's name with their number of direct reports (managers only).

- Tables: Employees
- Return columns (in this order): FirstName, LastName, DirectReports

**76. [NOT EXISTS]** List employees who do not manage anyone.

- Tables: Employees
- Return columns (in this order): EmployeeId, FirstName, LastName

**77. [Self join]** Find pairs of different employees in the same department who earn exactly the same salary (each pair once).

- Tables: Employees
- Return columns (in this order): Employee1, Employee2, Salary

**78. [GROUP BY]** How many customers signed up in each year?

- Tables: Customers
- Return columns (in this order): SignupYear, Customers
- Sorted by: SignupYear

**79. [SUM]** Show total revenue per calendar year.

- Tables: Orders, OrderItems
- Return columns (in this order): Yr, Revenue
- Sorted by: Yr

**80. [Multi-table JOIN]** Show total revenue per customer country.

- Tables: Customers, Orders, OrderItems
- Return columns (in this order): Country, Revenue
- Sorted by: Revenue DESC

**81. [SUM]** Which 3 customers lost the most revenue to Cancelled orders? (customer name, cancelled revenue)

- Tables: Customers, Orders, OrderItems
- Return columns (in this order): CustomerName, CancelledRevenue
- Sorted by: CancelledRevenue DESC

**82. [HAVING]** For job titles held by at least 2 employees, show the average salary.

- Tables: Employees
- Return columns (in this order): JobTitle, AvgSalary

**83. [Correlated subquery]** List products priced above the average price of their own category.

- Tables: Products
- Return columns (in this order): ProductName, Category, UnitPrice

**84. [COUNT DISTINCT]** For each sales rep, how many distinct customers have they sold to?

- Tables: Orders, Employees
- Return columns (in this order): FirstName, LastName, Customers

**85. [HAVING]** Which employees have exactly 3 records in SalaryHistory?

- Tables: SalaryHistory
- Return columns (in this order): EmployeeId, Records

**86. [SUM]** Which products gave away more than 1,000 in total discounts (Quantity * UnitPrice * Discount)?

- Tables: OrderItems, Products
- Return columns (in this order): ProductName, DiscountGiven

**87. [Self join]** List employees whose manager works in a different department (employee, employee dept, manager dept).

- Tables: Employees
- Return columns (in this order): FirstName, LastName, EmpDept, MgrDept

**88. [COUNT DISTINCT]** For each customer, how many distinct products have they ever ordered?

- Tables: Customers, Orders, OrderItems
- Return columns (in this order): CustomerName, Products

**89. [STRING_AGG]** For each department, list its employees' first names as one comma-separated string sorted alphabetically.

- Tables: Departments, Employees
- Return columns (in this order): DepartmentName, Employees

**90. [Metadata]** List each table in the database with its number of columns (use INFORMATION_SCHEMA.COLUMNS).

- Return columns (in this order): TABLE_NAME, ColumnCount


## Hard

**91. [UNION]** Create a single list of names with a Type column: all employees (Type='Employee') and all customers (Type='Customer').

- Tables: Employees, Customers
- Return columns (in this order): Name, Type

**92. [Correlated subquery]** Find employees who earn more than the average salary of their own department.

- Tables: Employees
- Return columns (in this order): FirstName, LastName, DepartmentId, Salary

**93. [EXISTS]** List customers who have at least one cancelled order.

- Tables: Customers, Orders
- Return columns (in this order): CustomerId, CustomerName

**94. [CTE]** Using a CTE, compute revenue per month (exclude Cancelled orders) and list only the months whose revenue is above the average monthly revenue.

- Tables: Orders, OrderItems
- Return columns (in this order): MonthStart, Revenue
- Sorted by: MonthStart

**95. [Multiple CTEs]** For each customer show their total revenue and their share (%) of overall revenue, largest share first. Use two CTEs.

- Tables: Orders, OrderItems, Customers
- Return columns (in this order): CustomerName, Revenue, SharePct
- Sorted by: SharePct DESC

**96. [Recursive CTE]** Display the organisation hierarchy starting from the CEO (EmployeeId = 1): employee name, level (CEO = 0) and manager id.

- Tables: Employees
- Return columns (in this order): EmployeeId, Name, Level, ManagerId
- Sorted by: Level, EmployeeId

**97. [Recursive CTE]** For every employee in the CEO's hierarchy, build the reporting chain as text, e.g. 'Alice > Bob > Grace > Ivy'.

- Tables: Employees
- Return columns (in this order): EmployeeId, Path
- Sorted by: Path

**98. [ROW_NUMBER]** Find the highest paid employee in each department (ignore employees without a department). Break ties by lowest EmployeeId.

- Tables: Employees, Departments
- Return columns (in this order): DepartmentName, FirstName, LastName, Salary

**99. [RANK / DENSE_RANK]** Rank employees by salary within their department showing both RANK and DENSE_RANK (call them SalaryRank and SalaryDenseRank). Show Engineering only (DepartmentId = 2).

- Tables: Employees
- Return columns (in this order): FirstName, LastName, Salary, SalaryRank, SalaryDenseRank
- Sorted by: Salary DESC

**100. [Running total]** Show monthly revenue together with a running (cumulative) total, ordered by month. Exclude Cancelled orders.

- Tables: Orders, OrderItems
- Return columns (in this order): MonthStart, Revenue, RunningTotal
- Sorted by: MonthStart

**101. [LAG]** Using SalaryHistory, show each salary change per employee with the previous salary and the percentage increase (1 decimal). Only rows that have a previous salary, for employees 9, 10 and 11.

- Tables: SalaryHistory
- Return columns (in this order): EmployeeId, EffectiveDate, PrevSalary, Salary, PctIncrease
- Sorted by: EmployeeId, EffectiveDate

**102. [Conditional aggregation]** Find customers whose 2024 revenue is higher than their 2023 revenue. Show both amounts.

- Tables: Customers, Orders, OrderItems
- Return columns (in this order): CustomerName, Rev2023, Rev2024
- Sorted by: c.CustomerName

**103. [PIVOT]** Show revenue by product Category (rows) and by year 2023, 2024, 2025 (columns).

- Tables: OrderItems, Orders, Products
- Return columns (in this order): Category, 2023, 2024, 2025
- Sorted by: Category

**104. [NTILE]** Split employees into 4 salary quartiles (1 = highest paid). Show name, salary and quartile. Break salary ties by EmployeeId.

- Tables: Employees
- Return columns (in this order): FirstName, LastName, Salary, Quartile

**105. [LEAD]** For customer 1, list each order date and the number of days until their next order (NULL for the last).

- Tables: Orders
- Return columns (in this order): OrderId, OrderDate, DaysToNext

**106. [FIRST_VALUE]** Show every employee with the name of the highest-paid person in their department (employees with a department only).

- Tables: Employees
- Return columns (in this order): FirstName, LastName, DepartmentId, Salary, TopEarner

**107. [Running total]** For customer 5, list orders with a running count of orders so far and a running total of order value (by order date).

- Tables: Orders, OrderItems
- Return columns (in this order): OrderId, OrderDate, Total, OrderNo, RunningTotal

**108. [Window SUM]** Show each employee's salary as a percentage of their department's total salary (2 decimals). Only employees with a department.

- Tables: Employees
- Return columns (in this order): FirstName, LastName, DepartmentId, Salary, PctOfDept

**109. [PERCENT_RANK]** Show each employee's PERCENT_RANK of salary across the company (rounded to 3 decimals).

- Tables: Employees
- Return columns (in this order): FirstName, LastName, Salary, PctRank

**110. [CUME_DIST]** Show each employee's cumulative distribution of salary (rounded to 3 decimals) across the company.

- Tables: Employees
- Return columns (in this order): FirstName, LastName, Salary, CumeDist

**111. [Window AVG]** Show each employee's salary, their department average and the difference from it (employees with a department).

- Tables: Employees
- Return columns (in this order): FirstName, LastName, DepartmentId, Salary, DeptAvg, Diff

**112. [CTE]** Using a CTE, list customers whose total revenue is above the average customer revenue.

- Tables: Orders, OrderItems, Customers
- Return columns (in this order): CustomerName, Revenue

**113. [DENSE_RANK]** Return the top 5 revenue-ranked products (DENSE_RANK on total revenue, highest = 1).

- Tables: OrderItems, Products
- Return columns (in this order): ProductName, Revenue, Rnk
- Sorted by: Rnk

**114. [Recursive CTE]** Generate the numbers 1 to 10 with a recursive CTE.

- Return columns (in this order): n

**115. [Recursive CTE]** List every direct and indirect subordinate of Grace Ong (EmployeeId 7): id, name and level below Grace.

- Tables: Employees
- Return columns (in this order): EmployeeId, Name, Level

**116. [Recursive CTE]** How many people (direct and indirect) report up to Carol Wong (EmployeeId 3)?

- Tables: Employees
- Return columns (in this order): TotalReports

**117. [Recursive CTE]** Produce one row per day of January 2024 with the number of orders on that day (0 if none).

- Tables: Orders
- Return columns (in this order): OrderDay, Orders
- Sorted by: D.d

**118. [Recursive CTE]** What is the maximum depth (levels below the CEO) of the organisation hierarchy, and how many employees are at each level?

- Tables: Employees
- Return columns (in this order): Level, Employees
- Sorted by: Level

**119. [CROSS APPLY]** For each customer, show their 2 most recent orders (customer, order id, order date).

- Tables: Customers, Orders
- Return columns (in this order): CustomerName, OrderId, OrderDate

**120. [OUTER APPLY]** List all customers with the date of their most recent order (NULL if none).

- Tables: Customers, Orders
- Return columns (in this order): CustomerName, LastOrderDate

**121. [PIVOT]** Show the number of orders per year (rows) split by Status (columns Delivered, Shipped, Pending, Cancelled).

- Tables: Orders
- Return columns (in this order): Yr, Delivered, Shipped, Pending, Cancelled
- Sorted by: Yr

**122. [UNPIVOT]** Show the salary statistics (minimum, maximum, average) of Employees as three rows: Stat and Value.

- Tables: Employees
- Return columns (in this order): Stat, Value

**123. [Conditional aggregation]** For each department show the number of employees earning at least 100,000 and the number earning less.

- Tables: Departments, Employees
- Return columns (in this order): DepartmentName, HighEarners, Others

**124. [Relational division]** Which customers have bought products from every product category?

- Tables: Customers, Orders, OrderItems, Products
- Return columns (in this order): CustomerName

**125. [INTERSECT]** Which customers placed orders in both 2023 and 2025? (customer id)

- Tables: Orders
- Return columns (in this order): CustomerId

**126. [EXCEPT]** Using EXCEPT, which customers (CustomerId) have never placed an order?

- Tables: Customers, Orders
- Return columns (in this order): CustomerId

**127. [LAG]** Show monthly revenue (non-cancelled orders) with the previous month's revenue and the % change (2 decimals).

- Tables: Orders, OrderItems
- Return columns (in this order): MonthStart, Revenue, PrevRevenue, PctChange
- Sorted by: MonthStart

**128. [LAG]** Show revenue per product category per year together with the previous year's revenue for the same category.

- Tables: OrderItems, Orders, Products
- Return columns (in this order): Category, Yr, Revenue, PrevYearRevenue

**129. [Self join]** List employees who earn at least 80% of their manager's salary.

- Tables: Employees
- Return columns (in this order): FirstName, LastName, Salary, Manager, ManagerSalary

**130. [HAVING]** List departments whose average salary is higher than the company-wide average salary.

- Tables: Departments, Employees
- Return columns (in this order): DepartmentName, AvgSalary

**131. [CTE]** List orders whose total value is higher than the average order value.

- Tables: Orders, OrderItems
- Return columns (in this order): OrderId, Total

**132. [ROW_NUMBER]** Show each customer's second most recent order (customer, order id, order date).

- Tables: Orders, Customers
- Return columns (in this order): CustomerName, OrderId, OrderDate

**133. [DATEDIFF]** For each customer show the number of days between their first and last order.

- Tables: Customers, Orders
- Return columns (in this order): CustomerName, SpanDays

**134. [LAG]** For each customer, compute the average number of days between consecutive orders (1 decimal).

- Tables: Orders, Customers
- Return columns (in this order): CustomerName, AvgGapDays

**135. [Running total]** Show employees ordered by hire date (EmployeeId as tie-break) with a running headcount.

- Tables: Employees
- Return columns (in this order): FirstName, LastName, HireDate, Headcount

**136. [DENSE_RANK]** Within each customer country, show the customer(s) with the highest total revenue.

- Tables: Customers, Orders, OrderItems
- Return columns (in this order): Country, CustomerName, Revenue

**137. [Cumulative share]** List products by revenue (highest first) with each product's share of total revenue and the cumulative share (2 decimals).

- Tables: OrderItems, Products
- Return columns (in this order): ProductName, Revenue, SharePct, CumulativePct
- Sorted by: Revenue DESC

**138. [Window SUM]** For each product, show its revenue and its percentage of its own category's revenue (2 decimals).

- Tables: OrderItems, Products
- Return columns (in this order): Category, ProductName, Revenue, PctOfCategory

**139. [Subquery]** For each customer country, show total revenue and the revenue of its single biggest order.

- Tables: Orders, OrderItems, Customers
- Return columns (in this order): Country, Revenue, BiggestOrder

**140. [RANK]** Rank sales reps by total revenue of their orders (RANK, highest = 1). Ignore orders without a rep.

- Tables: Orders, OrderItems, Employees
- Return columns (in this order): FirstName, LastName, Revenue, Rnk

**141. [Conditional aggregation]** Show revenue per year (rows) with columns Q1, Q2, Q3, Q4 (non-cancelled orders).

- Tables: Orders, OrderItems
- Return columns (in this order): Yr, Q1, Q2, Q3, Q4
- Sorted by: Yr

**142. [ROW_NUMBER]** For each employee, show their first and their latest salary from SalaryHistory and the percentage growth (1 decimal).

- Tables: SalaryHistory
- Return columns (in this order): EmployeeId, FirstSalary, LatestSalary, GrowthPct

**143. [Window COUNT]** List all employees whose last name is shared with at least one other employee (show all of them).

- Tables: Employees
- Return columns (in this order): EmployeeId, FirstName, LastName

**144. [ROW_NUMBER]** Show the employees that would be removed when de-duplicating on (Salary, HireDate), keeping the lowest EmployeeId of each group.

- Tables: Employees
- Return columns (in this order): EmployeeId, FirstName, LastName

**145. [PERCENTILE_CONT]** What is the median salary of all employees?

- Tables: Employees
- Return columns (in this order): MedianSalary

**146. [PERCENTILE_CONT]** What is the median salary in each department (employees with a department)?

- Tables: Employees
- Return columns (in this order): DepartmentId, MedianSalary

**147. [LAG]** What is the longest gap in days between two consecutive orders of the same customer? Show customer name and gap for each customer's longest gap.

- Tables: Orders, Customers
- Return columns (in this order): CustomerName, LongestGap

**148. [STRING_AGG]** For each department list the distinct job titles as a comma-separated, alphabetical string.

- Tables: Departments, Employees
- Return columns (in this order): DepartmentName, Titles

**149. [Window AVG]** For each customer show their total revenue and the average revenue of customers in the same country.

- Tables: Customers, Orders, OrderItems
- Return columns (in this order): CustomerName, Country, Revenue, CountryAvg

**150. [GROUP BY]** How many orders did customers place in the same year they signed up? Show customer name and count (customers with at least one).

- Tables: Customers, Orders
- Return columns (in this order): CustomerName, Orders

**151. [ROW_NUMBER]** For every order show its most expensive line item (product name and unit price).

- Tables: OrderItems, Products
- Return columns (in this order): OrderId, ProductName, UnitPrice

**152. [HAVING]** Which customers spent more in total than 'Acme Corp'?

- Tables: Customers, Orders, OrderItems
- Return columns (in this order): CustomerName, Revenue

**153. [EXISTS]** Find customers who have both a Cancelled order and a Delivered order.

- Tables: Customers, Orders
- Return columns (in this order): CustomerName

**154. [HAVING]** Which sales reps sold to more than 5 distinct customers?

- Tables: Orders, Employees
- Return columns (in this order): FirstName, LastName, Customers

**155. [Self join]** Find pairs of products that appear together in at least 3 orders (product names, number of shared orders).

- Tables: OrderItems, Products
- Return columns (in this order): ProductA, ProductB, Together

**156. [ROW_NUMBER]** For each year, which month had the highest non-cancelled revenue? (year, month start, revenue)

- Tables: Orders, OrderItems
- Return columns (in this order): Yr, MonthStart, Revenue

**157. [PERCENTILE_CONT]** List employees who earn above the 90th percentile of salaries.

- Tables: Employees
- Return columns (in this order): FirstName, LastName, Salary

**158. [CASE]** Show for each employee whether they are a 'Manager' (has direct reports) or 'Individual Contributor', using a single query without GROUP BY.

- Tables: Employees
- Return columns (in this order): FirstName, LastName, Role

**159. [Window MAX]** For each order, show the total and the customer's largest order total for comparison, only for orders that are the customer's largest.

- Tables: Orders, OrderItems
- Return columns (in this order): OrderId, CustomerId, Total

**160. [NOT EXISTS]** Which sales reps (employees with orders) have never handled a Cancelled order?

- Tables: Employees, Orders
- Return columns (in this order): FirstName, LastName


## Expert

**161. [DENSE_RANK]** Find the employee(s) with the second-highest salary in each department (departments with fewer than two distinct salaries should not appear).

- Tables: Employees, Departments
- Return columns (in this order): DepartmentName, FirstName, LastName, Salary

**162. [Duplicates]** Find groups of employees that share the same Salary and HireDate, listing the salary, hire date and how many employees are in each such group.

- Tables: Employees
- Return columns (in this order): Salary, HireDate, Employees

**163. [Top N per group]** Find the top 2 products by revenue in each product category (category, product, revenue, rank).

- Tables: OrderItems, Products
- Return columns (in this order): Category, ProductName, Revenue, Rnk
- Sorted by: Category, rn

**164. [Gaps and islands]** For each customer, find their longest streak of consecutive calendar months in which they placed at least one order. Return the top 5 customers by streak length (customer name, streak length in months, streak start month).

- Tables: Orders, Customers
- Return columns (in this order): CustomerName, StreakLen, StreakStart
- Sorted by: b.StreakLen DESC, c.CustomerName

**165. [Moving average]** Show monthly revenue (excluding Cancelled orders) with a 3-month moving average (current month and the 2 previous months), rounded to 2 decimals.

- Tables: Orders, OrderItems
- Return columns (in this order): MonthStart, Revenue, MovingAvg3
- Sorted by: MonthStart

**166. [Calendar gaps]** List every date in Q1 2024 (1 Jan - 31 Mar) on which no order was placed.

- Tables: Orders
- Return columns (in this order): EmptyDay

**167. [Gaps and islands]** Find runs of consecutive calendar days that all have at least one order. Return start date, end date and length for runs of 2 or more days.

- Tables: Orders
- Return columns (in this order): StartDate, EndDate, Days

**168. [Window SUM]** For each customer and year, list their orders with a running total of order value that restarts every year.

- Tables: Orders, OrderItems
- Return columns (in this order): CustomerId, OrderId, OrderDate, Total, YtdTotal

**169. [Retention]** How many customers ordered in 2023 and again in 2024 (retained), and what percentage of 2023 customers is that (1 decimal)?

- Tables: Orders
- Return columns (in this order): Retained, RetentionPct

**170. [ROW_NUMBER]** For each customer show the first order they ever placed: order id, date and order total.

- Tables: Orders, OrderItems
- Return columns (in this order): CustomerId, OrderId, OrderDate, Total

**171. [Bottom N per group]** For each product category, list the 2 products with the lowest stock (category, product, stock).

- Tables: Products
- Return columns (in this order): Category, ProductName, Stock

**172. [Recursive CTE]** For every manager, compute the total salary cost of their entire team (all direct and indirect reports, excluding the manager). Show manager name and team cost.

- Tables: Employees
- Return columns (in this order): Manager, TeamCost

**173. [PERCENTILE_CONT]** What is the median order value (using order totals)?

- Tables: Orders, OrderItems
- Return columns (in this order): MedianOrder

**174. [LAG]** For each employee, find their largest single percentage raise from SalaryHistory (1 decimal).

- Tables: SalaryHistory
- Return columns (in this order): EmployeeId, BiggestRaisePct

**175. [Point in time]** What salary was each employee earning on 2024-06-30 according to SalaryHistory? (EmployeeId, Salary). Exclude employees who had no record by then.

- Tables: SalaryHistory
- Return columns (in this order): EmployeeId, Salary

**176. [Point in time]** What was the total payroll on 2024-06-30 (sum of each employee's then-current salary)?

- Tables: SalaryHistory
- Return columns (in this order): Payroll

**177. [NTILE]** Find customers in the top revenue quartile (NTILE(4) = 1). Show customer name and revenue.

- Tables: Customers, Orders, OrderItems
- Return columns (in this order): CustomerName, Revenue

**178. [New customers]** For each month, count the customers placing their first-ever order, with a running total of acquired customers.

- Tables: Orders
- Return columns (in this order): FirstMonth, NewCustomers, CumulativeCustomers

**179. [Basket analysis]** Which products are most often ordered together with 'Laptop Pro 15'? Show product and number of shared orders for products shared in at least 3 orders.

- Tables: OrderItems, Products
- Return columns (in this order): ProductName, SharedOrders

**180. [Window SUM]** Find order lines that account for more than 50% of their order's value. Show OrderId, ProductId and the share (2 decimals).

- Tables: OrderItems
- Return columns (in this order): OrderId, ProductId, SharePct

**181. [Day of week]** Which weekday generates the most revenue (non-cancelled)? Return the weekday name and revenue.

- Tables: Orders, OrderItems
- Return columns (in this order): Weekday, Revenue
- Sorted by: Revenue DESC

**182. [Year to date]** Show 2024 monthly non-cancelled revenue with a year-to-date running total.

- Tables: Orders, OrderItems
- Return columns (in this order): MonthStart, Revenue, YtdRevenue

**183. [Year-over-year]** For each month show revenue and the revenue of the same month one year earlier (NULL if none) and the difference.

- Tables: Orders, OrderItems
- Return columns (in this order): MonthStart, Revenue, PrevYearRevenue, Diff

**184. [Recursive CTE]** Show the chain of command above Jon Tan (EmployeeId 36) up to the CEO: name and level above Jon (0 = Jon).

- Tables: Employees
- Return columns (in this order): Name, Level
- Sorted by: Level

**185. [Cross tab]** Show headcount per department (rows) and salary band (columns Low < 70000, Mid 70000-119999, High >= 120000). Only employees with a department.

- Tables: Departments, Employees
- Return columns (in this order): DepartmentName, Low, Mid, High

**186. [DATEDIFF]** For every customer who has ordered, show how many days passed between signing up and their first order.

- Tables: Customers, Orders
- Return columns (in this order): CustomerName, DaysToFirstOrder

**187. [LAG]** List orders whose Status is the same as that customer's previous order's status (customer, order id, status).

- Tables: Orders
- Return columns (in this order): CustomerId, OrderId, Status

**188. [Self join]** List employees who manage at least one person who is themselves a manager (i.e. managers of managers).

- Tables: Employees
- Return columns (in this order): EmployeeId, FirstName, LastName

**189. [PIVOT]** Show a cohort matrix: rows = customer signup year, columns = order year 2023, 2024, 2025, values = number of orders.

- Tables: Customers, Orders
- Return columns (in this order): SignupYear, 2023, 2024, 2025
- Sorted by: SignupYear

**190. [Distribution]** How many customers placed 1-5 orders, 6-10 orders, and 11+ orders? (bucket, customers). Include only customers with orders.

- Tables: Orders
- Return columns (in this order): Bucket, Customers

**191. [ROW_NUMBER]** Find customers whose most recent order was Cancelled.

- Tables: Orders, Customers
- Return columns (in this order): CustomerName

**192. [FIRST_VALUE]** For each department show the highest and lowest paid employee names (one row per department, employees with a department).

- Tables: Employees, Departments
- Return columns (in this order): DepartmentName, HighestPaid, LowestPaid

**193. [Anniversary]** For each employee compute their next work anniversary date on or after 2026-01-01.

- Tables: Employees
- Return columns (in this order): EmployeeId, FirstName, LastName, HireDate, NextAnniversary

**194. [Budgeting]** Starting from the highest-paid employee (ties by EmployeeId) and going down, which employees fit within a cumulative salary budget of 1,000,000? Show name, salary and running total.

- Tables: Employees
- Return columns (in this order): FirstName, LastName, Salary, RunningTotal

**195. [Metadata]** List every table with its row count using sys.tables and sys.partitions.

- Return columns (in this order): TableName, TotalRows

**196. [Dynamic ranking]** Rank customers by revenue within each year (DENSE_RANK, highest = 1) and return the top 3 per year with year, customer, revenue and rank.

- Tables: Customers, Orders, OrderItems
- Return columns (in this order): Yr, CustomerName, Revenue, Rnk

**197. [Anti join]** Find employees who never appear as the sales rep on any order and are in the Sales department.

- Tables: Employees, Orders
- Return columns (in this order): EmployeeId, FirstName, LastName

**198. [Moving average]** Show each month's non-cancelled revenue and the average of the previous 2 months only (excluding the current month), rounded to 2 decimals.

- Tables: Orders, OrderItems
- Return columns (in this order): MonthStart, Revenue, PrevTwoAvg

**199. [Orders vs average]** List each customer's orders whose value is above that customer's own average order value (customer, order id, total, customer average).

- Tables: Orders, OrderItems
- Return columns (in this order): CustomerId, OrderId, Total, CustAvg

**200. [Pivot from CTE]** Show total revenue per product category (rows) per Status (columns Delivered, Shipped, Pending, Cancelled).

- Tables: OrderItems, Orders, Products
- Return columns (in this order): Category, Delivered, Shipped, Pending, Cancelled

