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

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f" The year {year} is leap year.")
        else:
            print(f"The year {year} not is leap year.")
    else:
        print(f" The year {year} is leap year.")
else:
    print(f"The year {year} not is leap year.")
print("verification completed.")