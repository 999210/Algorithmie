print ("Prix des photocopies")
Nombre = int(input("Saisir votre nombre de photocopies : "))
print("Le nombre de photocopies est :", Nombre)
if Nombre <= 10:
    prix = Nombre * 0.1
elif Nombre <= 20:
    prix = (10 * 0.1) + (Nombre - 10) * 0.08
elif Nombre <= 50:
    prix = (10 * 0.1) + (10 * 0.08) + (Nombre - 20) * 0.06
else: prix = (10 * 0.1) + (10 * 0.08) + (30 * 0.06) + (Nombre - 50) * 0.03  
print ("Le prix est : ", round(prix,2))       