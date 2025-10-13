# [11x001] TP n° 4

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

## Commentaire
Plutôt que de créer par vous-même des listes, vous pouvez les générer aléatoirement grâce au code ci-dessous:

```python
import random
random.seed(42)
# Liste pseudo-aléatoire avec seed fixée (la liste ne change pas si vous relancez)
ma_liste = [random.randrange(100) for _ in range(20)]   # 20 nombres
# Cette façon de créer des listes s'appelle "list comprehension" et s'exécute
# généralement plus rapidement qu'une boucle for en plusieurs lignes.
# Cependant, par soucis de compréhension, il est des fois préférable d'écrire
# la boucle sur plusieurs lignes.
# Le _ entre le for et le in permet d'ignorer l'indice de boucle qui ne nous intéresse pas ici.
```

## Exercice 1

**TODO** : Ecrivez une fonction *itérative* (avec boucles while ou for) `def rechercheDichotomique(nombre, ma_liste)` qui

- Retourne -1 si le `nombre` ne fait pas partie de la liste triée/ordonnée `ma_liste`
- Sinon, la fonction doit retourner son index (sa position, commençant à $0$) dans `ma_liste`.

Pour cela, vous devez utiliser l'algorithme suivant (appelé recherche dichotomique ou binary search en anglais):
- Trouver la position la plus centrale de la liste (si la liste est vide, retourner -1).
- Comparer la valeur de cette case à l'élément recherché.
- Si la valeur est égale à l'élément, alors retourner la position, sinon reprendre la procédure dans la moitié pertinente de la liste.

**Remarque(s)** :

- Cette méthode vous permet d'éviter de parcourir toute la liste ! C'est similaire à quand vous essayez de trouver un mot dans un dictionnaire non électronique (si vous en utilisez encore de nos jours).
- En pratique, nous aurions juste pu faire `nombre in ma_liste` pour tester si le nombre est dans la liste mais là on vous demande de traverser la liste et retrouver l'indexe.
- On vous demande une version *itérative* alors qu'une version *récursive* est plus naturelle avec la description que nous avons donné.

## Exercice 2

Vous avez vu les fonctions et que c'est possible d'utiliser des `print` dedans ou appeler d'autres fonctions.

**TODO** : Créez deux fonctions:

- Une fonction `somme(x, y)` qui retourne `x + y`
- Une fonction `mafct(x, y)` qui retourne calcule (x + y)^2 mais en appelant/utilisant le fonction `somme`

**TODO** : Réfléchissez à l'ordre des instructions et l'endroit où vous vous trouvez dans le code durant l'exécution du programme. Comparez votre réflexion avec ce qui se passe réellement en utilisant le debugger ou des prints.

## Exercice 3 - Short-circuit/minimal evaluation

Les opérandes d'une expression booléenne ne sont pas toutes exécutées s'il est possible de déterminer le résultat de l'opération juste avec les premières opérandes.
Cela s'appelle en anglais "short-circuit evaluation".

**TODO** : Testez et essayez de comprendre les codes ci-dessous:

```python
liste = []
if True or liste[0]:    # Normalement liste[0] devrait donner une erreur !
    print(liste)
```

puis essayez

```python
liste = []
if liste[0] or True:
    print(liste)
```

Mathématiquement, c'est censé être la même chose mais ce n'est pas la même chose en pratique ! Vous pouvez aussi visiter les liens ci-dessous pour plus d'explications.


**Liens** :
- https://en.wikipedia.org/wiki/Lazy_evaluation
- https://en.wikipedia.org/wiki/Short-circuit_evaluation
- https://www.geeksforgeeks.org/python/short-circuiting-techniques-python/

## Exercice 4 - Calcul de moyenne

Vous avez codé une fonction qui calcule la somme des éléments d'une liste dans le TP2.  

Rappel:

$$\bar x = \frac{1}{n}\sum_{i=1}^{n} x_i$$

**TODO**:
- Créez une nouvelle fonction `moyenne_liste` qui renvoie la moyenne des éléments d'une liste. Vous devez appeler la fonction `somme_liste` créée dans le TP2. Aucune boucle n'est nécessaire dans `moyenne_liste`.


```python
def moyenne_liste(liste):
    # la fonction `somme_liste` doit être appelée
    return
```

## Exercice 5 - Calcul du produit scalaire (dot product)

**TODO**:
- Créez une fonction `dot_product` qui calcule le produit scalaire entre deux listes. Vous devez encore utiliser `somme_liste` mais il y a une étape en plus, à vous de la trouver (une nouvelle fonction pourra être créée).

Rappel:  

$$\langle  x ,y \rangle \ = x^Ty = \sum_{i=1}^{n} x_i.y_i $$

```python
def dot_product(liste1, liste2):
    assert len(liste1) == len(liste2), "Les listes doivent être de même taille"
    # la fonction `somme_liste` doit être appelée
    return
```

## Exercice 6 - Calcul de moyenne pondérée

