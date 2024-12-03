print("Calcul TVA et TTC")
ht = float(input("Saisir un montant HT : "))
print ("Le montant HT vaut :", ht)
taux = float(input("Le taux de TVA vaut :"))
print ("Le taux de TVA vaut :", taux)
tva = ht * (taux / 100)
print ("Le montant de la TVA vaut : ", round(tva,2) )
ttc = ht + tva
print ("Le montant TTC vaut : ", round(ttc,2))
