import random

from utils import exercice, generer_resultats

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
    nombres = list(range(10))
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice3():
    resultats = generer_resultats()
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice4():
    # ******************** Votre code ci-dessous ********************
    pass
    # ******************** Votre code ci-dessus *********************

def hamming(str1, str2):
    # ******************** Votre code ci-dessous ********************
    return -1
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice5():
    # ******************** Votre code ci-dessous ********************
    str1 = input("str1 = ")
    str2 = input("str2 = ")
    print(f"\nHamming({str1}, {str2}) = {hamming(str1, str2)}.")
    # ******************** Votre code ci-dessus *********************

@exercice
def exercice6():
    # ******************** Votre code ci-dessous ********************
    pass
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

    if (nb_disques < 1):
        print("Le nombre de disques ne peut pas être inférieur à 1.\n")
        return

    # TODO : commenter (ou supprimer) la ligne suivante
    hanoi_idiot(nb_disques, nom_tour_depart, nom_tour_arrivee, nom_tour_auxiliaire)
    
    # ******************** Votre code ci-dessous ********************
    
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
