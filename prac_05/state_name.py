
# Reformatting the dictionary code to follow PEP 8 convention
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

# Printing states and names neatly lined up
for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code:<3} is {state_name}")

# Using EAFP approach
while True:
    try:
        state_code = input("Enter short state: ")
        if state_code == "":
            break
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
