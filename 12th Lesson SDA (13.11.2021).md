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

```Py
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '1', 'J', 'Q', 'K', 'A'] #nulu v 10 musim posleze nahradit mezerou, protoze porovnani ve stringu jde znak od znaku
#string1 = str(input("Vloz 7 karetnich hodnot 1-10, J,Q,K nebo A: "))
#string2 = str(input("Vloz 7 karetnich hodnot 1-10, J,Q,K nebo A: "))
def battle(string1, string2):
    stav1 = 0
    stav2 = 0
    hrac1 = string1.replace("0","")
    hrac2 = string2.replace("0","")
    for kolo in range(len(hrac1)):
        if CARDS.index(hrac1[kolo]) == CARDS.index(hrac2[kolo]):
            continue
        elif CARDS.index(hrac1[kolo]) < CARDS.index(hrac2[kolo]):
            stav2 += 1
        else:
            stav1 += 1
    return f"Hrac 1 vyhral {stav1} her, Hrac 2 vyhral {stav2} her"
print(battle("JJ109810", "222KKK"))
print(battle("AKAKQ10", "AAAAAA"))
print(battle("876543", "1010101022"))
```
