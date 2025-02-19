# Based on https://fastapi.tiangolo.com/advanced/templates/#using-jinja2templates

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=PlainTextResponse)
async def hello(name: str="anon"):
    return f"Hello {name}"

@app.get("/fruits/{fruit}", response_class=JSONResponse)
async def fruit(fruit: str):
    with open("fruits.txt") as f:
        fruits = f.readlines()
    fruits = [fruit.strip() for fruit in fruits]
    return fruit in fruits

@app.get("/sumtwo/", response_class=HTMLResponse)
async def sumtwo(request: Request, a: int, b: int):
    print(request.headers)
    summen = a + b
    return templates.TemplateResponse(
        request=request, name="sumtwo.html", context={"a": a, "b": b, "summen": summen}
    )

@app.get("/hellojson/", response_class=JSONResponse)
async def hellojson(name: str):
    return {"Received": name,
            "Response": f"Hello {name}"}

@app.get("/items/{id}", response_class=HTMLResponse)
async def enkel_template(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )