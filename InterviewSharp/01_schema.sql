IF DB_ID('PracticeDB') IS NOT NULL
BEGIN
    ALTER DATABASE PracticeDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE PracticeDB;
END
GO
CREATE DATABASE PracticeDB;
GO
USE PracticeDB;
GO
CREATE TABLE Departments (
    DepartmentId   INT PRIMARY KEY,
    DepartmentName NVARCHAR(50) NOT NULL,
    Location       NVARCHAR(50) NULL
);
CREATE TABLE Employees (
    EmployeeId    INT PRIMARY KEY,
    FirstName     NVARCHAR(50) NOT NULL,
    LastName      NVARCHAR(50) NOT NULL,
    Email         NVARCHAR(100) NULL,
    DepartmentId  INT NULL REFERENCES Departments(DepartmentId),
    ManagerId     INT NULL REFERENCES Employees(EmployeeId),
    JobTitle      NVARCHAR(60) NOT NULL,
    HireDate      DATE NOT NULL,
    Salary        DECIMAL(10,2) NOT NULL,
    CommissionPct DECIMAL(4,2) NULL
);
CREATE TABLE SalaryHistory (
    SalaryHistoryId INT IDENTITY PRIMARY KEY,
    EmployeeId      INT NOT NULL REFERENCES Employees(EmployeeId),
    EffectiveDate   DATE NOT NULL,
    Salary          DECIMAL(10,2) NOT NULL
);
CREATE TABLE Customers (
    CustomerId   INT PRIMARY KEY,
    CustomerName NVARCHAR(80) NOT NULL,
    Email        NVARCHAR(100) NULL,
    City         NVARCHAR(50) NOT NULL,
    Country      NVARCHAR(50) NOT NULL,
    SignupDate   DATE NOT NULL
);
CREATE TABLE Products (
    ProductId   INT PRIMARY KEY,
    ProductName NVARCHAR(80) NOT NULL,
    Category    NVARCHAR(40) NOT NULL,
    UnitPrice   DECIMAL(10,2) NOT NULL,
    Stock       INT NOT NULL
);
CREATE TABLE Orders (
    OrderId    INT PRIMARY KEY,
    CustomerId INT NOT NULL REFERENCES Customers(CustomerId),
    EmployeeId INT NULL REFERENCES Employees(EmployeeId),
    OrderDate  DATE NOT NULL,
    Status     NVARCHAR(20) NOT NULL
);
CREATE TABLE OrderItems (
    OrderItemId INT PRIMARY KEY,
    OrderId     INT NOT NULL REFERENCES Orders(OrderId),
    ProductId   INT NOT NULL REFERENCES Products(ProductId),
    Quantity    INT NOT NULL,
    UnitPrice   DECIMAL(10,2) NOT NULL,
    Discount    DECIMAL(4,2) NOT NULL DEFAULT 0
);
GO
