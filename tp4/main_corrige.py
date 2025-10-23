import random

from utils import exercice
import math

#
# EXERCICE 1
#
def tri(ma_liste):  # fonction à un seul argument
    # Fonction présente dans la correction du TP3
    n = len(ma_liste)
    for i in range(0, n - 1):   # i va jusqu'à n - 2
        k = i
        for j in range(i + 1, n):   # i va jusqu'à n - 1
            if ma_liste[j] < ma_liste[k]:
                k = j
        
        if k != i:
            # Swap/échange. En Python, on peut le faire en une ligne
            ma_liste[i], ma_liste[k] = ma_liste[k], ma_liste[i]

def rechercheSimple(nombre, ma_liste):
    # Cette fonction peut traverser toute la liste
    for i, el in enumerate(ma_liste):
        if el == nombre:
            return i
    return -1

def rechercheDichotomique(nombre, ma_liste):
    tri(ma_liste)   # Pas besoin si ma_liste est déjà triée
    # Si on suppose que c'est déjà triée,
    # cette fonction évite de traverser toute la liste
    start = 0
    end = len(ma_liste) - 1
    while start < end-1:
        mid = (start + end) // 2
        valeur = ma_liste[mid]

        if valeur == nombre:
            return mid
        elif valeur < nombre:
            start = mid
        else: # valeur > nombre
            end = mid
    return -1

@exercice
def exercice1(nombre, ma_liste):
    # ******************** Votre code ci-dessous ********************
    print(rechercheDichotomique(nombre, ma_liste))
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice2():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice3():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

def somme_liste(liste):
    # Fonction présente dans la correction du TP2
    if len(liste) == 1:
        return liste[0]
    return liste[0] + somme_liste(liste[1:])

def moyenne(liste):
    # return sum(liste) / len(liste)
    return somme_liste(liste) / len(liste)

@exercice
def exercice4():
    # ******************** Votre code ci-dessous ********************
    print(moyenne([1, 2, 3, 4])) 
    # ******************** Votre code ci-dessus *********************

def dot_product(liste1, liste2):
    # la fonction `somme_liste` doit être appelée
    produit = []
    for i in range(len(liste1)):
        produit.append(liste1[i] * liste2[i])
    dot_product = somme_liste(produit)
    return dot_product

@exercice
def exercice5(liste1, liste2):
    # ******************** Votre code ci-dessous ********************
    assert len(liste1) == len(liste2), "Les listes doivent être de même taille"
    print(dot_product(liste1, liste2))
    # ******************** Votre code ci-dessus *********************

def moyenne_ponderee(liste_valeur, liste_poids):
    # les fonctions prédédantes doivent être appelées
    numerateur = dot_product(liste_valeur, liste_poids)
    denominateur = somme_liste(liste_poids)
    return numerateur / denominateur

@exercice
def exercice6(liste_valeur, liste_poids):
    # ******************** Votre code ci-dessous ********************
    assert len(liste_valeur) == len(liste_poids), "Les listes doivent être de même taille"
    print(moyenne_ponderee(liste_valeur, liste_poids))
    # ******************** Votre code ci-dessus *********************

def somme_complexe(z1, z2):
    assert len(z1) == len(z2) == 2
    z3 = [z1[0] + z2[0], z1[1] + z2[1]]
    print(f"z1+z2 = {z3[0]} + i*({z3[1]})")
    return

def conjugue(z1):
    assert len(z1) == 2
    z1_conj = [z1[0], -z1[1]]
    print(f"z_conj = {z1_conj[0]} + i*({z1_conj[1]})")
    return

def module(z1):
    assert len(z1) == 2
    mod = math.sqrt(z1[0]**2 + z1[1]**2)    # Pouvez aussi écrire puissance 1/2 pour racine carrée
    print(f"|z| = {mod:.3f}")
    return

def argument(z1):
    assert len(z1) == 2
    arg = math.atan(z1[1] / z1[0])
    print(f"arg(z) = {arg:.3f}")
    return

@exercice
def exercice7(z1, z2):
    # ******************** Votre code ci-dessous ********************
    print(f"{z1 = }, {z2 = }\n")
    somme_complexe(z1, z2)
    conjugue(z1)
    conjugue(z2)
    module(z1)
    module(z2)
    argument(z1)
    argument(z2)
    # ******************** Votre code ci-dessus *********************

def matmul(matrice, vecteur):
    resultat = []
    for ligne in matrice:
        resultat.append(dot_product(ligne, vecteur))
    return resultat

@exercice
def exercice8(matrice, vecteur):
    # ******************** Votre code ci-dessous ********************
    print(matmul(matrice, vecteur))
    # ******************** Votre code ci-dessus *********************


if __name__ == "__main__":
    # Astuce : commenter tous les exercices sauf celui en cours pour gagner du temps !
    import random
    random.seed(42)
    ma_liste = [random.randrange(100) for _ in range(20)]   # 20 nombres
    ma_liste2 = [random.randrange(100) for _ in range(20)]   # 20 nombres

    exercice1(11, ma_liste)
    exercice2()
    exercice3()
    exercice4()
    exercice5(ma_liste, ma_liste2)
    notes = [10, 15, 19, 6]
    coef = [1, 2, 0.5, 0.5]
    exercice6(notes, coef)
    z1 = [1, 3]
    z2 = [4, -5]
    exercice7(z1, z2)
    matrice = [[1,2,3], [4,5,6], [7,8,9]]
    vecteur = [1,1,1]
    exercice8(matrice, vecteur)
