import math
import string
import getpass

def check_pswd_strength():
    # checker la fiabilité du mdp
    password = getpass.getpass('Entrez le mot de passe: ')
    strength = 0
    remarks = ""
    # mettre à 0 les compteurs de caractères
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list (password):
        # comptage des différents caractères
        if char in string.ascii_lowercase:
            lower_count +=1
            # caractères minuscules
        elif char in string.ascii_uppercase:
            upper_count +=1
            # caractères majuscules
        elif char in string.digits:
            num_count +=1
            # chiffres
        elif char == '':
            wspace_count +=1
            # espaces
        else :
            special_count +=1
            # caractères spéciaux

    # boucle if pour déterminer la force du password 
    if lower_count >=1:
        strength +=1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

        # boucle if pour donner la force du password et donner un conseil
    if strength == 1:
        remarks = ('C\'est un mauvais mot de passe.'
           ' CHangez-le dès que possible.')
    elif strength == 2:
        remarks = ('C\'est un mot de passe moyen.'
                ' Vous devriez envisager de changer de mot de passe.')
    elif strength == 3:
        remarks = 'Le mot de passe est ok, mais peut-être le modifier.'
    elif strength == 4:
        remarks = ('Votre mot de passe est compliqué.'
                ' Vous pouvez le rendre encore plus compliqué.')
    elif strength == 5:
        remarks = ('Maintenant c\'est un mot de passe bien dur !!!'
                ' Hackers don\'t have a chance guessing that password!')
        
        # Affichage des résultats
        # Utilisation de f' pour implémenter les résultats dans l'affichage des résultats
    print('Votre mot de passe a : -')
    print(f'{lower_count} lettres minuscules')
    print(f'{upper_count} lettres majuscules')
    print(f'{num_count} nombres')
    print(f'{wspace_count} espaces')
    print(f'{special_count} caractères spéciaux')
    print(f'Score du mot de passe : {strength }/ 5')
    print(f' Remarque : {remarks}')

def check_pswd (another_pswd = False):
    valid = False
    if another_pswd:
        choice = input(
            'Voulez-vous checker la fiabilité d\'un autre mot de passe (y/n) :'
        )
    else :
        choice = input(
            "Voulez-vous checker la fiabilité de votre mot de passe (y/n): "
        )

    while not valid :
        if choice.lower() == 'y':
           return True
        elif choice.lower() == 'n':
            print('Ok à bientôt...')
            return False
        else:
            print('Fausse entrée... Recommencez encore \n')
        

if __name__ == "__main__":
    print('===== Bienvenue sur le testeur de fiabilité du mot de passe =====')
    check_pwd = check_pswd()
    while check_pwd:
        check_pswd_strength()
        check_pwd = check_pswd(True)


        

