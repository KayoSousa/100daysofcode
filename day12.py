## day12 - odd-even

# 1. write a program to check if a number is even or odd.

number = int(input(f"Enter an number interer: "))
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

print("End of program")