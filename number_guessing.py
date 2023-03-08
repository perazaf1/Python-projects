import math
import random

# importer les chiffres à deviner
number = random.randrange(1,20)
guess = int(input("Entrez un nombre : "))

while number != guess :
    if guess < number :
        print("Le nombre est trop bas !")
        guess = int(input("Entrez un nombre : "))
    elif guess > number : 
        print("Le nombre est trop haut !")
        guess = int(input("Entrez de nouveau un nombre : "))
    else :
        break
print("Vous l'avez deviné parfaitement !")




