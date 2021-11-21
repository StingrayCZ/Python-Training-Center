# 15th Lesson SDA (21.11.2021)

• [Typing lib] https://docs.python.org/3/library/typing.html

<p float="left">
  <img src="Photos/Reseni Adela.PNG" width="900" />


```Py
from __future__ import annotations
​
import csv
import typing as t
from datetime import date, datetime, timedelta
from pprint import pprint
​
​
# XXX: Tohle nechte plavat, nekdy se k tomu treba vratime!
def yield_from_csv(csv_file: str) -> t.Iterable[dict]:
    """https://docs.python.org/3/reference/expressions.html#yield-expressions
​
    Open a `csv_file` and **yield** rows as a Python dictionary, ie. one-by-one.
    """
    with open(csv_file, newline="", encoding="utf-8") as f:
        for d in csv.DictReader(f):
            yield d
​
​
def list_from_csv(csv_file: str) -> list[dict]:
    """
    Open a `csv_file` and return a list of rows as Python dictionaries.
    """
    # Rovnou konzumujeme ten generator
    # return list(yield_from_csv(csv_file))
​
    result = []
    with open(csv_file, newline="", encoding="utf-8") as f:
        for d in csv.DictReader(f):
            result.append(d)
​
    return result
​
​
flight_records = list_from_csv("flights.csv")
​
pprint(flight_records)
​
​
CHALLENGE_1 = """
### Úkol
​
Napište funkci, která vrátí všechny unikátní dvojice letišť, mezi kterými lítají letadla.
​
```
def unique_airport_combinations(flights):
    ...
```
​
Vracet to bude množinu všech dvojic, například:
​
```
{("DPS", "HKT"), ...}
```
​
V dokumentaci si můžete přečíst něco o tom, jak se používají množiny a n-tice:
​
* https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
* https://docs.python.org/3/library/stdtypes.html#tuples
​
​
**BONUS** Modifikujte funkci tak, aby vracela nikoliv dvojice, ale řetězec tvaru `<source>-><destination>`, takže například
​
```
{"DPS->HKT", ...}
```
"""
​
​
def unique_flight_combinations_v1(flights: t.Iterable[dict]) -> set[tuple[str, str]]:
    result = []
    for flight in flights:
        result.append((flight["source"], flight["destination"]))
​
    return set(result)
​
​
def unique_flight_combinations_v2(flights: t.Iterable[dict]) -> set[tuple[str, str]]:
    result = set()
    for flight in flights:
        result.add((flight["source"], flight["destination"]))
​
    return result
​
​
def unique_flight_combinations_v3(flights: t.Iterable[dict]) -> set[tuple[str, str]]:
    # Kompaktni zapis pres set-comprehension
    # https://www.pythonforbeginners.com/basics/set-comprehension-in-python
    return {(flight["source"], flight["destination"]) for flight in flights}
​
​
# Vsechny davaji stejny vysledek
print(unique_flight_combinations_v1(flight_records))
print(unique_flight_combinations_v2(flight_records))
print(unique_flight_combinations_v3(flight_records))
​
​
def unique_flight_combinations_bonus_v1(flights: t.Iterable[dict]) -> set[str]:
    result = []
    for flight in flights:
        result.append(f"{flight['source']}->{flight['destination']}")
​
    return set(result)
​
​
def unique_flight_combinations_bonus_v2(flights: t.Iterable[dict]) -> set[str]:
    result = set()
    for flight in flights:
        result.add(f"{flight['source']}->{flight['destination']}")
​
    return result
​
​
def unique_flight_combinations_bonus_v3(flights: t.Iterable[dict]) -> set[str]:
    # Kompaktni zapis pres set-comprehension
    # https://www.pythonforbeginners.com/basics/set-comprehension-in-python
    return {f"{flight['source']}->{flight['destination']}" for flight in flights}
​
​
# Vsechny davaji stejny vysledek
print(unique_flight_combinations_bonus_v1(flight_records))
print(unique_flight_combinations_bonus_v2(flight_records))
print(unique_flight_combinations_bonus_v3(flight_records))
​
​
CHALLENGE_2 = """
### Úkol
​
Naimplementujte funkci `parse_flight_info`, která bude brát slovník, který jsme dostali z toho `csv`,
a vrátí taktéž slovník, který už ale nebude mít cenu a jiné položky jako řetězce a datum bude pěkně v `datetime` objektu.
​
tj. slovník
​
```
{'source': 'USM',
 'destination': 'HKT',
 'departure': '2017-02-11T06:25:00',
 'arrival': '2017-02-11T07:25:00',
 'flight_number': 'PV404',
 'price': '24',
 'bags_allowed': '1',
 'bag_price': '9'}
