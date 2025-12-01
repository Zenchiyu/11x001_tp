import os
from pprint import pprint
import random

# Makes the assumption that function name is exerciceX
def exercice(func):
    def wrapper(*args, **kwargs):
        n = func.__name__.split("exercice")[-1]
        s = f"##### EXERCICE {n} #####"
        h = "#" * len(s)
        header = h + "\n" + s + "\n" + h + "\n"
        os.system("clear")
        print(header)        
        func(*args, **kwargs)
        print("\n\n")
        input("--> Appuyer sur 'Entrée' pour passer à l'exercice suivant")
    return wrapper

