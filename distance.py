from fastapi import FastAPI, Request
from my_function import main


app = FastAPI()

@app.get("/")
async def handler ():
    return "hello world"

@app.get("/distance/{a}/{b}")
async def handler (a:str, b:str ):
    r = main(a, b)
    return {"result":str(r)}
   










