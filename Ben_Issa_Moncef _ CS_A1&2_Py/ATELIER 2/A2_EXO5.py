#Declaration liste / dictionnaire :
liste = [47, 64, 69, 37, 76, 83, 95, 97]
result = []
dictionnaire = {'Yassine': 47, 'Imane': 69, 'Mohammed': 76, 'Abir': 97}

#copier les valeurs de dictionnaire dans une liste:
valeurs_list = list(dictionnaire.values())

#Comparaison des valeurs de dictionnaire avec la 1er liste + suppression
for e in liste:
   if e in dictionnaire.values():
       result.append(e)

print(result)