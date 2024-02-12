"""
CP1404: Practical 1
Student name: Tenzin Yoezer
Program: Menus
"""

menu = ("(H)ello"
        "(G)oodbye"
        "(Q)uit")
name = input("Enter name: ")

choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(menu)
    choice = input(">>> ").upper()
print('Finished')