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
-- pridavani udaju do vice radku
INSERT INTO countries
VALUES('Francie', 'Evropa', 70000000, 16620, 90),
('Nemecko', 'Evropa', 82000000, 18470, 95)
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

```sql
SELECT * FROM Customers
WHERE Country = 'UK' OR City IN ('Nantes', 'Lille')

SELECT * FROM Customers
WHERE Country IS 'UK' OR City IS 'Nantes' OR City IS 'Lille';

SELECT * FROM Customers
WHERE (Country = 'Mexico' AND CustomerID < 21) OR CustomerID > 80

SELECT * FROM Customers
WHERE (CustomerID BETWEEN 1 AND 20 AND Country = 'Mexico') OR CustomerID > 80


SELECT * FROM Customers
ORDER BY Country, City DESC

SELECT * FROM Customers
WHERE Country IN ('France', 'Germany') AND City NOT in('Paris', 'Berlin')
ORDER BY ContactName ASC;
```

```sql
-- 1) Najděte nejlevnější položku
SELECT MIN(Price) AS "Nejmensi cena"
FROM Products;

--2) Najděte top 10 nejdražsích položek
SELECT * FROM Products
ORDER BY PRICE DESC
Limit 10;

-- 3) vypočítejte průměrnou cenu položek
SELECT AVG(Price) AS Prumerna_Cena FROM Products;

--4) kolik je položek s CategoryID 4
Select COUNT(Unit) AS PolozkyID4 FROM Products
WHERE CategoryID = 4

--5) kolik je položek s CategoryID 4
Select COUNT(DISTINC(ProductName)) AS UniquwItems FROM Products;
```
