import json
from register import validate_email


def edit_project(user_name):
    try:
        file = open("projects.json", "r")
        projects = json.load(file)
        file.close()

        user_projects = []

        for project in projects:
            project_user_name = project.get("User")

            if project_user_name == user_name:
                user_projects.append(project)

            elif not user_projects:
                print("You have no projects to edit.")
                return

        print("Your Projects:")
        for idx, project in enumerate(user_projects, start=1):
            print(f"{idx}. {project['Title']}")

        selection = input("Enter the number of the project you want to edit: ")
        try:
            selection = int(selection)
            if selection < 1 or selection > len(user_projects):
                raise ValueError
        except ValueError:
            print("Invalid selection.")
            return

        selected_project = user_projects[selection - 1]
        print("Enter new details for the project (leave blank to keep current value):")
        selected_project["Title"] = (
            input(f"New Title ({selected_project['Title']}): ")
            or selected_project["Title"]
        )
        selected_project["Details"] = (
            input(f"New Details ({selected_project['Details']}): ")
            or selected_project["Details"]
        )
        selected_project["Total_Target"] = (
            input(f"New Total Target ({selected_project['Total_Target']}): ")
            or selected_project["Total_Target"]
        )
        selected_project["Start_Time"] = (
            input(f"New Start Date ({selected_project['Start_Time']}): ")
            or selected_project["Start_Time"]
        )
        selected_project["End_Time"] = (
            input(f"New End Date ({selected_project['End_Time']}): ")
            or selected_project["End_Time"]
        )

        f = open("projects.json", "w")
        json.dump(projects, f, indent=2)
        f.close()

        print("=== Project edited successfully! ===")

    except FileNotFoundError:
        print("No projects found.")
    except Exception as e:
        print("An error occurred:", e)


def edit(user_name):
    try:
        # user_email = input("Enter your email to edit: ")
        # if validate_email(user_email):
        edit_project(user_name)
    except Exception as e:
        print("An error occurred:", e)


# edit()
