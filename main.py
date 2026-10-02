from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 


app = FastAPI()

@app.get("/test")
def test():
        return {"message": "API opérationnel"}