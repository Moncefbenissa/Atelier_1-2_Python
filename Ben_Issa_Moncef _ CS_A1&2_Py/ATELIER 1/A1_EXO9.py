"""Fonction cheche cherche un element
dans une matrice puis renvoi saposition."""

def chercher(a, matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == a:
                return (i,j)

#Affichage de resultat:
matrice1 = [[1,2,3],[4,5,6],[7,8,9]]

n = input("Entrer un nombre: \n")
print ("La position de :",n, "est", chercher(n, matrice1))
