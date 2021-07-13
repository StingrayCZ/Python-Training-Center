# Oblast č.2: Odkazy na objekty

```Py
x = "modrá"
y = "zelená"
z = x

print(x, y, z) # Vypíše: modrá, zelená, modrá

z = y
print(x, y, z) # Vypíše: modrá, zelená, zelená

x = z
print(x, y, z) # Vypíše: zelená, zelená, zelená
```
