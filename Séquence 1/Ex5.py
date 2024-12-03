print ("Offres Telephoniques")
conso = int(input("Saisir votre consommation en heures : "))
print ("La consommation est :", conso)
if (10 + conso*0.5) < (20 + conso * 0.2):
	print ("Il faut choisir l offre 1")
elif (10 + conso*0.5) > (20 + conso * 0.2):
	print ("Il faut choisir l offre 2")
else: print ("Les deux offres sont equivalentes")   