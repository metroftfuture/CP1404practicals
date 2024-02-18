"""
CP1404/CP5632 - Practical
student name = Tenzin Yoezer
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""Questions
1. When will a ValueError occur?
= A ValueError will occur if the user enters a value that cannot be converted to an integer,
 such as a string or a floating-point number.

2.When will a ZeroDivisionError occur?
= A ZeroDivisionError will occur if the user inputs a denominator of zero,
 as division by zero is not defined in mathematics

3.Could you change the code to avoid the possibility of a ZeroDivisionError?
= To avoid the possibility of a ZeroDivisionError, we can add a condition to 
check if the denominator is zero before performing the division operation.

4. If you could figure out the answer to question 3, then make this change now.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
