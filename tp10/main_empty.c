#include <stdio.h>
#include <stdlib.h>


/****************************/
/* Vos fonctions ci-dessous */ 
/****************************/


// EXERCICE 1


// EXERCICE 2


// EXERCICE 4

int restreindre_intervalle_pure(int x, int min, int max) {
    /******************** Votre code ci-dessous ********************/
    /******************** Votre code ci-dessus ********************/
}

void restreindre_intervalle_bord(int *x, int min, int max) {
    /******************** Votre code ci-dessous ********************/
    /******************** Votre code ci-dessus ********************/
}

// EXERCICE 5

// EXERCICE 6

// EXERCICE 7

int rechercheDichotomique(int arr[], int low, int high, int x) {
    if (high >= low) {
        /******************** Votre code ci-dessous ********************/
        
        /******************** Votre code ci-dessus *********************/
    }
    return -1;
}

// EXERCICE 8


// EXERCICE 9 


/****************************/
/* Vos fonctions ci-dessus **/
/****************************/


void exercice1(void) {
    printf("\n\nEXERCICE 1\n\n");
    
    float a, b, c;
    
    printf("Entrer deux nombres à additioner : ");
    scanf("%f %f", &a, &b);
    
    // TODO : Décommenter la ligne suivante une fois que la fonction somme est implémentée
    // c = somme(a, b); 
    
    printf("%f + %f = %f\n", a, b, c);

    return;
}


void exercice2(void) {
    printf("\n\nEXERCICE 2\n\n");

    int nombre, exposant, resultat;

    printf("Entrer un nombre et un exposant (entiers) : ");
    scanf("%d %d", &nombre, &exposant); 

    /******************** Votre code ci-dessous ********************/
   
    /******************** Votre code ci-dessus *********************/

    printf("%d^%d = %d\n", nombre, exposant, resultat);

    return;
}


void exercice3(void) {
    printf("\n\nEXERCICE 3\n\n");
    
    int a = 10;
    printf("a = %d (adresse : %p) \n", a, &a);
    
    /******************** Votre code ci-dessous ********************/
    
    /******************** Votre code ci-dessus *********************/

    return;
}


void exercice4(void) {
    printf("\n\nEXERCICE 4\n\n");
    
    int x, min, max;
    
    printf("Entrer deux nombres entiers (intervalle [min, max]) : ");
    scanf("%d %d", &min, &max);
    
    printf("Entrer un nombre entier en dehors de cet intervalle : ");
    scanf("%d", &x);

    // Restriction à l'intervalle avec la version pure 
    int x_restreint = restreindre_intervalle_pure(x, min, max);
    printf("Après l'appel de la fonction pure, on a bien x_restreint = %d et x = %d (inchangée) \n", x_restreint, x);

    // Restriction à l'intervalle avec la version à effet de bord 
    restreindre_intervalle_bord(&x, min, max);
    printf("Après l'appel de la fonction à effet de bord, la variable x elle-même est changée et on a maintenant x = %d \n", x);

    return;
}


void exercice5(void) {
    printf("\n\nEXERCICE 5\n\n");

    int a, b;
    printf("Entrer deux nombres (a et b): ");
    scanf("%d %d", &a, &b);

    printf("Avant l'échange, a = %d et b = %d \n", a, b);
    
    /******************** Votre code ci-dessous ********************/

    /******************** Votre code ci-dessus *********************/

    printf("Après l'échange, a = %d et b = %d \n", a, b);
    
    return;
}


void exercice6(void) {
    printf("\n\nEXERCICE 6\n\n");
    
    int k, n, fact_k, fact_n, k_parmi_n;
    
    printf("k = ");
    scanf("%d", &k);

    printf("n = ");
    scanf("%d", &n);

    /******************** Votre code ci-dessous ********************/
    
    /******************** Votre code ci-dessus *********************/

    printf("%d! = %d\n", k, fact_k);
    printf("%d! = %d\n", n, fact_n);
    printf("%d parmi %d = %d\n", k, n, k_parmi_n);

    return;
}


void exercice7(void) {
    printf("\n\nEXERCICE 7\n\n");

    int arr[] = { 1, 5, 6, 9, 12, 28 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 12;
    int result = rechercheDichotomique(arr, 0, n - 1, x);
    if (result == -1) printf("L'élément n'est pas dans le tableau");
    else printf("L'élément est dans le tableau à l'index %d", result);

    return;
}

void exercice8(void) {
    printf("\n\nEXERCICE 8\n\n");
    
    int n, i;
    int *arr;

    printf("Enter the number of elements: ");
    scanf("%d", &n);

    // 1. TODO: Allouez la mémoire pour 'n' int avec malloc
    // arr = ...
    
    // 2. TODO: Vérifiez si l'allocation a échoué
    int check; // assignez la bonne condition à check
    if (check) {
        printf("Memory allocation failed!\n");
        return;
    }

    for (i = 0; i < n; i++) {
        arr[i] = i + 1;
        // *(arr + i) = i + 1; // equivalent
    }

    printf("The elements are: ");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    // 3. TODO: Libérez la mémoire
    // ...

    return;
}

void exercice9(void) {
    printf("\n\nEXERCICE 9\n\n");
    
    float a, x, precision;
    printf("*** Méthode de Héron ***\n\n");
    printf("Entrer le nombre dont vous voulez calculer la racine carrée : ");
    scanf("%f", &a);
    printf("Entrer la précision souhaitée : ");
    scanf("%f", &precision);
    
    // TODO : Décommenter la ligne suivante une fois que la fonction ,'racine_heron' est implémentée
    // x = racine_heron(a, precision);

    printf("Racine carrée de %f = %f\n", a, x);

    return;
}


void exercice10(void) {
    printf("\n\nEXERCICE 10\n\n");
    
    printf("Approximation de PI\n\n");
    
    int nb_points_par_axe;
    printf("Entrer le nombre de points à utiliser par axe --- /!\\ au delà des 10 000 points par axe (100 millions de points au total) le calcul commence à être vraiment long !! : ");
    scanf("%d", &nb_points_par_axe);

    /******************** Votre code ci-dessous ********************/
        
    /******************** Votre code ci-dessus *********************/

    return;
}


int main(void) {

    // Astuce : commenter tous les exercices sauf celui en cours pour gagner du temps !

    exercice1();
    exercice2();
    exercice3();
    exercice4();
    exercice5();
    exercice6();
    exercice7();
    exercice8();
    exercice9();
    exercice10();
    
    return 0;
}