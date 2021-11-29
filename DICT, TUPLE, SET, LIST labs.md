# DICT, TUPLE, SET, LIST labs

## Split function

```Py
txt = "welcome to the jungle"
x = txt.split()
print(x)

#Result: ['welcome', 'to', 'the', 'jungle']
```

```Py
txt = "welcome to.the jungle"
x = txt.split(".")
print(x)

#Result: ['welcome to', 'the jungle']
```

```Py
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

#Result: ['hello', 'my name is Peter', 'I am 26 years old']
```

```Py
txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)

#Result: ['apple', 'banana#cherry#orange']
```

## Sorted function
```Py
a = sorted("This is a test string from Andrew".split(), key=str.lower)
print(a)
#Result: ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']

b = sorted("This is a test string from Andrew".split(), key=str.upper)
print(b)
#Result: ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
```

 ## Python ZIP
The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
 ```Py
 languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6]

result = zip(languages, versions)
print(list(result))

# Output: [('Java', 14), ('Python', 3), ('JavaScript', 6)]
```
 
```Py
 def stock_price(val_a, val_b):
    return dict(zip(val_a, val_b))


akcie = ["META", "GOOG", "AMZN", "NTFX", "AAPL"]
cena = [100, 130, 160, 299, 120]
print(stock_price(akcie,cena))
print(stock_price(cena, akcie))

"""
RESULT
{'META': 100, 'GOOG': 130, 'AMZN': 160, 'NTFX': 299, 'AAPL': 120}
{100: 'META', 130: 'GOOG', 160: 'AMZN', 299: 'NTFX', 120: 'AAPL'}
"""
```
