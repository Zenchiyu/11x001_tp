# [11X001] TD n°9

---

Université de Genève, cours [11X001 Introduction à la Programmation des Algorithmes](https://wwwi.unige.ch/cursus/programme-des-cours/web/teachings/details/2021-11X001).

---

## Rappel: scanf

Un programme peut lire un entier en entrée comme ceci:

```c
int mon_entier;
scanf("%d", &mon_entier);
```

et une chaîne de caractères comme cela:

```c
char ma_chaine[30];
scanf("%s", ma_chaine);
```

Comme on fera beaucoup appel à scanf, pour demander à l'utilisateur d'entrer une valeur, nous vous conseillons de bien comprendre son fonctionnement

---

## Exercice 1 

**TODO** : Lire un entier relatif et afficher s'il est strictement négatif, nul ou strictement positif.

---

## Exercice 2

**TODO**: Lire un entier naturel et afficher la somme des entiers naturels jusqu'à ce dernier (inclus) à l'aide d'une boucle `while`.  
**TODO**: Même consigne mais cette fois-ci une boucle `for` doit être utilisée.

---

## Exercice 3

**TODO** : Lire un entier compris entre 0 et 6 et afficher le jour de la semaine correspondant à l'aide d'un `if` / ` else if` / `else`.  
**TODO** : Même consigne mais cette fois-ci un `switch` doit être utilisé.

---

## Exercice 4

**TODO** : Lire 5 entiers, les stocker dans un tableau puis afficher la somme des éléments du tableau.  
**TODO** : Afficher le plus petit élément et le plus grand élément contenus dans ce tableau.

---

## Exercice 5

**TODO** : Lire le prénom et la note d'un étudiant d'IPA puis stocker ces informations dans une structure. Enfin, afficher un message indiquant si l'étudiant a validé la matière.  
**TODO** : Cette fois-ci les informations de 3 étudiants sont lues et stockées dans un tableau d'étudiants. Le tableau est ensuite parcouru pour indiquer si chaque étudiant a validé la matière.  
**TODO** : A l'aide de `sizeof` (qui donne le nombre d'octets/bytes en mémoire utilisés), afficher le nombre d'éléments contenus par le tableau d'étudiants.

---

## Exercice 6
Une compagnie aérienne souhaite appeler les passagers de ses différents vols par leurs prénoms et numéros de sièges:
- Un vol est composé d'un point de départ, d'une destination, d'une durée de vol et d'un tableau de passagers.
- Chaque passager est composé de son prénom et d'un numéro de siège.

**TODO** : 

- Déclarer les différentes structures nécessaires à la réalisation de cette tâche.
- Lire en entrée les informations de 3 passagers de 2 vols différents et créer les structures correspondantes puis stocker les vols dans un tableau.
- Pour chaque vol, afficher les informations du vol et appeler ses passagers.

---

## Exercice 7

Vous avez vu en cours le concept de portée de variable.

Exemple:

```c
#include <stdio.h>

int main(void) {
    int a = 42;
    {
        int a = 3;
        printf("a=%d\n", a);
    }
    printf("a=%d\n", a);
    return 0;
}
```

**TODO:** deviner les valeurs affichées

```c
#include <stdio.h>
int val = 100;

void showLocal() {
    int val = 10;
    printf("in showLocal: %d\n", val);
}

int main() {
    printf("before showLocal: %d\n", val);
    
    showLocal();
    
    printf("after showLocal: %d\n", val);

    if (1 < 2) {
        int val = 1000; 
        printf("in if block: %d\n", val);
    }

    return 0;
}
```
