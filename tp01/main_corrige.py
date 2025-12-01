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
    print("Nom     : Michel LAMBDA\n")
    print("Né le   : 31.10.2001\n")
    print("Contact : michel.lambda@unige.ch\n")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice3():
    # ******************** Votre code ci-dessous ********************
    c1 = "U"
    c2 = "N"
    c3 = "I"
    c4 = "G"
    c5 = "E"
    
    print(f"A l'envers, {c1 + c2 + c3 + c4 + c5} s'écrit {c5 + c4 + c3 + c2 + c1}.")

    # ******************** Votre code ci-dessus *********************

@exercice
def exercice4():
    # ******************** Votre code ci-dessous ********************
    nombre = input("Entrez un nombre entre 0 et 9 inclus: ")
    if not nombre.isnumeric():
        print("Il fallait rentrer un nombre")
    elif int(nombre) not in list(range(0, 9 + 1)):
        print("Il fallait rentrer un nombre valide")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice5():
    PI = 3.1415926535
    rayon = int(input("Entrer le rayon du cercle (en m) : "))   # int(.) fait une conversion de type vers int
    # ******************** Votre code ci-dessous ********************
    perimeter = 2 * PI * rayon
    area = PI * rayon**2

    print(f"Un cercle de rayon {rayon} [m] a un périmètre de {perimeter:.2f} [m] et une surface/aire de {area:.2f} [m^2]")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice6():
    nb_of_days = int(input("Entrez un nombre de jours à convertir : "))
    # ******************** Votre code ci-dessous ********************
    years = nb_of_days // 365
    weeks = (nb_of_days % 365) // 7
    days = (nb_of_days - 365 * years - 7 * weeks)

    print(f"{nb_of_days} font {years} année(s), {weeks} semaine(s) et {days} jour(s).")
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
    i = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(f"u_{i} = {n}")
        i += 1
    
    print("Temps de vol: ", i)    
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
