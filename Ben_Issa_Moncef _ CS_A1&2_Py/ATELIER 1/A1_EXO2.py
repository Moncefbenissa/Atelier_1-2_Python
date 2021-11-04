#Foction pour convirtir le nombre decimal en binaire :
def decimalEnBinaire(dec):
    if dec > 1:
        decimalEnBinaire(dec// 2)
    print(dec % 2)


# Affichage de resultat
nmb_decimal = int(input("Entrer un nombre: "))
decimalEnBinaire(nmb_decimal)

