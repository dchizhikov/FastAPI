from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

def root():
    return {"message": "Hello World!"}

def health():
    return {"status": "healthy"}

def echo(data):
    return JSONResponse({"echo": data})

app.get("/")(root)
app.get("/health")(health)
app.post("/echo")(echo)
