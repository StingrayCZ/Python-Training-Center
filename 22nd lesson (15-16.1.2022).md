# 22nd lesson (15-16.1.2022)

```Py
import random


# round = random.sample(range(1, 51), 6)

# print(sorted(round))

class Sazka:

    def __init__(self, xx):
        pass

    def sportka(self):
        pass

    def extra_renta(self):
        pass

#######################################



def add_time(start):
    pass

timet = 654002
H = timet//3600
M = (timet//60)-H*60
S = timet-(timet//60)*60

print('%02d' % H,":",M,":",S)

print(f"{timet//3600}:{(timet//60)-(timet//3600)*60}:{timet-(timet//60)*60}")

n = 4
print('%02d' % n)


#
# timet = 4000
# print(f"{timet%3600}:{(60*(timet%60))%60}")


start_time = "11:59 PM"
added_time = "24:05"
start_t = start_time.split()
h_m = start_t[0].split(":")
hour, minute = int(h_m[0]), int(h_m[1])
am_pm = start_t[1]

# print(hour, minute, am_pm)

if am_pm == "PM":
    hour += 12

print(hour, minute)

# Rozdeleni added time
add_time = "24:05"
d = added_time.split(":")
add_hour, added_minute = int(d[0]), int(d[1])
# print(add_hour, added_minute)

# secteni na celkovy cas
total_h = hour + add_hour
total_m = minute + added_minute
# print(total_h, total_m)

dny = total_h // 24
hodiny = total_h % 24

# print(dny)
# print(hodiny)
#
# print("testovaci")
# print(31/5)
# print(31//5)
# print(31%5)



# set_width = int(input("Enter width:"))
# set_height = int(input("Enter height:"))
#
# print((set_width ** 2 + set_height ** 2) ** 0.5)

# for _ in range(set_height):
#     print("* "*set_width)

#
print("OOP " * 5)

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    # def __repr__(self):


    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_heigjt):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimetr(self):
        return (2 * self.width) + (2 * self.height)

    def ge_diagonal(self):
        return (self.width ** 2 + set_height **2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture"
        return self.height*(self.width*"*" + "\n")


rect = Rectangle(10, 5)
print(rect)

print("OOP II " * 5)

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(width=side, height=side)

    def __str__(self):
        return f"Ctverec se stranou delky {self.side}"

    def se_side(self, new_side):
        self.side = new_side

sq = Square(6)
print(sq.width)
print(sq.height)

print(sq.get_area())
sq.set_height(3)
print(sq.width)
print(sq.height)
```