```
​
bude po transformaci vypadat následovně
​
```
{'source': 'USM',
'destination': 'HKT',
'departure': datetime.datetime(2017, 2, 11, 6, 25),
'arrival': datetime.datetime(2017, 2, 11, 7, 25),
'flight_number': 'PV404',
'price': 24,
'bags_allowed': 1,
'bag_price': 9}
```
​
Tj. 
```
def parse_flight_info(d: dict) -> dict:
    # Vase implementace zde
```
​
Možná se vám bude hodit funkce `datetime.fromisformat` - https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat
​
​
**BONUS** Vytvořte další funkce `yield_parsed_from_csv` a `list_parsed_from_csv`, které budou brát 2 parametry -
`parser` a `csv_file`.
​
- `parser` bude funkce (ano, můžeme předávat funkci jako parametr jinou funkci!)
- `csv_file` bude mít význám jako původně
​
které budou dělat to stejné, jako jejich nemodifikované předlohy `yield/list_from_csv`, jen všechny prvky už budou prohnané skrz ten `parser`
​
```
def yield_parsed_from_csv(parser, csv_file: str):
    ...
```
"""
​
​
def parse_flight_info(raw: dict) -> dict:
    return {
        "source": raw["source"],
        "destination": raw["destination"],
        "flight_number": raw["flight_number"],
        "price": int(raw["price"]),
        "bags_allowed": int(raw["bags_allowed"]),
        "bag_price": int(raw["bag_price"]),
        "departure": datetime.fromisoformat(raw["departure"]),
        "arrival": datetime.fromisoformat(raw["arrival"]),
    }
​
​
def list_parsed_from_csv(
    parser_function: t.Callable[[dict], dict],
    csv_file: str,
) -> list[dict]:
    unparsed_records = list_from_csv(csv_file)
​
    result = []
    for record in unparsed_records:
        parsed = parser_function(record)
        result.append(parsed)
​
    return result
​
​
# Od ted uz vime, ze vsechny zaznamy jsou transformovane podle nasich predstav
parsed_records = list_parsed_from_csv(parse_flight_info, csv_file="flights.csv")
​
pprint(parsed_records)
​
​
CHALLENGE_3 = """
### Úkol
​
Napište funkce, které budou jako parametr brát seznam letů a vrátí
​
- kolik stál nejdražší let
- kolik stál nejlevnější let
- jak byl dlouhý nejdelší let
- kolik bylo nejvíce povolených zavazadel
​
Například:
​
```
def longest_flight_duration(flights) -> int:
    # Vase implementace zde
