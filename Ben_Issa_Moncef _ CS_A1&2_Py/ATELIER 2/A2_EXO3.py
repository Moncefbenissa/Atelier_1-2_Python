def occurrence(list):
    # creation d'un dictionnaire vide:
    dict_freq = {}
    for e in list:
        if (e in dict_freq):
            dict_freq[e] +=1
        else:
            dict_freq[e] = 1
    #Affichage de dictionnaire:
    for element, occurence in dict_freq.items():
        print ("% d : % d" % (element, occurence))
        
#Exemple:
ma_liste = [11, 45, 8, 11, 23, 45, 23, 45, 89]
occurrence(ma_liste)