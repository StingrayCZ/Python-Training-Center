## Oblast č.2: Odkazy na objekty

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

```Py
# zobrazení typu proměnné
route = 866
print(type(route))

route = "Sever"
print(type(route))
```

## Datové typy pro kolekce - Tuple, List
N-tice jsou neměnitelné, takže je po vytvoření již nelze změnit. Seznamy jsou měnitelné, takže lze 
snadno vkládat a odebírat prvky, kdykoli chceme.
