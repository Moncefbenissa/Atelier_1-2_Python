#Fonction qui calcule la fraquence d'un caractere:
def frequence(chaine, caractere):
    compteur=0
    for e in chaine:
        if e == caractere:
            compteur +=1
    return compteur

#L'affichage de resultat:
Exemple_Chaine ="Ecrire une fonction Python pour trouver " \
                "la frequence d'un caractere dans une chaine."

Exemple_cara = raw_input("Entrer un caracter: \n")
print("la frequence de caractere ",Exemple_cara, " est : ",
      frequence(Exemple_Chaine,Exemple_cara))