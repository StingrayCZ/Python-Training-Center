# SQL 

```sql
CREATE TABLE zeme
    (`ISO` varchar(2), `ISO3` varchar(3), `ISONumeric` int, `Country` varchar(44), `Capital` varchar(19), `Area` int, `Population` int, `Continent` varchar(2), `Domain` varchar(3), `CurrencyCode` varchar(3), `CurrencyName` varchar(16))
;
```


```sql
1) zobrazení zemí evropy a jejich hlavních měst
2) zobrazit 10 největších států podle rozlohy a seřadit je podle počtu obyvatel *
3) zobrazit všechny názvy měn
4) kolika currency name se platí (Count)
5) v jakých zemích se platí dolarem. Seradit podle populace
6) Jaká je průměrná velikost států v severní a jižní americe (continent SA, NA)
7) Kolik mají průměrný počet obyvatel státy afriky
8) zobrazte státy podle abeceby které mají pouze dvouciferný ISONumerický kod
9) zobrate státy jejichž první dvě písmena ISO3 kodu jsou stejné jako ISO kod (ten dvou písmenný))*
9 a 3/4) státy s doménou na "e"
10) zobrazte všechny řádky - měny které končí na "D" a seradte je podle velikosti země
11) Nahradte všechny jméná států evropy na `Evropska Unie`
12) vymažte všechny státy Asie a spočítejte kolik zůstalo položek *
```

```sql
-- 1) zobrazení zemí evropy a jejich hlavních měst
SELECT Country, Capital FROM zeme
where Continent IS "EU"

-- 2) zobrazit 10 největších států podle rozlohy a seřadit je podle počtu obyvatel *
SELECT * FROM
	(SELECT * FROM zeme ORDER BY Area DESC LIMIT 10)
ORDER BY Population DESC;

-- 3) zobrazit všechny názvy měn
SELECT DISTINCT CurrencyName FROM zeme;

-- 4) kolika currency name se platí (Count)
SELECT COUNT(DISTINCT CurrencyName) FROM zeme;

-- 5) v jakých zemích se platí dolarem. Seradit podle populace
SELECT Country, CurrencyName, Population  FROM zeme
WHERE CurrencyName == 'Dollar'
ORDER BY Population DESC;

-- 6) Jaká je průměrná velikost států v severní a jižní americe (continent SA, NA)
SELECT AVG(Area) FROM zeme
where continent is "NA" OR Continent is "SA"

SELECT AVG(Area) as AverageArea FROM zeme
where Continent IN ("SA", "NA")

7)
SELECT AVG(Population) as AveragePopAfrica FROM zeme
where Continent = 'AF'

8) zobrazte státy podle abeceby které mají pouze dvouciferný ISONumerický kod [chyba]
DELETE FROM zeme WHERE Continent = 'AS'
SELECT * FROM zeme
where ISONUMERIC Like "___:

9) zobrate státy jejichž první dvě písmena ISO3 kodu jsou stejné jako ISO kod (ten dvou písmenný) a 3/4) státy s doménou na "e"

9) zobrazte všechny řádky - měny které končí na "D" a seradte je podle velikosti země
SELECT * FROM zeme
WHERE Domain LIKE ".e_"

10) zobrazte všechny řádky - měny které končí na "D" a seradte je podle velikosti země
SELECT * FROM zeme
WHERE CurrencyCode Like '%D'
ORDER BY Area DESC

11) Nahradte všechny jméná států evropy na `Evropska Unie`
SELECT * FROM zeme
WHERE Continent = "EU"

12) vymažte všechny státy Asie a spočítejte kolik zůstalo položek *  [chyba]
DELETE FROM zeme WHERE Continent = 'AS'
SELECT COUNT(Area) AS CountryWithouAsia

```
