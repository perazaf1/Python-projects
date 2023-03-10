import math
import random
import time

# Début du jeu :
print ('=== Bienvenue sur le jeu du pendu ===')
name = input("Entrez votre nom : ")
print(f'Bonjour {name}, je te souhaite une bonne chance ! ')
time.sleep (1.5)
print ("Prépare-toi... \nJouons au pendu !")
time.sleep(1.5)

def main():
    # déclaration des variables pour le jeu
    global count
    global display
    global word
    global already_guessed
    global lentgh
    global play_game
    # liste pour les mots à deviner
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    # choix du mot
    word = random.choice(words_to_guess)
    # obtention de la longueur du mot
    lentgh = len(word)
    count = 0
    display = '_' * lentgh
    already_guessed = []
    play_game =""

# Choix booléen, réponse oui et non
def play_loop():
    global play_game
    # Choix du jeu ou non 
    play_game = input("Voulez-vous rejouer ? o = Oui, n = Non \n")
    while play_game not in ["o","n","O","N"]:
        play_game = input("Voulez-vous rejouer ? o = Oui, n = Non \n")
    if play_game == "o":
        main()
    elif play_game == "n":
        print("Merci d'avoir joué ! A bientôt !")
        exit()
    





