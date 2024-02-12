"""
CP1404 - Practical 2
Student name: Tenzin Yoezer
"""

def main():
    """Get a score and display its category."""
    try:
        score = float(input("Enter score: "))
        print(determine_category(score))
    except ValueError:
        print("Invalid input. Please enter a numeric score.")

def determine_category(score):
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