from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os

app = FastAPI(title="My API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Hello World!", "status": "ok"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": "2026-01-02"}

@app.post("/echo")
async def echo(request: Request):
    data = await request.json()
    return JSONResponse({"echo": data, "received": True})

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
