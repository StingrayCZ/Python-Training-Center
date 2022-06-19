 # TRY, Except, Else, finally
 
The **try** block lets you test a block of code for errors.

The **except** block lets you handle the error.

The **else** block lets you execute code when there is no error.

The **finally** block lets you execute code, regardless of the result of the try- and except blocks.

```Py
try:
    number = int(input("Enter a number: "))
    print(number)

except:
    print("invalid input")

else:
  print("Nothing went wrong")

finally:
  print("The 'try except' is finished")
  
```