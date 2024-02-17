import getpass
import json

from register import validate_email, validate_password
from CRUD.createProject import main
from CRUD.viewProjects import view_projects
from CRUD.updateProject import edit
from CRUD.deleteProject import delete


def login():
    try:
        while True:
            email = input("Email: ")
            if validate_email(email):
                break
            else:
                print("Invalid email. Please try again.")
        while True:
            password = getpass.getpass("Password: ")
            if validate_password(password):
                break
            else:
                print("Invalid email. Please try again.")

        try:
            with open("users.json", "r") as file:
                users = json.load(file)
        except FileNotFoundError:
            users = []

        for user in users:
            if user["email"] == email and user["password"] == password:
                print("=== Login successful ===")
                login_menu(user["first_name"])
                return

        raise ValueError("Invalid email or password")
    except ValueError as e:
        print("Login failed: " + str(e))


def login_menu(user_name):
    # print("Log-In")
    # user_mail = login()
    if user_name:
        while True:
            choice = int(input("""
                1- Create new project      2- View all projects
                3- Edit project            4- Delete project
                5- Logout
                """))

            if choice == 1:
                main(user_name)
            elif choice == 2:
                view_projects()  # Not logic to show all projects for every user check this
            elif choice == 3:
                edit(user_name)
            elif choice == 4:
                delete(user_name)
            elif choice == 5:
                return


if __name__ == "__main__":
    login()
