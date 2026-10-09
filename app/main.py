from fastapi import FastAPI, HTTPException
from app.routers import mission, users, inscription


app = FastAPI()
app.include_router(mission.router)
app.include_router(users.router)
app.include_router(inscription.router)

@app.get("/test")
def test():
    return {"message": "API fonctionel"}