import random

from utils import exercice

#
# EXERCICE 1
#

@exercice
def exercice1():
    # ******************** Votre code ci-dessous ********************
    print("Bonjour monde !")
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
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice5():
    PI = 3.1415926535
    rayon = int(input("Entrer le rayon du cercle (en m) : "))   # int(.) fait une conversion de type vers int
    # ******************** Votre code ci-dessous ********************
    
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice6():
    nb_of_days = int(input("Entrez un nombre de jours à convertir : "))
    # ******************** Votre code ci-dessous ********************
    
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice7():
    a = 7
    b = 2
    c = 7 // 2  # Ne modifier que cette ligne
    d = 7 % 2   # L'opérateur % est le "modulo", aussi écrit "mod" en maths
    print(f"{a} / {b} = {c:.2f}, reste = {d}")

@exercice
def exercice8():
    n = int(input("Entrez un entier strictement supérieur à 1: "))
    # ******************** Votre code ci-dessous ********************
    
    # ******************** Votre code ci-dessus *********************

if __name__ == "__main__":
    # Astuce : commenter tous les exercices sauf celui en cours pour gagner du temps !
    exercice1()
    exercice2()
    exercice3()
    exercice4()
    exercice5()
    exercice6()
    exercice7()
    exercice8()
