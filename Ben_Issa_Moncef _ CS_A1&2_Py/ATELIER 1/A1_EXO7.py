#Declaration d'une fonction qui inverse la liste
def inverser(a):
    inverse = []
    for e in a:
        inverse.append(e)
    print(inverse[::-1])

#Affichage de resultat
liste_Exemple = [1,2,3,4,5,6,7,8,9,10]
inverser(liste_Exemple)