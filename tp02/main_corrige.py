import random

from utils import exercice

#
# EXERCICE 1
#

@exercice
def exercice1():
    # ******************** Votre code ci-dessous ********************
    age = int(input("Entrez l'âge du patient: "))
    # fumeur = bool(int(input("Entrez 1 si le patient fume, sinon 0: ")))
    if age < 30:
        print("Peu de risque")
    else:
        fumeur = bool(int(input("Entrez 1 si le patient fume, sinon 0: ")))
        if fumeur:
            print("Grand risque")
        else:
            print("Peu de risque")
    
    # Une seconde version possible (autre possible)
    age = int(input("Entrez l'âge du patient: "))
    fumeur = bool(int(input("Entrez 1 si le patient fume, sinon 0: ")))
    if (age < 30 or not fumeur):
        print("Peu de risque")
    else:   # La négation donne: age >= 30 et fumeur
        print("Grand risque")

    # ******************** Votre code ci-dessus *********************

@exercice
def exercice2():
    # ******************** Votre code ci-dessous ********************
    x = 40      # TODO: Vous pouvez changer ici
    if x != 42:
        print("Not 42")
    if x != 42:
        print("Not 42")
    else:
        print("42")
    
    print("-------------------")
    if x != 42:
        print("Not 42")
    elif x != 42:
        print("Not 42")
    else:
        print("42")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice3():
    # ******************** Votre code ci-dessous ********************
    for i in range(5):
        for j in range(4):
            print(i, j)
        break   # TODO: Testez d'enlever cela, de le déplacer et aussi tester de rajouter continue ou même d'autres print
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice4():
    # ******************** Votre code ci-dessous ********************
    a = list(range(10, 20 + 1, 2)) 
    b = []
    for el in a:
        b.append(el**2) # pas ^2 !!
    print(b)
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice5():
    # ******************** Votre code ci-dessous ********************
    ma_liste = list(range(10, 20 + 1, 2)) 
    for i in range(len(ma_liste)):
        ma_liste[i] = ma_liste[i]**2 # pas ^2 !!
    print(ma_liste)
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice6():
    # ******************** Votre code ci-dessous ********************
    a = list(range(0, 9 + 1))
    b = a
    for i in range(len(a)):
        a[i] = a[i]**2 # pas ^2 !!
    print(a)
    print(b)
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice7():
    # ******************** Votre code ci-dessous ********************
    txt = "The quick brown fox jumps over the lazy dog <END>"
    seq = txt.split()
    print(seq)
    input_sequence = seq[:-1]
    target_sequence = seq[1:]
    print(input_sequence)
    print(target_sequence)
    # ******************** Votre code ci-dessus *********************

def somme_liste(liste):
    if len(liste) == 1:
        return liste[0]
    return liste[0] + somme_liste(liste[1:])

@exercice
def exercice8():
    # ******************** Votre code ci-dessous ********************
    liste = [1, 2, 3, 4]
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
