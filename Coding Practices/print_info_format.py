print("Multiply the 3 numbers you received from the user and print them on the screen. Try to print to the screen using the *format* method.")

# Ask the user for three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Multiply the numbers
result = num1 * num2 * num3

# Print the result using format method
print("The result of multiplying {} by {} by {} is: {}".format(num1, num2, num3, result))

print("*"*50)

print("University Enrollment")

name = input("Student name: ")
surname = input("Student surname: ")
age = int(input("Age: "))
department = input("University Department: ")

info = [name, surname, age, department]

print("Name: {}\tSurname: {}\nage: {}\nDepartment: {}".format(info[0],info[1],info[2],info[3]))
