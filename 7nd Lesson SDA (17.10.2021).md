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
