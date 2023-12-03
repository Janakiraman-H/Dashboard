from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/links", response_class=HTMLResponse)
async def get_links(request: Request):
    external_links = [
        {"name": "Link 1", "url": "https://example.com/link1"},
        {"name": "Link 2", "url": "https://example.com/link2"},
        {"name": "Link 3", "url": "https://example.com/link3"},
    ]
    return templates.TemplateResponse("links.html", {"request": request, "links": external_links})
