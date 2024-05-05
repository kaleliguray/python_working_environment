'''

2 Degree Equation: ax'2 + bx + c

Delta Calculation: b ** 2 - 4 * a * c

1.root : (-b - delta ** 0.5) / (2*a)
2.root : (-b + delta ** 0.5) / (2*a)

'''


a = int(input("a : "))
b = int(input("b: "))
c = int(input("c: "))

delta = b ** 2 - 4 * a * c

print("Delta", delta)

first_root = (-b - delta ** 0.5) / (2*a)
second_root = (-b + delta ** 0.5) / (2*a)

print("First root: ", first_root)
print("Second root: ", second_root)





