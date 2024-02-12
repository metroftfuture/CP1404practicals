"""def age_category():
    age = int(input("age:"))
    if age < 18:
        category = "child"
    elif age<65:
        category = "adult"
    else:
        category = "geriatric"
        print(category)

age_category()"""

def determine_category(age):
    if age < 18:
        return "child"
    elif age < 65:
        return "adult"
    else:
        return "geriatric"
for age in range (101):
    category = determine_category(age)
    print(f"{age} is {category}")


def is_adult (age):
    return age>- 18

print(f"Got {is_adult (18)}, expected True")
print(f"Got {is_adult (17)}, expected False")
assert is_adult(20)
assert not is_adult(0)
