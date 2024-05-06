print("Total Payment Calculation!")

litre = float(input("How much fuel does your vehicle consume per kilometer? "))

km = float(input("How many kilometers did he travel? "))

price = float(input("How much does fuel cost? "))

total_payment = litre * km * price

print("Litre: ", litre, "\nKM: ", km, "\nprice: ", price)

print()

print(f"Total Fuel Consumed (liters): {litre * km} ")
print(f"Total Payment: {total_payment}")