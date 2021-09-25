# 3rd Lesson SDA (25.9.2021)

## While loops

```Py
# Make loops as long as n is less than 5
n = 0
while True:
    # print(n)
    n += 1
    if n == 25:
        break
    if n == 5:
        break
        # continue
    print(n)
```

```Py
# Make loops as long as n is less than 5
n = 0
while n < 10:
    n += 1  # increment n with each loop loop
    if n == 8:  # if n is 4, end the loop
        break
    if n == 6:  # if n is 6, start a new iteration (preskok na dalsi smycku)
        continue
    print(n)
```

## For Loop

```Py
zvirata = ["Dog", "Cat", "Fish"]

# List all animals from the animals list
for zvire in zvirata:
    print(zvire)  # Lists one animal in turn
```

## For Loop (Range)

```Py
# Will print 0, 1, 2 in new lines
for i in range(3):
    print(i)
```

```Py
# Will print -3, -2, -1, 0 in new lines
for i in range(-3, 1):
    print(i)
```

```Py
# Will print 3, 5, 7, 9 in new lines
for number in range(3, 11, 2):
    print(number)
```

```Py
# Will print -1, -2, -3 in new lines
for number in range(-1, -4, -1):
    print(number)
```

## Enumerate

Počet indexů

```Py
fruits = ["apple", "banana", "lemon"]

for index, fruit in enumerate(fruits):
    print(f"Fruit: {fruit}, under the index: {index}.")
```

## Comprehension

```Py
# List in loop for
numbers = []
for i in range(1000):
    numbers.append(i)

print(len(numbers))  # Prints 1000

# Folded list
numbers = [i for i in range(1000)]
print(len(numbers))  # Prints 1000
```

## Task

• Řešení pomocí **for** (správně)
```Py
numbers = []
for i in range(3, 1000, 3):
    if i % 7 == 0:
        continue
    numbers.append(i)


print(len(numbers))  # Prints 1000
print(numbers)  # Prints 1000

```


• Řešení pomocí **for** (špatně)
```Py
numbers = []
for i in range(3, 1000, 3):

    numbers.append(i)

    if (i % 7 == 0) and (i % 3 == 0):
        continue

print(len(numbers))  # Prints 1000
print(numbers)  # Prints 1000
```

• Řešení pomocí **while** (správně)
```Py
numbers = []
n = 0

while n < 1001:
    n += 3
    if n % 7 == 0:
        continue
    numbers.append(n)

print(numbers)
print(len(numbers))
```

## Funkce

```Py
# Function definition of greet_by_name (name)
def greet_by_name(name):
    print(f"Hello, {name}")

# Call function greet_by_name (name) with "John" as the name argument
greet_by_name("John")
```

```Py
# funkce na testovani prvocisla
# Nefunguje zcela spravne
import math

def PrimeCheck(num):

    max_div  = math.floor((num) ** (1 / 2))
    prime = num % 2 == 0 and num % 3 == 0

    for i in range(2, max_div):
        if num % i == 0:
            print('Not Prime')
            exit()

    print("prime")


TestNumber = input("zadej cislo na test: \n")

PrimeCheck(int(TestNumber))
```

```Py
# Nefunguje zcela spravne
import math

def PrimeCheck(num):


    max_div = math.floor((num) ** (1 / 2))

    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            print("Neni prvocislo")
            # break out of loop
            break

        else:
            print("Je prvocislo")
            break

PrimeCheck(int(input("zadej cislo na test: \n")))
```

```Py
# Funguje!!! By Tatran 

import math

def prime(num):

    if num == 2:
        return True
    elif num % 2 == 0 or num <= 1:
        return False

    sqr = int(math.sqrt(num)) + 1

    for divisor in range(3, sqr, 2):
        if num % divisor == 0:
            return False
    return True

user_num = int(input("vlozit cislo: \n"))
print(prime(user_num))

```

```Py
# Funguje!!! By Katka 

import math

cislo = int(input("Zadej cele cislo:"))

def je_prvocislo(cislo):

    if cislo == 1:
        print("Cislo:", cislo, "neni prvocislo")
        
    else:
        odmocnina = int(math.sqrt(cislo))
        for i in range(2, odmocnina + 1):
            if cislo % 1 == 0:
                return False
            return  True

if je_prvocislo(cislo) == True:
    print("Cislo: ", cislo, "je prvocislo!")
else:
    print("Cislo: ", cislo, "neni prvocislo!")
```

## For Loop training

```Py
num = int(input("zadej cislo: \n"))

for i in range(num):
    print((i * " ") + (i * "*"))

for i in range(num, 0, -1):
    print((i * " ") + (i * "*"))
    
"""
 *
  **
   ***
    ****
     *****
    ****
   ***
  **
 *
"""
    
```

## HomeWork

```Py
def VenusSecret(num):
    numA = num
    numB = num

    for i in range(num):

        numA -= 1

        if i < 3:
            print(numA * " " + "*" + (2 * i) * " " + "*")
        else:
            print(numA * " " + "*" + (i - 1) * " " + "0" + i * " " + "*")

    for g in range(num):

        numB -= 1
        test = num

        if g < (test - 3):
            print(g * " " + "*" + (numB - 1) * " " + "0" + numB * " " + "*")
        else:
            print(g * " " + "*" + (2 * numB) * " " + "*")



number = input("Zadej velikost: \n")

VenusSecret(int(number))
```

```Py
zadane_cislo = int(input('Vloz cislo: \n'))
for i in range(0, zadane_cislo):
    for k in range(0, i + 1):
        print("*", end='')
    print("/r")

for i in range(zadane_cislo, 0, -1):
    for k in range(0, i - 1):
        print("*", end='')
    print("/r")
```
