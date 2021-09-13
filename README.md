# Python Training Center

## SDA Links

<a href="https://pythonremotecz5.zone.sdacademy.pro/schedule/"> 
Time Schedule</a>

## Variables

```Py
character_name  = "John"
character_age  = "35"     # string


print("There once was a man named" + character_name + ", ")
print("he was " + character_age + " years old")
print("He really liked the name George,")
print("but he didn't like being 70")
```

```Py
character_name  = "John"        # string
character_age  = 50.567754664   # number
is_male = False                 # boolean

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old")

character_name = "Mike"

print("He really liked the name " + character_name + ",")
print("but he didn't like being " + character_age)

```

## Práce s řetězci
```Py
print("Giraffe\"Academy")  # vyprintovani znaku
print("Giraffe\nAcademy")  # zalomeni radku
```

## Boolean - ověření, zda jsou znaky (třeba) velké

```Py
phrase = "Giraffe Academy "

print(phrase.islower())  # vysledek je False

```

```Py
phrase = "Giraffe Academy "

print(phrase.upper())            # všechna písmena velká

print(phrase.upper().isupper())  # kombinace zvetseni vsech pismen na velka, potom Boolean

print(phrase.capitalize())       # porvní písmeno v řetězci je velké
```

## Zmeření počtu prvků v řetezci
```Py
phrase = "GiraffeAcademy "
print(len(phrase))              # vysledek je 15, počítá i mezery
```

## Vyprintování určitého znaku
```Py
phrase = "GiraffeAcademy "
print(phrase[0])               # vysledek je G    
```

```Py
phrase = "GiraffeAcademy "
print(phrase[0], phrase[2])     # vysledek je G a r   
```

## Nalezení pořadí na základě dotazu
```Py
phrase = "Giraffe Academy "
print(phrase.index("Acad"))
```
```Py
# Pozor na velikost pismen
phrase = "Giraffe academy "
print(phrase.index("ac"))
```

## Záměna obsahu
```Py
phrase = "Giraffe Academy "
print(phrase.replace("Giraffe","Elephant"))
```

```Py
phrase = "Giraffe Academy "
print(phrase.replace("Gi","Elephant"))

# Vysledek je Elephantraffe Academy 
```

## Math functions
```Py
# Priklad zapisu cisel, neni potreba %d jako v C :-)

print(-2.4545)
print(3 * 4 + 5)
```

```Py
cislo = 2
mocnitel = 12

print(13 % 5)                   # Modulo, vysledek je 3
```

```Py
my_num = -35.33467284

print(round(abs(my_num)))   # výsledek je 35

# round = zaokrouhlit
# abs - absolutni cislo, tj. kladne
```

```Py
# srovnani
print(max(634, 342))
print(min(634, 342))
```

```Py
from math import *     # knihovna?

print(floor(3.5))  # zarovna na 3
print(ceil(3.5))   # zarovna na 4
```

```Py
from math import *

print(pow(5, 3))   # Mocnina, print(pow(cislo,mocnitel)), výsledek je 125.0

print(round(pow(5,3)))   # Výsledek je 125 
```

```Py
from math import *

print(round(sqrt(36)))   # Druha odmocnina, vysledek 6
```


## Změna cisla na string (řetězec)
```Py
# Je nutné cislo pred vyprintovanim prevest na string, pokud je ve vyprintovani i text

my_num = 35

print("My number is " + str(my_num))
```

```Py
# Pokud je ve vyprintovani jen samotne cislo, prevod na string neni potreba
my_num = 35

print(my_num)
```

```Py
cislo = 88
mocnitel = 12

print(str(cislo + mocnitel) + " cislo je")   # Výsledek je: 100 cislo je
```

```Py
from math import *

cislo = 2
mocnitel = 5

c = round(pow(cislo, mocnitel))

print(c)   # Výsledek je: 32
```

## Import
```Py
from math import *            # Import code from specific function of math

cislo = 88
mocnitel = 12

print(str(cislo + mocnitel) + " cislo je")  

print(floor(3.7))     # Spodni uroven
print(ceil(3.2))      # Horni uroven
print(round(sqrt(36)))

```

## Uživatelský vstup
```Py
name  = input("Enter your name: ")   # aktivace vstupu
age  = input("Enter your age ")
print("Hello " + name + "! And your age is " + age)
```

## Basic calculator
```Py
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = float(num1) + float(num2)    

# Input 5
# Input 8.3

print(result
#print(round(result))

# Output 9
```

