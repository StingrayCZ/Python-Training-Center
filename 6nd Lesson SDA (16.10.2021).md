# 6nd Lesson SDA (16.10.2021)

## HW
Úkol 1: Napiše program, který z telefonního čísla napsaného v kombinovaném písmenném a čáselném formátu udělá číselný formát. Vstupem budou jak čísla tak písmena, například "555ELEKTRO" a výstupem "5553535876". Korespondence čísel a písmen najdete na číselníku každého telefonu a smartphonu. Kdo by neměl, tak obrázek číselníku je v příloze. K řešení použijte slovník. Výsledek vypište jako formátovaný string do konzole.

Úkol 2: Vytvořte program, který po zadání částky v korunách na výstupu zobrazí minimální počet bankovek a mincí, kterými je možné částku reprezentovat. Například číslo 7500 - 1x 5000, 1x 2000, 1x 500. Hodnotami bankovek a mincí se můžete inspirovat u Koruny české. Výsledek vypište jako formátovaný string do konzole.

Úkol 3: Z posloupnosti hodnot [3, 5, 8, 9, 4, 21, 47, 20, 21, 7, 6, 50, 3, 4, 7, 5, 8, 13, 15, 7, 5] odstraňte všechny duplicitní hodnoty a seřaďte je od nejmenší po největší. Můžete použít sorted/sort a set. Výsledek vypište do konzole.

Úkol 4: Vytvořte program, který ze stringu, který může obsahovat libovolné znaky odstraní znaky, které nejsou písmena. Například: S654-k(o/d!!a, výstup Skoda.
Ke každému úkolu použijte alespoň jednu funkci, která bude vracet nějakou hodnotu. Tedy funkce nebude vypisovat výsledek, ale bude výsledek vracet jako proměnnou, která se následně vypíše do konzole. Všechny úkoly jsou dobrovolné.


<p float="left">
  <img src="Photos/HW 16-10-2021.png" width="500" />

## Modules

**Příklady importu**
  
```Py
import math as matika
import math as factorial, sqrt
```

```Py
# vsechny funkce v knihovne math
import math
print(dir(math))
```
  
## Objects
  
```Py
class Car:
    def __init__(self, znacka, typ):
        self.znacka = znacka
        self.typ = typ
        self.SPZ = ''

    def getZnacka(self):
        return self.znacka

    def getTyp(self):
        return self.typ

    def getSPZ(self):
        return self.SPZ

znacka, typ = 'Skoda', 'Octavia'
moje_auto = Car(znacka, typ)
print(moje_auto.getZnacka())

znacka, typ = 'VW', 'Tourage'
moje_auto2 = Car(znacka, typ)
print(moje_auto2.getZnacka())

print(f'Moje SPZ: {moje_auto2.getSPZ()}')
```

  
```Py
class Animal:
    NAME = ""  # class variable
    AGE = 0  # class variable

    def __init__(self):
        self.name = "John"  # set the default value for the name field of the Animal class object
        self.age = 2

    def print_details(self):  # method for printing the state of an object
        print(f"Name: {self.name}, age: {self.age}.")


animal = Animal()
animal.print_details()

puppy = Animal()
dog = Animal()
puppy.age = 1
puppy.name = "Rex Senior"

print(f'My dog {puppy.name}, {puppy.age} and the older {dog.name}, {dog.age}')

class Shelter:
    def __init__(self):
        zviratka= []

    # def pridejZvirato(self. zviratko):
```

## 
  
```Py
class Animal:

    def __init__(self, name='Rex', age=2):
        self.name = name
        self.age = age

dog_a = Animal()
dog_b = dog_a
# nesmysl = dog_b
nesmysl = Animal()


print(dog_a.name)
print(dog_b.name)
print(nesmysl)

nesmysl.name = 'Pongo'
print(dog_a.name)
print(dog_b.name)  
``` 
  
```Py
class Animal:

    def __init__(self, name='Rex', age=2):
        self.name = name
        self.age = age

    def initials(self):
        return  f'{self.name,}, {self.age}'

    def copy(self):
        return Animal(self.name, self.age)


dog_a = Animal()
dog_a.name = 'Arex'
dog_b = dog_a
dog_a_copy = dog_b.copy()
# nesmysl = dog_b
nesmysl = Animal()


print(dog_a)
print(dog_b)
print(dog_a_copy)
print(nesmysl)

nesmysl.name = 'Pongo'
print(dog_a.initials())
print(dog_b.name)
print(dog_a_copy.initials())
print(nesmysl.name)  
  
```  
