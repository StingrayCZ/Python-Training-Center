# SQL Structured Query Language

```sql
1) orderID - 10248 - SMALLINT
2) supplierName - New Orleans Cajun Delights - VARCHAR (255)
3) phone - (171)555-2222 - VARCHAR(13)
4) price - 21.35 FLOAT(2)
5) unit - 10 boxes x 20 bags - VARCHAR(2)
6) date - 1996-07-04 DATE
```

```sql
CREATE TABLE `countries` (
 `country` varchar(25) NOT NULL,
 `region` varchar(25) NOT NULL,
 `populace` int(12) DEFAULT NULL,
 `area` int(12) DEFAULT NULL,
 `literacy` float(2) DEFAULT NULL
)
```

```sql
Add 1
SELECT DISTINCT Country FROM Customers;

Add 2
SELECT * FROM Customers
WHERE Country NOT IN ('Germany', 'Mexico')

SELECT * FROM Customers
WHERE Country != 'Germany' AND Country != 'Mexico'

Add 3
SELECT CustomerID ContactName, Address FROM Customers
WHERE CustomerID >= 10 AND CustomerID <= 30

SELECT CustomerID ContactName, Address FROM Customers
WHERE CustomerID BETWEEN 10 and 30;

Add 4 ??
SELECT * FROM Customers
WHERE ContactName LIKE 'Maria%';

Add 5
SELECT * FROM Customers
WHERE City IN('Berlin', 'London', 'Paris', 'Madrid')
```
