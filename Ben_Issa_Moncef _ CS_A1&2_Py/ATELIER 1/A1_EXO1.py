i = 1
add = 0

# Declaration d'une fonction qui calcule le factorial
def factorial(n):
     if n == 0:
        return 1
     else:
        result = n * factorial(n - 1)
        return result

# La fonction qui calcule la somme de la serie
def somme(nmb):
    if (nmb == 0):
        return 1
    else:
        result = (factorial(nmb)/nmb) + somme(nmb - 1)
        return result

print(somme(5))