
from fastapi import FastAPI
from pydantic import BaseModel

class Names(BaseModel):
    first_name: str
    last_name: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "pipe es feo"}


@app.get("/say-name/{name}")
async def say_name(name: str):
    return {"message": f"hello {name}"}


@app.post("/say-names/")
async def say_names(names: Names):
    return names