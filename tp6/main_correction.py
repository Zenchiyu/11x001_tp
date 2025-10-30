
from utils import exercice

#
# EXERCICE 1
#

class Voiture:

    def __init__(self, marque, couleur, kilometrage=10000):

        self.marque = marque
        self.couleur = couleur
        self.kilometrage = kilometrage

    def __str__(self):
        text = "Voici ma voiture\n"
        text += f"Marque: {self.marque}\n"
        text += f"Couleur: {self.couleur}\n"
        text += f"Kilométrage: {self.kilometrage:.2f} km\n"
        return text
    
    def avancer(self, vitesse, temps):
        print("La voiture avance.")
        distance = vitesse * temps / 1000
        self.kilometrage += distance
        print(f"Nouveau kilométrage: {self.kilometrage:.2f} km\n")

    def avancer_2(self, vitesse, temps):
        print("La voiture avance.")
        distance = f_dist(vitesse, temps)
        self.kilometrage += distance
        print(f"Nouveau kilométrage: {self.kilometrage:.2f} km\n")

f_dist = lambda vitesse, temps: vitesse*temps/1000 if temps >= 0 else 0


@exercice
def exercice1():
    # ******************** Votre code ci-dessous ********************
    v = Voiture(marque='Toyota',
                couleur='blanche',
                kilometrage=25000
                )
    print(v)
    v.avancer(vitesse=50/3.6, temps=20*60)
    # v.avancer_2(vitesse=50/3.6, temps=20*60)
    print(v)
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice2():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice3():
    import random
    random.seed(0)
    a = [random.randrange(0, 100) for _ in range(1000)]
    # ******************** Votre code ci-dessous ********************
    # Méthode 1: avec liste
    # b = []
    # for element in a:
    #     if element not in b:
    #         b.append(element)
    #     else:
    #         pass

    # Méthode 2: avec set
    b = list(set(a))

    # Retirer les nombres pairs de b
    pairs = set(range(0,100,2))
    c = list(set(b) - pairs)

    print(f"Liste initiale:\n{a}\n")
    print(f"Liste sans doublon:\n{b}\n")
    print(f"Liste sans nombre pair:\n{c}\n")
    print(len(a), len(b), len(c))
    # ******************** Votre code ci-dessus *********************


if __name__ == "__main__":
    # Astuce : commenter tous les exercices sauf celui en cours pour gagner du temps !
    exercice1()
    exercice2()
    exercice3()
