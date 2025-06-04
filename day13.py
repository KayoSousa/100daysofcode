## day13 - Largest of three numbers

# 1. write a program to find largest of three numbers.

num1 = int(input("\nEnter the first number: "))
num2 = int(input("\nEnter the second number: "))
num3 = int(input("\nEnter the three number: "))

if num1 >= num2:
    if num1 >= num3:
        print(f"The largest number is {num1}.")
    else:
        print(f"The largest number is {num3}.")
else:
    if num2 >= num3:
        print(f"The largest number is {num2}.")
    else:
        print(f"The largest number is {num3}.")