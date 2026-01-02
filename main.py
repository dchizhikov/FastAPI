from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import os

app = FastAPI()

# HTML главная страница
login_page = """
<!DOCTYPE html>
<html>
<head><title>My App</title></head>
<body>
    <h1>Hello FastAPI!</h1>
    <p><a href="/docs">Swagger</a></p>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)(lambda: login_page)
@app.get("/health")(lambda: {"status": "healthy"})
@app.post("/echo")(lambda request: JSONResponse({"echo": request.json()}))
@app.get("/items/{item_id}")(lambda item_id, q=None: {"item_id": item_id, "q": q})

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
