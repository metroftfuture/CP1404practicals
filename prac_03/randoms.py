"""
CP1404/CP5632 - Practical
student name = Tenzin Yoezer
"""
import random

print(random.randint(5, 20))  # line 1
# The output was a random integer between 5 and 20, inclusive.
#  Smallest number: 5, Largest number: 20

print(random.randrange(3, 10, 2))  # line 2

# The output was a random odd integer between 3 and 9, inclusive.
# Smallest number: 3, Largest number: 9
# No, line 2 could not have produced a 4 because the step size is 2,
# starting from 3, so it only generates odd numbers.

print(random.uniform(2.5, 5.5))  # line 3

# The output was a random floating-point number between 2.5 and 5.5.
# Smallest number: 2.5, Largest number: 5.5


# Code to produce a random number between 1 and 100 inclusive:

print(random.randint(1, 100))

