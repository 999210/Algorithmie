# exercice 2 : remplissage d'un tableau
T = [0] * 10
i = 0

# saisie des 10 entiers
while i < 10:
    T[i] = int(input("Saisir un entier : "))
    i += 1

# affichage du contenu du tableau
for i in range(0, 10, 1):
    print(T[i])
    
# autre solution pour afficher 
i = 0
while i < 10:
    print(T[i])
    i += 1
