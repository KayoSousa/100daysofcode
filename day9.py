## day9 - Random Number Generator

# 1. Write a program that generates a random number.
# 2. Write a program that generates random number between 2 integers

# Program 1 #
### Generator random number betwenn 0 an 1 ###
import random
number_random = random.random()
print (f"Insert a number random {random}",number_random)

# Program 2 #
### Define values minimum as maximum ###
import random
number_min = int(input(f"Insert a number minimum: "))
number_max = int(input(f"Insert a number maximum: "))

### Generator a number random between the min as max ###
number_random = random.randint(number_min, number_max)
print(f"Number random generator between {number_min} and {number_max} is: {number_random}")
