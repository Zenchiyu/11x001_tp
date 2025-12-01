#include <math.h>
#include <stdio.h>


void exercice1(void){
    printf("\n\nEXERCICE 1\n\n");
    
    printf("Bonjour monde !\n");

    printf("Nom\t: Michel LAMBDA\n");
    printf("Né le\t: 31.10.2001\n");
    printf("Contact\t: michel.lambda@unige.ch\n");
    
    return;
}


void exercice2(void){
    printf("\n\nEXERCICE 2\n\n");
    
    /******************** Votre code ci-dessous ********************/
    char v1 = 'U';
    char v2 = 'N';
    char v3 = 'I';
    char v4 = 'G';
    char v5 = 'E';
    printf("%c%c%c%c%c\n", v1, v2, v3, v4, v5);
    printf("%c%c%c%c%c\n", v5, v4, v3, v2, v1);
    /******************** Votre code ci-dessus *********************/
    
    return;
}


void exercice3(void) {
    printf("\n\nEXERCICE 3\n\n");

    const float PI = 3.1415926535;

    // Lecture du rayon
    float radius = 10;
    float height = 5; 
    
    /******************** Votre code ci-dessous ********************/
    float surface = PI * radius * radius * 2 + height * (2 * PI * radius);
    float volume = PI * radius * radius * height;

    printf("Surface: %f (en m2)\n", surface);
    printf("Volume: %f (en m3) \n", volume);
    /******************** Votre code ci-dessus *********************/

    return;
}

void exercice4(void) {
    printf("\n\nEXERCICE 4\n\n");

    // Affectation de la date de naissance
    int birth_year = 1990;
    int birth_month = 06;
    int birth_day = 15;  // Déclaration et affectation des variables

    // Affectation de la date du jour
    int today_year = 2025;
    int today_month = 11;
    int today_day = 17;  // Déclaration et affectation des variables

    // Affiche les dates entrées par l'utilisateur
    printf("Je suis né.e le %d/%d/%d.\n", birth_day, birth_month, birth_year);
    printf("Aujourd'hui, nous sommes le %d/%d/%d.\n\n", today_day, today_month, today_year);    

    int age_in_day = 0;

    /******************** Votre code ci-dessous ********************/
    age_in_day = (today_year - birth_year) * 360 + (today_month - birth_month) * 30 + (today_day - birth_day);
    /******************** Votre code ci-dessus *********************/

    printf("==> Mon âge est (approximativement) de %d jours.\n", age_in_day);
    
    return;
}


void exercice5(void) {
    printf("\n\nEXERCICE 5\n\n");

    // Lecture du nombre de jours
    int nb_of_days = 2153;
    int nb_of_days_0 = nb_of_days;
   
    /******************** Votre code ci-dessous ********************/
    int nb_of_years = nb_of_days / 365;
    nb_of_days = nb_of_days - 365 * nb_of_years;
    int nb_of_weeks = nb_of_days / 7;
    nb_of_days = nb_of_days - 7 * nb_of_weeks;
    printf("%d jours font %d année(s), %d semaine(s) et %d jour(s)\n",
        nb_of_days_0, nb_of_years, nb_of_weeks, nb_of_days);
    /******************** Votre code ci-dessus *********************/

    return;
}


void exercice6(void) {
    printf("\n\nEXERCICE 6\n\n");

    int a = 7, b = 2;
    float c, d;  
    
    /******************** Votre code ci-dessous ********************/
    c = a / (float) b; // Ne modifier que cette ligne
    /******************** Votre code ci-dessus *********************/
    
    printf("%d / %d = %f \n", a, b, c);

    return;
}

void exercice7(void) {
    printf("\n\nEXERCICE 7\n\n");
    
    /******************** Votre code ci-dessous ********************/
    int x = 15;
    if (x <= 9 && x >= 0) {
        printf("Bien dans la plage demandée\n");
    }
    else {
        printf("x=%d n'est pas entre 0 et 9\n", x);
    }
    /******************** Votre code ci-dessus *********************/

    return;
}

void exercice8(void) {
    printf("\n\nEXERCICE 8\n\n");
    
    /******************** Votre code ci-dessous ********************/

    /******************** Votre code ci-dessus *********************/

    return;
}

void exercice9(void) {
    printf("\n\nEXERCICE 9\n\n");
    
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

    return 0;
}
