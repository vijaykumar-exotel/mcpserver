from fastapi import FastAPI
import openaitest
app = FastAPI()


@app.get("/prompt")
async def read_item(q: str | None = None):
    if q:
        data = await openaitest.execute()
        return {"status": "sucess", "data": data}
    return {"status": "failed"}

