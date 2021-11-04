#Fonction qui compte les chiffres d'un nombre:
compteur=0
def compterChiffres(nbr):
    global compteur
    if (nbr != 0):
        compteur +=1
        compterChiffres(nbr // 10)
    return compteur

#Affichage de resultat:
n=int(input("Entrer un nombre: "))
print(compterChiffres(n))