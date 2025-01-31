# Based on https://fastapi.tiangolo.com/advanced/templates/#using-jinja2templates

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=PlainTextResponse)
async def hello(name: str="anon"):
    return f"Hello {name}"

@app.get("/hellojson/", response_class=JSONResponse)
async def hellojson(name: str):
    return {"Received": name,
            "Response": f"Hello {name}"}

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )

@app.get("/sumtwo/", response_class=HTMLResponse)
async def sumtwo(request: Request, a: int = 0, b: int = 10):
    return templates.TemplateResponse(
        request=request, name="sumtwo.html", context={"a": a, "b":b}
    )
