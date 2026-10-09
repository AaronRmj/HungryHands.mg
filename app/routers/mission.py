from fastapi import APIRouter, HTTPException
from app.models import Mission, MissionCreate, MissionUpdate
from app.database import db_mission
#definition route mission 
router = APIRouter(prefix="/missions", tags=["missions"])


#prefix pour eviter d'ecrire mission a chaque fois, juste ""

@router.post("/", response_model=Mission, status_code=201)
def create_mission(mission: MissionCreate):
    new_id = max([m.id for m in db_mission], default=0) + 1
    new_mission = Mission(
        id = new_id,
        titre = mission.titre,
        description = mission.description,
        lieu = mission.lieu,
        date = mission.date,
        nb_place = mission.nb_place
    )

    db_mission.append(new_mission)
    return new_mission

#retourner tous les missions
@router.get("/", response_model=list[Mission])
def get_all_mission():
    return db_mission

#rechecher une mission
@router.get("/{mission_id}", response_model=Mission)
def get_mission(mission_id: int):
    for mission in db_mission:
        if mission.id == mission_id:
            return mission
    
    raise HTTPException(status_code=400, detail="Mission introuvable")

@router.put("/{mission_id}", response_model=Mission)
def update_mission(mission_id: int, mission_update: MissionUpdate):
    for mission in db_mission:
        if mission.id == mission_id:
            if mission_update.titre is not None:
                mission.titre = mission_update.titre
            if mission_update.description is not None:
                mission.description = mission_update.description
            if mission_update.lieu is not None:
                mission.lieu = mission_update.lieu
            if mission_update.date is not None:
                mission.date = mission_update.date
            if mission_update.nb_place is not None:
                mission.nb_place = mission_update.nb_place

            print("Modification reussit")
            return mission

    raise HTTPException(status_code=400, detail="Mission introuvable")


@router.delete("/{mission_id}", response_model=Mission)
def delete_mission(mission_id: int):
    for mission in db_mission:
        if mission.id == mission_id:
            db_mission.remove(mission)
            return {"message": "Mission supprimé"}

    raise HTTPException(status_code=400, detail="Problème rencontré")