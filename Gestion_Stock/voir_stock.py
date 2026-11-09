print("=== MON STOCK ===")

fichier = open("mes_produits.txt", "r")
lignes = fichier.readlines()

for ligne in lignes:
    # On utilise ce qu'on a appris !
    ligne_propre = ligne.strip()
    morceaux = ligne_propre.split(",")
    
    nom = morceaux[0]
    quantite = int(morceaux[1])  # int() pour convertir en nombre
    
    print(f"• {nom} : {quantite} unités")
    
    # Vérification d'alerte
    if quantite < 5:
        print(f"  ⚠️  ALERTE : Stock faible pour {nom} !")

fichier.close()