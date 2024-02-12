"""
CP1404 - Practical 2
Student name: Tenzin Yoezer
"""

MENU_OPTIONS = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    """program for converting temperature."""
    print(MENU_OPTIONS)
    user_choice = input(">>> ").upper()
    while user_choice != "Q":
        if user_choice == "C":
            celsius_value = float(input("Enter temperature in Celsius: "))
            fahrenheit_result = celsius_to_fahrenheit(celsius_value)
            print(f"Result: {fahrenheit_result:.2f} Fahrenheit")
        elif user_choice == "F":
            fahrenheit_value = float(input("Enter temperature in Fahrenheit: "))
            celsius_result = fahrenheit_to_celsius(fahrenheit_value)
            print(f"Result: {celsius_result:.2f} Celsius")
        else:
            print("Invalid option")
        print(MENU_OPTIONS)
        user_choice = input(">>> ").upper()
    print("Thank you for using the temperature conversion program.")

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

    main()