**TODO**:
* Créez une fonction qui calcule la moyenne pondérée à partir de deux listes (une pour les valeurs, une pour les poids). Vous avez déjà crée toutes les fonctions nécessaires pour faire ce calcul, la fonction doit faire 3 lignes maximum (sans compter le *assert*).  

Rappel:

$$\bar x_w = \frac{\sum\limits_{i=1}^{n} x_i.w_i}{\sum\limits_{i=1}^{n} w_i}$$

```python
def moyenne_ponderee_liste(liste_valeur, liste_poids):
    assert len(liste_valeur) == len(liste_poids), "Les listes doivent être de même taille"
    # les fonctions prédédantes doivent être appelées
    return
```

## Exercice 7 - Nombres complexes

Un nombre complexe est composé d'une partie réelle `a` et d'une partie imaginaire `b` et s'écrit sous la forme: $z=a+ib$ avec $i^2=-1$.  
On représentera un nombre complexe par une liste de deux éléments (partie réelle, partie imaginaire).  
Vous devrez afficher vos résultats en utilisant les `f-string` pour afficher les nombres complexes avec `i` si nécessaire.  
Pour calculer les module et argument d'un nombre complexe, vous aurez besoin d'importer la librairie `math` et les fonctions `sqrt` et `atan`.  

**TODO**:
* Créez une fonction qui affiche la somme de deux nombres complexes.
* Créez une fonction qui affiche le conjugué d'un nombre complexe.
* Créez une fonction qui affiche le module d'un nombre complexe.
* Créez une fonction qui affiche l'argument d'un nombre complexe.

Rappel:

Si $z_1=a_1+ib_1$ et $z_2=a_2+ib_2$, alors:

$$z_1+z_2=(a_1+a_2)+i(b_1+b_2) $$
$$\bar z_1= a_1-ib_1$$
$$|z_1| = \sqrt{a_1^2 + b_1^2}$$
$$\arg(z_1) = \arctan\left(\frac{b_1}{a_1}\right)$$

```python
def somme_complexe(z1, z2):
    assert len(z1) == len(z2) == 2
    return

def conjugue(z1):
    assert len(z1) == 2
    return

def module(z1):
    assert len(z1) == 2
    return

def argument(z1):
    assert len(z1) == 2
    return

z1 = [1, 3]
z2 = [4, -5]
```

## Exercice 8 - Multiplication matricielle (matrice avec vecteur)

Un vecteur ou une matrice (ou sa généralisation p.ex. pour les images RGB ou vidéos) regroupe des valeurs qui peuvent signifier différentes choses:

- Cela peut être des données qu'on veut traiter tel que les données d'un(e) patient(e) (p.ex. âge, hauteur, poids etc.), images, vidéos, etc.

- Cela peut être des données plus utilisées pour spécifier l'opération à appliquer aux données qu'on veut traiter. Cela peut correspondre à une opération linéaire ou affine (p.ex. pour faire tourner une image) ou les paramètres/poids d'un réseau de neurones artificiels.

Il existe des librairies qui vous donne des fonctions déjà implémentés pour faire des calculs matriciels (p.ex. NumPy, PyTorch, JAX). Notez que ces matrices ou vecteurs peuvent avoir des types différents quand vous utilisez la fonction `type`.

---

Sans ces librairies, vous pouvez représenter une matrice par des listes de listes et un vecteur par une liste. Cependant, vous devez implémenter par vous même les opérations pour faire des calculs dessus et cela peut être inefficace.

**TODO** : En utilisant votre fonction `dot_product` prenant deux listes de taille $n$ en entrée, implémentez une *fonction* prenant une liste de listes et une liste.
Votre fonction doit retourner le produit matrice-vecteur $y = A x$ où $A \in \mathbb{R}^{m \times n}$ et $x \in \mathbb{R}^{n}$ et $y \in \mathbb{R}^{m}$.

Vous pouvez prendre:
```python
A = [[1, 0], [0, -1]]
x = [1, 0]
```

**Rappel(s)** :

- Un produit matrice-vecteur équivaut à faire un produit scalaire (multiplier élément par élément deux vecteurs ensemble puis sommer le vecteur qui en résulte) entre chaque
ligne de la matrice $A$ et le vecteur $x$. Autrement dit, cela correspond à cette formule:

$$y_{i} = \sum_{j=1}^n A_{ij} x_{j},\quad i=1,\dots,m$$

où $y_{i}$ est le $i$-ème élément du vecteur $y$.

- Attention les indexes en Python commencent à 0 et non à 1.
- Le symbole $\sum$ indique une somme
- La liste de liste ci-dessous correspond à une matrice identité de taille $3 \times 3$:

```python
identity = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# Pour accéder à la première ligne: 
print(identity[0])
```

**Lien(s) et remarque(s)** :

- https://fr.wikipedia.org/wiki/Produit_matriciel
- La matrice $A$ peut être apprise par un algorithme d'apprentissage (les valeurs peuvent donc changer) et $y$ peut être la prédiction de votre modèle (p.ex. hauteur) pour une donnée $x$ (p.ex. poids de la personne). Cela peut donc être un petit modèle d'IA. 

