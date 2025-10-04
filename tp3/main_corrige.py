import random

from utils import exercice

#
# EXERCICE 1
#

@exercice
def exercice1():
    # ******************** Votre code ci-dessous ********************
    nombre = int(input("Renseignez un entier relatif : "))

    if (nombre < 0):
        print(f"{nombre} est strictement négatif.")
    elif (nombre == 0):
        print(f"{nombre} est nul.")
    else:
        print(f"{nombre} est strictement positif.") # si on ne le met pas dans le else, c'est toujours exécuté !

    # ******************** Votre code ci-dessus *********************

@exercice
def exercice2():
    ma_liste = [4, 3, 7, 10, 42, 1]
    # ******************** Votre code ci-dessous ********************
    maxi = -10_000  # Pour rappel _ dans ce cas n'est là que pour aider à la lecture du nombre
    # Version avec while:
    i = 0
    while i < len(ma_liste):
        if ma_liste[i] > maxi:
            maxi = nombre
        i += 1
    print(f"Maximum de {ma_liste}: {maxi}")

    # Version avec for:
    maxi = -10_000
    for nombre in ma_liste: # Parcourt la liste
        if nombre > maxi:   # Si on trouve plus grand, c'est notre plus grand
            maxi = nombre
    print(f"Maximum de {ma_liste}: {maxi}")
    
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice3():
    ma_liste = [4, 3, 7, 10, 42, 1]
    # ******************** Votre code ci-dessous ********************
    mini = 10_000  # Pour rappel _ dans ce cas n'est là que pour aider à la lecture du nombre
    # Version avec while:
    i = 0
    while i < len(ma_liste):
        if ma_liste[i] < mini:
            mini = nombre
        i += 1
    print(f"Minimum de {ma_liste}: {mini}")

    # Version avec for:
    mini = 10_000
    for nombre in ma_liste:
        if nombre < mini:   # Si on trouve plus petit, c'est notre plus petit
            mini = nombre
    print(f"Minimum de {ma_liste}: {mini}")
    
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice4():
    # ******************** Votre code ci-dessous ********************
    # La généralisation directement
    # Il y a plusieurs façons de faire, en voici une:
    hauteur = int(input("Donnez la hauteur du losange: "))

    assert hauteur % 2 == 1, f"{hauteur} n'est pas impair"
    
    # Premier "triangle"
    for i in range(hauteur // 2):
        # Espaces avant le bord gauche
        nb_gauche = hauteur // 2 - i
        espaces_gauche = " " * nb_gauche   # Vous pouviez aussi faire une boucle ici et concaténer des " "

        # Espaces avant le bord droite en comptant depuis le bord gauche
        if i == 0:
            print(espaces_gauche + "*")
        else:
            nb_droite = hauteur - nb_gauche * 2 - 2
            espaces_droite = " " * nb_droite
            print(espaces_gauche + "*" + espaces_droite + "*")

    # Milieu et deuxième "triangle"
    for i in range(hauteur // 2, hauteur): 
        # Espaces avant le bord gauche
        nb_gauche = i - hauteur // 2
        espaces_gauche = " " * nb_gauche   # Vous pouviez aussi faire une boucle ici et concaténer des " "
        # Espaces avant le bord droite en comptant depuis le bord gauche
        if i == hauteur - 1:
            print(espaces_gauche + "*")
        else:
            nb_droite = hauteur - nb_gauche * 2 - 2
            espaces_droite = " " * nb_droite
            print(espaces_gauche + "*" + espaces_droite + "*")

    # ******************** Votre code ci-dessus *********************

def fibo_iteratif(n):   # fonction à un seul argument
    # TODO n° 2 de l'ex 5:
    fibos = [0, 1, 1]   # Liste stockant les résultats intermédiaires
    for i in range(len(fibos), n + 1):  # i commence à 3 ici et se termine à n
        fibos.append(fibos[i - 1] + fibos[i - 2]) 
        # print(f"F_{i} = {fibos[i]}")
    return fibos[n]

@exercice
def exercice5():
    # ******************** Votre code ci-dessous ********************
    # TODO n° 1:
    n = int(input("Entrez n: "))
    fibos = [0, 1, 1]   # Liste stockant les résultats intermédiaires
    for i in range(len(fibos), n + 1):  # i commence à 3 ici et se termine à n
        fibos.append(fibos[i - 1] + fibos[i - 2]) 
        # print(f"F_{i} = {fibos[i]}")
    print(f"F_{n} = {fibos[n]}")
    
    # TODO n° 2:
    # Appel de fonction
    fib = fibo_iteratif(n)
    print(f"F_{n} = {fib}")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice6():
    # ******************** Votre code ci-dessous ********************
    # TODO n° 1
    ma_liste = ["Alice", "Bob"]
    ma_liste += ["Charlie", "Eve"]

    print(ma_liste)
    
    ma_liste = ["Alice", "Bob"]
    deuxieme_liste = ["Charlie", "Eve"]
    for el in deuxieme_liste:
        # Si on avait fait avec append: ma_liste.append(el)
        # Sinon:
        ma_liste += [el]
    print(ma_liste)

    # ******************** Votre code ci-dessus *********************

def tri(ma_liste):  # fonction à un seul argument
    # TODO n° 2 de l'exercice 7 (version in-place):
    n = len(ma_liste)
    for i in range(0, n - 1):   # i va jusqu'à n - 2
        k = i
        for j in range(i + 1, n):   # i va jusqu'à n - 1
            if ma_liste[j] < ma_liste[k]:
                k = j
        
        if k != i:
            # Swap/échange. En Python, on peut le faire en une ligne
            ma_liste[i], ma_liste[k] = ma_liste[k], ma_liste[i]

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
    # TODO n° 1 en commentaire (sous forme de doc-string):
    """
    Une idée serait de prendre le plus petit nombre et le mettre tout à gauche
    Et continuer de faire ça jusqu'à tout soit trier.
    
    Plus précisément pour une liste L de n éléments:

    n <- nombre d'éléments de la liste L
    pour i allant de 0 à n - 2
        # On veut déplacer le plus petit élément de L[i:] dans L[i]
        k <- i
        # Pour cela, on compare L[i] avec le reste des éléments de la liste
        pour j allant de i + 1 à n - 1
            si L[j] < L[k], alors:
                k <- j  # k est l'index de la valeur qu'on veut échanger

        # S'il y a bien un élément plus petit
        si k != i, alors:
            # On échange
            tmp = L[i]
            L[i] = L[k]
            L[k] = tmp
    
    Cet algorithme s'appelle tri par sélection. Il y a pleins de façons de faire.
    Il y a une autre où on traverse la liste et échange des paires d'éléments
    s'ils ne sont pas dans l'ordre. On répète jusqu'à que la liste soit triée.
    Cette façon s'appelle tri à bulles.
    """
    # TODO n° 2: Implémentation
    tri(ma_liste)
    print("Liste triée:", ma_liste)
    
    # TODO n° 3: Plus rapide ?
    # Il y a des versions plus rapides que celle présentée.
    # Vous pouvez, pour trier une liste:
    #   Trier deux sous-listes (diviser).
    #   Dès qu'elles sont triées, recombinez les deux listes triées.
    # Il y a de la récursivité dans la définition ! Et le cas de base
    # est quand les sous-listes n'ont qu'un seul élément.
    # C'est l'algorithme merge sort (tri fusion en français)
    # On reviendra dessus dans la partie algorithmique du cours.
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice8():
    import random
    random.seed(7)
    # Liste pseudo-aléatoire avec seed fixée (la liste ne change pas si vous relancez)
    ma_liste = [random.randrange(100) for _ in range(10)]   # 10 nombres
    print("Liste à séparer:", ma_liste) 
    # ******************** Votre code ci-dessous ********************
    # Version "List comprehension"
    pairs = [el for el in ma_liste if el % 2 == 0]
    impairs = [el for el in ma_liste if el % 2 != 0]
    print(f"Pairs:\n{pairs}")
    print(f"Impairs:\n{impairs}")

    # Version avec plusieurs lignes mais une seule boucle for:
    pairs = []
    impairs = []
    for el in ma_liste:
        if el % 2 == 0:
            pairs.append(el)
        else:
            impairs.append(el)
    print(f"Pairs:\n{pairs}")
    print(f"Impairs:\n{impairs}")

    # ******************** Votre code ci-dessus *********************


@exercice
def exercice9():
    # ******************** Votre code ci-dessous ********************
    a = [2, 3]
    b = a
    print(a)
    print(b)
    
    b[0] = 1
    print(a)
    print(b)
    
    a = [5, 6]
    b[0] = 10
    print(a)
    print(b)
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice10():
    liste_de_liste = [[93, 49, 71], [36, 83, 53], [66, 32, 51]]
    liste_applatie = []
    # ******************** Votre code ci-dessous ********************
    for liste in liste_de_liste:
        liste_applatie += liste

    print(liste_applatie)
    # ******************** Votre code ci-dessus *********************

# Fonction à compléter ex11:
def est_palindrome(ma_chaine):
    # ******************** Votre code ci-dessous ********************
    # Plusieurs façons de faire. En voici une:
    mid = len(ma_chaine) // 2
    print(ma_chaine[:mid], ma_chaine[:-mid-1:-1])
    return ma_chaine[:mid] == ma_chaine[:-mid-1:-1]
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice11():
    ma_chaine = input("Entrez la chaine de caractères: ")
    # ******************** Votre code ci-dessous ********************
    if est_palindrome(ma_chaine):
        print(f"{ma_chaine} est un palindome")
    else:
        print(f"{ma_chaine} n'est pas un palindome")
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
