from fastapi import APIRouter, HTTPException
from app.models import Mission, MissionCreate, MissionUpdate
from app.database import db_mission

#definition route mission 
router = APIRouter(prefix="/missions", tags=["missions"])

@router.post("", response_model=Mission, status_code=200)
def create_mission(mission: MissionCreate):
    new_id = max([m.id for m in db_mission], default=0) + 1
    new_mission = Mission(
        id = new_id,
        titre = mission.titre,
        desciption = mission.description,
        lieu = mission.lieu,
        date = mission.date,
        nb_place = mission.nb_place
    )

    db_mission.append(new_mission)
    return new_mission


