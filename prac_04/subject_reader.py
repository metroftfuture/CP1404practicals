"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data_list = []  # Initialize an empty list to store the data
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer
        data_list.append(parts)  # Append the parts to the data list
    input_file.close()
    return data_list  # Return the list of lists


main()

def display_subject_details(data):
    """Display subject details."""
    for subject_data in data:
        subject_code = subject_data[0]
        lecturer = subject_data[1]
        num_students = subject_data[2]
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students")


def main():
    data = get_data()
    display_subject_details(data)


main()
