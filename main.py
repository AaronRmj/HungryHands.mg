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
        User(id= 1, pseudo= "kirito", nom="kirigaya", prenom = "ego", age=14),
        User(id= 2, pseudo= "kaneki", nom="ken", prenom= "feu", age=22)
]


#creer un nouveau benevole
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

@app.get("/users", response_model=list[User], status_code=200)
def get_all_user():
        return db_user

#specific user
@app.get("/users/{user_id}")
def get_user(user_id: int):
        for user in db_user:
                if user.id == user_id:
                        return user



#modifier un benevole
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserUpdate):
        for user in db_user:
                if user.id == user_id:

                        if user_update.pseudo is not None:
                                user.pseudo = user_update.pseudo
                        if user_update.age is not None: 
                                user.age = user_update.age
                        if user_update.nom is not None:
                                user.nom = user_update.nom
                        if user_update.prenom is not None:
                                user.prenom = user_update.prenom
                return user
        raise HTTPException(status_code=400, detail="Erreur lors de la modification")


@app.delete("/users/{user_id}", status_code=200)
def delete_user(user_id: int):

        # on doit uliliser global pour modifier une variable globale
        global db_user

        # valeur de retour user, pour chq user dans db on parcours et creer une nouvelle liste sans l'user_id entré en params
        db_user = [user for user in db_user if user.id != user_id]
        return {"message": "Utilisateur supprimé"}
        raise HTTPException(status_code=400, detail="Erreur lors de la suppression")
