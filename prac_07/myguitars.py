"""
CP1404 - Practical 7
Name: TENZIN YOEZER
"""

from guitar import Guitar

def load_guitars(filename):
    """Read guitars from a file and store them in a list."""
    guitars = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    name, year, cost = parts[0], int(parts[1]), float(parts[2])
                    guitar = Guitar(name, year, cost)
                    guitars.append(guitar)
                else:
                    print(f"Ignoring invalid line: {line}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print(f"Error: Invalid data in file '{filename}'.")

    return guitars

def display_guitars(guitars):
    """Display details of guitars in a list."""
    for index, guitar in enumerate(guitars, 1):
        print(f"Guitar {index}: {guitar}")

def sort_guitars_by_year(guitars):
    """Sort guitars in a list by year."""
    guitars.sort(key=lambda x: x.year)

def main():
    """Main function."""
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    if guitars:
        print("List of guitars:")
        display_guitars(guitars)

        print("\nSorted list of guitars by year:")
        sort_guitars_by_year(guitars)
        display_guitars(guitars)

if __name__ == "__main__":
    main()
