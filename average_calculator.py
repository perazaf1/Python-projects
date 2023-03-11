from math import *

#Fonction prenant en paramètres les notes et les coefficients
def average(listeNotes,listeCoefficients):
    #Initialiser la moyenne
    average = 0
    #Initialiser somme des coeff des notes
    sum_coeff = 0
    for i in range (0 , len(listeNotes)):
        #calcul somme des notes*coeff
        average=average + listeNotes[i]*listeCoefficients[i]
        #calcul somme des coeff
        sum_coeff = sum_coeff + listeCoefficients[i]
    average = average/sum_coeff
    return average

#Input utilisateur des notes
n = int(input("Nombre de notes : "))
#Stockage dans une liste
listeNotes = list(int(notes) for notes in input("Entrez les notes séparées par un espace :  ").strip().split())[:n]
#listNotes = [15,17,9]

#Demande du nombre de coeffs
m = int(input("Coefficients des notes : "))
#Stockage dans une liste des coefficients
listeCoefficients = list(int(coeff) for coeff in input("Entrez les coefficients séparés par un espace :  ").strip().split())[:m]
#listeCoefficients=[1,1,2]

print("\n")
print("La moyenne est : ", average(listeNotes, listeCoefficients))
print("\n")

#Faire un commentaire sur la moyenne obtenue
moyenne = int(average(listeNotes, listeCoefficients))

if (moyenne <= 10):
    print("Pas terrible, tu peux t'améliorer...")
elif (moyenne>= 10 and moyenne <=14  ):
    print("Jolie moyenne, tu peux faire mieux...")
else:
    print("Excellent ! Continue ainsi !")

