# 7nd Lesson SDA (17.10.2021)

## File Operations

```Py
import os
root_dir = 'C:\\Users\jarom\Desktop\Test'    # Nutne upravit adresu na dve lomitka
dir_list = os.listdir(root_dir)

# print(dir_list)

for fl in dir_list:
    print(os.path.join(root_dir,fl))
    print(f'(root_dir)\\{fl}')
    print(f'{fl}')
```

```Py
import os
root_dir = 'C:\\Users\jarom\Desktop\Test'     # Nutne upravit adresu na dve lomitka
dir_list = os.listdir(root_dir)               # Zobrazeni obsah adresare
# print(dir_list)

# print(dir_list)

for idx, fl in enumerate(dir_list):
    cesta = os.path.join(root_dir,fl)
    # print(cesta)                            # Zobrazeni cesty ke kazdemu soubrou
    nova_cesta = os.path.join(root_dir, fl)
    path, extension = os.path.splitext(cesta)
    filename = os.path.basename(path)
    # print(f'{os.path.basename(path)} {extension}')
    # print(f'Prejmenovani souboru: {cesta} na {nova_cesta}')

    print(f'Cesta bez pripony: {path}, pripona: {extension}, nazev souboru bez pripony: {filename}')
    nova_cesta = f'{root_dir}\\{filename}_{idx}{extension}'

    print(f'Prejmenovavam soubor: {cesta} na {nova_cesta}')

```

```Py
import os

root_dir = 'C:\\Users\jarom\Desktop\Test'  # Zadejte cestu do vaseho pracovniho adresare s testovacimi soubory napr. abc.txt, bcd.txt, cde.txt
dir_list = os.listdir(root_dir)

print(os.getcwd())
# print(dir_list)

# for idx, fl in enumerate(dir_list):
#     cesta = os.path.join(root_dir, fl)
#     path, extension = os.path.splitext(cesta)
#     filename = os.path.basename(path)
#
#     print(f'Cesta bez pripony: {path}, pripona: {extension}, nazev souboru bez pripony: {filename}')
#
#     nova_cesta = f'{root_dir}\\{filename}_{idx}{extension}'
#
#     print(f'Prejmenovavam soubor: {cesta.swapcase()} na {nova_cesta}')
#
#     # Odkomentujte az si budete jisti, ze obe cesty jsou spravne, at vam to neprepise vase soubory!
#     # os.rename(cesta, nova_cesta)

textovy_soubor = 'C:\\Users\jarom\Desktop\Test\cde_2.txt.txt'
zapis_soubor = 'C:\\Users\jarom\Desktop\Test\CDE_2.txt'
with open(textovy_soubor, 'r') as f:
    # for line in range(10):
    lines = f.readlines()

    with open(zapis_soubor, 'w') as fz:
        for line in f:
            fz.write(line.swapcase())

```
