"""
CP1404 - Practical 7
Name: TENZIN YOEZER
"""

from project import Project

def load_projects(filename):
    """Load projects from a file."""
    projects = []
    try:
        with open(filename, 'r') as file:
            next(file)  # Skip header
            for line in file:
                name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
                start_date = Project.parse_date(start_date)
                priority = int(priority)
                cost_estimate = float(cost_estimate)
                completion_percentage = int(completion_percentage)
                project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                projects.append(project)
        print(f"Loaded {len(projects)} projects from {filename}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print(f"Error: Invalid data in file '{filename}'.")

    return projects

def save_projects(projects, filename):
    """Save projects to a file."""
    try:
        with open(filename, 'w') as file:
            file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
            for project in projects:
                file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
        print(f"Projects saved to {filename}")
    except IOError:
        print(f"Error: Unable to write to file '{filename}'.")

def display_projects(projects):
    """Display projects."""
    for project in projects:
        print(project)

def filter_projects_by_date(projects):
    """Filter projects by date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    date = Project.parse_date(date_string)
    filtered_projects = [project for project in projects if project.is_started_after_date(date)]
    display_projects(filtered_projects)

def add_new_project(projects):
    """Add a new project."""
    name = input("Name: ")
    start_date = Project.parse_date(input("Start date (dd/mm/yyyy): "))
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)

def update_project(projects):
    """Update a project."""
    try:
        index = int(input("Project index to update: "))
        project = projects[index]
        new_percentage = int(input("New Percentage: "))
        new_priority = int(input("New Priority: "))
        if new_percentage:
            project.update_completion_percentage(new_percentage)
        if new_priority:
            project.update_priority(new_priority)
    except (ValueError, IndexError):
        print("Invalid index.")

def main():
    """Main function."""
    projects_filename = 'projects.txt'
    projects = load_projects(projects_filename)

    while True:
        print("\nMenu:")
        print("(L)oad projects")
        print("(S)ave projects")
        print("(D)isplay projects")
        print("(F)ilter projects by date")
        print("(A)dd new project")
        print("(U)pdate project")
        print("(Q)uit")

        choice = input(">>> ").strip().lower()

        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(projects, filename)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_option = input(f"Would you like to save to {projects_filename}? ").strip().lower()
            if save_option.startswith('y'):
                save_projects(projects, projects_filename)
            print("Thank you for using Pythonic Project Management.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("Welcome to Pythonic Project Management")
    main()
