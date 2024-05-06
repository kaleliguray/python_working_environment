print("Ask the user for two numbers and replace the values of these numbers with each other.")

first = int(input("First Number: "))
second = int(input("Second Number: "))

print("Before changing---> " + f"First Number: {first} " + f" Second Number: {second}")

print()

temp = first
first = second
second = temp

print("After changing---> " + f"First Number: {first} " + f" Second Number: {second}")

print("*" * 50)

print("Changing again, but different method")

first, second = second, first

print("After changing---> " + f"First Number: {first} " + f" Second Number: {second}")
