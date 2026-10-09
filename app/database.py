# ici on met la connexion avec la base de données
from app.models import User, Mission, Inscription
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


db_user: list[User] = [
                User(id= 1, pseudo= "kirito", nom="kirigaya", prenom = "ego", age=14),
                User(id= 2, pseudo= "kaneki", nom="ken", prenom= "feu", age=22)
]

db_inscription : list[Inscription] = [
    Inscription(
        id = 1,
        user_id = 2,
        mission_id = 2
    ),
    Inscription(
        id = 2,
        user_id = 1,
        mission_id = 2,
    ),
    Inscription(
        id = 3,
        user_id = 3,
        mission_id = 2
    )
]