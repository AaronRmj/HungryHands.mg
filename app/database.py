# ici on met la connexion avec la base de données
from models import User, Mission
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
