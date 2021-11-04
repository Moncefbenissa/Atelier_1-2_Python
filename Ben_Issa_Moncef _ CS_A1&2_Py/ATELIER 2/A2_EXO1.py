def fusionnerImpairePaire(liste1,liste2):
    lenListe1=len(liste1)
    lenListe2=len(liste2)
    liste3=[] #Creartion de la 3eme liste

    #Ajouter les elements impaires de la 1er liste:
    for i in liste1:
        a = liste1.index(i)
        if a % 2 == 1:
            liste3.append(liste1[a])
        else:
            continue
    # Ajouter les elements paires de la 2er liste:
    for i in liste2:
        b = liste2.index(i)
        if b % 2 == 0:
            liste3.append(liste2[b])

    #resultat:
    return liste3

#Exemple:
liste1 = [3, 6, 9, 12, 15, 18, 21]
liste2 = [4, 8, 12, 16, 20, 24, 28]

print(fusionnerImpairePaire(liste1,liste2))