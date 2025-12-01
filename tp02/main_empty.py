import random

from utils import exercice

#
# EXERCICE 1
#

@exercice
def exercice1():
    # ******************** Votre code ci-dessous ********************
    pass
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

@exercice
def exercice4():
    # ******************** Votre code ci-dessous ********************
    # liste = [i for i in range(10, 21, 2)]
    liste = list(range(10, 21, 2))
    resultat = []
    for element in liste:
        resultat.append(element**2)
    print(resultat)
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice5():
    # ******************** Votre code ci-dessous ********************
    liste = list(range(10, 21, 2))
    for i in range(len(liste)):
        liste[i] = liste[i] ** 2
    print(liste)
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice6():
    # ******************** Votre code ci-dessous ********************
    a = list(range(0,10,1))
    b = a
    for i in range(len(a)):
        a[i] = a[i] ** 2
    print(f"Liste A: {a}")
    print(f"Liste B: {b}")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice7():
    # ******************** Votre code ci-dessous ********************
    chaine = "The quick brown fox jumps over the lazy dog <END>"
    liste = chaine.split(" ")
    print(liste)
    input_sequence = liste[:-1]
    target_sequence = liste[1:]
    print(f"Input_sequence: {input_sequence}")
    print(f"Target_sequence: {target_sequence}")
    # ******************** Votre code ci-dessus *********************

def somme_liste(liste):
    if len(liste) == 1:
        return liste[0]

    return liste[0] + somme_liste(liste[1:])  

@exercice
def exercice8():
    # ******************** Votre code ci-dessous ********************
    liste = list(range(0,5))
    print(somme_liste(liste))
    # ******************** Votre code ci-dessus *********************

if __name__ == "__main__":
    # Astuce : commenter tous les exercices sauf celui en cours pour gagner du temps !
    # exercice1()
    # exercice2()
    # exercice3()
    # exercice4()
    # exercice5()
    # exercice6()
    # exercice7()
    exercice8()
