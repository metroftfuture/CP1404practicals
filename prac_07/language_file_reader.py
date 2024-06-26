"""
CP1404 - Practical 7
Name: TENZIN YOEZER
"""

from programming_language import ProgrammingLanguage

def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # Open the file for reading
    with open('languages.csv', 'r') as in_file:
        # Skip the header line
        next(in_file)
        # All other lines are language data
        for line in in_file:
            # Strip newline from end and split it into parts (CSV)
            parts = line.strip().split(',')
            if len(parts) >= 5:  # Ensure the line has at least 5 values
                # Reflection is stored as a string (Yes/No) and we want a Boolean
                reflection = parts[2] == "Yes"
                # Pointer Arithmetic is stored as a string (Yes/No) and we want a Boolean
                pointer_arithmetic = parts[4] == "Yes"
                # Construct a ProgrammingLanguage object using the elements
                # year should be an int
                language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
                # Add the language we've just constructed to the list
                languages.append(language)
            else:
                print(f"Ignoring invalid line: {line}")

    # Loop through and display all languages (using their str method)
    for language in languages:
        print(language)


if __name__ == "__main__":
    main()
