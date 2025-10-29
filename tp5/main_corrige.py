import random

from utils import exercice, generer_resultats

#
# EXERCICE 1
#

@exercice
def exercice1():
    def fib(n):
        if n <= 1:
            return n
        return fib(n-1) + fib(n-2);
    
#    def fib(n):
#        f = [0, 1]
#        while len(f) < n:
#            f.append(f[-1] + f[-2])
#        return f[-1]

    N = int(input("Entrez un nombre: "));
    res = fib(N)
    print(f"Le {N}-ème élément de la suite de Fibonacci est {res}")


@exercice
def exercice2():
    nombres = list(range(10))
    # ******************** Votre code ci-dessous ********************
    carres = [k**2 for k in nombres]
    for nombre, carre in zip(nombres, carres):
        print(f"{nombre}, {carre}")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice3():
    resultats = generer_resultats()
    # ******************** Votre code ci-dessous ********************
    eleves = dict()
    for examens in resultats:
        for eleve, note in examens.items():
            if eleve not in eleves:
                eleves[eleve] = []
            eleves[eleve].append(note)
    print(eleves)
    for (nom, notes) in eleves.items():
        n = len(notes)
        moyenne = sum(notes) / n
        s = "s" if n > 1 else " "
        print(f"{nom:>10} : {n} note{s} - {moyenne:.2} de moyenne.")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice4():
    # ******************** Votre code ci-dessous ********************
    text = input("Entrez un texte:\n");
    text = text.lower()
    text = text.split(" ")
    text = "-".join(text);
    print(text)
    # ******************** Votre code ci-dessus *********************

def hamming(str1, str2):
    # ******************** Votre code ci-dessous ********************
    # if len(str1) != len(str2):
    #     return -1

    # Les deux chaines sont de la même taille ici
    # dist = 0
    # for c1, c2 in zip(str1, str2):
    #     if c1 != c2:
    #         dist += 1
    # return dist

    # dist = 0 
    # for i in range(len(str1)):
    #     if str1[i] != str2[i]:
    #         dist += 1
    # return dist
    return -1 if len(str1) != len(str2) else sum([c1 != c2 for c1, c2 in zip(str1, str2)])
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice5():
    # ******************** Votre code ci-dessous ********************
    str1 = input("str1 = ")
    str2 = input("str2 = ")
    print(f"\nHamming({str1}, {str2}) = {hamming(str1, str2)}.")
    # ******************** Votre code ci-dessus *********************

def fact(n): # n! = n * (n - 1)!, 0! = 1, 1! =1
    if n == 1:
        return 1
    return fact(n - 1) * n

def coeff_binom(n, k):
    return fact(n) // (fact(k) * fact(n - k))

@exercice
def exercice6():
    # ******************** Votre code ci-dessous ********************
    n = int(input("n = "))
    k = int(input("k = "))
    assert n >= k, "n est censé être plus grand ou égal à k"
    print(f"\nk parmi n: k={k}, n={n}) = {coeff_binom(n, k)}.")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice7():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

def afficher_instruction_hanoi(nom_tour_1, nom_tour_2):
    input(f"Prendre le disque sur la tour {nom_tour_1} et le déposer sur "\
          f"la tour {nom_tour_2} (appuyer sur n'importe quelle touche pour continuer)\n")

def hanoi_idiot(nb_disques, nom_tour_depart, nom_tour_arrivee, nom_tour_auxiliaire):

    match nb_disques:
        case 1:
            afficher_instruction_hanoi(nom_tour_depart, nom_tour_arrivee)
        case 2:
            afficher_instruction_hanoi(nom_tour_depart, nom_tour_auxiliaire)
            afficher_instruction_hanoi(nom_tour_depart, nom_tour_arrivee)
            afficher_instruction_hanoi(nom_tour_auxiliaire, nom_tour_arrivee)
        case _:
            print("Je ne sais pas comment faire avec %d disques.\n", nb_disques)

    return

def hanoi(nb_disques, nom_tour_depart, nom_tour_arrivee, nom_tour_auxiliaire):

    # TODO : commenter (ou supprimer) la ligne suivante
    # hanoi_idiot(nb_disques, nom_tour_depart, nom_tour_arrivee, nom_tour_auxiliaire)
    if (nb_disques == 1):
        afficher_instruction_hanoi(nom_tour_depart, nom_tour_arrivee)
        return
    # ******************** Votre code ci-dessous ********************
    hanoi(nb_disques - 1, nom_tour_depart, nom_tour_auxiliaire, nom_tour_arrivee)
    # afficher_instruction_hanoi(nom_tour_depart, nom_tour_arrivee)
    hanoi(1, nom_tour_depart, nom_tour_arrivee, nom_tour_auxiliaire)
    hanoi(nb_disques - 1, nom_tour_auxiliaire, nom_tour_arrivee, nom_tour_depart)
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice8():
    print("\n*** Tours de Hanoi ***\n\n");
    print("Par ici pour jouer : https://www.mathsisfun.com/games/towerofhanoi.html\n\n");

    nb_disques = int(input("Avec combien de disques voulez-vous jouer ? "));

    hanoi(nb_disques, '1', '3', '2');

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
