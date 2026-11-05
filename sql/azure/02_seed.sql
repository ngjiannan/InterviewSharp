INSERT INTO Departments VALUES
(1,'Executive','Singapore'),(2,'Engineering','Singapore'),(3,'Sales','New York'),
(4,'Marketing','London'),(5,'Human Resources','Singapore'),(6,'Finance','New York'),
(7,'Support','Manila'),(8,'Legal','London');   -- Legal has no employees

-- Hierarchy: 1 CEO -> VPs -> managers -> staff
INSERT INTO Employees (EmployeeId,FirstName,LastName,Email,DepartmentId,ManagerId,JobTitle,HireDate,Salary,CommissionPct) VALUES
(1,'Alice','Tan','alice.tan@corp.com',1,NULL,'CEO','2015-01-05',250000,NULL),
(2,'Bob','Lim','bob.lim@corp.com',2,1,'VP Engineering','2015-03-10',180000,NULL),
(3,'Carol','Wong','carol.wong@corp.com',3,1,'VP Sales','2015-06-01',175000,NULL),
(4,'David','Chen','david.chen@corp.com',4,1,'VP Marketing','2016-02-15',160000,NULL),
(5,'Eva','Ng','eva.ng@corp.com',5,1,'HR Director','2016-05-20',140000,NULL),
(6,'Frank','Lee','frank.lee@corp.com',6,1,'CFO','2015-09-01',190000,NULL),
(7,'Grace','Ong','grace.ong@corp.com',2,2,'Engineering Manager','2017-01-09',130000,NULL),
(8,'Henry','Koh','henry.koh@corp.com',2,2,'Engineering Manager','2017-04-17',128000,NULL),
(9,'Ivy','Teo','ivy.teo@corp.com',2,7,'Senior Developer','2018-02-12',110000,NULL),
(10,'Jack','Goh','jack.goh@corp.com',2,7,'Senior Developer','2018-07-23',110000,NULL),
(11,'Kate','Sim','kate.sim@corp.com',2,7,'Developer','2019-03-04',85000,NULL),
(12,'Liam','Yeo','liam.yeo@corp.com',2,8,'Developer','2019-08-19',82000,NULL),
(13,'Mia','Chua','mia.chua@corp.com',2,8,'Developer','2020-01-13',80000,NULL),
(14,'Noah','Ho','noah.ho@corp.com',2,8,'QA Engineer','2020-06-01',72000,NULL),
(15,'Olivia','Low','olivia.low@corp.com',2,7,'Junior Developer','2022-02-14',60000,NULL),
(16,'Peter','Pang','peter.pang@corp.com',3,3,'Sales Manager','2016-08-08',120000,0.05),
(17,'Quinn','Lau','quinn.lau@corp.com',3,16,'Sales Rep','2018-05-14',70000,0.10),
(18,'Rachel','Foo','rachel.foo@corp.com',3,16,'Sales Rep','2018-11-05',72000,0.10),
(19,'Sam','Tay','sam.tay@corp.com',3,16,'Sales Rep','2019-09-09',68000,0.08),
(20,'Tina','Yap','tina.yap@corp.com',3,16,'Sales Rep','2021-03-22',65000,0.08),
(21,'Uma','Ang','uma.ang@corp.com',3,16,'Sales Rep','2022-10-03',62000,0.05),
(22,'Victor','Seah','victor.seah@corp.com',4,4,'Marketing Manager','2017-10-30',105000,NULL),
(23,'Wendy','Ler','wendy.ler@corp.com',4,22,'Marketing Specialist','2019-04-15',68000,NULL),
(24,'Xavier','Poh','xavier.poh@corp.com',4,22,'Content Writer','2020-09-14',58000,NULL),
(25,'Yvonne','Khoo','yvonne.khoo@corp.com',5,5,'HR Specialist','2018-12-03',65000,NULL),
(26,'Zack','Ling','zack.ling@corp.com',5,5,'Recruiter','2021-05-17',60000,NULL),
(27,'Amy','Soh','amy.soh@corp.com',6,6,'Accountant','2017-07-24',78000,NULL),
(28,'Ben','Tang','ben.tang@corp.com',6,6,'Financial Analyst','2019-11-11',82000,NULL),
(29,'Cindy','Wee','cindy.wee@corp.com',6,27,'Accounts Clerk','2021-08-30',50000,NULL),
(30,'Dan','Quek','dan.quek@corp.com',7,3,'Support Manager','2018-03-19',90000,NULL),
(31,'Ella','Chong','ella.chong@corp.com',7,30,'Support Agent','2020-02-10',48000,NULL),
(32,'Finn','Neo','finn.neo@corp.com',7,30,'Support Agent','2020-10-12',48000,NULL),
(33,'Gina','Lai','gina.lai@corp.com',7,30,'Support Agent','2021-06-07',46000,NULL),
(34,'Hugo','Mak','hugo.mak@corp.com',7,30,'Support Agent','2023-01-16',45000,NULL),
(35,'Iris','Tham','iris.tham@corp.com',NULL,NULL,'Consultant','2023-05-01',95000,NULL),  -- no dept, no manager
(36,'Jon','Tan','jon.tan@corp.com',3,16,'Sales Rep','2023-07-10',60000,0.05),
(37,'Kim','Lim',NULL,2,7,'Developer','2023-09-18',78000,NULL),                         -- NULL email
(38,'Leo','Wong','leo.wong@corp.com',2,8,'Developer','2019-03-04',85000,NULL),          -- same salary & date as Kate
(39,'Mary','Ong','mary.ong@corp.com',4,22,'Marketing Specialist','2021-01-11',68000,NULL),
(40,'Nick','Teo','nick.teo@corp.com',6,27,'Accountant','2022-06-06',76000,NULL);

