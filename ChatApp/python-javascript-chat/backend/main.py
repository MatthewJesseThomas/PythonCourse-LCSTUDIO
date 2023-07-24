from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PRIVATE_KEY = "7cc3f081-8467-407a-9161-81a673153a08"


class User(BaseModel):
    username: str


@app.post('/authenticate')  # Change to POST instead of GET
async def authenticate(user: User):
    response = requests.put('https://api.chatengine.io/users/',
        data={
            "username": user.username,
            "secret": user.username,
            "first_name": user.username
        },
        headers={"Private-Key": PRIVATE_KEY}
    )
    return response.json()


@app.get('/')  # Define a handler for the root endpoint
async def root():
    return {"message": "Hello, welcome to the API!"}
