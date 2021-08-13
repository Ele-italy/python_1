from fastapi import FastAPI, Request
from pydantic import BaseModel
from task_3_6 import drink


app = FastAPI()


@app.get("/task/{a}")
async def handler(a:int):
    r = drink(a)
    return {"result":str(r)}
   










