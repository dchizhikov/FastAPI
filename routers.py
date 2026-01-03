def root():
    return {"message": "Hello World!"}

def health():
    return {"status": "healthy"}

async def echo(data):
    return JSONResponse({"echo": data})
