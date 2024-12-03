def luhnFonction(card_number):
    numeros = [int(numeros) for numeros in card_number[::-1]]

    for i in range(1, len(numeros), 2):
        numeros[i]*= 2
        if numeros[i] > 9:
            numeros[i] -= 9

    totale = sum(numeros)
    return totale % 10 == 0

def main():

    numeroCarte = input("Entrez le numéro de carte bancaire :")

    if numeroCarte.isdigit() and len(numeroCarte) >= 13 and len(numeroCarte) <= 19:
        if luhnFonction(numeroCarte):
            print("Numéro valide")
        else:
            print("Numéro invalide")
    else:
        print("Ceci est invalide")



main()                    