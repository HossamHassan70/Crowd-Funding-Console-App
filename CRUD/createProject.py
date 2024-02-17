import datetime
import json


def validate_datetime(input_date):
    try:
        date_obj = datetime.datetime.strptime(input_date, '%d/%m/%Y')
        return date_obj
    except ValueError:
        print("Invalid date format use the format dd/mm/yyyy.")
        return None


def target_amount(amount):
    try:
        amount_float = float(amount)
        if amount_float <= 0:
            print("Total target amount must be a positive number.")
            return None
        return amount_float
    except ValueError:
        print("Invalid target amount format")
        return None


def create_project(user_name):
    try:
        title = input("Enter the title of the Project: ")
        details = input("Enter the details of the Project: ")
        total_target = input("Enter the total target amount: ")
        total_target = target_amount(total_target)
        if total_target is None:
            return None

        start_date = input("Enter the start date(dd/mm/yyyy): ")
        start_date = validate_datetime(start_date)
        if start_date is None:
            return None

        end_date = input("Enter the end date(dd/mm/yyyy): ")
        end_date = validate_datetime(end_date)
        if end_date is None:
            return None

        if end_date <= start_date:
            print("End date must be after the start date.")
            return None

        project_data = {
            "Title": title,
            "Details": details,
            "Total_Target": total_target,
            "Start_Time": start_date.strftime('%d/%m/%Y'),
            "End_Time": end_date.strftime('%d/%m/%Y'),
            "User": user_name
        }

        return project_data
    except Exception as e:
        print("Error occurred while creating project:", e)
        return None


def save_project(project_data):
    try:
        try:
            file = open("projects.json", 'r')
            existing_projects = json.load(file)
            file.close()
        except (FileNotFoundError, json.JSONDecodeError):
            existing_projects = []

        existing_projects.append(project_data)

        file = open("projects.json", 'w')
        json.dump(existing_projects, file, indent=2)
        file.close()
        print("=== Project created and saved successfully! ===")
    except Exception as e:
        print("Error occurred while saving project:", e)


def main(user_name):
    try:
        # while True:
        # user_email = input("Enter your email address: ")
        project_data = create_project(user_name)
        if project_data:
            save_project(project_data)
            # print("=== Project created successfully! ===")
        else:
            print("Sorry, Project creation failed, try again")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main(user_name="")
