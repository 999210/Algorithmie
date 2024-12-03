print("Comparer deux dates")
j1 = int(input("Saisir le jour de la premiere date : "))
m1 = int(input("Saisir le mois de la premiere date : "))
a1 = int(input("Saisir l'annee de la premiere date : "))
j2 = int(input("Saisir le jour de la deuxieme date : "))
m2 = int(input("Saisir le mois de la deuxieme date : "))
a2 = int(input("Saisir l'annee de la deuxieme date : "))

if a1 < a2:
    print("La date 1 est la plus ancienne")
elif a1 > a2:
    print("La date 2 est la plus ancienne")
else:
    if m1 < m2:
        print("La date 1 est la plus ancienne")
    elif m1 > m2:
        print("La date 2 est la plus ancienne")
    else:
        if j1 < j2:
            print("La date 1 est la plus ancienne")
        elif j1 > j2:
            print("La date 2 est la plus ancienne")
        else:
            print("Les 2 dates sont identiques")
