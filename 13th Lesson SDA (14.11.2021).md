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
