## day6 - Functions and Code Reusability

#####     Simple Function      #####

# Program 1: Greet_user function
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Kayo")
print()

#####     Default and Keyword Arguments      #####

# Program 2: Greet_user function with default values as argument
def greet_user(name="Guest"):
    print(f"Hello,{name}")

greet_user() #Output: Hello, Guest
greet_user("Kayo") #Output: Hello, Kayo
print()

#####     Function With Return Values      #####

# Program 3: Calculate and returns the area of a retangle
def calculate_area(length, breadth):
    return length * breadth

area = calculate_area(5, 3)
print(f"The area of the retangle is {area}.")
print()
