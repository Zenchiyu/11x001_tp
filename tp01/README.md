# [11x001] TP n° 1

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

L'exercice est déjà implémenté, il affiche simplement:

```
Bonjour monde !
```
**TODO** : Observer le code de cet exercice, en particulier l'usage de `print` ainsi que les guillemets. Vous l'utiliserez dans l'exercice suivant.

---

## Exercice 2

**TODO** : Ecrire un programme qui affiche votre nom, date de naissance et adresse e-mail. Par exemple, il affichera:

```
Nom     : Michel LAMBDA
Né le   : 31.10.2001
Contact : michel.lambda@unige.ch
```

## Exercice 3

Une variable en informatique est à la fois similaire et non à celle en mathématiques.
Une variable est associé à un identifiant (nom) et type indiquant s'il s'agit d'un entier, d'une chaîne de caractères ou autre. La valeur que contient la variable est stockée dans la mémoire et prend une certaine place, un certain nombre de bits (0 et 1) ou bytes (8 bits).
En mémoire, des textes ou des images sont stockés sous forme de 0 et de 1 et prend donc de l'espace ! On reviendra sur cela quand on fera du C.

Pour voir le type d'une variable `x`, vous pouvez l'afficher avec `print(type(x))`
Notez que le symbole `=` en informatique ne correspond en général pas à une comparaison mais plutôt à une *assignation*: le terme de gauche prend la valeur indiquée par le terme à droite.


**TODO** : Ecrivez 5 variables de type `str` correspondant aux cinq caractères qui composent le mot *UNIGE*.

**TODO** : Affichez avec ces 5 variables et `print` le mot *UNIGE* caractère par caractère, d'abord à l'endroit, puis à l'envers.

## Exercice 4 - input et if

**Contexte** : On vous demande d'écrire un code qui demande à l'utilisateur de choisir un nombre entre $0$ et $9$ correspondant à la catégorie d'une image montrée à l'écran. Cela permettrait d'obtenir un ensemble de données permettant l'entrainement d'un modèle en IA pour de la classification d'images.

**TODO** :
- Demandez à l'utilisateur un nombre entre $0$ et $9$ inclus.
- Si l'utilisateur ne rentre pas un de ces nombres, affichez avec `print` qu'il fallait
rentrer un nombre valide.

## Exercice 5 - f-strings

**TODO** : Calculer et afficher le périmètre et l'aire d'un cercle.

**Remarques** : 
- Pour la valeur de Pi, utilisez la variable `PI`, définie au début de l'exercice :

```python
PI = 3.1415926535
```

- Le rayon du cercle est un nombre flottant et est demandé à l'utilisateur lors de l'exécution du programme, grâce à la fonction `input`. **/!\ Cette partie est déjà implémentée pour vous !** Comme on fera appel à `input` dans les prochains TPs, pour demander à l'utilisateur d'entrer une valeur, nous vous conseillons de commencer à observer son fonctionnement :

```python
rayon = int(input("Entrez le rayon du cercle (en m) : ")) # message d'invitation (plus user-friendly). int(.) fait une conversion de type vers int
```

Il y a quelques différences avec le C que vous devriez faire attention plus tard.

> Astuce : Pour injecter une variable dans l'affichage du print avec un formatage particulier, utilisez les f-strings ("f" devant les guillemets et utilisation d'accolades):

```python
x = 42
y = "exemple"
print(f"Voici la valeur de ma variable: {x}. Vous pouvez avoir du texte après.")
print(f"Voici un autre {y}.")
```

Pour avoir un certain nombre de décimales (ici 2) après la virgule pour les nombres flottants (float -> f):
```python
x = 1.234567
print(f"Voici mon nombre: {x:.2f}")
```

## Exercice 6

**TODO** : Convertir en jours, semaines, années le nombre de jours stocké dans la variable `nb_of_days` (dont la valeur est demandée à l'utilisateur avec la fonction `input`, similairement aux exercices précédents). Vous pouvez considérer qu'un an fait toujours 365 jours.

**Exemple** : Si l'utilisateur entre le nombre $2153$, on veut afficher :

```
2153 jours font 5 année(s), 46 semaine(s) et 6 jour(s).
```

## Exercice 7 - Division euclidienne et reste

**TODO** : Observer le code de l'exercice:

```python
a = 7
b = 2
c = 7 // 2  # Ne modifier que cette ligne
d = 7 % 2   # le % est l'opérateur modulo, cela donne le reste de la division euclidienne
print(f"{a} / {b} = {c:.2f}, reste = {d}")
```

Il affiche :

```
7 / 2 = 3.00, reste = 1
```
**TODO**: Utilisez `/` à la place de `//` et regardez ce que vous obteniez.

## Exercice 8 - Suite de Syracuse

**TODO** : Essayez de coder la [suite de Syracuse](https://fr.wikipedia.org/wiki/Conjecture_de_Syracuse#Suite_de_Syracuse) en utilisant une boucle `while`, un `if`, un `else` et un `print` pour afficher $u_n$.

C'est un exemple de code **itératif**.

**Indices/Rappels** :
- Pour voir si un nombre est pair, vous pouvez regarder si le reste
de la division entière est zéro ou non (en utilisant l'opérateur modulo)
- `x = x + 1` ou `x += 1` veut dire qu'on incrémente la valeur de `x` par 1
