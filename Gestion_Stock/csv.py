# exporter.py
import csv

print("=== EXPORTER EN CSV ===")

# Lire le fichier texte
fichier_texte = open("mes_produits.txt", "r")
lignes = fichier_texte.readlines()
fichier_texte.close()

# Créer un fichier CSV
fichier_csv = open("export_stock.csv", "w")
fichier_csv.write("Nom,Quantité\n")  # En-têtes

for ligne in lignes:
    nom, quantite = ligne.strip().split(",")
    fichier_csv.write(f"{nom},{quantite}\n")

fichier_csv.close()
print("✅ Exporté vers export_stock.csv !")