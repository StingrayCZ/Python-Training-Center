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
