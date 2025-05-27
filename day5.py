## day5 - Conditional Statements and Loops

#####     If-else Statements      #####

# Program 1: Check if number is evenm/odd
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
        