-- Salary history: each employee hired at (Salary*0.85), raise after ~1y and ~3y (deterministic)
INSERT INTO SalaryHistory (EmployeeId,EffectiveDate,Salary)
SELECT EmployeeId, HireDate, CAST(Salary*0.85 AS DECIMAL(10,2)) FROM Employees;
INSERT INTO SalaryHistory (EmployeeId,EffectiveDate,Salary)
SELECT EmployeeId, DATEADD(YEAR,1,HireDate), CAST(Salary*0.92 AS DECIMAL(10,2)) FROM Employees WHERE HireDate < '2024-01-01';
INSERT INTO SalaryHistory (EmployeeId,EffectiveDate,Salary)
SELECT EmployeeId, DATEADD(YEAR,3,HireDate), Salary FROM Employees WHERE DATEADD(YEAR,3,HireDate) < '2026-01-01';

INSERT INTO Customers VALUES
(1,'Acme Corp','contact@acme.com','New York','USA','2020-01-15'),
(2,'Globex','info@globex.com','London','UK','2020-02-20'),
(3,'Initech','hello@initech.com','Austin','USA','2020-04-11'),
(4,'Umbrella Ltd','sales@umbrella.com','Manchester','UK','2020-06-30'),
(5,'Hooli','biz@hooli.com','San Francisco','USA','2020-09-05'),
(6,'Stark Industries','pepper@stark.com','New York','USA','2021-01-22'),
(7,'Wayne Enterprises','bruce@wayne.com','Gotham','USA','2021-03-14'),
(8,'Wonka Foods','willy@wonka.com','Berlin','Germany','2021-05-09'),
(9,'Tyrell Corp','info@tyrell.com','Munich','Germany','2021-07-18'),
(10,'Cyberdyne','sales@cyberdyne.com','Tokyo','Japan','2021-10-01'),
(11,'Soylent Co','contact@soylent.com','Osaka','Japan','2022-01-12'),
(12,'Vandelay Imports','art@vandelay.com','Singapore','Singapore','2022-03-03'),
(13,'Pied Piper','richard@piedpiper.com','Palo Alto','USA','2022-05-25'),
(14,'Dunder Mifflin','michael@dm.com','Scranton','USA','2022-08-16'),
(15,'Oscorp','norman@oscorp.com','New York','USA','2022-11-02'),
(16,'Gringotts','goblin@gringotts.com','London','UK','2023-01-08'),
(17,'Massive Dynamic','info@massive.com','Boston','USA','2023-03-21'),
(18,'Aperture Science','cave@aperture.com','Seattle','USA','2023-06-15'),
(19,'Black Mesa','gordon@blackmesa.com','Albuquerque','USA','2023-09-09'),
(20,'Prestige Worldwide','dale@prestige.com','Singapore','Singapore','2024-01-20'),
(21,'Sterling Cooper','don@sterling.com','New York','USA','2024-03-05'),
(22,'Bluth Company','george@bluth.com','Newport','USA','2024-05-30'),
(23,'Los Pollos','gus@pollos.com','Albuquerque','USA','2024-08-12'),
(24,'Duff Brewing',NULL,'Springfield','USA','2024-10-27'),
(25,'Nakatomi Trading','takagi@nakatomi.com','Tokyo','Japan','2025-02-14'),
(26,'Never Ordered Ltd','none@never.com','Paris','France','2025-03-01'),   -- no orders
(27,'Ghost Customer','ghost@ghost.com','Lyon','France','2025-04-01');       -- no orders

