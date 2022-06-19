# Decorators

A decorator takes in a function, adds some functionality and returns it. In this tutorial, you will learn how you can create a decorator and why you should use it.

```Py
def inc(x):
    return  x + 1

def operate(funcg, x):
    result = funcg(x)
    return result

print(operate(inc, 3))
print(inc(3))
```

```Py
def print_nsg(message):
    greeting = "Hello"

    def printer():
        print(greeting, message)

    printer()

func = print_nsg("Python is awesome")
func()
```

```Py
def printer():
    print("Hello world")

def display_info(func):

    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("Finished execution")

    return inner

# printer()

decpreted_func = display_info(printer)
decpreted_func()
```

```Py
def display_info(func):

    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("Finished execution")

    return inner

@display_info
def printer():
    print("Hello world")


printer()
```
## Dekorator s parametry

```Py
# Decorator with parameters

def smart_divide(func):
    def inner(a, b):
        print('Dividing', a, 'by', b)
        if b == 0:
            print('Cannot divide by 0!')
            return
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    return a / b

value1 = divide(18, 0)
print(value1)
```

```Py
def star(func):
    def inner(arg):
        print('*' * 30)
        func(arg)
        print('*' * 30)
    return inner

def percent(func):
    def inner(arg):
        print('%' * 30)
        func(arg)
        print('%' * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)

# without @ symbol
# printer = star(percent(printer))
    
printer("Hello decorators")
```