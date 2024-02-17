import json


def delete_project(user_name):
    try:
        f = open("projects.json", 'r')
        projects = json.load(f)
        f.close()
    except FileNotFoundError:
        print("No projects found.")
        return

    user_projects = []
    for project in projects:
        if project.get("User") == user_name:
            user_projects.append(project)

    if not user_projects:
        print("You have no projects to delete.")
        return

    print("Your Projects:")
    for idx, project in enumerate(user_projects, start=1):
        print(f"{idx}. {project['Title']}")

    selection = input("Enter the number of the project you want to delete: ")
    try:
        selection = int(selection)
        if selection < 1 or selection > len(user_projects):
            raise ValueError
    except ValueError:
        print("Invalid selection.")
        return

    del projects[projects.index(user_projects[selection - 1])]

    f = open("projects.json", 'w')
    json.dump(projects, f, indent=2)
    f.close()

    print("=== Project deleted successfully! ===")


def delete(user_name):
    try:
        # user_email = input("Enter your email address: ")
        delete_project(user_name)
    except Exception as e:
        print("An error occurred:", e)
# delete()
