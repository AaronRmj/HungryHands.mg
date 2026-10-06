from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.routers import mission, users


app = FastAPI()
app.include_router(mission.router)
app.include_router(users.router)
