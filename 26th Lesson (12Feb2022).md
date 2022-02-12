# 26th Lesson (12Feb2022)

```Py
from matplotlib import pyplot as plt  # convention to name it as "plt"
import numpy as np
import csv
import pandas as pd
from collections import Counter

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
# Median Python Developer Salaries by Age
py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

print(plt.plot(dev_x, dev_y))
# plt.show()

# Definice stylu
plt.style.use('classic')
plt.tight_layout()
plt.xkcd()  # komiks

# Pridani py devu
plt.plot(py_dev_x, py_dev_y, color="k", linestyle="--")

plt.savefig("graf_1.png")  # ulozeni do png.

plt.title("Median salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend(["Pyton", "All_devs"])
# plt.legend(["All_devs", "Pyton"])
print(plt.style.available)
plt.show()

```
