# 4nd Lesson SDA (2.10.2021)

## Úkol s pizzou a průměrem

<a href="https://pythontutor.com/">Python Tutor</a>

```Py

num = (int(input("Napis cislo: \n"))
)

def PrimeTest (cislo):

    if cislo < 2:
        return False
    elif cislo < 2:
        return True
    elif cislo % 2 == 0:
        return False

    max = sqr



if PrimeTest(num) == True:
    print("Je prvocislo")

else:
    print("Neni prvocislo")
```

```Py
lst = []
lst = list(range(10))

lst = lst[0: ]
#lst.remove(0)
#lst = lst

print(lst)
```

```Py
lst = []
lst = list(range(10))

lst = lst[0: ]
#lst.remove(0)
#lst = lst

print(lst)

suma = 0

for n in lst:
    suma = suma + n

print(suma)

lst = list(range(10,20))
print(lst)

suma = 0

for i in range(len(lst)):
    suma += lst[i] #suma = suma + lst[1]

print(suma)


```

```Py



lst = []
lst = list(range(10))

lst = lst[0: ]
#lst.remove(0)
#lst = lst

print(lst)

suma = 0

for n in lst:
    suma = suma + n

print(suma)

lst = list(range(10,20))
print(lst)

suma = 0

for i in range(len(lst)):
    suma += lst[i] #suma = suma + lst[1]

print(suma)

def suma_2(lst):
    suma = 0
    for n in lst:
        suma_2 = suma + n
    return suma
print(suma_2)

```

# Trénování if, elif, else... 

```Py
def kolik_vajicek(pocet_vajicek):

    if pocet_vajicek == 1:
        return("vajicko")

    elif pocet_vajicek > 1 and pocet_vajicek < 5:
        return("vajicka")

    else:
        return ("vajicek")

num = (int(input("Napis pocet kusu: \n")))

print("Pocet " + kolik_vajicek(num) + " je " + str(num))
```

# Trénování stringů

```Py
veta = 'Kobyla ma maly bok.'
# kazdy treti znak velkym pismenem a za kazdym ctvtym vykricnik

print(len(veta))
print(veta.count(' '))
print(veta.count('m'))

idx_znak = veta.index('a')
print(f'Na indexu {idx_znak} je znak {veta[idx_znak]}')

idx_znak = 7
print(f'Na indexu {idx_znak} je znak {veta[idx_znak]}')

idx_1, idx_2 = 0, 6
print(f'Mezi indexy {idx_1} a {idx_2} je {veta[idx_1:idx_2]}')

idx_1, idx_2, step = 0, 16, 3
print(f'Mezi indexy {idx_1} a {idx_2} s krokem {step} je {veta[idx_1:idx_2:step]}')

#pozpatku
print(f'{veta[::-1]}')

print(f'{veta.upper()}')
print(f'{veta.lower()}')
print(f'{veta[4:12].upper()}')

#znak na pozici indexu velkymi pismeny
idx_upper = 10
str1 = veta[:idx_upper] + veta[idx_upper].upper() + veta[idx_upper+1:]
print(str1)
```
