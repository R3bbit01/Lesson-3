num1 = float(input("What is the price of a Child's meal?: " ))
num2 = float(input("What is the price of an adult's mean?: "))
num3 = int(input("How many children are there?: "))
num4 = int(input("How many adults are there?: " ))
num5 = float(input("What is the sales tax rate?: "))
print()

sum = num1 * num3 + num2 * num4
print("Subtotal: $", sum)
print("Sales Tax: $", num5 * sum / 100)
print("Total: $", num5 * sum / 100 + sum)
print()
amount = int(input("What is the payment amount:$ "))
print("Change: $", (num5 * sum / 100 + sum) - amount)
