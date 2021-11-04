#Definition de 1er set et la 2eme set:
set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}
#Afficher les elements d'intersection:
print ("L'intersection entre le 1er set et le 2eme set est :",
       set.intersection(set2))

#Supprimer les elements d'intersection:
for element in set1.intersection(set2):
    set1.remove(element)
#Affichage de 1er set apres la suppression:
print ("Le 1er set apres la suppression des elements d'intersection:", set1)
