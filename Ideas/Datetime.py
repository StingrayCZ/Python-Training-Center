import datetime as dt
import math as mm

print(mm.gcd(24,72))

timestamp = dt.datetime.timestamp(125)
print("Date =", timestamp)


# date class - to work with date
# time class - to work with time
# datetime class - combination of date and times classes

# current_date = dt.date.today()  # Year-Month-Day
current_date = dt.datetime.now() # fsfsf
# print(current_date)  # ALL
print(current_date.hour, current_date.minute, current_date.second)


date = dt.date(2021, 1, 5)       # pro zapis ve formatu
# print(date)

# SEPARATELY
date_b = dt.date.today()

# print("Year", date_b.year)
# print("Month", date_b.month)
# print("Day", date_b.day)

time1 = dt.time(10, 45, 30, 45667)
# time1 = dt.time.hour()
print(time1)