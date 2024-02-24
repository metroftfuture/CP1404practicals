numbers = [3, 1, 4, 1, 5, 9, 2]

#my answer

# numbers[2:5]

# The expression numbers[2:5] is meant to slice the list numbers from index 2 up to (but not including) index 5. However
# if we want to include the element at index 5, we should adjust it to numbers[2:6]

"""numbers[0]: The first element of the list, which is 3.
numbers[-1]: The last element of the list, which is 2.
numbers[3]: The element at index 3, which is 1.
numbers[:-1]: All elements except the last one, so [3, 1, 4, 1, 5, 9].
numbers[3:4]: Elements from index 3 up to (but not including) index 4, which is [1].
5 in numbers: Checks if 5 is present in the list, which is True.
7 in numbers: Checks if 7 is present in the list, which is False.
"3" in numbers: Checks if the string "3" is present in the list, which is False because the list contains integers, not
strings.
numbers + [6, 5, 3]: Concatenation of the list numbers with [6, 5, 3], resulting in [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]."""


# Change the first element of numbers to "ten"
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)