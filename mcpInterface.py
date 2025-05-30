from fastapi import FastAPI
import mcp_client
app = FastAPI()


@app.get("/prompt")
async def read_item(q: str | None = None):
    if q:
        data = await mcp_client.execute()
        return {"status": "sucess", "data": data}
    return {"status": "failed"}

