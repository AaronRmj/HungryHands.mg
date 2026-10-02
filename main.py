from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

@app.get("/test")
def test():
        return {"message": "API opérationnel"}


class User(BaseModel):
        id: int
        pseudo: str
        nom: str
        prenom: str
        age: int


class UserCreate(BaseModel):
        pseudo: str
        nom: str
        prenom: str
        age: int


class UserUpdate(BaseModel):
        pseudo: str
        nom: str
        prenom: str
        age: int


db_user: list[User] = [
        User(id= 0, pseudo= "kirito", nom="kirigaya", prenom = "ego", age=14),
        User(id= 1, pseudo= "kaneki", nom="ken", prenom= "feu", age=22)
]

@app.post("/users", response_model=User, status_code=200)
def create_user(benevole: UserCreate):
        new_id = max([u.id for u in db_user], default=0) + 1
        new_user = User (
                id = new_id,
                pseudo = benevole.pseudo,
                nom = benevole.nom,
                prenom = benevole.prenom,
                age = benevole.age
        )
        db_user.append(new_user)
        print("User crée avec succès")
        return new_user

@app.get("/users", response_model=list[User])
def get_all_user():
        return db_user