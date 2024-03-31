"""
CP1404 - Practical 7
Name: TENZIN YOEZER
"""

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance.

        name: string, name of the guitar (default "")
        year: int, year the guitar was made (default 0)
        cost: float, cost of the guitar (default 0.0)
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def is_vintage(self, current_year):
        """Check if the guitar is considered vintage."""
        return current_year - self.year >= 50

    def compare_cost(self, other_guitar):
        """Compare the cost of this guitar with another guitar."""
        if self.cost < other_guitar.cost:
            return f"{self.name} is cheaper than {other_guitar.name}"
        elif self.cost > other_guitar.cost:
            return f"{self.name} is more expensive than {other_guitar.name}"
        else:
            return f"{self.name} costs the same as {other_guitar.name}"

def main():
    """Demo/test Guitar class."""
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2012, 2999.95)

    print(guitar1)
    print(guitar2)

    print(f"{guitar1.name} is vintage: {guitar1.is_vintage(2024)}")
    print(f"{guitar2.name} is vintage: {guitar2.is_vintage(2024)}")

    print(guitar1.compare_cost(guitar2))

if __name__ == "__main__":
    main()
