## Répéter des instructions avec une boucle for

On peut répéter un morceau de code plusieurs fois sans avoir à les copier coller. La boucle `for` est un exemple d'instruction qui permet la répétition.

Supposons que dans un univers hypothétique, l'usage soit de toquer à la porte 1500 fois et non 3.

L'approche naïve serait de copier-coller (ici en Python) :

```python
print("Toque")
print("Toque")
print("Toque")
... (encore 1497 fois)
```

Nous avons donc besoin d'un moyen pour exprimer la répétition. En pseudo code (très informel et haut niveau), cela ressemblerait par exemple à :

```
Répéter 1500 fois:
    Toque
```

Nous avons cette possibilitié en Python également, par exemple avec la boucle `for`:

```python
for i in range(1500):
    print("Toque")
```

## Exercice 3

Essayez de comprendre le code suivant
```python
for i in range(15):
    print(i)
```
puis écrivez une boucle `for` pour sommer tous les éléments de 0 jusqu'à 10. Pour rappel, `x = x + 1` veut dire qu'on incrémente une variable x par 1.

## Tant que ... Alors fait ... (while)

On peut aussi répéter des instructions en utilisant la boucle `while`. Cette boucle continue tant qu'une condition reste satisfaite.

Voici un exemple de boucle `while`.
```python
i = 1
while i < 10:
    print(i)
    i = 2 * i
```
(affiche: 1, 2, 4, 8)

L'intérêt principal du `while` est de répéter un nombre de fois que l'on ne connait pas forcément (exemple de pseudo-code ci-dessous). On y reviendra plus tard dans le cours.

```
Tant que soleil:
    Alors faire BBQ
```
