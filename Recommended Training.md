# Dictionary [Key - Value]

<a href="https://www.youtube.com/watch?v=daefaLgNkw0">Dictionaries (YoutubeVid)</a>

```Py
student = {"name": "John", "age": 25, "courses": ["Math", 'ComSci']}

# muze obsahovat list

print(student)               # print celeho obsahu
student["phone"] = "555-5555"   # Pridani dalsiho keywordu + obsahu
student["name"] = "Jane"        # Prepise jmeno

# Hromadne prepsani vybranych casti
student.update({"name": "Jane", "age": 26, "phone": 555-6666})

# Smazani veku
# del student["age"]

age = student.pop("age")
print(age)

print(student)               # print celeho obsahu
print(student["courses"])    # print jen obsahu courses

print(student.get("phone", "Not Found"))
"""
key - key to be searched in the dictionary
value (optional) - Value to be returned if the key is not found. The default
the value for the specified key if key is in the dictionary.
None if the key is not found and value is not specified.
value if the key is not found and value is specified.
"""
```

```Py
student = {"name": "John", "age": 25, "courses": ["Math", 'ComSci']}

print(student.keys())     # dict_keys(['name', 'age', 'courses'])
print(student.values())   # dict_values(['John', 25, ['Math', 'ComSci']])
print(student.items())    # dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'ComSci'])])
```

```Py
student = {"name": "John", "age": 25, "courses": ["Math", 'ComSci']}

for _ in student:
    print(_)  # Print keys

for _ in student.items():
    print(_)  # Print items, e.g. ('name', 'John')

for a, _  in student.items():
    print(a, _)  # Print items, e.g. name John

```

# Function

<a href="https://www.youtube.com/watch?v=daefaLgNkw0">Functions (YoutubeVid)</a>

```Py
def hello(greetings):
    return "{} Function.".format(greetings)   # e.g. of format string

print(hello("Hi"))
```

# Format()

<a href="https://www.w3schools.com/python/ref_string_format.asp">Function explanation</a>

```Py
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1} a {2}".format("John",36, "mm")
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)
```
```Py
#Simplified
print(f"Value is {num:.1f}")
```

```Py
# Args and kwargs
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info("Math", "Art", name="John", age=22)
```
