# [11X001] TP n°10

---

Université de Genève, cours [11X001 Introduction à la Programmation des Algorithmes](https://wwwi.unige.ch/cursus/programme-des-cours/web/teachings/details/2021-11X001).

---

**Remarque générale**

Pour les exercices de ce TD, implémenter vos fonctions dans le fichier `main.c` dans la zone indiquée : 

```
/****************************/
/* Vos fonctions ci-dessous */ 
/****************************/



/****************************/
/* Vos fonctions ci-dessus **/ 
/****************************/

```

car le compilateur va vérifier qu'elles sont bien déclarées avant leur appel. 


---

## Exercice 1 
    
**TODO** : 
- Dans le fichier `main.c`, coder une fonction qu'on appelera `somme`, qui prend deux `float` en entrée et retourne leur somme.
- Dans le code de `exercice1`, décommenter la ligne correspondant à l'appel à votre fonction :    

```c
c = somme(a, b);
```

---


## Exercice 2
    
**TODO** : 
- Dans le fichier `main.c`, coder une fonction `puissance` qui prend deux nombres entiers `nombre` et `exposant` et retourne `nombre`^`exposant`. **Indice** : On pourra utiliser une boucle `for`.
- Dans la fonction `exercice2`, ajouter l'appel à votre fonction `puissance` pour calculer `nombre`^`exposant`.


---


## Exercice 3

**TODO** :

- Déclarer `p1` et `p2`, deux pointeurs vers un `int`. 
- Faire en sorte que `p1` pointe vers la variable `a` fournie.
- Utiliser `p1` pour soustraire 3 à `a`. 
- Ensuite, faire en sorte que `p2` pointe vers la même adresse mémoire que `p1`.
- Utiliser `p2` pour multiplier `a` par 6.

On pourra copier-coller la ligne fournie : `printf("a = %d (adresse : %p) \n", a, &a);` pour afficher la valeur et l'adresse de `a` au fur et à mesure des modifications.

Pour bien comprendre le rôle des deux pointeurs, on pourra également afficher leurs valeurs.


---


## Exercice 4 

La fonction `exercice4` est déjà complétée. Elle demande trois nombres entiers à l'utilisateur : `min`, `max` et `x` et fait appel à deux fonctions auxiliaires. 

Vous allez devoir compléter ces deux fonctions auxiliaires dont le but est de restreindre `x` à l'intervalle [`min`, `max`] : 

**Exemples** :

- Si `x` = 5, `min` = 2, `max` = 9, la valeur de `x` n'est pas modifiée.
- Si `x` = 5, `min` = 2, `max` = 3, la valeur de `x` est changée à 3.
- Si `x` = 5, `min` = 7, `max` = 9, la valeur de `x` est changée à 7.

Cet exercice a pour objectif de vous faire coder la restriction à l'intervalle de deux façons : l'une avec une fonction **pure** et l'autre avec une fonction **à effet de bord**.  

### Fonction pure (passage par valeur)

**TODO** : Compléter la fonction `restreindre_intervalle_pure` dont le squelette est fourni :

```c
int restreindre_intervalle_pure(int x, int min, int max) {

}
```

Elle retourne `min` si `x` est inférieure à `min`, `max` si `x` est supérieure à `max` et `x` sinon. 

Observer son appel dans la fonction `exercice4` : 

```c
x_restreint = restreindre_intervalle(x, min, max);
```

La variable `x` n'est pas directement modifiée.

### Fonction à effet de bord (passage par référence)

**TODO** : Compléter la fonction `restreindre_intervalle_bord` dont le squelette est fourni, et faire en sorte, en utilisant le pointeur passé en premier paramètre, que la variable soit **modifiée directement dans la fonction** :

```c
void restreindre_intervalle_bord(int *x, int min, int max) {

} 
```

Comme la variable est modifiée directement, notre fonction ne retourne rien (type `void`). 

Observer son appel dans la fonction `exercice4` (notamment le premier argument  est fourni grâce à l'opérateur `&` qui fournit l'adresse mémoire de notre variable `x`) :

```c
restreindre_intervalle_bord(&x, min, max); 
``` 

---


## Exercice 5

La fonction `exercice5` est partiellement complétée. Pour l'instant, elle demande à l'utilisateur deux nombres entiers `a` et `b` et les affiche.

**TODO** : 
- Coder une fonction `echange` qui prend en entrée deux `int` **par référence** et échange leurs valeurs. Votre fonction ne doit donc rien retourner (type `void`).
- Dans la fonction `exercice5`, ajouter l'appel à votre fonction `echange`.

**Indices** : 
- S'inspirer de la fonction `restreindre_intervalle_bord` de l'exercice 4 pour le passage par référence.
- Utiliser une variable auxiliaire pour stocker une des deux valeurs avant de faire l'échange.


---


## Exercice 6

La fonction `exercice6` est partiellement complétée. Pour l'instant, cinq `int` sont déclarés `int k, n, fact_k, fact_n, k_parmi_n;`, les valeurs de `k` et de `n` sont demandées à l'utilisateur avec un `scanf` et les valeurs de `fact_k`, `fact_n` et `k_parmi_n` sont affichées. 

**TODO** :

- Implémenter une fonction **récursive** que l'on nommera `factorielle` qui prend un entier `n` et retourne `n! = n x (n - 1) x ... x 2 x 1` (avec la convention `0! = 1`). 
- Implémenter une fonction que l'on nommera `coefficient_binomial` qui prend en entrée deux entiers `k` et `n` et retourne le nombre de combinaisons de `k` parmi `n`, que l'on calcule comme `n! / ( k! x (n - k)! )`.
- Dans la fonction `exercice6`, appeler votre fonction `factorielle` pour `k` puis pour `n` et stocker les valeurs obtenues dans les variables `fact_k` et `fact_n`.
- De même, affecter la sortie de la fonction `coefficient_binomial` à la variable `k_parmi_n`.

L'affichage est déjà implémenté. 

**Remarque** : On pourra optionnellement implémenter une fonction `factorielle_iteratif` sans appel récursif et avec une boucle `for` pour comparer avec l'implémentation récursive. 


---

## Exercice 7 : Recursive binary search

**TODO** : Ecrivez une fonction *récursive* (sans boucle while ni boucle for) `int rechercheDichotomique(int arr[], int low, int high, int x)` qui

- Retourne -1 si le `nombre` ne fait pas partie de la liste triée/ordonnée `ma_liste`
- Sinon, la fonction doit retourner son index (sa position, commençant à $0$) dans `ma_liste`.

Pour cela, vous devez utiliser l'algorithme suivant (appelé recherche dichotomique ou binary search en anglais):
- Trouver la position la plus centrale de la liste (si la liste est vide, retourner -1).
- Comparer la valeur de cette case à l'élément recherché.
- Si la valeur est égale à l'élément, alors retourner la position, sinon reprendre la procédure dans la moitié pertinente de la liste.

**Remarque(s)** :

- Cette méthode vous permet d'éviter de parcourir toute la liste ! C'est similaire à quand vous essayez de trouver un mot dans un dictionnaire non électronique (si vous en utilisez encore de nos jours).

---

## Exercice 8 : Allocation dynamique avec ``malloc`` et ``free``

**TODO** : compléter l'exercice dans le ``main_empty.c``. Pour le malloc, n'oubliez pas de convertir le résultat vers le bon type.


## Exercice 9 (optionnel) : Méthode de Héron

La [méthode de Héron](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_H%C3%A9ron#Approche_géométrique) est un algorithme pour calculer la racine carrée d'un nombre. 

**Algorithme** : 

- Soit `a` le nombre réel dont on cherche la racine `x`.
- Initialiser `x` à une valeur quelconque, par exemple 1 ou `a`. Attention, ne pas initialiser à zéro (pour éviter une division par zéro à l'étape suivante).
- Tant que `|x^2 - a| > precision`, mettre à jour `x` avec la valeur `(x + a/x) / 2`

**TODO** : Coder la fonction `racine_heron` qui prend deux `float` en entrée : `a` et `precision` et qui retourne la racine carrée de `a` calculée avec la méthode de Héron.

**Astuce** : Il peut être plus clair de coder séparément la fonctionnalité de valeur absolue, par exemple dans une fonction `float valeur_absolue(float x)`. 

**Amélioration** : Une meilleure valeur initiale pour `x` (plutôt que 1 ou `a`) est la partie entière de la racine carrée de `a`. Vous pouvez coder une fonction `initialiser_heron` qui prend un `float` en entrée et retourne la partie entière de sa racine (indice : on pourra par exemple utiliser avec une boucle `while`). Ensuite, appeler votre fonction `initialiser_heron` pour initialiser la valeur de `x` dans `racine_heron`.


---


## Exercice 10 (optionnel) : Calcul d'une valeur approchée de Pi 


On peut approximer Pi avec l'idée suivante : 

- Dans le plan 2D, parcourir une grille régulière du point (0, 0) au point (1, 1) (plus il y a de points sur cette grille, plus l'approximation sera précise). 
- Compter le nombre de points de la grille qui sont à l'intérieur du cercle unité (c'est-à-dire dont la distance à l'origine est inférieure à 1). 
- La proportion de points dans le cercle par rapport au nombre de points total de la grille correspond approximativement au rapport de l'aire du quart de disque unité (= Pi / 4) sur l'aire du carré délimité par la grille ( = 1), c'est-à-dire Pi / 4.
- Ainsi, la valeur approchée de Pi est donnée par `4 x nombre_de_points_dans_cercle_unite / nombre_total_de_points`. 

**TODO** : Implémenter une fonction que l'on nommera `approximer_pi` qui prend en entrée le nombre de points par axe de la grille et retourne une valeur approchée de Pi.

Autre explication de cette méthode [ici](https://fr.wikipedia.org/wiki/Approximation_de_%CF%80#Approximation_de_l'aire_d'un_disque_par_quadrillage).

