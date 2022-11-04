from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class AgentName(str, Enum):
    jett = "jett"
    sova = "sova"
    sage = "sage"


@app.get("/")
async def root():
    return {"message": "Hello World"}

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
