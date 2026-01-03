from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from html_templates import login_page
from routers import *

app = FastAPI()

#app.get("/")(root)
app.get("/", response_class=HTMLResponse)(lambda: login_page)
app.get("/health")(health)
app.post("/echo")(echo)
