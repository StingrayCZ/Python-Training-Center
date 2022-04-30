# OOP Object Oriented Programming

## Lesson A - basic
Základní struktura objektu:

```Py
class Student:

    def __int__(self, name, major, gpa, is_on_probation):
        self.name  = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
```
Aplikace využívající class Student
```Py
from Student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student1.name)
print(student1.gpa)
```
## Lesson B - soutez

```Py
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
```

```Py
from Question import Question

question_prompts = [
    "Whats color are apple?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "Whats color are Bannanas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "Whats color are strawberries\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

print(type(question_prompts))

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('You got ' + str(score) + '/' + str(len(questions)) + ' correct')

run_test(questions)
```

## Lesson C - Object Function
