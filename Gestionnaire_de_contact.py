contacts=[]
def afficher_menu():
    print("\n -------Menu-------")
    print("1. Ajouter un contact")
    print("2. Afficher les contacts")
    print("3. Chercher un contact")
    print("4. Supprimer un contact")
    print("5. Sortir")
    
    choix= input("Choisir une option: ")
    match choix:
        case "1":
            ajoute_contact()
        case "2":
            affiche_contact()
        case "3":
            chercher_contact()
        case "4":
            supprimer_un_contact()
        case "5":
            print("A la prochaine")
        case _:
            print("Regarde j'aime pas hein, faut bien faire")
            afficher_menu()

def ajoute_contact():
    nom=input("Entrez un nom: ")
    tel=input("Entrez le numéro: ")
    contact={
        "nom":nom,
        "tel":tel
    }
    contacts.append(contact)
    print("Contact ajouté avec succès")
    afficher_menu()
    
def affiche_contact():
    if len(contacts)==0:
        print("tu as enregistré quelques choses et puis tu veux afficher tchrrrr")
    else:
        for c in contacts:
            print(f"{c["nom"]} - {c["tel"]}")
    afficher_menu()
    
def chercher_contact():
    nom_recherche = input("Nom à chercher : ")
    trouve = False

    for c in contacts:
     if c["nom"].lower() == nom_recherche.lower():
        print(f"Contact trouvé   : {c['nom']} - {c['tel']}")
        trouve = True
        break

     if not trouve:
      print("Aucun contact ne correspond.")
    afficher_menu()
    
def supprimer_un_contact():
    nom_recherche= input("donnez le nom du contact à supprimer: ")
    supprime=False
    
    for c in contacts:
        if c["nom"].lower()==nom_recherche.lower():
            contacts.remove(c)
            print("Contact supprimé avec succès")
            supprime=True
            break
        if not supprime:
            print("le contact n'existe pas")
    afficher_menu()


afficher_menu()
    
    
            
    
            