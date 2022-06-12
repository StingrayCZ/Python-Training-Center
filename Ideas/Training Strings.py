str_test = 1,2,3,4,5

print(str_test)

print(type(str_test))
a = 0
for _ in str_test:
    a = a + _
    print(a)

print(a)


fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")