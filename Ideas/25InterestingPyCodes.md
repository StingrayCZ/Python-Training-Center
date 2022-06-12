# 25InterestingPyCodes

## If trochu jinak
```Py
def TEE():
    print("YES")

def NBB():
    print("Nope")

A = 3
# print("Yep") if (A == 2)                   # spatne
# print("Yep") if (A == 2) else print("Nope")       #
TEE() if (A == 2) else NBB()     #
```

## Letter Anagram
```Py
from collections import Counter

s1 = 'below'
s2 = 'elbow'

print('anagram') if Counter(s1) == Counter(s2) else print('not an anagram')

```

## Binary to Decimal
```Py
decimal = int('FBA', 16)
print(decimal) #10
```

## Encoding
```Py
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

"""
b'My name is St\\xe5le'
b'My name is Stle'
b'My name is St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
b'My name is St?le'
b'My name is Ståle'
"""
```

## Copy File

```Py
import shutil

shutil.copyfile('source.txt', 'dest.txt')
```

## Fibonacci + Lambda + recursion

```Py 
fib = lambda x: x if x<=1 else fib(x-1) + fib(x-2)

print(fib(20))
```
```Py
def Fibb(n):
    if n<=1:
        return n
    else:
        return Fibb(n-1) + Fibb(n-2)

for _ in range(10):
    print(Fibb(_))
```

**The next examples of lambda usage...**
```Py

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


y = lambda rok, narozeni: rok - narozeni
print(y(2023, 1988))
```

