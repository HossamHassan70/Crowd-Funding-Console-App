import re
# import json
import getpass
from josn_op import read_data, write_data


# from main_menu import validate_email
# from main_menu import validate_password


def validate_email(email):
    # Check if the email is not empty and has a valid format
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, email))


def validate_password(password):
    password_regex = r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return bool(re.match(password_regex, password))


def validate_name(name):
    # Check if the name is not empty and contains only alphabetical characters
    return name and name.isalpha()


def validate_mobile(mobile):
    # Check if the mobile number is not empty and matches a specific pattern
    mobile_regex = r"^01[0125][0-9]{8}$"
    return bool(re.match(mobile_regex, mobile))


def register_user():
    # global data
    try:
        # first_name = input("Enter First Name: ")
        # last_name = input("Enter Last Name: ")
        # email = input("Enter Email: ")
        # password = getpass.getpass("Enter Password: ")
        # confirm_password = getpass.getpass("Confirm Password: ")
        # mobile = input("Mobile Phone: ")
        # email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        # password_regex = r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        # mobile_regex = r"^01[0125][0-9]{8}$"
        # Input validation using a while loop
        while True:
            # Prompt for first name until valid input is provided
            first_name = input("Enter First Name: ")
            if validate_name(first_name):
                break
            else:
                print("Invalid first name. Please try again.")

        while True:
            # Prompt for last name until valid input is provided
            last_name = input("Enter Last Name: ")
            if validate_name(last_name):
                break
            else:
                print("Invalid last name. Please try again.")
        while True:
            # Prompt for email until valid input is provided
            email = input("Enter Email: ")
            if validate_email(email):
                break
            else:
                print("Invalid email. Please try again.")
        while True:
            # Prompt for password securely until valid input is provided
            password = getpass.getpass("Enter Password: ")
            if validate_password(password):
                break
            else:
                print("Invalid password. Please try again.")

        while True:
            # Prompt for confirming password securely until it matches the original password
            confirm_password = getpass.getpass("Confirm Password: ")
            if confirm_password == password:
                break
            else:
                print("Passwords do not match. Please try again.")

        while True:
            # Prompt for mobile number until valid input is provided
            mobile = input("Mobile Phone: ")
            if validate_mobile(mobile):
                break
            else:
                print("Invalid mobile number. Please try again.")

        # if not re.match(email_regex, email):
        #     raise ValueError("Invalid email format (example@domain.com)")
        #
        # if not re.match(password_regex, password):
        #     raise ValueError("\33Invalid Password format (Should Contains alphabetical character, digit, special "
        #                      "character and at least 8 characters)\0")
        #
        # if password != confirm_password:
        #     raise ValueError("Passwords do not match")
        #
        # if not re.match(mobile_regex, mobile):
        #     raise ValueError("Invalid Egyptian phone number")

        user = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "mobile": mobile
        }

        old_data = read_data("users.json")
        old_data.append(user)
        saved = write_data("users.json", old_data)
        if saved:
            print("=== Register Successfully ===")

    except Exception as e:
        print("Registration failed: " + str(e))


"""
        try:
            with open("users.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append(user)

        with open("users.json", "w") as file:
            json.dump(data, file, indent=2)

        print("Registration successful")
    except ValueError as e:
        print("Registration failed: " + str(e))
"""
if __name__ == "__main__":
    register_user()
