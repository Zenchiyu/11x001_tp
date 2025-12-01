# Demande a l'utilisateur qqch en entree. levier est un booleen (vrai ou faux)
levier = input("Voulez vous activer le levier? (oui/non) ") == "oui"

if levier:
    print("Proche meurt")
else:
    print("5 inconnus meurent")
