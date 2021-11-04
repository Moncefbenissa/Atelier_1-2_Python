#Declaration des fonction de triage:
def triBull(l):
    n = len(l)
    for j in range(n):
        for i in range(n-j-1):
            if l[i] > l[i + 1]:
                a = l[i]
                l[i] = l[i + 1]
                l[i + 1] = a
    return l
def triInsertion(l):
    n = len(l)
    for i in range(n):
        r = i
        for j in range(i + 1, n):
            if l[r] > l[j]:
                r = j
        nbr = l[i]
        l[i] = l[r]
        l[r] = nbr
    return l
def triSelection(l):
    n = len(l)
    for i in range(1, n):
        k = l[i]
        j = i - 1
        while j >= 0 and k < l[j]:
            l[j + 1] = l[j]
            j -= 1
            l[j + 1] = k
    return l

#Affichage de resultat:
liste = [10, 3, 2, 7, 0]
print("Le tri a bull: ",triBull(liste),
      "| Le tri par selection: ",triSelection(liste),
      "| Le tri par insertion: ",triInsertion(liste))




