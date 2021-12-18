## In

```Py
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
  print("yes")
```

## Assert

```Py
from typing import List

def search(n: int, xs: List[int]) -> List[int]:
    if n in xs:
        return xs.index(n)

# <editor-fold defaultstate="collapsed" desc="Tests">
def test_search():
    assert search(1, [1, 2, 3]) == 0
    assert search(1, [0, 1, 2, 3]) == 1
    assert search(0, [1, 2, 3]) is None
    assert search(5, []) is None
    assert search(1, [0, 1, 0, 1]) == 1
# </editor-fold>

test_search()
```

## Break

```Py
def TEST():
    for i in range(59):
        if i >= 3:
            break
        print(f"iteraceke {i}")
    print(i)


print(TEST())  # Vysledek je 3
```

## Continue
The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.

```Py
for i in range(9):
  if i == 3:
    continue
  print(i)

# 0, 1, 2, 4, 5, 6, 7, 8   vynechana 3
```

```Py
for i in range(9):
  if i == 3 or i == 5:
    continue
  print(i)

# 0, 1, 2, 4, 6, 7, 8   vynechana 3 a 5
```
