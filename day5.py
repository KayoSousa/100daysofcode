## day5 - Conditional Statements and Loops

#####     If-else Statements      #####

# Program 1: Check if number is evenn/odd
number = int(input("Enter an interer: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Program 2: Determine age category
age = int(input("\nEnter your age: "))
if age < 13:
    print("Your are a child.")
elif 13 <= age < 20:
    print("Your are a teenager.")
elif 20<= age < 60:
    print("Your are an adult.")
else:
    print("You are a senior citizen.")

#####     Nested If-else Statements      #####

# Program 3: using nested if-else, find the largest os three numbers
num1 = int(input("\nEnter the first number: "))
num2 = int(input("Enter the secong number: "))
num3 = int(input("Enter three number: "))

if num1 >= num2:
    if num1 >= num3:
        print(f"The largest number is {num1}.")
    else:
        print(f"The largest number {num3}.")
else:
    if num2 >= num3:
        print(f"The largest number is {num2}.")
    else:
        print(f"The largest number is {num3}.")

#####     For Loop      #####

# Program 4: Calculate the sum of all numbers up to the given input number
number = int(input("\nEnter a positive number to calculate the sum up to that number: "))
sum = 0
for n in range(1,number + 1):
    sum += n
print(f"The sum of all numbers from 1 to {number} is {sum}.")

#####     While Loop      #####

# Program 5: Calculate the factorial of a give number
number = int(input("\nEnter a number to calculate its factorial: "))
factorial = 1
while number > 1:
    factorial *= number
    number -= 1
print(f"The factorial of {number} is {factorial}.")

print("\nCongratulations on completing Day 5 of the 100 days of Python Of Code challenge!\n")