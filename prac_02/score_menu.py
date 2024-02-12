"""
CP1404 - Practical 2
Student name: Tenzin Yoezer
"""



MENU = ("(G)et a valid score"
        "(P)rint result"
        "(S)how stars"
        "(Q)uit")


def main():
    print(MENU)
    choice = input("Enter: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_status(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Enter: ").upper()
    print("Farewell")


def get_valid_score():
    """Get a score and validate its input."""
    score = int(input("Enter your score: "))
    while not (0 <= score <= 100):
        print("Invalid score. Score must be between 0 and 100 inclusive.")
        score = int(input("Enter your score: "))
    return score


def show_stars(score):
    """Display as many stars equivalent to the score."""
    print(score * "*")

def determine_status(score):
    """Determine the category of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"




main()