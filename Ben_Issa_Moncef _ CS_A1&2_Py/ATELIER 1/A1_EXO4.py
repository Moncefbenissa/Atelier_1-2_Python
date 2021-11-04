#Fonction qui calcule la serie de fibunacci:
def fibunacci(n):
   if n <= 1:  
       return n  
   else:  
       return(fibunacci(n-1) + fibunacci(n-2))

#Affichage de resultat:
nmb = input("Entrer un nombre ")
print(fibunacci(nmb))

