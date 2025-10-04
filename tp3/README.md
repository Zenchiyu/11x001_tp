# [11x001] TP n° 3 (optionnel)

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

## Commentaires/Remarques

Dans le précédent TP, vous avez implémenté une fonction récursive `somme_liste` mais une fonction existante `sum` vous permet de faire la même chose. Notez qu'en informatique, nous utilisons des fois le terme "tableau" d'une façon interchangeable avec "liste".

Ce TP est optionnel et contient donc plus d'exercices afin de renforcer vos connaissances pour vous préparer à l'examen. Vous pouvez aussi essayer de réimplémenter Fibonacci et le palindrome dans des fonctions récursives bien que nous reviendrons dessus dans de prochains TPs.

## Exercice 1

**TODO** : Lire un entier relatif et afficher s'il est strictement négatif, nul ou strictement positif.

**Rappel** : `input` retourne un `str` et le type `int` correspond à des entiers relatifs.

**Remarque** : Une variable, étant stockée en mémoire, a généralement des contraintes sur combien de bits ou octets (bytes en anglais)
elle prend en espace. Il y a donc généralement un nombre fini de valeurs possibles que peut prendre une variable ayant un certain type. Cependant, c'est un peu compliqué pour Python et cela dépend aussi de quelle version vous utilisez ([explication optionelle](https://www.datacamp.com/tutorial/everything-you-need-to-know-about-pythons-maximum-integer-value)). Cela sera plus clair en C.

## Exercice 2

**TODO** : En utilisant une boucle `while` mais sans utiliser la fonction existante `max`, trouver l'élément le plus grand d'une liste de nombres tel que `[4, 3, 7, 10, 42, 1]`.

**TODO** : Faites pareil mais avec une boucle `for`.

**Indice(s)** :

- En parcourant la liste, stockez la dernière valeur maximale trouvée dans une variable. N'utilisez pas `max` comme nom de variable car c'est le nom d'une fonction existante.
- Vous pouvez initialiser la valeur de cette variable à un nombre très petit et négatif.

## Exercice 3

**TODO** : Répétez l'exercice 2 mais pour trouver le minimum, sans utiliser la fonction existante `min`.

**Indice(s)** :

- Vous pouvez initialiser la valeur de votre variable à un nombre très grand.


## Exercice 4

**TODO** : Affichez un carré tourné 45 degré (comme le carreau dans les jeux de cartes) à l'aide de boucle `for` ou `while` et des caractères `' '`, `'*'` et `\n`.

**TODO** : Généralisez le carreau en demandant à l'utilisateur sa hauteur grâce à `input`. Partez du principe que la hauteur donnée est toujours impaire.

**Indice(s)** : Utilisez la concaténation de chaines de caractères

## Exercice 5

**TODO** : Essayer de coder la [suite de Fibonacci](https://fr.wikipedia.org/wiki/Suite_de_Fibonacci#D%C3%A9finition_formelle) en utilisant une boucle `while` ou `for` et un `print` pour afficher `F_n` à partir d'un $n \geq 2$ donné par l'utilisateur.

**TODO** : Réécrivez votre code dans une *fonction* `fibo_iteratif(n)` et appeler la depuis la fonction `exercice5`.

**Indice(s)** :

- Vous pouvez utiliser plusieurs variables ou une liste pour stocker les valeurs déjà calculées.

**Remarques** :

- Nous reverrons sa version *récursive*. **Veuillez ne pas confondre itératif vs récursif à l'examen !**
- Savoir passer d'une représentation à une autre est très utile (formule mathématique à pseudo-code et pseudo-code à code, etc. ou dans l'autre sens).
- Le corrigé donne une façon de faire mais ce n'est pas la seule.


## Exercice 6 - Affectation composée et concaténation de listes

Vous avez vu en cours les opérateurs d'affectation composée (`+=`, `-=` etc.), ce sont des opérations "in-place" qui modifient directement la partie de gauche.

**TODO** : Concaténater la liste `["Alice", "Bob"]` avec `["Charlie", "Eve"]` en utilisant `+=` mais sans utiliser de boucles.

**TODO** : Faites pareil mais avec une boucle mais sans utiliser `append`.

**Indice** : Vous pouvez concaténer des listes avec des listes ne contenant qu'un seul élément.


## Exercice 7 - Tri (plusieurs solutions possibles)

**Contexte factice** : Vous vous trouvez dans une situation où vous essayez de sortir d'une pièce qui peut s'écrouler à tout moment. Cependant, pour sortir, vous devez réarranger des objets (même forme mais différentes tailles) placés sur des socles (même hauteurs). Votre premier réflexe est donc de trier des objets dans l'ordre croissant (du plus petit au plus grand).

**TODO** : Sans Python, réfléchissez à comment vous pourriez trier ces objets, étape par étape. Essayer d'être précis sur quel objet déplacer sur quel socle. Votre méthode est un algorithme de tri !

**Contexte factice** : Après être sorti de cette pièce, vous êtes confronté à un problème similaire mais avec plus d'objets. N'ayant pas le temps de réarranger à la main, mais ayant un accès à un ordinateur avec Python installé et un bras robotique pouvant déplacer les objets, vous pouvez donc coder votre algorithme et l'appliquer à la liste des tailles des objets déjà donné.

**TODO** : Avec Python mais sans utiliser de fonction prédéfinie pour trier des listes, écrivez une fonction `tri(ma_liste)` qui soit retourne la nouvelle liste triée, soit la modifie in-place.

**TODO (plus dur)** : Est-ce que vous pouvez faire plus rapide ? Si oui, comment ? (en n'utilisant qu'une seule machine)


**Remarque(s)** :

- Le contexte est inspiré du jeu escape room simulator.
- Nous pourrons y revenir dessus dans le semestre (pas forcément avec du Python)
- Bien que ce TP est optionnel, vous pouvez nous montrer votre algorithme !

## Exercice 8


La variable `ma_liste` fournie contient une liste de quelques nombres entiers. 

**TODO** :

- Séparer cette liste en deux listes qu'on appelera `pairs` et `impairs`, la première contenant les nombres pairs et l'autre les nombres impairs. 
- Afficher ces deux listes pour vérifier votre solution.

## Exercice 9

**TODO** : Qu'affiche ce code ?

```python
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
```

Vous pouvez copier-coller ce code dans la fonction `exercice9` pour vérifier votre raisonnement.

**Remarque** : Il est bien plus utile de réfléchir à la question **avant** de faire le copier-coller bien sûr.

## Exercice 10


La variable `liste_de_liste` contient une liste de liste de nombres aléatoires, par exemple : `[[93, 49, 71], [36, 83, 53], [66, 32, 51]]`.


**TODO** :
- Ajouter tous les nombres dans la variable `liste_applatie` en utilisant la concaténation de liste.

Dans notre exemple, on aura `liste_applatie` qui vaut `[93, 49, 71, 36, 83, 53, 66, 32, 51]`.

**Remarque(s)** :

- Vous pouvez penser à cette liste de listes comme une matrice (ici de taille $3 \times 3$)

## Exercice 11

Un [palindrome](https://fr.wikipedia.org/wiki/Palindrome) est une chaine de caractères dont l'ordre reste le même qu'on le lise de gauche à droite ou de droite à gauche. 

Exemples : 
- kayak
- radar
- engagelejeuquejelegagne

**TODO** : 

- Compléter la fonction `est_palindrome` qui prend une chaine de caractères en entrée et doit renvoyer `True` si cette chaine est un palindrome, `False` sinon.


