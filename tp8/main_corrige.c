#include <math.h>
#include <stdio.h>


void exercice1(void){
    printf("\n\nEXERCICE 1\n\n");
    
    char ma_chaine[] = "J'aime les pizzas"; // déclaration et affectation
    
    /******************** Votre code ci-dessous ********************/
    for (int i = 0; i < sizeof(ma_chaine); i++) {
        printf("%c-", ma_chaine[i]);
    }
    printf("\n");
    /******************** Votre code ci-dessus *********************/
    
    return;
}


void exercice2(void){
    printf("\n\nEXERCICE 2\n\n");
    
    char ma_chaine[] = "On est a Geneve";
    
    /******************** Votre code ci-dessous ********************/
    /* Avec une boucle
    for (int i = 0; i < 1000000; i++) {
        printf("%c\n", ma_chaine[i]);
    }
    */
    // Sans boucle (comme demandé dans l'énoncé)
    printf("%c\n", ma_chaine[20]);
    // printf("%c\n", ma_chaine[1000000]);  // en commentaire car sinon à l'exécution on a un segfault et ne pourrait pas voir le résultat des autres exercices
    // on reviendra sur le concept de mémoire. Segfault veut dire qu'on a essayé d'accéder à une zone de la mémoire non permise
    /******************** Votre code ci-dessus *********************/
    
    return;
}


void exercice3(void) {
    printf("\n\nEXERCICE 3\n\n");

    int height = 7;
    
    /******************** Votre code ci-dessous ********************/
    for (int i = 0; i < height; i++) {
        for (int j = 0; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }
    /******************** Votre code ci-dessus *********************/

    return;
}

void exercice4(void) {
    printf("\n\nEXERCICE 4\n\n");

    int x = 42;
    printf("++x: %d\n", ++x);
    printf("x après %d\n\n", x);

    x = 42;
    printf("x++: %d\n", x++);
    printf("x après %d\n\n", x);

    x = 42;
    printf("x+=1: %d\n", x += 1);
    printf("x après %d\n\n", x);

    /******************** Votre code ci-dessous ********************/
    // Same with --
    x = 42;
    printf("--x: %d\n", --x);
    printf("x après %d\n\n", x);

    x = 42;
    printf("x--: %d\n", x--);
    printf("x après %d\n\n", x);

    x = 42;
    printf("x-=1: %d\n", x -= 1);
    printf("x après %d\n\n", x);

    /******************** Votre code ci-dessus *********************/
    
    return;
}

/******************** Votre fonction ci-dessous ********************/
// fonction carre
int square(int x) {
    return x * x; // pas de x**2 possible. Si vous utilisez math.h, n'oubliez pas -lm quand vous utilisez la commande clang pour compiler
}

int add(int x, int y) {
    return x + y;
}

/******************** Votre fonction ci-dessus *********************/

void exercice5(void) {
    printf("\n\nEXERCICE 5\n\n");
   
    /******************** Votre code ci-dessous ********************/
    int y = square(5);
    printf("%d\n", y);
    /******************** Votre code ci-dessus *********************/

    return;
}


void exercice6(void) {
    printf("\n\nEXERCICE 6\n\n");
    
    /******************** Votre code ci-dessous ********************/
    int y = square(3.14);
    // Essayez aussi d'additionner deux chaines de caractères en C et comparez avec le Python (avec la fonction add ci-dessus)
    // Essayez de multiplier une chaine de caracteres par un nombre et comparez avec le Python
    printf("%d\n", y);

    /******************** Votre code ci-dessus *********************/

    return;
}

void exercice7(void) {
    printf("\n\nEXERCICE 7\n\n");
    
    int ouch = 3 < 4 < 2;
    /*
    Dependant de la version du compilateur ou de la machine, cela 
    peut donner une erreur a la compilation ou un warning a la place.
    
    clang version 21.1.6 sur une machine linux -> error: chained comparison
    clang version 17.0.0 sur une macbook -> warning à la place
     */
    printf("%d\n", ouch);

    return;
}

void exercice8(void) {
    printf("\n\nEXERCICE 8\n\n");
    
    /**************************************************************/
    /********* Exemple d'overflow du type 'unsigned char' *********/
    /**************************************************************/

    unsigned char a, b, c;

    // Vérifions qu'un 'unsigned char' occupe bien 8 bits
    int size_of_unsigned_char = sizeof(a);
    printf("Le type 'unsigned char' utilise %d octets, c'est-à-dire %d bits.\n", size_of_unsigned_char, 8 * size_of_unsigned_char);

    // Exemple d'overflow
    a = 61;
    b = 213;
    c = a + b;  // Overflow : c ne vaut pas 61 + 213 = 274 mais 274 % 256 = 18
    printf("%d + %d = %d\n", a, b, c);
    
    /*************************************/
    /********* Fin de l'exemple *********/
    /*************************************/


    /******************** Votre code ci-dessous ********************/
    int x, y, z;
    
    int size_of_int = sizeof(x);    // 32 bits -> 4 octets/bytes. On peut avoir des nombres negatifs avec ce type
    printf("Le type 'int' utilise %d octets, c'est-à-dire %d bits.\n", size_of_int, 8 * size_of_int);

    // Exemple d'overflow
    x = 2147483647; // le plus grand nombre positif est 2^31 - 1
    y = 1;          
    z = x + y;  // Overflow : z ne vaut pas 2^31 car le bit de poids le plus fort a changé -> le signe change. Voir complément à deux
    printf("%d + %d = %d\n", x, y, z);
    
    /*************************************/
    /********* Fin de l'exemple *********/

   
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

    return 0;
}