```
​
PS: Nemusíte jít popořadě a zároveň se nemusíte stresovat, že nemáte všechny
"""
​
​
def most_expensive_flight_v1(flights: list[dict]) -> int:
    prices = []
​
    for flight in flights:
        prices.append(flight["price"])
​
    return max(prices)
​
​
def most_expensive_flight_v2(flights: list[dict]) -> int:
    max_price_so_far = 0
    for flight in flights:
        if flight["price"] > max_price_so_far:
            max_price_so_far = flight["price"]
        else:
            continue
​
    return max_price_so_far
​
​
def most_expensive_flight_v3(flights: list[dict]) -> int:
    flight_info_of_most_expensive = max(flights, key=lambda x: x["price"])
    return flight_info_of_most_expensive["price"]
​
​
# Vsechny davaji stejny vysledek
print("Nejdrazsi let:")
print(most_expensive_flight_v1(parsed_records))
print(most_expensive_flight_v2(parsed_records))
print(most_expensive_flight_v3(parsed_records))
​
​
def cheapest_flight_v1(flights: list[dict]) -> int:
    prices = []
​
    for flight in flights:
        prices.append(flight["price"])
​
    return min(prices)
​
​
def cheapest_flight_v2(flights: list[dict]) -> int:
    min_price_so_far = flights[0]["price"]
    for flight in flights:
        if flight["price"] < min_price_so_far:
            min_price_so_far = flight["price"]
        else:
            continue
​
    return min_price_so_far
​
​
def cheapest_flight_v3(flights: list[dict]) -> int:
    flight_info_of_most_expensive = min(flights, key=lambda x: x["price"])
    return flight_info_of_most_expensive["price"]
​
​
def cheapest_flight_v4(flights: list[dict]) -> int:
    # Nekonecno je mozna dobra vychozi hodnota - vse je mensi nez nekonecno :D
    min_price_so_far = float("+inf")
    for flight in flights:
        if flight["price"] < min_price_so_far:
            min_price_so_far = flight["price"]
        else:
            continue
​
    return int(min_price_so_far)
​
​
# Vsechny davaji stejny vysledek
print("Nejlevnejsi let:")
print(cheapest_flight_v1(parsed_records))
print(cheapest_flight_v2(parsed_records))
print(cheapest_flight_v3(parsed_records))
print(cheapest_flight_v4(parsed_records))
​
​
def longest_flight_v1(flights: list[dict]) -> timedelta:
    max_duration_so_far = timedelta(seconds=0)
    for flight in flights:
        duration = flight["arrival"] - flight["departure"]
        if duration > max_duration_so_far:
            max_duration_so_far = duration
        else:
            continue
​
    return max_duration_so_far
​
​
def longest_flight_v2(flights: list[dict]) -> timedelta:
    longest_flight = max(flights, key=lambda x: x["arrival"] - x["departure"])
    return longest_flight["arrival"] - longest_flight["departure"]
​
​
# Vsechny davaji stejny vysledek
print("Nejdelsi let:")
print(longest_flight_v1(parsed_records))
print(longest_flight_v2(parsed_records))
​
​
def max_bags_allowed_v1(flights: list[dict]) -> int:
    max_allowed_so_far = 0
    for flight in flights:
        if flight["bags_allowed"] > max_allowed_so_far:
            max_allowed_so_far = flight["bags_allowed"]
        else:
            continue
​
    return max_allowed_so_far
​
​
print(max_bags_allowed_v1(parsed_records))
​
​
# Takhle funguji typove anotace v Pythonu
def add_annotated(x: int, y: int, z: int) -> int:
    return x + y + z
​
​
# Pythonu je uplne jedno, jestli tam anotace jsou nebo ne
def add(x, y, z):
    return x + y + z
​
​
# Volani int na nejakou hodnotu
# print(int("123"))


CHALLENGE_4 = """
### Úkol


Napište funkci, která bude brát jako parametr let a číslo vyjadřující počet zavazadel a vrátí 
`True/False` podle toho, jestli je umožněno mít s sebou tolik zavazadel na daném letu.


```
def number_of_bags_allowed(flight: dict, bags: int) -> bool:
    # Vase implementace zde
```
"""


CHALLENGE_5 = """
### Úkol

Napište funkci, která bude brát jako parametr let a číslo vyjadřující počet zavazadel a vrátí 
celkovou cenu letenky.

Využijte k tomu již vytvořenou funkci `number_of_bags_allowed`. Pokud daný počet zavazadel není umožněn,
vyhoďte vyjímku `ValueError("Invalid number of bags!")`


```
def number_of_bags_allowed(flight: dict, bags: int) -> bool:
    # Vase implementace zde
```
"""
```

## Dnesni codeni

