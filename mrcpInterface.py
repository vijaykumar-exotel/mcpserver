from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/prompt")
def read_item( q: str = None):
    return { "q": q}
    