INSERT INTO Products VALUES
(1,'Laptop Pro 15','Electronics',1500.00,40),(2,'Laptop Air 13','Electronics',1100.00,55),
(3,'Wireless Mouse','Accessories',25.00,300),(4,'Mechanical Keyboard','Accessories',90.00,150),
(5,'USB-C Hub','Accessories',45.00,200),(6,'27in Monitor','Electronics',320.00,80),
(7,'Webcam HD','Electronics',70.00,120),(8,'Noise-Cancelling Headset','Electronics',180.00,90),
(9,'Office Chair','Furniture',250.00,35),(10,'Standing Desk','Furniture',480.00,20),
(11,'Desk Lamp','Furniture',35.00,150),(12,'Notebook (5-pack)','Stationery',12.00,500),
(13,'Gel Pens (12)','Stationery',8.00,600),(14,'Whiteboard','Stationery',60.00,45),
(15,'External SSD 1TB','Electronics',110.00,100),(16,'Smartphone X','Electronics',900.00,70),
(17,'Tablet Mini','Electronics',450.00,60),(18,'Printer Laser','Electronics',210.00,25),
(19,'Backpack','Accessories',55.00,130),(20,'Cable Organizer','Accessories',10.00,400),
(21,'Discontinued Fax','Electronics',150.00,0),   -- never ordered
(22,'Mystery Gadget','Electronics',99.00,10);    -- never ordered

-- Deterministic order generation (no RANDOM): 300 orders over 2023-2025
;WITH N AS (SELECT TOP (300) ROW_NUMBER() OVER (ORDER BY (SELECT 1)) AS n FROM sys.all_objects a CROSS JOIN sys.all_objects b)
INSERT INTO Orders (OrderId,CustomerId,EmployeeId,OrderDate,Status)
SELECT n,
       ((n*7) % 25) + 1,                                                   -- customers 1..25 only
       CASE WHEN n % 17 = 0 THEN NULL ELSE 16 + ((n*3) % 6) END,           -- sales team 16..21, some NULL
       DATEADD(DAY, (n*11) % 1000, '2023-01-01'),
       CASE n % 10 WHEN 0 THEN 'Cancelled' WHEN 1 THEN 'Pending' WHEN 2 THEN 'Shipped' ELSE 'Delivered' END
FROM N;

;WITH N AS (SELECT TOP (900) ROW_NUMBER() OVER (ORDER BY (SELECT 1)) AS n FROM sys.all_objects a CROSS JOIN sys.all_objects b)
INSERT INTO OrderItems (OrderItemId,OrderId,ProductId,Quantity,UnitPrice,Discount)
SELECT n, ((n-1)/3)+1, p.ProductId, ((n*5)%9)+1, p.UnitPrice,
       CASE n % 6 WHEN 0 THEN 0.10 WHEN 3 THEN 0.05 ELSE 0 END
FROM N
JOIN Products p ON p.ProductId = ((n*13) % 20) + 1;   -- products 1..20 only
GO
