def add(q):
    E = "Easy"
    q(E, "WHERE", "List all employees in the Sales department (DepartmentId = 3): first name, last name and job title.",
      ["Filter Employees by DepartmentId."],
      "SELECT FirstName, LastName, JobTitle\nFROM Employees\nWHERE DepartmentId = 3;",
      "A simple equality filter on a foreign key column.")
    q(E, "ORDER BY", "List Electronics products (name and price) from the most expensive to the cheapest.",
      ["Filter on Category, then ORDER BY UnitPrice DESC."],
      "SELECT ProductName, UnitPrice\nFROM Products\nWHERE Category = 'Electronics'\nORDER BY UnitPrice DESC;",
      "WHERE is applied before ORDER BY.")
    q(E, "WHERE", "List the customers located in Singapore.",
      ["Filter on the Country column."],
      "SELECT CustomerId, CustomerName, City\nFROM Customers\nWHERE Country = 'Singapore';",
      "String comparisons are case-insensitive under the default collation.")
    q(E, "Dates", "List employees hired on or after 1 January 2021 (name and hire date), earliest first.",
      ["Compare HireDate with a date literal.", "Use ORDER BY HireDate."],
      "SELECT FirstName, LastName, HireDate\nFROM Employees\nWHERE HireDate >= '2021-01-01'\nORDER BY HireDate;",
      "ISO date literals (yyyy-mm-dd) are language-independent for the DATE type.")
    q(E, "BETWEEN", "Find products priced between 50 and 200 (inclusive), showing name and price.",
      ["BETWEEN is inclusive on both ends."],
      "SELECT ProductName, UnitPrice\nFROM Products\nWHERE UnitPrice BETWEEN 50 AND 200;",
      "BETWEEN a AND b is equivalent to >= a AND <= b.")
    q(E, "WHERE", "List all orders that are currently Pending.",
      ["Filter Orders on Status."],
      "SELECT OrderId, CustomerId, OrderDate\nFROM Orders\nWHERE Status = 'Pending';",
      "Straightforward equality filter on a status column.")
    q(E, "String functions", "Show department names in upper case together with the length of each name.",
      ["UPPER() and LEN()."],
      "SELECT UPPER(DepartmentName) AS DeptUpper, LEN(DepartmentName) AS NameLength\nFROM Departments;",
      "LEN ignores trailing spaces; DATALENGTH counts bytes.")
    q(E, "LIKE", "Find employees whose last name ends with 'ng'.",
      ["Put the wildcard at the start of the pattern."],
      "SELECT FirstName, LastName\nFROM Employees\nWHERE LastName LIKE '%ng';",
      "A leading wildcard prevents index seeks - fine for small tables, costly on big ones.")
    q(E, "MIN", "What is the lowest product price?",
      ["Use an aggregate function."],
      "SELECT MIN(UnitPrice) AS CheapestPrice FROM Products;",
      "MIN/MAX ignore NULLs.")
    q(E, "SUM", "What is the total number of units in stock across all products?",
      ["SUM over the Stock column."],
      "SELECT SUM(Stock) AS TotalStock FROM Products;",
      "SUM returns NULL if there are no rows; wrap with COALESCE if you need 0.")
    q(E, "AVG", "What is the average unit price of products in the Accessories category?",
      ["AVG with a WHERE filter."],
      "SELECT AVG(UnitPrice) AS AvgPrice\nFROM Products\nWHERE Category = 'Accessories';",
      "WHERE filters rows before the aggregate is calculated.")
    q(E, "NOT", "List customers who are not in the USA (name and country).",
      ["Use <> or NOT IN."],
      "SELECT CustomerName, Country\nFROM Customers\nWHERE Country <> 'USA';",
      "<> and != are equivalent in T-SQL; <> is ANSI standard.")
    q(E, "TOP", "Show the 3 most recently signed-up customers (name and signup date).",
      ["TOP 3 with ORDER BY SignupDate DESC."],
      "SELECT TOP 3 CustomerName, SignupDate\nFROM Customers\nORDER BY SignupDate DESC;",
      "Dates in this table are unique enough that there is no tie at the cut-off.")
    q(E, "NULL", "List employees who have no email address recorded.",
      ["IS NULL."],
      "SELECT EmployeeId, FirstName, LastName\nFROM Employees\nWHERE Email IS NULL;",
      "NULL checks need IS NULL.")
    q(E, "DISTINCT", "How many different countries do our customers come from?",
      ["COUNT(DISTINCT column)."],
      "SELECT COUNT(DISTINCT Country) AS Countries FROM Customers;",
      "COUNT(DISTINCT x) ignores NULLs and duplicates.")
