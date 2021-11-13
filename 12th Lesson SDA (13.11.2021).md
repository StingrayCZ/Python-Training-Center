# 12th Lesson SDA (13.11.2021)
**PYTHON - intermediate**

```Py
import random
#import string

CARDS = ["A", "K", "Q", "J", "1", "9", "8" "7", "6", "5", "4", "3", "2"]
Player_A, Player_B = 0, 0  # pocatecni body
number_of_rounds = 7       # 

List_A = random.choice(CARDS)
List_B = random.choice(CARDS)

# Test
# print(f"Vybrany znak je {List_A}, index je {CARDS.index(List_A)}")
# print(f"Vybrany znak je {List_B}, index je {CARDS.index(List_B)}")

test_a = CARDS.index(List_A)
test_b = CARDS.index(List_B)


for i in range(number_of_rounds):
    if CARDS.index(List_A) > CARDS.index(List_B):
        Player_A += 1
    else:
        Player_B += 1


# def battle(string1, string2):
#     cards = {"A":14, "K":13, "2":2}  # Dict
#     cards = ["A", "K", "Q", "J", "1", "9", "8". "7", "6", "5", "4","3", "2"]   # List
#

```
