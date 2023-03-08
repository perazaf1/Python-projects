import math
import random

# importer les chiffres à deviner
number = random.randrange(1,20)
# choix du chiffre
guess = int(input("Entrez un nombre : "))


# boucle pour deviner le chiffre
while number != guess :
    if guess < number :
        # chiffre trop bas
        print("Le nombre est trop bas !")
        guess = int(input("Entrez un nombre : "))
    elif guess > number : 
        # chiffre trop haut
        print("Le nombre est trop haut !")
        guess = int(input("Entrez de nouveau un nombre : "))
    else :
        # le cas est bon 
        break
    
print("Vous l'avez deviné parfaitement !")




