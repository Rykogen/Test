# Créons notre fichier de produits de base
fichier = open("mes_produits.txt", "w")
fichier.write("Ordinateur,10\n")
fichier.write("Souris,5\n") 
fichier.write("Clavier,3\n")
fichier.close()

print("✅ Fichier créé avec 3 produits de base")