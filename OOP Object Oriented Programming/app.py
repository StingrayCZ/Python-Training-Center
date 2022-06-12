from Student import Student
from Chef import Chef
from ChineseChef import ChineseChef

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)
student3 = Student("Pam", "Art", 4.5, True)

# print(student1.name)
# print(student1.name)
# print(student1.gpa)
# print(student3.gpa)

# print(student3.on_honor_roll())


myChef = Chef()
myChef.make_chicken()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()