```Py
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = num1 + num2      # chybny zapis, pokud je soucet 5 + 8.3, vysledek je chybnych 58.3, protože se jedná o součet řetězců

# Input 5
# Input 8.3

print(result)
```

## Mad Libs Game

```Py
color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity: ")


print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
```
## Přístup k prvkům (v řetězcích)

```py
# Zápis v Idle (Python shell)
"těžké časy"   # Výstup: č
"žirafa"       # Výstup: ž

# Zápis v PyCharm
print("Těžké časy"[6])   # Výstup: č
print("žirafa"[0])       # Výstup: ž
```

## Lists (seznam)
N-tice (tuple) jsou neměnitelné, takže je po vytvoření již nelze změnit. Seznamy(list) jsou měnitelné, takže lze 
snadno vkládat a odebírat prvky, kdykoli chceme.

```Py
# Příklad co všechno se dá uložit do listu
friends = ["Kevin", 2,False]
```


```Py
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends[0])  # Vypíše nultou pozici
```

```Py
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends[1] = "Mike"  # Karen se mění na Mike
print(friends[1])  
```

```Py
print(friends[1:])   # Vyprintuje pozici 1 a následující
print(friends[-1])   # Vyprintuje poslední pozici
print(friends[1:3])  # Vypíše vše od pozice 1 až po pozici 3, tedy "Karen", "Jim"
```

## List Functions

```Py
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)   # Spojení dvou listů
print(friends)

# Výsledek: ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby', 4, 8, 15, 16, 23, 42]
```

```Py
friends.append("Creed")     # Přidání dalšího str na poslední místo listu
friends.pop()               # Vyřadí poslední pozici v listu
print(friends.count("Jim")  # Spočítá kolikrát se v listu objeví tento výáraz
friends.sort()              # Seřazení vzestupně
friends.reverse()           # Otočení pořadí
friends2 = friends.copy()   # Zkopírování obsahu do jiného listu
```


```Py
friends.insert(1, "Creed") # Vnoření dalšío jmína na pozici 1 a posunutí zbytku za něj
# Výsledek: ['Kevin', 'Creed', 'Karen', 'Jim', 'Oscar', 'Toby']
```

```Py
friends.remove("Jim") # Smazání určité pozice dle jména
```

```Py
friends.clear() # Smazání všeho. Výsledek: []
```

```Py
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends.index('Mike'))  # Vyprintování pozice. V případě že tu jméno není, je hlášena chyba
```


## Tuple (n-tice)

Neměnitelné

```Py
(1,)    # jednoprvková n-tice
"one,"
()      # prazdna n-tice
```

```Py
coordinates = (4, 5)
coordinates = [4, 5]
coordinates = [(4, 5), (6, 7), (80, 34)]
print(coordinates)
print(coordinates[1])
```

```Py
coordinates[0] = 10   # Nelze provést
```
## Function (definition)

```Py
def say_hi():
    print("Hello User")

say_hi()
```

```Py
# Pouze řetězce
def say_hi(name, age):
    print("Hello" + name + ", you are " + age)

say_hi("Mike", "35")
say_hi("Steve", "70")
```
```Py
# Řetězce a čísla
def say_hi(name, age):
    print("Hello" + name + ", you are " + (str)ge)

say_hi("Mike", 35)
say_hi("Steve", 70)
```

## Return Statement

```Py
# Chybný zápis, vrací None
def cube(num):
    num*num*num

print(cube(3))
```

```Py
def cube(num):
    return num*num*num    # Návrat hodnoty

print(cube(3))
```
```Py
def cube(num):
    return num*num*num
    print("cod")        # nevrátí

result = cube(4)

print(result)
```

## If Statements

```Py
is_male = True # Boolean variable

if is_male:
    print("You are male")

else:
    print("You are not a male")
```

```Py
is_male = False # Boolean variable
is_tall = False

if is_male or is_tall:
#if is_male or is_tall:
    print("You are male")
    
elif is_male and not is_tall

else:
    print("You are not a male")
```

```Py
is_male = False # Boolean variable
is_tall = False

if is_male and is_tall:
    print("You are male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but are tall")
else:
    print("You are neither man nor tall or both")
```

## If Statements & Comparisons

```Py
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(160, 40, 50))
```

## Build a better calculator

```Py
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invali operator")
```

## Dictionaries

```Py

```

