from guitar import Guitar

def main():
    print("My guitars!")
    guitars = []
    guitar_number = 1

    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.\n")

    print("\nThese are my guitars:")
    for guitar in guitars:
        vintage_string = " (vintage)" if guitar.is_vintage(2024) else ""
        print(f"Guitar {guitar_number}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
        guitar_number += 1

if __name__ == "__main__":
    main()


