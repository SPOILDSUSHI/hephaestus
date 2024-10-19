from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")


@app.get("/")
async def index(request: Request) -> HTMLResponse:
    """Index endpoint

    Returns:
        HTMLResponse: returns base webpage.
    """
    return templates.TemplateResponse(request=request, name="base.html")
