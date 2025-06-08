## day15 - Factorial

# 1. write a function to calculate the factorial of a number.

number = int(input("\nEnter a number to calculate its factorial: "))
factorial = 1

while number > 1:
    factorial *= number
    number -= 1
print(f"The factorial of {number} is {factorial}.")
