from fastapi import FastAPI
from enum import Enum
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Agent(BaseModel):
    name: str
    description: Union[str, None] = None

class AgentName(str, Enum):
    jett = "jett"
    sova = "sova"
    sage = "sage"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/items/")
async def createAgent(agent: Agent):
    return agent

@app.get("/agents/{agent_id}")
async def agents(agent_id: AgentName):
    if agent_id is AgentName.jett:
        return {"agent_id": agent_id, "message": "Watch Out!"}

    if agent_id.value == "sova":
        return {"agent_id": agent_id, "message": "Recon!"}

    return {"agent_id": agent_id, "message": "For you!"}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
