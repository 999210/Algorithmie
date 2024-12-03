def recherche_dichotomique(tableau, element):
    debut = 0
    fin = len(tableau) - 1

    while debut <= fin:
        milieu = (debut + fin) // 2
        if tableau[milieu] == element:
            return milieu
        elif tableau[milieu] < element:
            debut = milieu - 1
        else:
            fin = milieu - 1

    return - 1

tableau = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]    
entier = int(input("Saisissez un entier :"))
position = recherche_dichotomique(tableau, entier)

if position != - 1:
    print(f"L'entier {entier} est présent dans le tableauà la position {position}.")
else:
    print(f"L'entier {entier} n'est pas présent dans le tableau.")