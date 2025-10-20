# [11x001] TP n° 5

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

- Ecrivez la version récursive de la fonction `fibonacci` qui prend un entier naturel `n` en entrée et doit renvoyer le `n`-ème terme de la [suite de Fibonacci](https://fr.wikipedia.org/wiki/Suite_de_Fibonacci).


## Exercice 2

La variable `nombres` fournie contient la liste des entiers de 0 à 9. 

**TODO** :
- Créer une liste `carres` qui contient les éléments de la liste `nombres` élevés au carré.
- Afficher chaque nombre et son carré.

>**Aide** : Exemple d'utilisation de `zip` :
```python 
l1 = [2, 3]
l2 = [4, 5]
for e1, e2 in zip(l1, l2):
    print(f'{e1}, {e2}')
# Affiche
# 2, 4
# 3, 5
```

## Exercice 3 - Manipulation de `dict` et `list`

La variable `resultats` est une `list` de `dict`. Chaque `dict` contient les notes des élèves participants à un cours. 


```python
# exemple de contenu de la variable resultats
[
    {
        'Adam': 5,
        'Alice': 1,
        'Ambre': 5,
        'Arthur': 5,
    },
    {
        'Adam': 3,
        'Ambre': 4,
        'Emma': 3,
        'Maël': 1,
        'Rose': 3
    }
]
```

Dans l'exemple ci-dessus, il y a deux cours différents : le premier cours concerne 4 élèves et le deuxième cours en concerne 5.  

Le contenu de cette variable est regénéré aléatoirement à chaque fois que vous exécutez votre code.

**TODO** :

- Créer un `dict` appelé `eleves` dont les clés sont les noms des élèves. La valeur associée à une clé est la liste des notes obtenues par l'élève.
- Afficher le nom, le nombre de note et la moyenne de chaque étudiant. 

Pour notre exemple : 

```python 
# exemple de contenu de la variable eleves
{
    'Adam': [5, 3],
    'Alice': [1],
    'Ambre': [5, 4],
    'Arthur': [5],
    'Emma': [3],
    'Maël': [1],
    'Rose': [3],
}
``` 
Affichage :
```
  Adam : 2 notes - 4.00  de moyenne.
 Alice : 1 note  - 1.00  de moyenne.
 Ambre : 2 notes - 4.50  de moyenne.
Arthur : 1 note  - 5.00  de moyenne.
  Emma : 1 note  - 3.00  de moyenne.
  Maël : 1 note  - 1.00  de moyenne.
  Rose : 1 note  - 3.00  de moyenne.
```

## Exercice 4 - Slugify

**TODO** :
- Demander un texte à l'utilisateur. 
- Afficher ce texte tout en minuscule et en remplaçant les espaces par des tirets (`-`).

**Exemple** : 

Le texte :

`Ce procédé est parfois appelé slugify car on convertit notre texte en son équivalent limace` 

sera convertit en : 

`ce-procédé-est-parfois-appelé-slugify-car-on-convertit-notre-texte-en-son-équivalent-limace` 

Pour information, une version complète comme [celle-ci](https://blog.tersmitten.nl/slugify/) se charge également d'enlever les accents et les caractères spéciaux.

**Aide** :

- Conversion en minuscule avec `.lower()`

- Exemple d'utilisation de `split` :

```python 
texte = "Exemple de texte."
mots = texte.split(" ") # mots est une liste ["Exemple", "de", "texte."]
```

- Exemple d'utilisation de `join` :

```python 
mots = ["Exemple", "de", "texte."]
texte = "XXX".join(mots) # texte est un str : "ExempleXXXdeXXXtexte."
```

## Exercice 5 - Distance de Hamming

**TODO** : Compléter la fonction `hamming` qui prend en entrée deux chaines de caractères et qui retourne un entier correspondant à la distance de Hamming entre ces deux chaines de caractères. Si les deux chaines ne font pas la même longueur, cette fonction retourne -1.

**Remarque** : La fonction `exercice5` est déjà implémentée pour vous. Elle demande deux chaines de caractères à l'utilisateur et appelle la fonction `hamming` sur ces deux chaines.

**Rappel** : Pour deux chaines de caractères de même longueur, la [distance de Hamming](https://fr.wikipedia.org/wiki/Distance_de_Hamming) est définie comme le nombre de positions où les deux chaines diffèrent.

**Aide** :

- Sommer les éléments d'une liste: `sum(ma_liste)`


## Exercice 6 - Coefficient binomial

**TODO** : Implémentez une fonction qui prend en entrée deux entiers $k$ et $n$ et retourne le nombre de combinaisons de $k$ parmi $n$, que l'on calcule comme:

$$\binom{n}{k} = \frac{n! }{k! (n - k)!}$$

Utilisez la fonction que vous avez écrite plus tôt.

## Exercice 7 - Tuples

**TODO**: Testez ces codes ci-dessous et essayez de comprendre ce qui s'est passé

```python
a = (1, 2, 3)
a[0] = 42
```

```python
a = ([1, 2], 2, 3)
b = a
b[0][0] = 42
print(a)
print(b)
```

```python
import random


def createurDeTuples():
    x = random.randint(0, 10)
    y = random.randint(0, 10) 
    return x, y

ma_liste = [createurDeTuples() for _ in range(10)]
print(ma_liste)
```

## Exercice 8 - Tours de Hanoi (plus difficile)

Le but de cet exercice est d'utiliser le concept de **fonction récursive** pour implémenter une solution au jeu des *Tours de Hanoi*.

Les règles sont les suivantes : 

- Le but du jeu est de déplacer tous les disques vers la tour 3.
- On ne peut pas placer un disque plus grand sur un disque plus petit.

Pour commencer, suivre [ce lien](https://www.mathsisfun.com/games/towerofhanoi.html) pour y jouer et bien comprendre les règles. Essayer d'abord de résoudre le jeu avec 3 disques, puis augmenter le nombre de disques (par exemple 8).


**TODO** : Complétez le corps de la fonction `hanoi` fournie pour que votre code affiche la succession de coups pour gagner le jeu. Vous pouvez utiliser le lien précédent pour tester votre solution. 

**Indice** : Une solution **récursive** permet de résoudre ce jeu pour un nombre de disque quelconque.

**Remarques** : 

La fonction `hanoi` prend quatre paramètres :

- `nb_disques` : le nombre de disques
- `nom_tour_depart`: le nom de la tour de départ (par exemple `'1'`)
- `nom_tour_arrivee`: le nom de la tour d'arrivée (par exemple `'3'`)
- `nom_tour_auxiliaire`: le nom de la dernière tour, qu'on appellera tour auxiliaire (par exemple `'2'` dans notre cas).

Cette fonction ne renvoit rien (type de retour `NoneType`) car on veut simplement afficher avec `print` la succession de coups à jouer. 

La fonction `hanoi_idiot` implémente brutalement une solution pour 1 et 2 disques. Au contraire, la solution que nous voulons est générale et résout le jeu pour un nombre de disque quelconque. 

Pour l'affichage des coups, on fera appel à la fonction fournie `afficher_instruction_hanoi`. La fonction `hanoi_idiot` sert avant tout à illustrer l'utilisation de cette fonction d'affichage, vous pouvez ensuite commenter / supprimer son appel dans la fonction `hanoi`.

### Aide

Cet exercice n'est pas évident et nous vous proposons un peu d'aide pour faire émerger la solution récursive.  

> - On nomme les trois tours '1', '2' et '3',  et `nb_disques` le nombre de disques. 
> - La situation de départ est la suivante : tous les disques se trouvent sur la tour 1.
> - Notre but est de les déplacer vers la tour 3. 

L'idée fondamentale est de relier la solution du jeu avec `nb_disques` disques à la solution avec `nb_disques - 1` disques.

Par exemple, supposons que nous ayons `nb_disques = 3` disques et que nous sachions résoudre le jeu avec `nb_disques - 1 = 2` disques. Alors, nous pouvons faire comme suit : 
- Déplacer les 2 premiers disques de la tour 1 sur la tour 2. **On sait le faire car on suppose qu'on sait résoudre le jeu avec 2 disques**.
- Prendre le disque restant sur la tour 1 et le déposer sur la tour 3.
- Déplacer les 2 disques de la tour 2 sur la tour 3. A nouveau, on sait le faire car cette opération concerne 2 disques et on suppose cette capacité acquise.

Cette solution fait donc deux appels récursifs (premier et troisième points). En pratique, on peut compléter la fonction `hanoi` en suivant exactement ces trois points. 

**Attention** : Il faut un cas de base pour arrêter la récursion. Dans notre situation, si `nb_disques` vaut 1 on se contente d'afficher l'instruction évidente à l'aide de `afficher_instruction_hanoi(nom_tour_depart, nom_tour_arrivee)` **et on ne fait pas les appels récursifs décrits précédemment** (cela stoppe donc la récursion).
