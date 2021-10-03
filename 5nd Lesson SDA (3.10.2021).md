# 5nd Lesson SDA (3.10.2021)

```Py
# kazdy treti znak velkym pismenem a za kazdym ctvtym vykricnik
veta = 'Kobyla ma maly bok'

for i in range(10):

    if (i % 3) == 0:
        print(f'{veta.upper()} cislo je {i}')
    elif (i % 4) == 0:
        print(veta + f"!, cilo je {i}")
    else:
        print(veta + f'cislo je {i}')

```

## Diamond

```Py
number = int(input("Write a number"))

for i in range(1, number + 1):
    print(i * "*")
for i in range(number - 1, 0 , -1):
    print(i * "*")

space = number

print(space)
for i in range(0, number + 1):
    print((space - i)* " " + i * "* ")

for i in range(number -1, 0, -1):
    print((space - i) * " " + i * "* ")
```

```Py
num = int(input("zadej cislo: \n"))

for i in range(num):
    print(i * "*")

for i in range(num, 0, -1):
    print(i * "*")
```
