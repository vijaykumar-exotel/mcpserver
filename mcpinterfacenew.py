from fastapi import FastAPI
import openaitest
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <- allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # <- allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # <- allows all headers
)

@app.get("/prompt")
async def read_item(q: str | None = None):
    if q:
        data = await openaitest.execute(q)
        return {"status": "sucess", "data": data}
    return {"status": "failed"}

