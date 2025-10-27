# [11x001] TP n° 6

---

Université de Genève, cours [11x001 Introduction à la Programmation des Algorithmes](https://pgc.unige.ch/main/teachings/details/2025-11X001)

---

## Consignes générales (pour tous les TPs)

- La **consigne** de chaque exercice est dans le fichier `README.md`. Les **TODO** indiquent des consignes à suivre.
- Le **code** des exercices est dans le fichier `main_empty.py` ou `main_empty.c`. Chaque exercice correspond à une fonction dans ce fichier, nommée `exercice1` pour l'exercice 1, `exercice2` pour l'exercice 2 etc.
- L'endroit où vous êtes supposés écrire votre code est délimité par `Votre code ci-dessous` et `Votre code ci-dessus`
- Pour exécuter votre programme, vous pouvez taper dans le terminal:
    - Pour Python: `python3 <nom_fichier>.py`
    - Pour C: `clang <nom_fichier>.c -o <nom_executable>` puis `./<nom_executable>`
- Les **solutions partielles** seront fournises une semaine après le TP. Vous pouvez tout de même nous demander des questions sur les solutions non fournises.

## Exercice 1

**TODO** :

- Créez une classe `Voiture` avec trois attributs : *marque*, *couleur*, *kilometrage*.
- Créez une méthode `avancer` qui prend en argument *vitesse* (en m/s) et *temps* (en s) qui fait avancer la voiture et donc augmente le kilométrage de la distance correspondante (à calculer).
- Créez une instance de cette classe avec une Toyota, blanche, 25000 kilomètres au compteur. Faites la avancer pendant 20 min à 50 km/h.

## Exercice 2

**TODO** :

- Créez une fonction anonyme (`lambda`) qui prend en argument *vitesse* (en m/s) et *temps* (en s) et renvoie la distance en km, si $t \geq 0$, sinon renvoie $0$.  
Remarque: utiliser une condition sur une ligne s'appelle du ternaire.  

- Utilisez cette fonction dans la classe `Voiture` pour mettre à jour le kilométrage.

## Exercice 3

**TODO** :

- Enlevez les doublons qu'il y a dans cette liste sans utiliser `set`
```python
import random
random.seed(0)
a = [random.randrange(0, 100) for _ in range(1000)]
```
- Enlevez les doublons qu'il y a dans cette liste en utilisant `set`. Le résultat doit être une liste.

- Enlever les nombres pairs dans la liste sans doublon à l'aide du set `set(range(0,100,2))`. Le résultat doit encore être une liste. Pas de boucle
