try:
    number = int(input("Enter a number: "))
    print(number)

except:
    print("invalid input")

else:
  print("Nothing went wrong")

finally:
  print("The 'try except' is finished")