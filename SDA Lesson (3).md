# 3rd Lesson SDA (25.9.2021)

## While loops

```Py
# Make loops as long as n is less than 5
n = 0
while True:
    # print(n)
    n += 1
    if n == 25:
        break
    if n == 5:
        break
        # continue
    print(n)
```

```Py
# Make loops as long as n is less than 5
n = 0
while n < 10:
    n += 1  # increment n with each loop loop
    if n == 8:  # if n is 4, end the loop
        break
    if n == 6:  # if n is 6, start a new iteration (preskok na dalsi smycku)
        continue
    print(n)
```

## For Loop

```Py
zvirata = ["Dog", "Cat", "Fish"]

# List all animals from the animals list
for zvire in zvirata:
    print(zvire)  # Lists one animal in turn
```

## For Loop (Range)

```Py
# Will print 0, 1, 2 in new lines
for i in range(3):
    print(i)
```

```Py
# Will print -3, -2, -1, 0 in new lines
for i in range(-3, 1):
    print(i)
```

```Py
# Will print 3, 5, 7, 9 in new lines
for number in range(3, 11, 2):
    print(number)
```

```Py
# Will print -1, -2, -3 in new lines
for number in range(-1, -4, -1):
    print(number)
```

## Enumerate

Počet indexů

```Py
fruits = ["apple", "banana", "lemon"]

for index, fruit in enumerate(fruits):
    print(f"Fruit: {fruit}, under the index: {index}.")
```

## Comprehension

```Py
# List in loop for
numbers = []
for i in range(1000):
    numbers.append(i)

print(len(numbers))  # Prints 1000

# Folded list
numbers = [i for i in range(1000)]
print(len(numbers))  # Prints 1000
```

## Task

• Řešení pomocí **for** (správně)
```Py
numbers = []
for i in range(3, 1000, 3):
    if i % 7 == 0:
        continue
    numbers.append(i)


print(len(numbers))  # Prints 1000
print(numbers)  # Prints 1000

```


• Řešení pomocí **for** (špatně)
```Py
numbers = []
for i in range(3, 1000, 3):

    numbers.append(i)

    if (i % 7 == 0) and (i % 3 == 0):
        continue

print(len(numbers))  # Prints 1000
print(numbers)  # Prints 1000
```

• Řešení pomocí **while** (správně)
```Py
numbers = []
n = 0

while n < 1001:
    n += 3
    if n % 7 == 0:
        continue
    numbers.append(n)

print(numbers)
print(len(numbers))
```
