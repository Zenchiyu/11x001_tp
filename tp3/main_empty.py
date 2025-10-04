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
    ma_liste = [4, 3, 7, 10, 42, 1]
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice3():
    ma_liste = [4, 3, 7, 10, 42, 1]
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice4():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

def fibo_iteratif(n):   # fonction à un seul argument
    # TODO n° 2 de l'ex 5:
    # ******************** Votre code ci-dessous ********************
    pass    # il faut des "return"
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice5():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice6():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

def tri(ma_liste):  # fonction à un seul argument
    # TODO n° 2 de l'exercice 7 (version in-place):
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice7():
    import random
    random.seed(42)
    # Liste pseudo-aléatoire avec seed fixée (la liste ne change pas si vous relancez)
    ma_liste = [random.randrange(100) for _ in range(20)]   # 20 nombres
    # Cette façon de créer des listes s'appelle "list comprehension" et s'exécute
    # généralement plus rapidement qu'une boucle for en plusieurs lignes.
    # Cependant, par soucis de compréhension, il est des fois préférable d'écrire
    # la boucle sur plusieurs lignes.
    # Le _ entre le for et le in est juste pour dire qu'on n'utilise pas cette valeur.
    print("Liste à trier:", ma_liste) 
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice8():
    import random
    random.seed(7)
    # Liste pseudo-aléatoire avec seed fixée (la liste ne change pas si vous relancez)
    ma_liste = [random.randrange(100) for _ in range(10)]   # 10 nombres
    print("Liste à séparer:", ma_liste) 
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************


@exercice
def exercice9():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice10():
    liste_de_liste = [[93, 49, 71], [36, 83, 53], [66, 32, 51]]
    liste_applatie = []
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

# Fonction à compléter ex11:
def est_palindrome(ma_chaine):
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice11():
    ma_chaine = input("Entrez la chaine de caractères: ")
    # ******************** Votre code ci-dessous ********************
    pass
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
    exercice9()
    exercice10()
    exercice11()
