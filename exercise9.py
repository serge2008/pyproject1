number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print("The sum of the two numbers is:", number1 + number2)
print("The difference when the second number is subtracted from the first number is:", number1 - number2)
print("The product of the two numbers is:", number1 * number2)
if number2 != 0:
    print("The quotient when the first number is divided by the second number is:", number1 / number2)
else:
    print("Cannot divide by zero. Please choose a non-zero second number.")