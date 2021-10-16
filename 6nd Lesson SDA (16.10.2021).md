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
