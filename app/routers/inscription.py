from app.models import InscriptionCreate
from fastapi import APIRouter, HTTPException
from app.database import db_mission, db_user

router = APIRouter(prefix="/missions", tags=["inscriptions"])

@router.post("/{mission_id}/inscriptions")

# mission_id sy user_id no avaty am client refa anao inscriptions
def inscrire(mission_id: int, data: InscriptionCreate):

    # verifier que la mission existe
    mission = None
    for m in db_mission:
        if m.id == mission_id:
            mission = m 
            break
    if mission is None:
        raise HTTPException(status_code=404, detail="Mission introuvable")

    # verifier que user existe
    user = None
    for u in db_user:
        if u.id == data.user_id:
            user = u
            break
    if user is None:
        raise HTTPException(status_code=404, detail="Mission introuvable")


    