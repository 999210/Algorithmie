print ("Delais de livraison")
qte = int(input("Saisir une quantite : "))
mode = str(input("Saisir un mode de livraison : rapide ou normal --> "))
if mode == "rapide":
    if qte < 50:
        delai = 2
    elif qte < 100:
        delai = 3
    else:
        delai = 5
else:
    if qte < 50:
        delai = 4
    elif qte < 100:
        delai = 5
    else:
        delai = 7
print ("Le delai de livraison est de", delai, "jours")
