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


db_mission: list[Mission] = [
    Mission(
        id=1,
        titre="Aide sans abris",
        description="La mission consistera a aider les pauvres du quartier anosizato",
        lieu = "anosizato",
        date = "2026-10-04T08:00:00",
        nb_place = 30
    ),
    Mission(
        id=2,
        titre="Visite pere pedro",
        description="Distribution de repas a pere pedro",
        lieu = "bypass",
        date = "2026-10-04T08:00:00",
        nb_place = 40
    ),

]
