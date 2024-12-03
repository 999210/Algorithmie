print ("Augmentation des tarifs")
pu = float(input("Saisir un prix unitaire: "))
if pu < 20:
    pu = pu * 1.1
elif pu < 50:
    pu = pu * 1.075
elif pu < 100:
    pu = pu * 1.05
else:
    pu = pu * 1.025
print ("Le nouveau prix est : ", pu)
