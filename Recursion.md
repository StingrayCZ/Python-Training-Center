# Recursion

Zdroj: <a href="https://naucse.python.cz/lessons/beginners/recursion/">Rekurze</a>

```Py
def pruzkum(hloubka):
    print(f'Rozhlížím se v hloubce {hloubka} m')

    if hloubka >= 30:
        print('Už toho bylo dost!')
    else:
        print(f'Zanořuju se (z {hloubka} m)')

        pruzkum(hloubka + 10)
        
        print(f'Vynořuju se (na {hloubka} m)')

pruzkum(0)
```

<p float="left">
  <img src="Photos/Recursion.PNG" width="650" />
    

• Python si nadefinuje funkci pruzkum </p>
Zavolá funkci pruzkum s hloubkou 0: </p>
Vypíše Rozhlížím se v hloubce 0 m </p>
Zkontroluje, že 0 ≥ 30 (což neplatí) </p>
Vypíše Zanořuju se (z 0 m) </p>
Zavolá funkci pruzkum s hloubkou 10 m: </p>
Vypíše Rozhlížím se v hloubce 10 m </p>
Zkontroluje, že 10 ≥ 30 (což neplatí) </p>
Vypíše Zanořuju se (na 10 m) </p>
Zavolá funkci pruzkum s hloubkou 20 m: </p>
Zkontroluje, že 20 ≥ 30 (což neplatí) </p>
Vypíše Zanořuju se (na 20 m) </p>
Zavolá funkci pruzkum s hloubkou 30 m: </p>
Zkontroluje, že 30 ≥ 30 (což platí! konečně!) </p>
Vypíše Už toho bylo dost! a skončí </p>
Vypíše Vynořuju se (na 20 m) </p>
Vypíše Vynořuju se (na 10 m) </p>
Vypíše Vynořuju se (na 0 m) </p>

## Příklad nekonečné rekurze (až do vyčerpání paměti)

```Py
def rekurzivni_funkce():
    vysledek = ...
    rekurzivni_funkce()
    return vysledek

rekurzivni_funkce()
```
