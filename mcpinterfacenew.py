from fastapi import FastAPI
import openaitest
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
import subprocess

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


@app.get("/call")
async def read_item(q: str | None = None):
    number = "07411179773"
    url = f"https://399117e47411d9f0f9120de1181323056e55b88c664d2f67:80711a9d4562955dc3591f1ada24790f3b5088dbaa3263db@api.in.exotel.com/v1/Accounts/ameyo5m/Calls/connect.json?From=sip:saurabhsf258cafa&To={number}&CallerId=02247788868"
    headers = {
        'Authorization': 'Basic e3tBdXRoS2V5fX06e3tBdXRoVG9rZW59fQ==',
        'Content-Type' : 'application/json'
    }
    #response = requests.request("POST", url, headers=headers)
    headers = ["-H", "Content-Type: application/json"]
    result = subprocess.run(
        ["curl", "-s", "-X", "POST", url] + headers ,
        capture_output=True,
        text=True
    )
    return {"status": "success"}
