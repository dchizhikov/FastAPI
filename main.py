from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from html_templates import login_page

app = FastAPI()

def root():
    return {"message": "Hello World!"}

def health():
    return {"status": "healthy"}

async def echo(data):
    return JSONResponse({"echo": data})

#app.get("/")(root)
app.get("/", response_class=HTMLResponse)(lambda: login_page)
#app.get("/health")(health)
#app.post("/echo")(echo)
