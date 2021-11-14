# 13th Lesson SDA (14.11.2021)

## JSON (Java Script Object Notation)

```Py
import random
from random import randint

# x = random.randint(1,1000)
x = randint(1, 1000)  # range
print(x)

x = random.choice(["red", "green", "blue"])
print(x)
```

## Faker

```Py
import random
import math
import csv
# import faker
from faker import Faker

fake = Faker()

def input_data_dict(x: int) -> dict:
# def input_data_dict(x):
    students = {}
    for i in range(x):
        students[i] = {}
        students[i]["id"] = random.randint(1,100)
        students[i]["name"] = fake.name()
        students[i]["email"] = fake.email()
        students[i]["country"] = fake.country()
        students[i]["True/False"] = random.choice([True, False])
    return students


print(input_data_dict(10))
```

## Zapis do JSON souboru
```Py
import random
import math
import json
import csv
# import faker
from faker import Faker

fake = Faker()

def input_data_dict(x: int) -> dict:
# def input_data_dict(x):
    students = {}
    for i in range(x):
        students[i] = {}
        students[i]["id"] = random.randint(1,100)
        students[i]["name"] = fake.name()
        students[i]["email"] = fake.email()
        students[i]["country"] = fake.country()
        students[i]["True/False"] = random.choice([True, False])
    return students


# print(input_data_dict(10))

"""
json.dumps meni format
meni dict(slovnik) na string
indent - odsazeni
"""
student_data = input_data_dict(10)
json_data = json.dumps(student_data, indent = 4)

print(json_data)
# print(type(json_data))

with open('students.json', "w") as file:
    json.dump(student_data, file)
```

## JSON file.json
```json
[
  {
    "id": 12,
    "name": "Jeremiah Mullen",
    "email": "newmanelizabeth@example.net",
    "country": "Somalia"
  },
  {
    "id": 72,
    "name": "Beth Wilson",
    "email": "sfoster@example.net",
    "country": "Germany"
  },
  {
    "id": 57,
    "name": "Brett Bernard",
    "email": "moniquepollard@example.net",
    "country": "Zimbabwe"
  },
  {
    "id": 4,
    "name": "Vanessa White",
    "email": "bishopshelia@example.net",
    "country": "Haiti"
  },
  {
    "id": 57,
    "name": "Robert Romero",
    "email": "evelyn17@example.com",
    "country": "Cambodia"
  },
  {
    "id": 62,
    "name": "Alyssa Harris",
    "email": "ellistimothy@example.com",
    "country": "Dominican Republic"
  },
  {
    "id": 47,
    "name": "Shelby White",
    "email": "krista13@example.org",
    "country": "Rwanda"
  },
  {
    "id": 32,
    "name": "Brian Vazquez",
    "email": "smithjorge@example.org",
    "country": "Kazakhstan"
  },
  {
    "id": 66,
    "name": "Mariah Carrillo",
    "email": "jessicagreen@example.net",
    "country": "Korea"
  },
  {
    "id": 90,
    "name": "Eric Brown",
    "email": "robert67@example.net",
    "country": "Martinique"
  }
]
```

## CSV (Comma Separate Values)
```Py
import csv
from pprint import pprint   #pretty print

with open("test_flights.csv", "r") as file:
    reader = csv.reader(file)
    pprint(list(reader))
    # print(reader)

    for let in reader:
        print(let)

nadpis = ["odkud","kam","cas_odletu","cas_priletu","cislo_letu","cena","kufry","cena_kurfu"]
slozeny_list = [
    ["USM","HKT","2017-02-12T12:15:00","2017-02-12T13:15:00","PV755","23","2","9"],
    ["HKT","DPS","2017-02-12T14:35:00","2017-02-12T16:30:00","PV996","23","1","15"],
    ["DPS","HKT","2017-02-13T00:00:01","2017-02-13T03:40:00","PV961","70","1","39"],
    ["HKT","USM","2017-02-13T06:10:00","2017-02-13T08:30:00","PV953","48","1","25"]
]

konec = ["odkud","kam","cas_odletu","cas_priletu","cislo_letu",str(88),"kufry","cena_kurfu"]


with open("lety", "w") as file:
    writer = csv.writer(file)
    writer.writerows(slozeny_list)

# ukol vytvorte

with open("lety_SDA.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(nadpis)
        writer.writerow(slozeny_list)
        writer.writerow(konec)
```
