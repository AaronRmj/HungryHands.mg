from app.models import InscriptionCreate
from fastapi import APIRouter, HTTPException
from app.database import db_mission, db_user

router = APIRouter(prefix="mission", tags=["inscription"])
@router.post("/{mission_id}/inscription", status_code=200)

#user_id et mission_id no avy amin ny client
def inscrire(mission_id: int, data: InscriptionCreate):

    #verifier si la mission existe
    mission = None
    for m in db_mission:

        #izany hoe hita anaty bd ilay mission (existe)
        if m.id == mission_id:
            mission = m 
            break

    #izany hoe 
    if mission is None:
        raise HTTPException(status_code=404, detail="La mission n'existe pas")

    #verifier si le user concerné existe

    user = None
    for u in db_user:
        if u.id == data.user_id:
            user = u
            break

    #ra tsy ao ilay user
    if user is None:
        raise HTTPException(status_code=400, detail="Utilisateur non existant")


    # verifier que non inscrit 




    # verifier si nombre de places tjr dispo