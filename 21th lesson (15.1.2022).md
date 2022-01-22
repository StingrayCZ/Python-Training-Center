# 21st lesson (15.1.2022)

```Py
# import this

import re

#scraping bike name from html (wiht spaces, new lines, labels ) - "New"  'Neuron 7 WMN         New'"""
scraped_name = """New  Neuron 7 WMN      \n   New"""

def _normalize_name(raw_name):
    _name = re.sub("New", "", raw_name)
    formatted_name = _name.lstrip().rstrip().replace("\n", "")

    return formatted_name

print(_normalize_name(scraped_name))
```

## Sazka
Vytvorte script, ktery bude replikovat plny tiket nahodneho tahu pro hry - sportka a euromiliony od Sazky. Kazda z funkci/method bude vracet plny tiket nahodnych cisel.

plny tiket Sportky - 10 rad 6 cisel od 1 do 49 # 1, 3, 7, 10, 45, 49
plny tiket euromiliony - 6 rad 5 cisel od 1 do 50 a 2 cisla od 1 do 10 # (3, 19, 23, 45, 50)(3,7) 

```Py
# generator cisel.randit(1, 49)
# stringy aby se daly appendovat
# nested list [[], [], [],...] || [(),(),()]
# pouzivat loop // vnoreny loop
# pouzit extend (""pridani prvku) // append (==pridat jeden prvek)
# funkce random sample

- na co si davat pozor:
    - cisla v tahu byla serazena podle velikosti
    - pozor na opakovani cisel (--> set)

# STRUKTURA
- sla by udelat funkce, ktera bere vstup

- OOP
Class Sazka()
    
    def na cokoliv
        pass
    
    def sportka
        pass
    
    def euromiliony
        pass
        
```
    
