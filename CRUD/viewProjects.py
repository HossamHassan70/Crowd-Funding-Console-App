import json


def view_projects():
    try:
        f = open("projects.json", 'r')
        projects = json.load(f)
        f.close()

        if projects:
            print("All Projects:")
            for idx, project in enumerate(projects, start=1):
                print(f"\nProject {idx}:")
                print("Title:", project["Title"])
                print("Details:", project["Details"])
                print("Total Target:", project["Total_Target"])
                print("Start Time:", project["Start_Time"])
                print("End Time:", project["End_Time"])
        else:
            print("No projects found.")
    except FileNotFoundError:
        print("No projects found.")

# view_projects()
