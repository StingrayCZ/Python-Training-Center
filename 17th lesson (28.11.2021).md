# 17th lesson (28.11.2021)

## Rozcvicka

```Py
import math

def uspesni(list):
    list_100 = []

    for i in list:
        if i > 100:
            list_100.append(i)
    return list_100

def na_treti(list):
    list_pow_3 = []
    for i in list:
        list_pow_3.append(round(pow(i,3)))
    return list_pow_3

def stock_price(val_a, val_b):
    return dict(zip(val_a, val_b))

def light_cars(cars):
    res = []
    for i in cars:
        if cars[i] < 2500:
            res.append(i)
    return res


"""TEST UKOL 1"""
Test_ukol_1 = [101,85,62,400,123,60,75,81,99]
print(uspesni(Test_ukol_1))

"""TEST UKOL 2"""
Test_ukol_2 = [1,2,3,4,5,6,7,8,9]
print(na_treti(Test_ukol_2))

"""TEST UKOL 3"""
akcie = ["META", "GOOG", "AMZN", "NTFX", "AAPL"]
cena = [100, 130, 160, 299, 120]
print(stock_price(akcie,cena))

"""TEST UKOL 4"""
cars_kilos ={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Combi": 1700, "Roadster": 1110}
print(light_cars(cars_kilos))

```
## lambda - anonymn9 funkcelambda xasf

```Py
lambda x: x*2
lambda x,y: x+y

nasobeni = lambda x,y: x*y
print(nasobeni(6,10))

normalize_name = lambda x: x.upper()
print(normalize_name("Jaromir Baca"))

Note = """
UKOL 1
"""
vysledky_testu = [101,85,62,400,123,60,75,81,99]
uspesni = filter(lambda x: x>100, vysledky_testu)
print(list(uspesni))
```

```Py
zvirata =["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]
print(f"Serazeni podle abecedy: {sorted(zvirata)}")
print(f"Serazeni podle velikosti: {sorted(zvirata, key=lambda x: len(x))}")

mesta_populace =[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
# #1) seradte mesta podle abecedy
print(f"Serazeni podle abecedy:{sorted(mesta_populace, key=lambda x:x[1])}")
print(f"Serazeni podle populace:{sorted(mesta_populace, key=lambda x:x[0], reverse=True)}")
# print(f"Max:{max(mesta_populace, key=lambda x:x[1], reverse=True)}")

# #2) seradte mesta podle populace
# #3) vyberte mesto s největší a nejmenší populaci
# podle_max_populace =
# mesta_podle_abecedy =
# max_populace
# programmer = [{'Name':'Mark', 'Programming':'Python', 'Year of Experience': 3},
#                {'Name':'Nicole', 'Programming':'C', 'Year of Experience': 1},
#                {'Name':'Jason', 'Programming':'R', 'Year of Experience': 10}]
# # seradte programatory podle let zkušeností
# sorted_programmer =
#
#

```

# List Comprehension
```Py
hodnoty = [1,2,3,4,5,6,7,8,9]
na_treti = [x**3 for x in hodnoty]
print(na_treti)
sude_liche = ["sudé" if x%2 == 0 else "liché" for x in na_treti]
print(sude_liche)
```

```Py
cisla = [44,54,64,74,104]
#prictete ke kazdemu cislu 6
plus_sest = [x+6 for x in cisla]
print(plus_sest)

cars_kilos ={"Skoda": 1500, "Kodiaq": 2000, "Pickup": 2500, "Man": 16000, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
#vytvorte list se jmeny aut s váhou do 2500kg
# car_names_up_to_2500 = filter(lambda x: x < 2500, cars_kilos)
car_names_up_to_2500 = [car for car in cars_kilos if cars_kilos[car]<2500]
print(car_names_up_to_2500)


akcie = ["Face", "KOFOLA", "MONETA", "CEZ", "AAPL"]
cena = [100, 130, 160, 299, 120]

#vytvořte dict stocks s key = akcie, value = cena ...{"META":100}
akcie_cena = {akcie[i]:cena[i] for i in range(len(akcie))}
print(akcie_cena)

#stocks
akcie_cena = {stock: price for stock, price in zip(akcie, cena)}
print(akcie_cena)
print(type(akcie_cena))

cena = [100, 130, 160, 299, 300]
set_cena = set(cena)
print(set_cena)
print(type(set_cena))
```
