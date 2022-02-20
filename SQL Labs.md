# SQL Labs

SQL - structured Query Language

```SQL
INT               -- Whole Numbers
DECIMAL(10,4)      -- Decimal Numbers (Exact Value)
VARCHAR(100)        -- String of text of lenght 1
BLOB              -- Binary Large Object, Store large data
DATE              -- YYYY-MM-DD
TIMESTAMP         -- YYYY-MM-DD HH:MM:SS
```


## MySQL Password
PythonSDA#22
Windows Service Name: MySQL80


```sql
CREATE TABLE student (
    student_id INT PRIMARY KEY,   -- definice sloupce + dat. typu
    name VARCHAR(20),             -- 20 pozic
    major VARCHAR(20)
);

```
## Creating a table

```sql
CREATE TABLE student (
    student_id INT,   -- definice sloupce + dat. typu
    name VARCHAR(20),             -- 20 pozic
    major VARCHAR(20),
    PRIMARY KEY(student_id)
);

DESCRIBE student;

DROP TABLE student;


ALTER TABLE student ADD gpa DECIMAL(3, 1);
-- pridani dalsiho sloupce
-- ADD add extra table onto the table

ALTER TABLE student DROP COLUMN gpa;  -- deleting specific column

```
