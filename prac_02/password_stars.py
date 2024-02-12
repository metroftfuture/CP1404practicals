"""
CP1404 - Practical 2
Student name: Tenzin Yoezer
"""

def main():
    min_length = 8  # Minimum password length
    password = get_password(min_length)
    print_asterisks(password)


def get_password(min_length):
    """Get password from user, ensuring it meets the minimum length."""
    while True:
        password = input(f"Enter password of at least {min_length} characters: ")
        if len(password) >= min_length:
            return password
        else:
            print("Password too short. Please try again.")


def print_asterisks(password):
    """Print asterisks corresponding to the password's length."""
    print('*' * len(password))


main()



