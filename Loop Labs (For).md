## Loop Labs (For)

```Py

g = [2, 5, 12, 8, 6]

for i in range[0:-2]:
    print(f"{i}"+ f"{g}")
    
```

```Py
odds = [1,3,5,7,9]
evens = [2,4,6,8,10]
fevens = [2,4,6,8,10]
for oddnum, evennum, bb in zip(odds,evens, fevens):
    print(oddnum + evennum + bb)
    # print(evennum)

```

In Python, common examples of iterables are:

Lists </p>
Strings </p>
Dictionaries </p>
Tuples </p>
Sets </p>


```Py
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for number in row:
        print(number)

# 1
# 2
# 3
# 4...
```

## The List Comprehension (for loop)

```Py
numbers = [4, -2, 7, -4, 19]
new_nums = []
for num in numbers:
    if num > 0:
        new_nums.append(num)
# [4, 7, 19]
```

```Py
numbers = [4, -2, 7, -4, 19]
new_nums = [num for num in numbers if num > 0]
print(new_nums)

# [4, 7, 19]
```

```Py
numbers = [1, 2, 3]
[print(number) for number in numbers]
```

## The Dict Comprehension (for loop)
