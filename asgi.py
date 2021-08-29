from fastapi import Body
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.responses import Response
from users import gen_random_name
from users import get_user
from util import apply_cache_headers
from util import static_response

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def _(response: Response):
    apply_cache_headers(response)

    return static_response("index.html", response_cls=HTMLResponse)


@app.get("/img", response_class=Response)
async def _(response: Response):
    apply_cache_headers(response)

    return static_response("image.jpg", binary=True)


@app.get("/js", response_class=Response)
async def _(response: Response):
    apply_cache_headers(response)

    return static_response("index.js")



@app.post("/task/4")
async def _(request: Request, response: Response, data: str = Body(...)):
    user = get_user(request) or gen_random_name()
    response.set_cookie("user", user)