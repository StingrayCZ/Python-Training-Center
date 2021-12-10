# Dictionary [Key - Value]

<a href="https://www.youtube.com/watch?v=daefaLgNkw0">Dictionaries</a>

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
