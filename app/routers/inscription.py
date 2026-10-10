from app.models import InscriptionCreate, Inscription
from fastapi import APIRouter, HTTPException
from app.database import db_mission, db_user, db_inscription
from datetime import datetime

router = APIRouter(prefix="/mission", tags=["inscription"])
@router.post("/{mission_id}/inscription", status_code=201)

#user_id et mission_id no avy amin ny client
def inscrire(mission_id: int, data: InscriptionCreate):

    #verifier si la mission existe
    mission = None
    for m in db_mission:

        #izany hoe hita anaty bd ilay mission (existe)
        if m.id == mission_id:
            mission = m 
            break

    #izany hoe ra tsy miexsite le mission
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
    #comparena ny user_id et mission_id ra micorrespondonre anatinle base

    
    for ligne in db_inscription:
        if mission_id == ligne.mission_id and data.user_id == ligne.user_id:
            deja_inscrit = True
            raise HTTPException(status_code=409, detail="L'Utilisateur est déja inscrit a cette mission")



    # verifier si nombre de places tjr dispo
    cpt = 0
    for ligne in db_inscription:
        if mission_id == ligne.mission_id:
            cpt +=1 

    if cpt >= mission.nb_place:
        raise HTTPException(status_code=400, detail="Limite nombre de places atteintes")
            


    # apres verification on va creer le nouvel inscription
    new_id = max((i.id for i in db_inscription), default=0) + 1
    inscription = Inscription(
        id = new_id,
        user_id = data.user_id,
        mission_id = mission_id,
        date_inscription= datetime.now()
    )

    db_inscription.append(inscription)

    return {"message": "Inscription reussit", "inscription": inscription}