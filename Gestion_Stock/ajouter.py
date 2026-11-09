print("======Ajouter un produit======")
nom= input("Veuillez entrer le nom du produit:")
quantite=input("Quelle est sa quantité:")


fichier=open("mes_produits.txt","a")
fichier.write(f"{nom},{quantite}\n")
fichier.close
print("Article ajouté avec succés")