import os
import json
from pathlib import Path
from collections import defaultdict
from fastapi import FastAPI, Request, Response, Body


def gen_random_name():
    return os.urandom(16).hex()


def get_user(request: Request):
    return request.cookies.get("user")


def write_file(filename: str, numbers: dict, user: str):
    file_path = Path(filename)
    if not file_path.is_file():
        with open(filename, 'w') as new_file:
            new_data = json.dumps(numbers)
            new_file.writelines(new_data)
    else:
        with open(filename, 'r') as file:
            old_data = json.load(file)
            with open(filename, 'w') as f1:
                if user in old_data.keys():
                    old_data[user] += numbers[user]
                    new_data = json.dumps(old_data)
                    f1.writelines(new_data)
                else:
                    old_data[user] = numbers[user]
                    new_data = json.dumps(old_data)
                    f1.writelines(new_data)


def read_file(filename: str, user: str):
    with open(filename, 'r') as file:
        data = json.load(file)
        return sum(data[user])

app = FastAPI()

@app.post('/add_number')
async def handler(request: Request, response: Response, data: str = Body(...)):
    filename = "save_cookies.txt"
    numbers = defaultdict(list)
    user = get_user(request) or gen_random_name()
    response.set_cookie("user", user)
    if data == "stop":
        return read_file(filename, user)
    else:
        assert data.isdigit()
         numbers[user].append(int(data))
        write_file(filename, numbers, user)
        return {"Введеное число": numbers[user]}

    
 
