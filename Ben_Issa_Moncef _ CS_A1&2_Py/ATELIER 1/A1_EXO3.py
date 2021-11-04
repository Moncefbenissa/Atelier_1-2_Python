#Foction calcule la somme de la serie par recursivite:

def somme(n):
    if n <= 1:
        return n
    else:
        resultat = n + somme(n-1)
        return resultat

#Affichage de resultat:

n= input("Entrer un nombre: ")
print(somme(n))