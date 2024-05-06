print("Take the two perpendicular sides (a, b) of a right triangle from the user and try to find the length of the hypotenuse.")

a = int(input("a: "))
b = int(input("b: "))

hypotenuse = int((a*a + b*b) ** 0.5)

print("Hypotenuse length: ", hypotenuse)