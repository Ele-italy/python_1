from fastapi import FastAPI, Request
from pydantic import BaseModel


app = FastAPI()
    
@app.put("/task/{age}")
async def handler(age:int):
    if age < 0:
        r = f"Вы ввели неверный возраст"
    elif age < 18:
        r = f"CocaCola"
    else:
        r = f"Beer"
    return {"result":r}
   










