from guitar import Guitar

def test_guitar_methods():
    # Test data
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 500)

    # Test get_age()
    print("Gibson L-5 CES get_age() - Expected 100. Got", guitar1.get_age(2022))
    print("Another Guitar get_age() - Expected 9. Got", guitar2.get_age(2022))

    # Test is_vintage()
    print("Gibson L-5 CES is_vintage() - Expected True. Got", guitar1.is_vintage(2022))
    print("Another Guitar is_vintage() - Expected False. Got", guitar2.is_vintage(2022))

if __name__ == "__main__":
    test_guitar_methods()
