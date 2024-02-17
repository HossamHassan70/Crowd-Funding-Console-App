# import re
# import getpass
# import json
from register import register_user
from login import login

# def validate_email(email):
#     # Check if the email is not empty and has a valid format
#     email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
#     return bool(re.match(email_regex, email))
#
#
# def validate_password(password):
#     # Check if the password is not empty and meets certain criteria
#     password_regex = r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
#     return bool(re.match(password_regex, password))
#

# def login():
#     try:
#         email = input("Email: ")
#         password = getpass.getpass("Password: ")
#
#         try:
#             with open("users.json", "r") as file:
#                 users = json.load(file)
#         except FileNotFoundError:
#             users = []
#
#         for user in users:
#             if user["email"] == email and user["password"] == password:
#                 print("Login successful")
#                 return
#
#         raise ValueError("Invalid email or password")
#     except ValueError as e:
#         print("Login failed: " + str(e))


def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                register_user()
            elif choice == "2":
                login()
            elif choice == "3":
                print("See you later...")
                break
            else:
                raise ValueError("Invalid choice")
        except ValueError as e:
            print("Error: " + str(e))


if __name__ == "__main__":
    main()
