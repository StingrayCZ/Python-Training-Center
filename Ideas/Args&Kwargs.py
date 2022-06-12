# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)

def testArg(*num):
    for _ in range(len(num)):
        print(type(num[_]))

def JUMP():
    print("\n")

# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# myFun('1', 2)
# testArg('1', 2)

# Python program to illustrate
# *kwargs for variable number of keyword arguments

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

# Driver code
# myFun(first ='Geeks', mid ='for', last='Geeks', keys=123)

JUMP()

def myFun(arg1, arg2, **kwargs):

    print(f"{arg1}, {arg2}")

    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
        print(f"{key} == {value}")


# Driver code
# myFun("Hi" , "Sheet", first='Geeks', mid='for', last='Geeks')

def myFun(*args,**kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks','for','geeks',first="Geeks",mid="foppr",last="Geeks")
