# Python-Training-Center

## Variables

```Py
character_name  = "John"
character_age  = "35"


print("There once was a man named" + character_name + ", ")
print("he was " + character_age + " years old")
print("He really liked the name George,")
print("but he didn't like being 70")
```

```Py
character_name  = "John"
character_age  = 50.567754664
is_male = False

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old")

character_name = "Mike"

print("He really liked the name " + character_name + ",")
print("but he didn't like being " + character_age)

```

```Py
print("Giraffe\"Academy")
```

## Zmeření počtu prvků v řetezci
```Py
phrase = "GiraffeAcademy "
print(len(phrase))
```

## Vyprintování určitého znaku
```Py
phrase = "GiraffeAcademy "
print(phrase[0])
```

## Nalezení pořadí na základě dotazu
```Py
phrase = "Giraffe Academy "
print(phrase.index("Acad"))
```

## Záměna obsahu
```Py
phrase = "Giraffe Academy "
print(phrase.replace("Giraffe","Elephant"))
```

## Math function
```Py

cislo = 2
mocnitel = 12

print(pow(cislo,mocnitel))
print(13 % 5)
```

## Změna cisla na string (řetězec)
```Py
cislo = 88
mocnitel = 12

print(str(cislo + mocnitel) + " cislo je")
```

## Import
```Py
from math import *            # Inmport code fro specific function of math

cislo = 88
mocnitel = 12

print(str(cislo + mocnitel) + " cislo je")  # This won't run

print(floor(3.7))     # Spodni uroven
print(ceil(3.2))      # Horni uroven
print(round(sqrt(36)))

```


## Uživatelský vstup
```Py
name  = input("Enter your name: ")   # aktivace vstupu
age  = input("Enter your age ")
print("Hello " + name + "! AndČ your age is " + age)
```

## Basic calculator
```Py

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = float(num1) + float(num2)

# Input 5.3
# Input 3.3

print(round(result))

# Output 9
```
