def is_student(name):
    students = ["Rahul", "Amit", "Priya"]
    return name in students

name = input("Enter name: ")
if is_student(name):
    print(name, "is a Student")
else:
    print(name, "is not a Student")