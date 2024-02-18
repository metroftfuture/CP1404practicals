"""CP1404/CP5632 - Practical
student name = Tenzin Yoezer
"""

# Task 1: Write user's name to a file
name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)

# Task 2: Read user's name from the file and print it
with open("name.txt", "r") as file:
    name = file.read()
print(f"Your name is {name}")


# Task 3: Add the first two numbers from numbers.txt
with open("numbers.txt", "r") as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
result = number1 + number2
print("Sum of the first two numbers:", result)

# Task 4: Read all numbers from numbers.txt and print their total
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)
print("Total of all numbers:", total)