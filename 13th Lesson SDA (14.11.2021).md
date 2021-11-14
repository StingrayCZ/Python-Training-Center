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

## Kombinator letu

```Py
import csv
from pprint import pprint  # pretty print
import datetime as dt

"""
Postup:
1) Seradit lety podle data odletu s pomoci datetime
2) let1=[] let2=[] - lety musi navazovat - letiste se musi rovnat

a) nacist data z csv filu do slozeneho listu bez nadpisu
b) jestli let 1 a 2 navazuje
c) jestli je casove rozmezi mezi lety pri 1 az 4 hodiny
d) spocitat celkovou cenu dvou letu
5) vytvorit kombinace + dat jim nejaky format (slozeny)
6) zapsat data do csv filu
"""


def start(file):
    with open(file, "r") as file:
        reader = csv.reader(file)
        flight = list(reader)
        flight.pop(0)  # odstraneni prvniho radku
    return flight


# print(start("test_flights.csv"))
flights = (start("test_flights.csv"))
for flight in flights:
    print(flight)

let1 = ['USM', 'HKT', '2017-02-12T12:15:00', '2017-02-12T13:15:00', 'PV755', '23', '2', '9']
let2 = ['DPS', 'HKT', '2017-02-13T00:00:01', '2017-02-13T03:40:00', 'PV961', '70', '1', '39']


def sort_flight(flights):
    flights.sort(key=lambda x: x[2])


def is_connecting(flight1, flight2):
    if flight1[0] == flight2[1]:
        return True
    return False


def count_flight_price(flight1, flight2):
    total_price = int(flight1[5]) + int(flight2[5])
    return total_price


def time_widow(flight1, flight2):
    td1 = dt.datetime.strptime(flight1[3], "%Y-%m-%dT%H:%M:%S")
    td2 = dt.datetime.strptime(flight2[2], "%Y-%m-%dT%H:%M:%S")
    delta = td2 - td1

    if dt.timedelta(minutes=59) < delta < dt.timedelta(hour=4, minutes=1):
        return True
    return False


def maiking_pair(flights):
    combinations = []
    for flight1 in flights:
        for flight2 in flight:
            if is_connecting(flights1, flights2) and time_widow(flight1, flight2):
                price = count_flight_price(flight1, flight2)
                new_combination = [
                    flight1[0],
                    flight1[1],
                    flights2[1],
                    flight1[2],
                    flight2[3],
                    price
                ]
                combinations.append(new_combination)
    return combinations


# TEST
print(is_connecting(let1, let2))
print(count_flight_price(let1, let2))
#
cas_letu_jedna = dt.datetime.strptime(let1[3], "%Y-%m-%dT%H:%M:%S")
cas_letu_dva = dt.datetime.strptime(let1[2], "%Y-%m-%dT%H:%M:%S")
delta = cas_letu_dva - cas_letu_jedna
print(delta)
```
