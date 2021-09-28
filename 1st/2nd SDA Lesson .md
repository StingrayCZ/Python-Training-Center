## 1st Lesson SDA

• basic data structures </p> 
• bite-sized examples </> 

**Framework**
• django </p> 
• MVC
• Rest-ful APIS
• Aglue (SRCUM)
• IDE - Integrated Development Enviroment
• CodeWars

• int, float, complex, str, bool(bolean), NoneType (special), undefined
• batteriesincludes - modules (package)

• test-driven development

• python advanced contstruct
• pthon internals
• MRO, GIL
• performance testing

• SQL
• CRUD
• databases
• http basic
• internet communication protocol
• Rest-Apis

• html, css, JavaScript
• Visual Studio
• PEP8 - style guide
# hashtag


```Py
for x in range(10):
    print(x)
```

```Py
print("Ahoj", end=", ")
print("svete!")

print("Ahoj", "svete!", sep=", ")
```

## 2nd Lesson SDA (18th Sep 2021)

```Py
cislo = int("5")
print(type(cislo))

"""
Multiline comment
"""

```

### KeyWords

<p float="left">
  <img src="KeyWords.PNG" width="900" />
    
### Operators
    
<p float="left">
  <img src="Operator.PNG" width="900" />
    
### Formatting
    
```Py
# Formating
title = "General"
name = "Kenobi"
print("Hello there, {} {}".format(title, name))
print("Hello there, {} {} {}".format(title, name, name))

print(f"Hello there, {title} {name}")

print("Hello there, {name} {title}".format(name=name, title=title))
print("Hello there, {n} {m}".format(n=name, m=title))    
```    
    
```Py
print("abc" + "edf")          # spojovani stringu
print(("Hi" + " ") * 5)       # 

```
    
### Value Error
• Type
• Value
• Name
• ZeroError
• Syntax    
    
    
### Assigment operator
    
 ```Py
a = 5
a += 7
print(a)
    
```

```Py
print(False and False or True)
    
```   
    
### Separator
    
```Py
a = 123
b = "abc"
print(a, b, sep="-")    # 123-abc    
    
```

### Decimal Number
    
```Py    
n = 109.2345654324
print(f"{n: .3f}") # will display 109.234
```
   
### Percent    
```Py
percent = 0.71
print(f"{percent: .1%}")  # will display 71.0%
```

### Prime Number
    
```Py
import math

num_to_check = 30
max_div = math.floor((num_to_check) ** (1/2))
prime = num_to_check % 2 == 0 and num_to_check % 3 == 0

for i in range(2, max_div):
    if num_to_check % i == 0:
        print('Not Prime')
        exit()

print(prime)    
 ```

## 3rd Lesson SDA (19th Sep 2021)
  
### Strings  
  
```Py  
sample_string = 'Hello, World!"'
print(sample_string[::-1])
```
    
### Data Types
    
```Py
print(type("Text to print"))
print(type(-17.0))
print(type(123.4))
print(type(False))
print(type(None))
    
```    

### Collection

• List (list)
• Dictionary (dict)
• Tuple
• Set
    
### Add List
    
```Py
test_list = [1, 2, 3]
test2 = [1, 2, 6]             # Nested List
test_list.append('10')
print(test_list)              # Delka listu je 4, 3 casti + 1 blok
    
```
    
```Py
test_list = [1, 2, 3]
test2 = [1, 2, 6]                   # Nested List
# test_list.append('10')
test_list.append(test2)             # Prirazeni        
test_list.extend(["f", "d", "g"])   # Pridani
print(test_list)                    # Delka listu je 4, 3 casti + 1 blok

print(test_list[3])
print(test_list.index(2))           # index urciteho znaku
```        
    
### Sort() vs. Sorted
    
```Py
test2 = [1, 2, 6, 4, 9, 15, 78, 3]             # Nested List

test3 = sorted(test2)
test2.sort()

print(test3)
print(test2)st2)    
```    

    
 ### List Functions
    
• 
• Pop
    
```Py
    
```    
    
    
### Dictionaries

```Py
# Create an empty dictionary
phonebook = {}

# Add two items
phonebook["John"] = 111111111
phonebook["Jack"] = 222222222

print(phonebook)
print(phonebook["Jack"])

# Definition of the finished dictionary
phonebook2 = {
    "John": 111111111,
    "Jack": 222222222
}
```

    
### Input
    
```Py
# Je cislo delitelne 5?
num = int(input("Zadej cislo: "))

if (num % 5) == 0:
    print(" je delitelne")
else:
    print("Neni delitelne") 
``` 
    
```Py
# Spocitej vyskyt urciteho jmena
name = ['Aneta', 'Pavla', 'Mirek', 'Ota','Aneta', 'Pavla', 'Mirek', 'Ota','Aneta', 'Pavla',
        'Mirek', 'Mirek', 'Ota', 'Pavel']

query = input("Zadej jmeno: ")

# name.count(query))

if name.count(query) == 0:
    print("Jmeno neexistuje")

else:
    print(f"Jmeno {query} je obazeno v poli {name.count(query)} krat")    
```    

### Pokus 
```Py
import math

# numbers_list = [1, 1, 0, 5, 6, 8, 9, 156, 1515151515, 89, 62, 5, 89, 45, 3, 3]
numbers_list = [1, 1, 1, 8, 6, 6]

BlackList = []

for x in range(len(numbers_list)):

    if (numbers_list.count(numbers_list[x])) > 1:

        print(numbers_list[x])


        # numbers_list.remove(val)



    # iteraton += 1

# print(len(numbers_list))


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x) {name.count(query)} krat")
#
# if numbers_list.count(x) > 1:
#     # numbers_list.pop(num)
#
#     name = numbers_list[num]
#     print(name) 
```
### Reseni

```Py
# úkol: z listu vyhodit duplicitní čísla a následně list uspořádat  vzestupně:
numbers_list  =  [1, 1, 0, 5, 6, 8, 9, 156, 1515151515, 89, 62, 5, 89, 45, 3, 3]
numbers_list  = list(dict.fromkeys(numbers_list ))
numbers_list.sort()
print(numbers_list ) 

# Vysledek [0, 1, 3, 5, 6, 8, 9, 45, 62, 89, 156, 1515151515]
```
    
```Py
# 1st Reseni by Tatran    
numbers_list  =  [1, 1, 0, 5, 6, 8, 9, 156, 1515151515, 89, 62, 5, 89, 45, 3, 3]    
print(sorted(set(numbers_list))) 
```    
    
```Py
# 2nd Reseni by Tatran 
numbers_list  =  [1, 1, 0, 5, 6, 8, 9, 156, 1515151515, 89, 62, 5, 89, 45, 3, 3]

set = set(numbers_list)
print(set)
set2 = list(set)
print(set2)
set3_sorted = sorted(set2)
print(set3_sorted)    
```    
