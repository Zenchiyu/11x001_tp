# [11X001] TP n°8
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
- Les **solutions partielles** seront fournies une semaine après le TP. 


---

## Exercice 1

Vous avez vu les chaines de caractères en cours comme un tableau de caractères et pouvez l'afficher comme ci-dessous:

```c
char ma_chaine[] = "bonjour";
printf("Voici ma chaine: %s\n", ma_chaine); // %s indique le format pour les chaines de caractères
```

**TODO**: Affichez caractère par caractère, séparé par des tirets, avec une boucle `for` la chaîne de caractère ci-dessous:

```c
char ma_chaine[] = "J'aime les pizzas";
```

**Indice(s)**:

- Pour accéder au i-ème élément de la chaîne de caractères, vous pouvez utiliser `ma_chaine[i]` tout comme en Python
- Vous pouvez utiliser `%c` au lieu de `%s`.

## Exercice 2

Voici une chaine de caractères

```c
char ma_chaine[] = "On est à Genève";
```

**TODO**: Affichez avec un printf le caractère `ma_chaine[i]` pour `i` entier valant `20` puis essayez avec `i` valant `1000000`.

**Remarque(s)**:
- Contrairement à Python, le C peut afficher des choses en dehors du tableau (ici tableau de caractères). Ce comportement est indéfini et peut potentiellement dépendre du système.
- Dépendant du compilateur, vous aurez peut-être des warnings mais cela compile toujours (pas d'erreur de compilation).
- On peut souvent faire des erreurs de Segmentation fault en C. Vous reverrez ce que cela signifie plus tard.

## Exercice 3

**TODO**: Ecrivez deux boucles `for` pour construire/afficher un escalier de hauteur `height` (entier déclarée au début du code).

Exemple pour `height=5`, cela devrait afficher:

```bash
*
**
***
****
*****
```


## Exercice 4 - Post-incrément/décrément, pré-incrément/décrément et affectation composée

```c
int x = 42;
printf("++x: %d\n", ++x);
printf("x après %d\n\n", x);

x = 42;
printf("x++: %d\n", x++);
printf("x après %d\n\n", x);

x = 42;
printf("x+=1: %d\n", x += 1);
printf("x après %d\n\n", x);
```

**TODO**: Essayez de comprendre le code ci-dessus puis reéssayez avec `-` au lieu de `+`.

## Exercice 5

Le concept de fonction que nous avons vu en Python peut être appliqué en C. Cependant vous devez aussi écrire dans la signature/en-tête de la fonction le type de chaque argument ainsi que le type de retour.

Exemple:
```c
#include <stdio.h>

int add(int x, int y) { // le int tout à gauche correspond au type de sortie
    return x + y;
}

int main(void) {
    // L'appel se trouve dans la fonction main
    int z = add(5, 3);
    printf("z = 5 + 3 = %d\n", z);
    return 0;
}
```

**TODO**: Ecrivez une fonction `square` qui prend un int et retourne un int qui est son carré. Testez votre fonction en appelant votre fonction avec `5`, depuis le corps de la fonction exercice5.

**Remarque(s)**:
- `**` ne marche pas ici comme en Python.

## Exercice 6

**TODO**: Testez votre fonction avec `3.0`, `3.14` puis `hello`. Pour cela, appelez votre fonction depuis le corps de la fonction exercice6.

**Remarque(s)**:
- Python est plus laxiste.

## Exercice 7 - Opérations booléennes

Vous avez vu en cours que
```c
int ouch = 3 < 4 < 2;
printf("%d\n", ouch);
```
affiche $1$.

**TODO**: Comparer ce résultat avec ce que donnerait un code Python qui affiche `3 < 4 < 2`.

## Exercice 8 (Optionnel)

Le but de cet exercice est de comprendre la représentation en mémoire d'un nombre entier et d'illustrer la limitation dite de *dépassement d'entier*, ou **integer overflow** en anglais.

--- 

### Principe

#### Rappel sur les bases 

- Nous avons l'habitude de considérer les nombres en **décimal** (base 10). Prenons quelques exemples : 
    - Le nombre 42 : les chiffres '4' et '2' signifient **4** x 10 + **2** x 1, qu'on écrira **4** x 10^1 + **2** x 10^0
    - Le nombre 591 : les chiffres '5', '9' et '1' signifient **5** x 10^2 + **9** x 10^1 + **1** x 10^0
- Mais on peut en fait représenter les nombres dans la base que l'on veut. Par exemple : 
    - Le nombre 42 en base 8 se décompose comme **5** x 8^1 + **2** x 8^0 et s'écrit donc '52'
    - Le nombre 591 en base 5 se décompose comme **4** x 5^3 + **3** x 5^2 + **3** x 5^1 + **1** x 5^0 et s'écrit donc '4331'
- Dans un ordinateur, les nombres sont représentés en **binaire** (base 2). Par exemple : 
    - Le nombre 42 en base 2 se décompose comme **1** x 2^5 + **0** x 2^4 + **1** x 2^3 + **0** x 2^2 + **1** x 2^1 + **0** x 2^0 et s'écrit donc '101010'
    - Le nombre 591 en base 2 se décompose comme **1** x 2^9 + **0** x 2^8 + **0** x 2^7 + **1** x 2^6 + **0** x 2^5 + **0** x 2^4 + **1** x 2^3 + **1** x 2^2 + **1** x 2^1 + **1** x 2^0 et s'écrit donc '1001001111'

#### Stockage d'un entier 

Comme la mémoire d'un ordinateur n'est pas infinie, il faut décider combien de bits on utilise au maximum pour stocker un nombre entier.

Par exemple : 
- Si on décide d'utiliser 1 bit, on pourra stocker les nombres '0' et '1'
- Si on décide d'utiliser 2 bits, on pourra stocker les nombres '00', '01', '10' et '11' (correspondants en décimal à 0, 1, 2 et 3).
- Si on décide d'utiliser 3 bits, on pourra stocker les nombres '000', '001', '010', '011', '100', '101', '110', '111',  (correspondants en décimal à 0, 1, 2, 3, 4, 5, 6 et 7).

On voit qu'à chaque fois qu'on rajoute un bit, on double le nombre d'entiers que l'on peut représenter. Ainsi, si on décide d'utiliser **n** bits, on pourra représenter **2^n** entiers.

Par exemple, avec 8 bits, on peut stocker 2^8 entiers (les nombres de 0 à 255) : 
- 0 s'écrit '00000000'
- 1 s'écrit '00000001'
- 27 s'écrit '00011011'
- 254 s'écrit '11111110'
- 255 s'écrit '11111111'

#### Dépassement d'entier / integer overflow

Mais alors, comment stocker 256 avec 8 bits ? En binaire, 256 s'écrit '100000000' (un '1' suivi de huit '0'). Comme on ne dispose que de 8 bits, on tronque le 9ème bit et on obtient donc '00000000', ce qui correspond au nombre 0. On ne peut donc pas représenter un nombre supérieur ou égal à 256 avec seulement 8 bits.

De même, 259 s'écrit '100000011'. On tronque le 9ème bit et on obtient '00000011', ce qui correspond au nombre 3.

Ce phénomène s'appelle un **integer overflow** : quand un nombre est trop grand pour rentrer dans le nombre de bits dont on dispose, on tronque les bits en trop et on obtient donc un autre nombre. Ceci est la plupart du temps indésirable et constitue une source de bug à surveiller !

**Remarque** : On obtient en fait le nombre de départ modulo 2^n (avec n le nombre de bits utilisés). Par exemple, avec 8 bits, 259 % 2^8 = 3. 

---

### Mise en pratique

- **TODO**: Observer / comprendre / jouer avec le code fourni dans la fonction `exercice9`. 

**Remarque** : On utilise le type `unsigned char` car il permet de stocker des nombres entiers sur 8 bits, comme dans l'explication précédente.

- **TODO (plus avancé)** : Reproduire le même exemple mais avec le type `int`. En particulier, vous pouvez : 
    - Déclarer une nouvelle variable de type `int`.
    - Utiliser la fonction `sizeof` sur cette variable, pour savoir sur combien d'octets est stocké un `int` (multiplier par 8 pour avoir le résultat en bits).
    - Créer un overflow en affectant un nombre supérieur à la capacité maximale du type `int`. 

**Remarque** : Le type `int` est **signé**, ce qui veut dire qu'il permet de représenter des nombres entiers négatifs. Avec n bits, on garde un bit pour représenter le signe et les bits restants servent à encoder la valeur. Ainsi, avec 8 bits, on représentera les entiers de -128 à +127 si notre type est signé, et les entiers de 0 à 255 si notre type n'est pas signé. **Cela explique pourquoi l'overflow apparait dès 2^31 et non à 2^32.**

**Pour aller plus loin** : Pour que l'addition des représentations binaires soit en accord avec ce que l'on attend (addition classique d'entiers relatifs), on représente les entiers négatifs avec leur complément à 2^n : voir [cet article Wikipédia sur le complément à deux](https://fr.wikipedia.org/wiki/Compl%C3%A9ment_%C3%A0_deux) pour en savoir plus.


