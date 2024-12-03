print ("Calcul HT et Remises")
qte = float(input("Saisir une quantite: "))
print ("La quantite vaut :", qte)
pu = float(input("Saisir un prix unitaire : "))
print ("Le taux vaut :", pu)
print ("Le prix unitaire vaut :", pu)
ht = qte * pu
print ("Le montant HT vaut : ", ht) 
if ht < 200:
    print ("Remise 2.5 %")
    ht = ht * 0.975
elif ht < 400:
    print ("Remise 5 %")
    ht = ht * 0.95
elif ht < 700:
    print ("Remise 7.5 %")
    ht = ht * 0.925
else: 
    print ("Remise 10 %")
    ht = ht * 0.9
print ("Le montant HT apres remise vaut : ", round(ht,2))
print ("Le montant de TVA vaut : ", round(ht * 0.2,2))
print ("Le montant TTC vaut : ", round(ht * 1.2,2))




# total / remise 
# coef / total *% /100
# exemple : 120*10 /100
















