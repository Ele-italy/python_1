from fastapi import FastAPI
from my_function import main
import useful_fun


app = FastAPI()


@app.get("/distance/{a}/{b}")
async def handler (a:str, b:str ):
    r = main(a, b)
    return {"result":str(r)}

@app.post('/add_number')
async def handler(request: Request, response: Response, data: str = Body(...)):
    filename = "Numbers.txt"
    numbers = defaultdict(list)
    user = useful_fun.get_user(request) or useful_fun.gen_random_name()
    response.set_cookie("user", user)
    if data == "stop":
        return request.cookies.read_file(filename, user)
    else:
        assert data.isdigit()
        numbers[user].append(int(data))
        useful_fun.write_file(filename, numbers, user)
        return {"Введеное число": numbers[user]}
   










