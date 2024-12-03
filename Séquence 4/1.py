def ajouter_contact(nom, prenom, email, fichier="contacts.txt"):
    try:
        with open(fichier, 'a') as file:
            file.write(f"{nom},{prenom},{email}\n")
        print(f"Contact {prenom} {nom} ajouté avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout du contact : {e}")

def lecture_contacts(fichier="contacts.txt"):
    try:
        with open(fichier, 'r') as file:
            lignes = file.readlines()

        for ligne in lignes:
            ligne = ligne.strip()
            if ligne:
                nom, prenom, email = ligne.split(',')
                print(f"Nom : {nom}, Prénom : {prenom}, Email : {email}")

    except FileNotFoundError:
        print(f"Le fichier {fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def trier_contacts(fichier="contacts.txt"):
    try:
        with open(fichier, 'r') as file:
            lignes = file.readlines()

        lignes.sort(key=lambda x: x.split(',')[0])

        with open(fichier, 'w') as file:
            file.writelines(lignes)

        print("Contacts triés avec succès.")
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def compter_contacts(fichier="contacts.txt"):
    try:
        with open(fichier, 'r') as file:
            lignes = file.readlines()
        nombre_contacts = len(lignes)
        print(f"Il y a {nombre_contacts} contacts dans le fichier.")
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def recherche_contact(nom, fichier="contacts.txt"):
    try:
        with open(fichier, 'r') as file:
            lignes = file.readlines()
        trouve = False
        for ligne in lignes:
            ligne = ligne.strip()
            if ligne:
                nom_contact, prenom, email = ligne.split(',')
                if nom_contact == nom:
                    print(f"Nom : {nom_contact}, Prénom : {prenom}, Email : {email}")
                    trouve = True
                    break
        if not trouve:
            print(f"Aucun contact trouvé avec le nom {nom}.")
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def modifier_contact(nom, fichier="contacts.txt"):
    try:
        with open(fichier, 'r') as file:
            lignes = file.readlines()
        trouve = False
        for i, ligne in enumerate(lignes):
            ligne = ligne.strip()
            if ligne:
                nom_contact, prenom, email = ligne.split(',')
                if nom_contact == nom:
                    nouveau_prenom = input("Saisir le nouveau prénom : ")
                    nouvel_email = input("Saisir le nouvel email : ")
                    lignes[i] = f"{nom},{nouveau_prenom},{nouvel_email}\n"
                    trouve = True
                    break
        if trouve:
            with open(fichier, 'w') as file:
                file.writelines(lignes)
            print(f"Contact {nom} modifié avec succès.")
        else:
            print(f"Aucun contact trouvé avec le nom {nom}.")
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def supprimer_contact(nom, fichier="contacts.txt"):
    try:
        with open(fichier, 'r') as file:
            lignes = file.readlines()
        trouve = False
        for i, ligne in enumerate(lignes):
            ligne = ligne.strip()
            if ligne:
                nom_contact, prenom, email = ligne.split(',')
                if nom_contact == nom:
                    del lignes[i]
                    trouve = True
                    break
        if trouve:
            with open(fichier, 'w') as file:
                file.writelines(lignes)
            print(f"Contact {nom} supprimé avec succès.")
        else:
            print(f"Aucun contact trouvé avec le nom {nom}.")
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def main():
    while True:
        print("\nMenu:")
        print("1. Ajouter un contact")
        print("2. Afficher les contacts")
        print("3. Trier les contacts")
        print("4. Compter les contacts")
        print("5. Rechercher un contact")
        print("6. Modifier un contact")
        print("7. Supprimer un contact")
        print("8. Quitter")
        choix = input("Choisissez une option : ")

        if choix == '1':
            nom = input("Saisir un nom : ")
            prenom = input("Saisir un prénom : ")
            email = input("Saisir une adresse mail : ")
            ajouter_contact(nom, prenom, email)
        elif choix == '2':
            lecture_contacts()
        elif choix == '3':
            trier_contacts()
            lecture_contacts()
        elif choix == '4':
            compter_contacts()
        elif choix == '5':
            nom = input("Saisir le nom du contact à rechercher : ")
            recherche_contact(nom)
        elif choix == '6':
            nom = input("Saisir le nom du contact à modifier : ")
            modifier_contact(nom)
        elif choix == '7':
            nom = input("Saisir le nom du contact à supprimer : ")
            supprimer_contact(nom)
        elif choix == '8':
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")
main()
