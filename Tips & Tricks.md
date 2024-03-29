# Tips and Tricks

# Tisk na jeden řádek
```Py
cities = ["Delhi", "Mumbai", "Kolkata"]

for city in cities:
		print(city, end=", ")   # Tisk na jeden radek
		# print(city)           # Tisk pod sebe (klasicky)

```

## Mutable & Immutable objects

Mutable object (List) which contains an immutable objects (Tuples)
```Py
list1 = [(1, 2, 3), (4, 5, 6)]
print(list1)
print(hex(id(list1)))

list1[0] = (7, 8, 9)

print(list1)
print(hex(id(list1)))
```

Immutable object (Tuple) which contains mutable objects (Lists)
```Py
person = (['Ayaan', 5, 'Male'], ['Aaradhya', 8, 'Female'])

print(person)
print(hex(id(person)))   #0xa450e8

person[0][1] = 4

print(person)
print(hex(id(person)))  #0xa450e8
```

```Py

""" IMMUTABLE"""
x = 10
print(x)
print(hex(id(x))) #0x6a39f840

y = 10
print(y)
print(hex(id(y))) #0x6a39f840

""" IMMUTABLE"""
string_a = "Adam"
print(string_a)
print(hex(id(string_a))) #0x30f1280

string_b = "Adam"
print(string_b)
print(hex(id(string_b))) #0x30f1280

""" IMMUTABLE"""
tup_a = (1, 5, 6)
print(hex(id(tup_a))) #0x2fb3788
tup_b = (1, 5, 6)
print(hex(id(tup_b))) #0x2fb3788


""" MUTABLE"""
tup_a = [1, 5, 6]
print(hex(id(tup_a))) #0x2e6ef28
tup_b = [1, 5, 6]
print(hex(id(tup_b))) #0x2fb36c8

```

## \*args

```Py
"""S *arg"""
def my_sum(*integers):
    # print(hex(id(my_integers)))
    result = 0
    for x in integers:
        print(x)
    # return result

x, y, z = 5, 2, 6
print(my_sum(x , y , z))
```

```Py
"""BEZ *arg"""
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

x, y, z = 5, 2, 6
list = [x, y, z]
print(my_sum(list))
```

## \*\*Kwargs

```Py
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    # for arg in kwargs.values():   # Vypise KeyWords: RealPythonIsGreat!
    for arg in kwargs:              # Vypise Key: abcde
        print(arg)
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

```
