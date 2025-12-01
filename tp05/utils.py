import os
from pprint import pprint
import random


LISTE_PRENOMS = ["JADE", "LOUISE", "EMMA", "ALICE", "AMBRE", "LINA", "ROSE", "CHLOÉ", "MIA", "LÉA", "LÉO", "GABRIEL", "RAPHAËL", "ARTHUR", "LOUIS", "JULES", "ADAM", "MAËL", "LUCAS", "HUGO"] 
LISTE_PRENOMS = [p.lower().capitalize() for p in LISTE_PRENOMS]
# source : prenoms les plus données en France  en 2020 https://www.insee.fr/fr/statistiques/3532172

# Decorator to print a header before an exercice. 
# Makes the assumption that function name is exerciceX
def exercice(func):
    def wrapper():
        n = func.__name__.split("exercice")[-1]
        s = f"##### EXERCICE {n} #####"
        h = "#" * len(s)
        header = h + "\n" + s + "\n" + h + "\n"
        os.system("clear")
        print(header)        
        func()
        print("\n\n")
        input("--> Appuyer sur 'Entrée' pour passer à l'exercice suivant")
    return wrapper

def generer_resultats(afficher=True):
    nb_etudiants = len(LISTE_PRENOMS)
    nb_cours = random.randint(2, 5)
    resultats = []
    for _ in range(nb_cours):
        nb_eleves = random.randint(3, nb_etudiants)
        prenoms_eleves = random.sample(LISTE_PRENOMS, nb_eleves)
        notes = {prenom: random.randint(1, 6) for prenom in prenoms_eleves}
        resultats.append(notes)
    if afficher:
        print(f"{len(resultats)} cours différents :")
        for i, notes in enumerate(resultats):
            print(f"\nCours n°{i + 1} : {len(notes)} participants.\n")
            pprint(notes)
    return resultats