# 17th lesson (28.11.2021)

```Py
import math

def uspesni(list):
    list_100 = []

    for i in list:
        if i > 100:
            list_100.append(i)
    return list_100

def na_treti(list):
    list_pow_3 = []
    for i in list:
        list_pow_3.append(round(pow(i,3)))
    return list_pow_3

def stock_price(val_a, val_b):
    return dict(zip(val_a, val_b))

def light_cars(cars):
    res = []
    for i in cars:
        if cars[i] < 2500:
            res.append(i)
    return res


"""TEST UKOL 1"""
Test_ukol_1 = [101,85,62,400,123,60,75,81,99]
print(uspesni(Test_ukol_1))

"""TEST UKOL 2"""
Test_ukol_2 = [1,2,3,4,5,6,7,8,9]
print(na_treti(Test_ukol_2))

"""TEST UKOL 3"""
akcie = ["META", "GOOG", "AMZN", "NTFX", "AAPL"]
cena = [100, 130, 160, 299, 120]
print(stock_price(akcie,cena))

"""TEST UKOL 4"""
cars_kilos ={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Combi": 1700, "Roadster": 1110}
print(light_cars(cars_kilos))

```
