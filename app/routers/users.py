from fastapi import FastAPI, HTTPException, APIRouter
from app.models import User, UserCreate, UserUpdate
from app.database import db_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/test")
def test():
        return {"message": "API opérationnel"}


#creer un nouveau benevole
@router.post("/users", response_model=User, status_code=200)
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

@router.get("/users", response_model=list[User], status_code=200)
def get_all_user():
        return db_user

#specific user
@router.get("/users/{user_id}")
def get_user(user_id: int):
        for user in db_user:
                if user.id == user_id:
                        return user
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")


#modifier un benevole
@router.put("/users/{user_id}", response_model=User)
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


@router.delete("/users/{user_id}", status_code=200)
def delete_user(user_id: int):
        for user in db_user:
                if user.id == user_id:
                        db_user.remove(user)
                        return {"message": "Utilisateur supprimé"}
        raise HTTPException(status_code=404, detail="User Non trouvé")

