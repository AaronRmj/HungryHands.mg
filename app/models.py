from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Mission(BaseModel):
    id: int
    titre: str
    description: str
    lieu: str
    date: datetime
    nb_place: int

class MissionCreate(BaseModel):
    titre: str
    description: str
    lieu: str
    date: datetime
    nb_place: int

class MissionUpdate(BaseModel):
    titre: Optional[str] = None
    description: Optional[str] = None
    lieu: Optional[str] = None
    date: Optional[datetime] = None
    nb_place: Optional[int] = None


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
        pseudo: Optional[str] = None
        nom: Optional[str] = None
        prenom: Optional[str] = None
        age: Optional[int] = None


# id fotsiny no ilaina satria efa miexiste ilay user
# c est comme emprunt livre librairie
class InscriptionCreate(BaseModel):
    user_id: int

# si je veux afficher j'utilise cette classe
class Inscription(BaseModel):
      id: int 
      user_id: int
      mission_id: int

    