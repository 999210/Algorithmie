def tri_insertion(tableau):
    for i in range(1, len(tableau)):
        cle = tableau[i]
        j = i - 1
        while j >= 0 and cle < tableau[j]:
            tableau[j + 1] = tableau[j]
            j -= 1
        tableau[j + 1] = cle
tableau = [3,7,1,9,5,10,2,8,6,4]
tri_insertion(tableau)
print("Tableau trié :", tableau)
