# Import Methods

## import modul.py
```Py
import math

result_fact = math.factorial(5)  # Calculates the factorial of 5
print(result_fact)

result_sqrt = math.sqrt(16)  # Calculates the square root of 16
print(result_sqrt)
```

## from modul.py import function(s)
```Py
from math import factorial, sqrt

result_fact = factorial(5)  # Calculates the factorial of 5
print(result_fact)

result_sqrt = sqrt(16)  # Calculates the square root of 16
print(result_sqrt)
```

## from modul.py import function(s) as new_name
```Py
from math import factorial as novy_nazev_A
from math import sqrt as novy_nazev_B


result_fact = novy_nazev_A(5)  # Calculates the factorial of 5
print(result_fact)

result_sqrt = round(novy_nazev_B(25))  # Calculates the square root of 16
print(result_sqrt)
```

-------------------------------------------------
Import všeho

```Py
from math import*

result_fact = factorial(5)  # Calculates the factorial of 5
print(result_fact)

result_sqrt = sqrt(16)  # Calculates the square root of 16
print(result_sqrt)
```
