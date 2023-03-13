import random
import time
print("\nBienvenue sur le jeu du Pendu !\n")
name = input("Entre ton nom :  ")
print(f"Bonjour {name}, je te souhaite bonne chance !")
time.sleep(0.85)
print("\n Jouons")
time.sleep(0.85)


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

# Initialisation des conditions 
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("C'est le mot du pendu : " + display + "Entrez votre choix : \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Mauvais choix, Essaye une lettre \n")
        hangman()
    
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed :
        print("Essaye une autre lettre ! \n")
    
    else :
        count += 1
        #Comptage des pendus 

        if count == 1 :
            time.sleep(0.7)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Mauvais choix. " + str(limit - count) + " choix restants\n")

        elif count == 2:
            time.sleep(0.7)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Mauvaix choix. " + str(limit - count) + "choix restants\n")

        elif count == 3:
           time.sleep(0.7)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Mauvaix choix. " + str(limit - count) + " choix restants\n")

        elif count == 4:
            time.sleep(0.7)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Mauvaix choix. " + str(limit - count) + " dernier essai !\n")

        elif count == 5:
            time.sleep(0.7)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Mauvaix choix. Tu as été pendu !!!\n")
            print("Le mot était:",already_guessed,word)
            play_loop()
        
        if word == '_' * lentgh:
            print("Bravo ! Tu as trouvé le bon mot !")
            play_loop()
        
        elif count != limit :
            hangman()

main()
hangman()











