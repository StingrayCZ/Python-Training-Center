# Nested list

<p float="left">
  <img src="/Photos/img.png" width="200" />

```Py
L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']

print(L[2])
# Prints ['cc', 'dd', ['eee', 'fff']]

print(L[2][2])
# Prints ['eee', 'fff']

print(L[2][2][0])
# Prints eee
```

## Add Items to a Nested list

**append - pridani hodnoty nakonec** 

To add new values to the end of the nested list, use append() method.
```Py
L = ['a', ['bb', 'cc'], 'd']
L[1].append('xx')
print(L)

# Prints ['a', ['bb', 'cc', 'xx'], 'd']
```

**Insert - pridani hodnoty na spefickou pozici**

When you want to insert an item at a specific position in a nested list, use insert() method.
```Py
L = ['a', ['bb', 'cc'], 'd']
L[1].insert(0,'xx')
print(L)

# Prints ['a', ['xx', 'bb', 'cc'], 'd']
```

**Extended - vlozeni listu**

You can merge one list into another by using extend() method.
```Py
L = ['a', ['bb', 'cc'], 'd']
L[1].extend([1,2,3])
print(L)
# Prints ['a', ['bb', 'cc', 1, 2, 3], 'd
```