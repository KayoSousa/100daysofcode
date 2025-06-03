## day12 - odd-even

# 1. write a program to check if a number is even or odd.

while True:
    try:
        number_str = input(f"Enter an number interer: ")
        number = int(number_str)

        break

    except ValueError:
        print(f"Error: '{number_str}' is not a valid integer. Please, enter only numbers.")
        print("The Program could not verify the type of the number.")

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

print("End of program")