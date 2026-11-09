print("=== MODIFIER UNE QUANTITÉ ===")

# 1. Afficher les produits disponibles
fichier = open("mes_produits.txt", "r")
lignes = fichier.readlines()
fichier.close()

print("Produits disponibles :")
for i, ligne in enumerate(lignes):
    nom, quantite = ligne.strip().split(",")
    print(f"{i+1}. {nom} : {quantite} unités")

# 2. Demander lequel modifier
choix = int(input("\nQuel produit veux-tu modifier ? (numéro) ")) - 1

# 3. Demander la nouvelle quantité
nouvelle_quantite = input("Nouvelle quantité : ")

# 4. Modifier la ligne
lignes[choix] = f"{lignes[choix].split(',')[0]},{nouvelle_quantite}\n"

# 5. Sauvegarder
fichier = open("mes_produits.txt", "w")
fichier.writelines(lignes)
fichier.close()

print("✅ Quantité modifiée !")