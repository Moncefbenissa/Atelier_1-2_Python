def deviser_inverser(liste):
  #declarations des listes
  liste1=[]
  liste2=[]
  liste3=[]
  lenListe=len(liste)
  # Division de la liste sur 3 parties:
  for i in range(lenListe/3):
    lenliste = lenListe//3
    liste1.append(liste[i])
    liste2.append(liste[i+lenliste])
    liste3.append(liste[i+2*lenliste])
  #Affichage de resultat en inverse:
  print(liste1[::-1],liste2[::-1],liste3[::-1])


#Exemple:

Exemple_liste = [11, 45, 8, 23, 14, 12, 78, 45, 89]
deviser_inverser(Exemple_liste)
