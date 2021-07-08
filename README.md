# Python Training Center

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

## Lists

```Py

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]


print(friends[0])
```

```Py
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends[1] = "Mike"
print(friends[1])
```
