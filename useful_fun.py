import os
import json
from fastapi import Request
from pathlib import Path


def gen_random_name():
    return os.urandom(16).hex()


def get_user(request: Request):
    return request.cookies.get("user")


def write_file(filename: str, numbers: dict, user: str):
    file_path = Path(filename)
    if file_path.is_file():
        with open(filename, 'r') as file:
            old_data = json.load(file)
            if user in old_data.keys():
                old_data[user] += numbers[user]
                new_data = json.dumps(old_data)
                with open(filename, 'w') as f1:
                    f1.writelines(new_data)
            else:
                with open(filename, 'w') as f2:
                    old_data[user] = numbers[user]
                    new_data = json.dumps(old_data)
                    f2.writelines(new_data)
    else:
        with open(filename, 'w') as new_file:
            new_data = json.dumps(numbers)
            new_file.writelines(new_data)


def read_file(filename: str, user: str):
    with open(filename, 'r') as file:
        data = json.load(file)
        return sum(data[user])
