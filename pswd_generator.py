import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!:/*$£'"

while 1:
    password_len=int(input("Longueur de mot de passe :"))
    password_count = int(input("Nombre de mots de passe :"))
    for x in range (0, password_count):
        password = ""
        for x in range (0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("Voilà votre mot de passe : ", password)