```Py
def number_of_bags_allowed_v1(flight: dict, bags: int) -> bool:
    # Implementace 1
    if bags < 0:
        return False
    if bags <= flight["bags_allowed"]:      
        return True       
    else:      
        return False      
        
      
def number_of_bags_allowed_v2(flight: dict, bags: int) -> bool:      
    if bags <= flight["bags_allowed"] and bags >= 0:      
        return True      
    else:      
        return False    
    
    
def number_of_bags_allowed_v3(flight: dict, bags: int) -> bool:    
    # Pythoni zpusob na dotaz, jestli je `x` v intervalu [a, b]    
    # if a <= x <= b:    
    #   ....    
    if 0 <= bags <= flight["bags_allowed"]:    
        return True    
    else:    
        return False    
    
                             
print(parsed_records[10])                                  
print(number_of_bags_allowed_v2(parsed_records[10], 5))
print(number_of_bags_allowed_v2(parsed_records[10], 1))
print(number_of_bags_allowed_v2(parsed_records[10], 0))
print(number_of_bags_allowed_v2(parsed_records[10], -2))


# V Pythonu jsou pole velmi flexibilni a mohou obsahovat uplne                
# cokoliv                                                               
my_list = ["abcd", 1, "efg", {"Ahoj": "cau"}, None, [1, 2, 3]]                                     
print(my_list)                                                          
print(my_list[1])  # cislo 1                                                                  
print(my_list[2][0])  # 1. pismeno retezce "efg"


# Nekde ve funkci total_flight_price bude tento radek
raise ValueError("Invalid number of bags!")


def total_flight_price_v1(flight: dict, bags: int) -> int:
    if number_of_bags_allowed_v1(flight, bags):
        # Nemusi zde byt prirazeni do promenne    
        # return flight["price"] + flight["bag_price"] * bags    
        total_price = flight["price"] + flight["bag_price"] * bags    
        return total_price    
    else:    
        raise ValueError("Invalid number of bags!")    
    
    
def total_flight_price_v2(flight: dict, bags: int) -> int:    
    if number_of_bags_allowed_v1(flight, bags):    
        # Nemusi zde byt prirazeni do promenne    
        # return flight["price"] + flight["bag_price"] * bags    
        total_price = flight["price"] + flight["bag_price"] * bags    
        return total_price    
                                                                                 
    raise ValueError("Invalid number of bags!")      
                                                                                                          
                                         
def total_flight_price_v3(flight: dict, bags: int) -> int:      
    if not number_of_bags_allowed_v1(flight, bags):             
        raise ValueError("Invalid number of bags!")          
    else:                                                
        total_price = flight["price"] + flight["bag_price"] * bags
        return total_price


print(total_flight_price_v1(parsed_records[10], 2))
print(total_flight_price_v2(parsed_records[10], 2))
print(total_flight_price_v3(parsed_records[10], 2))

try:
    print(total_flight_price_v1(parsed_records[10], -5))
except ValueError:
    print("Nesmyslny dotaz")

# Odkomentujte, pokud chcete videt vyjimku
# print(total_flight_price_v1(parsed_records[10], -5))

# Co se stane, kdyz budu chytat nespravnou vyjimku?
# Odkomentujte, pokud chcete videt vyjimky
# try:
# print(total_flight_price_v1(parsed_records[10], -5))
# except TypeError:
# print("Nesmyslny dotaz")


def total_price_v1(flights: list[dict], bags: int) -> int:      
    total_price = 0      
    for flight in flights:      
        total_price += total_flight_price_v1(flight, bags)      
    return total_price      
      
      
def total_price_v2(flights: list[dict], bags: int) -> int:      
    flight_prices = []      
    for flight in flights:      
        flight_prices.append(total_flight_price_v1(flight, bags))      
      
    return sum(flight_prices)           
                                          
                                          
first_and_fifth_flights = [parsed_records[0], parsed_records[4]]      
pprint(first_and_fifth_flights)           
                                          
print(total_price_v1(first_and_fifth_flights, 1))      
print(total_price_v2(first_and_fifth_flights, 1))      
                                          
# Pocet zavazadel musi byt povoleny pro **vsechny** lety    
# odkomentujte pro vyjimku                                                                                                                                   
# print(total_price_v2([parsed_records[0], parsed_records[1]], 2))

```
