import json


def read_data(file_param):
    # read the data from users.json file
    try:
        file = open(file_param, "r")
    except FileNotFoundError:
        print("Error: File Not Found")
    except Exception as e:
        print(e)
    else:
        try:
            data = json.load(file)
        except Exception as e:
            print(e)
            data = []
        file.close()
        return data


def write_data(file_name, data: list):
    try:
        file = open(file_name, "w")
    except Exception as e:
        print(e)
        return False
    else:
        json.dump(data, file, indent=2)
        file.close()
        return True
