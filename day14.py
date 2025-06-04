## day14 - Leap Year

# 1. write a program that checks if a given input year is a leap year or not.

while True:
    try:
        year_str = input("Enter a year to see if it is a leap year: ")
        year = int(year_str)
        break
    except ValueError:
        print(f"Error: not is a year valid. Please, enter only whole numbers.")
        print("Try again.")      