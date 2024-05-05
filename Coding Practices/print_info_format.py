print("University Enrollment")

name = input("Student name: ")
surname = input("Student surname: ")
age = int(input("Age: "))
department = input("University Department: ")

info = [name, surname, age, department]

print("Name: {}\tSurname: {}\nage: {}\nDepartment: {}".format(info[0],info[1],info[2],info[3]))