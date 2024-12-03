
print ("Calculatrice")
print ("Vous pouvez effectuer les operations suivantes : (+,-,*,/)")
print ("Saisissez '!' pour arreter la calculatrice.")


rst = float(input("Entrer votre premier nombre :"))

while True:
    op = str(input("Entrez une operation avec (+,-,*,/) ou entrez '!' pour quitter la calculatrice :"))
    if op == '!':
        print("Merci d'avoir utilisé la calculatrice !")
        break
    if op not in ['+', '-', '*', '/']:
        print("Erreur : opération non valide. Essayez à nouveau.")
        continue

    nombre = float(input("Entrez un nombre : "))
    if op == '+':
        rst += nombre
    elif op == '-':
        rst -= nombre
    elif op == '*':
        rst *= nombre
    elif op == '/':
        if nombre == 0:
            print ("Erreur : La division par zero est malheureusement impossible.")
            while nombre == 0:
                nombre = float(input("Entrez un nombre : "))
        rst /= nombre

    print(f"Resultat : {rst}")




