def cesar(message, decalage, sens):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_chiffre = ''

    for char in message:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            if sens == 'ordre alphabétique':
                new_index = (index + decalage) % 26
            elif sens == 'ordre alphabetique inverse':
                new_index = (index - decalage) % 26
            new_char = alphabet[new_index]
            if char.isupper():
                new_char = new_char.upper()
            message_chiffre += new_char
        else:
            message_chiffre += char

    return message_chiffre

def main():
    message = input("Saisissez le message à chiffrer :")
    decalage = int(input("Saisissez le nombre de caractere de decalage :"))
    sens = input("Saisissez le sens du decalage (ordre alphabétique ou ordre alphabétique inverse) : ")

    message_chiffre = cesar(message, decalage, sens)
    print("Message chiffré :", message_chiffre)     

if __name__ == "__main__":
    main()            