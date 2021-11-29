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
