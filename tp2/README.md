# [11x001] TP n° 2

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

## Commentaires/informations

En Python, vous avez vu qu'il faut *indenter* votre code en appuyant sur la touche Tab et cela correspond à 4 espaces. Sans ces indentations, vous auriez des erreurs ! 


## Exercice 1 - Opérateurs booléens et if/else imbriqués


Vous avez vu que certaines variables peuvent prendre une valeur qui est soit `True`, soit `False`. Ce sont des variables *booléennes*.

Par exemple dans le code ci-dessous, l'expression `nombre >= 2` est `True` !

```python
nombre = 5
if nombre >= 2:
    print("Mon nombre est plus grand ou égal à 2")
```

Vous pouvez donc faire ceci:

```python
nombre = 5
ma_variable = nombre >= 2
```

L'opérateur `>=` est un exemple d'opérateur relationnel. Il existe aussi des opérateurs sur les booléens (voir cours PFO et l'algèbre de Boole) qui représentent par exemple: ET, OU, NON.

Voici leurs tables de vérité (0 pour faux et 1 pour vrai):

- AND (⋀ en maths)

| A | B | A and B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   0   |
| 1 | 0 |   0   |
| 1 | 1 |   1   |

- OR (⋁ en maths)

| A | B | A or B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   1   |
| 1 | 0 |   1   |
| 1 | 1 |   1   |

- NOT (¬ en maths)

| A | not(A) |
|---|----|
| 0 |  1 |
| 1 |  0 |

---

Vous pouvez donc utiliser des opérateurs booléens par exemple dans vos boucles ou conditions.

Exemple:

```python
nombre = int(input("Veuillez rentrer un nombre entre 0 et 9: "))

while (nombre < 0 or nombre > 9):
    print(f"Votre nombre {nombre} n'est pas dans l'intervalle voulu (entre 0 et 9 inclus)")
    nombre = int(input("Veuillez rentrer un nombre entre 0 et 9: "))

print(f"Voici mon nombre {nombre}")
```

---

**Contexte factice** : On vous demande de créer un modèle d'IA (apprentissage automatique) qui affiche si une personne a des risques d'avoir un accident cardiovasculaire ([source de l'exemple originel](https://fr.wikipedia.org/wiki/Arbre_de_d%C3%A9cision#Exemple_simple)).

On vous donne déjà le modèle calculé automatiquement à partir de données des patients.


**TODO** : En suivant le pseudo-code très informel ci-dessous ou l'exemple originel, réimplémentez le en Python avec des `if`, `else`, et `print`

```
# age est un entier non negatif et fumeur est un booleen

Si age strictement plus petit que 30
    Affichez que le patient a peu de risque
Sinon
    Si fumeur
        Affichez que le patient a un grand risque
    Sinon
        Affichez que le patient a peu de risque
```

**TODO** : Implémentez ensuite une autre version qui au final affiche la même chose en combinant des opérateurs booléens. Autrement dit, cela ne suivrait plus le pseudo-code mais affiche la même chose quand `age` et `fumeur` valent la même chose.


**Remarques** :

- N'oubliez pas de donner des valeurs à `age` et `fumeur`, vous pouvez utiliser `input(.)`, `int(.)` et `bool(.)`.

- Le modèle de l'exemple originel s'appelle arbre de décision et est un modèle très interprétable. Vous le reverrez plus tard dans votre cursus dans le cours d'IA.

- Il ne faut pas confondre les opérateurs booléens avec ceux bit à bit. En Python `&`, `|`, et `^` correspondent à un ET, OU, et XOR entre les représentations binaires de deux nombres (voir PFO).

## Exercice 2 - Elif (Else if) et !=

- En plus du `if` et `else`, il y a le `elif` qui fait les choses un peu différemment que le if.

- Vous avez aussi vu l'opérateur `==` qui permet de comparer si deux variables/valeurs (ex. `x` et `y`) sont égales avec `x == y`. Pour comparer si elles diffèrent, vous pouvez soit utiliser `not ( x == y )`, soit `x != y`

**TODO** :  Testez les codes ci-dessous (déjà codés) et réfléchissez à ce qui change en les exécutant. Vous pouvez utiliser le debugger dans VSCode pour voir quelles instructions sont exécutés !

```python
x = 40
if x != 42:
    print("Not 42")
if x != 42:
    print("Not 42")
else:
    print("42")
```

```python
x = 40
if x != 42:
    print("Not 42")
elif x != 42:
    print("Not 42")
else:
    print("42")
```

Vous pouvez changer la valeur de la variable `x` et voir ce que cela change. 


## Exercice 3 - Break, continue et boucles imbriqués

Dans une boucle que cela soit un for ou un while, vous pouvez sauter à la prochaine itération de la boucle ou même en sortir.

- Le mot clé `continue` permet de sauter les instructions qui suivent (qui sont dans la boucle & au même niveau d'indentation) et aller à la prochaine itération.
- Le mot clé `break` permet de sortir de la boucle

**Attention** : Etant donné que vous pouvez avoir des boucles dans des boucles, `continue` et `break` n'affectent pas toutes les boucles.

**TODO** : Jouez avec les deux mots-clés en les déplaçant pour voir ce que cela donne dans le code ci-dessous (déjà implémenté):

```python3
for i in range(5):
    for j in range(4):
        print(i, j)
    break   # Testez d'enlever cela, de le déplacer et aussi tester de rajouter continue ou même d'autres print
```

**Remarque** : En informatique, nous utilisons souvent `i`, `j`, et `k` lorsqu'on n'a pas de nom particulier à donner à nos variables pour les boucles ou qu'on réfère à quelque chose qu'on appelle indice ou indexe.

Un indice ou indexe est un nombre indiquant une position dans un certain type de structure de donnée.

## Exercice 4 - Listes

Tout comme une liste de course, une structure de donnée avec une notion d'ordre existe en Python permettant de stocker plusieurs valeurs. Cette structure de donnée est une liste et est de type `list`.

En Python, les valeurs que peuvent prendre la liste n'ont pas forcément besoin d'être du même type. On peut donc avoir des entiers, des chaînes de caractères, des nombres à virgules etc. dedans. Cela est différent en C, on reviendra dessus.

Voici un exemple de liste allant de 0 à 9 inclus:

```python
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Etant donné qu'on peut créer des listes plus compliqués, Python vous donne un moyen de créer cela avec `range` (ce que vous avez vu rapidement dans de précédents exercices). Tout comme ce mot-clé où vous pouvez *itérer* à travers, vous pouvez aussi itérer à travers une liste avec une boucle `for`. Compte tenu du fait que `range` ne donne pas exactement une liste si vous essayez de regarder son type (on y reviendra dessus), il faut le convertir avec `list(.)`.

Exemple:

```python
ma_liste = list(range(5))
```

Exemple d'itération à travers une liste:

```python
noms = ["Bob", "Alice", "Charlie"]
for nom_utilisateur in noms:
    print(f"Nom utilisateur: {nom_utilisateur}")
```

Vous pouvez aussi utiliser les indexes pour accéder à des éléments de la liste:

```python
print(noms[0])  # Affiche le premier nom
print(noms[1])  # Affiche le deuxième
# Vous pouvez faire une boucle

for i in range(len(noms)):  # len donne aussi le nb d'éléments dans la liste
    print(noms[i])  # i est l'indice/index 
```

**TODO** :

- Créez une liste allant de 10 et 20 (inclus) avec un saut de 2.
- Créez une liste vide
- Avec une boucle for, mettez au carré les valeurs dans la liste et stockez cela dans la liste vide avec `append`.
- Affichez votre liste

**Indices/Rappels/Remarques** :

- Range peut prendre 3 valeurs entre les parenthèses au lieu de juste un: debut, fin pas inclus, saut.
- Append est utilisé comme ça: `ma_liste.append(nouveau_element)` où `nouveau_element` est par exemple un entier.
- En Python, vous pouvez directement affichez votre liste en faisant un `print` de votre variable. Cela ne marche pas en C où il faut print un par un les éléments de la liste/du tableau.

## Exercice 5 - In-place

**TODO**:

- Créez une liste allant de 10 à 20 (inclus) avec un saut de 2.
- Avec une boucle for allant à travers les différents indices, mettez au carré les valeurs de la liste en restockant directement dedans (in-place modification).
- Affichez votre liste

## Exercice 6 - Mutabilité des listes

Cet exercice vous montre qu'il y a des variables qui peuvent être modifiés implicitement donc il faut faire très attention.

**TODO**: 

- Créez une liste `a` allant de 0 à 9 (inclus)
- Créez une liste `b = a`
- Avec une boucle for allant à travers les différents indices, mettez au carré les valeurs de la liste en restockant directement dans `a` (in-place).
- Affichez les deux listes
- Réfléchissez à ce qu'il s'est passé

## Exercice 7 - Slicing et .split()

Tout comme vous pouvez extraire une sous-chaîne de caractères d'une chaîne de caractères, vous pouvez aussi extraire une sous-liste d'une liste en utilisant `ma_liste[debut:finpasinclus:saut]` où `debut`, `finpasinclus` et `saut` sont des `int`. Si vous ne spécifiez pas certains entiers, ils sont considérés comme: 0, `len(ma_liste)` et 1 respectivement par défaut.

Exemple:

```python
l = [1, 2, 3, 4, 5]
print(l[::2])
print(l[::])
print(l[:-1:2])
print(l[::-1])
```

De plus, comme l'on peut convertir un string en un entier (lorsque possible), on peut aussi convertir un string en une liste de chaînes de caractères:

- Utiliser `list(ma_chaine)` donnerait une liste où chaque élément contient un caractère 
- Utiliser `ma_chaine.split()` crée une liste de mots !


**Contexte**: Vous avez plusieurs textes que vous pouvez convertir en listes de mots et voulez entrainer un modèle (Transformer, le T dans GPT) à prédire le prochain mot à partir des mots précédents. Pour entrainer ce modèle efficacement, on voudrait que pour chaque $i$-ème mot dans un texte, la prédiction du prochain mot (le $i+1$-ème) soit correcte.

Par exemple, si on a un texte / une séquence de mots: "The quick brown fox jumps over the lazy dog \<END\>". Le modèle serait entrainé sur des données pré-traitées de sorte à prédire "quick" à partir de "The", "fox" à partir de "The" et "quick", etc.

**TODO** :

- Créez une liste de mots à partir de la chaîne de caractère: "The quick brown fox jumps over the lazy dog \<END\>"
- Créez deux listes `input_sequence` et `target_sequence` basées sur la première liste et en utilisant le "slicing" introduit précédemment:
    - `input_sequence` commence à "The" et se termine à "dog"
    - `target_sequence` commence à "quick" et se termine à "\<END\>"

Le modèle serait entrainé sur ces données pré-traitées de sorte à prédire "quick" à partir de "The", "fox" à partir de "The" et "quick", etc.

