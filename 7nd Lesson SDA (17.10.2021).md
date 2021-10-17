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
