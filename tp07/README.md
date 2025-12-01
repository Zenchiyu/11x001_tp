# [11X001] TP n°7
---

Université de Genève, cours [11x001 Introduction à la Programmation des Algorithmes](https://pgc.unige.ch/main/teachings/details/2025-11X001)

---

## Consignes générales (pour tous les TPs de C)

- La **consigne** de chaque exercice est dans le fichier `README.md`. Les **TODO** indiquent des consignes à suivre.
- Le **code** des exercices est dans le fichier `main.c`. Chaque exercice correspond à une fonction dans ce fichier, nommée `exercice1` pour l'exercice 1, `exercice2` pour l'exercice 2 etc.
- L'endroit où vous êtes supposés écrire votre code est délimité comme suit : 

```c 
/******************** Votre code ci-dessous ********************/
    


/******************** Votre code ci-dessus *********************/
```

- Pour compiler et exécuter votre programme, vous pouvez taper `clang <nom_fichier>.c -o <nom_executable>` puis `./<nom_executable>`. 
- Les **solutions partielles** seront fournies une semaine après le TD. 


---

## Exercice 0 - Exceptions en Python

Comme dernier exercice de Python (à écrire dans un fichier à part):

**TODO**: Ecrivez une fonction `divide` qui prend deux nombres et lève une `ValueError` si le nombre est plus petit ou égal à $0$, sinon retourne le premier nombre divisé par le second.


---

## Exercice 1 - Du C

**TODO**: Écrire un programme qui affiche votre nom, date de naissance et adresse e-mail. Par exemple, il affichera : 

```
Nom     : Michel LAMBDA
Né le   : 31.10.2001
Contact : michel.lambda@unige.ch
```

**TODO**: Qu'est-ce qui a changé entre le `print` en Python et le `printf` en C ?

--- 

## Exercice 2

**TODO** : Déclarer et affecter cinq variables de type `char` correspondant aux cinq caractères qui composent le mot *UNIGE*.

**TODO** : Afficher le mot *UNIGE* caractère par caractère, d'abord à l'endroit, puis à l'envers, en utilisant `printf` et ces cinq variables.

> **Astuce** : Pour injecter une variable dans l'affichage de `printf`, utiliser : 
- `%c` pour une variable de type `char`
- `%d` pour une variable de type `int`
- `%f` pour une variable de type `float`

> Par exemple : 
```c 
printf("Première lettre = %c", 'a');            // Affiche "Première lettre = a"
printf("2 x 6 = %d x %d = %d", 3, 4, 6 + 6);    // Affiche "2 x 6 = 3 x 4 = 12"
printf("Racine de 2 vaut environ %f", 1.41421); // Affiche "Racine de 2 vaut environ 1.41421"
```

---


## Exercice 3

**TODO** : Calculer et afficher la surface et le volume d'un cylindre de rayon $r$ et de hauteur $h$.  

**Astuce** : L'astuce de l'exercice 2 est utile ici aussi.

**Remarques** :

- Pour la valeur de Pi, utiliser la variable `PI`, définie au début de l'exercice : 

```c
const float PI = 3.1415926535;
```

- Le rayon et la hauteur du cylindre sont des `float` déjà donnés.

```c
float radius = 10;
float height = 5; 
```


---


## Exercice 4

**TODO** : Calculer son âge en jours et stocker le résultat dans la variable `age_in_day`. Pour faire simple, on ignore les années bissextiles et on considère qu'un mois fait toujours 30 jours, et donc qu'un an fait 360 jours.

```c
int birth_year = 2000;
int birth_month = 01;
int birth_day = 01;  // Déclaration et affectation des variables 
```


---


## Exercice 5

**TODO** : Convertir en jours, semaines, années le nombre de jours stocké dans la variable `nb_of_days`. Vous pouvez considérer qu'un an fait toujours 365 jours.

```c
int nb_of_days = 2153;
```


**Exemple** : Si l'utilisateur entre le nombre 2153, on veut afficher : 

```
2153 jours font 5 année(s), 46 semaine(s) et 6 jour(s).
```

**TODO** : Réfléchissez à la différence entre `//` en Python et `/` en C entre deux entiers.

---


## Exercice 6

**TODO** : Observer le code de l'exercice : 

```c 
int a = 7, b = 2;
float c;  

c = a / b; // Ne modifier que cette ligne

printf("%d / %d = %f \n", a, b, c); 
```

Il affiche : 
```
7 / 2 = 3.000000
```

**TODO** : Utiliser une conversion explicite en `float` pour que votre code affiche : 
```
7 / 2 = 3.500000
```

**Remarque**: Ne modifier que la ligne indiquée. En particulier, ne pas changer les types de `a`, `b` et `c` lors de leur déclaration.


---

## Exercice 7

Vous avez vu les `if`, `elif` et `else` en Python, c'est similaire en C avec `if`, `else if` et `else`

```python
# En Python
x = 40
if x != 42:
    print("Not 42")
elif x != 42:
    print("Not 42")
else:
    print("42")
```

```c
// En C
int x = 40;
if (x != 42) {
    printf("Not 42\n");
}
else if (x != 42) {
    printf("Not 42\n");
}
else {
    printf("42\n");
}
```

**Contexte** : On vous demande d'écrire un code qui définit un nombre entre $0$ et $9$ correspondant à la catégorie d'une image montrée à l'écran. Cela permettrait d'obtenir un ensemble de données permettant l'entrainement d'un modèle en IA pour de la classification d'images.

**TODO** :
- Si le nombre défini n'est pas dans la plage souhaitée, affichez avec `printf` qu'il fallait rentrer un nombre valide.


## Exercice 8

En C, il existe aussi le `do...while` (qui n'existe pas en Python) qui exécute le corps de la boucle une fois avant de vérifier la condition contrairement au ``while``, qui ne rentre pas dans le corps si la condition est fausse.

Exemple:

```c
int x = 42;
do {
    printf("J'affiche même si x vaut 42\n");
} while (x != 42);  // attention à ce dernier point-virgule
```

**TODO**:  Comprendre la syntaxe du ``do...while``.

## Exercice 9

Vous avez vu les boucles `for` en Python. Contrairement à Python, les boucles `for` en C sont similaires aux boucles `while`.

Exemple:

```c
// En C
for (int i=0; i < 10; i++) {
    printf("%d\n", i);
}
```

**TODO**:  Comprendre la syntaxe du ``for``.
