def extract_name(email):
    # Split email by "@" to get the username part
    username = email.split('@')[0]

    # Split username by "." and capitalize each part
    parts = username.split('.')
    capitalized_parts = [part.title() for part in parts]

    # Join the capitalized parts to form the name
    name = ' '.join(capitalized_parts)
    return name


def main():
    users = {}
    while True:
        email = input("Email: ").strip()
        if email == "":
            break

        # Extract name from email
        name = extract_name(email)

        # Ask the user if the extracted name is correct
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()

        # If user doesn't confirm or says 'no', ask for the correct name
        if confirm != "y" and confirm != "":
            name = input("Name: ").strip()

        # Store email and name in dictionary
        users[email] = name

    # Print users' names and emails
    for email, name in users.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
