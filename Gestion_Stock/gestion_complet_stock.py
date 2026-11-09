import csv
import os
from datetime import datetime

def afficher_menu():
    print("\n" + "="*50)
    print("🎯 GESTIONNAIRE DE STOCK PROFESSIONNEL V2.0")
    print("="*50)
    print("1. 📋 Voir le stock complet")
    print("2. 🔍 Rechercher un produit")
    print("3. ➕ Ajouter un produit")
    print("4. ✏️  Modifier un produit")
    print("5. 🗑️  Supprimer un produit")
    print("6. ⚠️  Voir les alertes stock")
    print("7. 📊 Voir les statistiques")
    print("8. 📤 Exporter en CSV")
    print("9. 🚪 Quitter")
    print("="*50)

def demander_entier(message, min_val=0, max_val=None):
    """Demande un nombre entier de façon sécurisée avec plage"""
    while True:
        try:
            valeur = int(input(message))
            if valeur < min_val:
                print(f"❌ Erreur : Le nombre doit être au moins {min_val} !")
            elif max_val is not None and valeur > max_val:
                print(f"❌ Erreur : Le nombre doit être au maximum {max_val} !")
            else:
                return valeur
        except ValueError:
            print("❌ Erreur : Tu dois entrer un nombre entier !")

def demander_texte(message):
    """Demande un texte non vide"""
    while True:
        texte = input(message).strip()
        if texte:
            return texte
        print("❌ Erreur : Ce champ ne peut pas être vide !")

def lire_produits():
    """Lit tous les produits du fichier de façon sécurisée"""
    try:
        # Vérifier si le fichier existe et n'est pas vide
        if not os.path.exists("mes_produits.txt") or os.path.getsize("mes_produits.txt") == 0:
            return []
            
        with open("mes_produits.txt", "r", encoding='utf-8') as fichier:
            lignes = fichier.readlines()
        
        produits = []
        for i, ligne in enumerate(lignes):
            try:
                ligne_propre = ligne.strip()
                if ligne_propre and ',' in ligne_propre:
                    nom, quantite_str = ligne_propre.split(',', 1)
                    quantite = int(quantite_str)
                    produits.append({"nom": nom, "quantite": quantite})
            except ValueError:
                print(f"⚠️  Ligne {i+1} ignorée : format invalide -> {ligne}")
            except Exception as e:
                print(f"⚠️  Erreur ligne {i+1} : {e}")
        
        return produits
        
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"❌ Erreur inattendue : {e}")
        return []

def sauvegarder_produits(produits):
    """Sauvegarde la liste des produits dans le fichier"""
    try:
        with open("mes_produits.txt", "w", encoding='utf-8') as fichier:
            for produit in produits:
                fichier.write(f"{produit['nom']},{produit['quantite']}\n")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde : {e}")
        return False

def afficher_stock():
    """Affiche le stock de façon organisée"""
    produits = lire_produits()
    
    if not produits:
        print("\n📭 Le stock est vide")
        return
    
    print(f"\n{'='*60}")
    print(f"{'📦 STOCK COMPLET':^60}")
    print(f"{'='*60}")
    print(f"{'N°':<3} {'PRODUIT':<30} {'QUANTITÉ':<12} {'STATUT':<15}")
    print(f"{'-'*60}")
    
    for i, produit in enumerate(produits, 1):
        quantite = produit["quantite"]
        nom = produit["nom"]
        
        # Déterminer le statut
        if quantite == 0:
            statut = "🔴 RUPTURE"
        elif quantite < 3:
            statut = "🟠 TRÈS FAIBLE"
        elif quantite < 5:
            statut = "🟡 FAIBLE"
        else:
            statut = "✅ OK"
        
        print(f"{i:<3} {nom:<30} {quantite:<12} {statut:<15}")
    
    print(f"{'='*60}")
    print(f"📊 Total produits : {len(produits)}")

def rechercher_produit():
    """Recherche un produit par nom"""
    produits = lire_produits()
    
    if not produits:
        print("\n📭 Aucun produit dans le stock")
        return
    
    print("\n🔍 RECHERCHE DE PRODUIT")
    print("-" * 30)
    
terme_recherche = demander_texte("Entrez le nom ou une partie du nom : ").lower()
    
resultats = []
for produit in produits:
        if terme_recherche in produit["nom"].lower():
            resultats.append(produit)
    
        if not resultats:
          print(f"\n❌ Aucun produit trouvé avec '{terme_recherche}'")
    
print(f"\n✅ {len(resultats)} produit(s) trouvé(s) :")
print(f"{'='*50}")
print(f"{'PRODUIT':<30} {'QUANTITÉ':<10} {'STATUT':<10}")
print(f"{'-'*50}")
    
for produit in resultats:
        quantite = produit["quantite"]
        statut = "OK" if quantite >= 5 else "FAIBLE" if quantite >= 3 else "CRITIQUE"
        print(f"{produit['nom']:<30} {quantite:<10} {statut:<10}")

def ajouter_produit():
    """Ajoute un nouveau produit de façon sécurisée"""
    print("\n➕ AJOUT D'UN NOUVEAU PRODUIT")
    print("-" * 30)
    
    nom = demander_texte("Nom du produit : ")
    quantite = demander_entier("Quantité initiale : ", 0)
    
    # Vérifier si le produit existe déjà
    produits = lire_produits()
    for produit in produits:
        if produit["nom"].lower() == nom.lower():
            print(f"❌ Le produit '{nom}' existe déjà !")
            confirmation = input("Voulez-vous ajouter à la quantité existante ? (o/n) : ")
            if confirmation.lower() in ['o', 'oui', 'y', 'yes']:
                # Trouver le produit et modifier sa quantité
                for p in produits:
                    if p["nom"].lower() == nom.lower():
                        p["quantite"] += quantite
                        if sauvegarder_produits(produits):
                            print(f"✅ Quantité mise à jour : {p['quantite']} unités")
                        return
            else:
                return
    
    # Ajouter le nouveau produit
    produits.append({"nom": nom, "quantite": quantite})
    
    if sauvegarder_produits(produits):
        print(f"✅ Produit '{nom}' ajouté avec {quantite} unités !")

def modifier_produit():
    """Modifie la quantité d'un produit existant"""
    produits = lire_produits()
    
    if not produits:
        print("\n📭 Aucun produit à modifier")
        return
    
    print("\n✏️  MODIFICATION DE PRODUIT")
    print("-" * 30)
    
    # Afficher la liste numérotée
    for i, produit in enumerate(produits, 1):
        print(f"{i}. {produit['nom']} : {produit['quantite']} unités")
    
    choix = demander_entier("\nQuel produit modifier ? (numéro) : ", 1, len(produits))
    
    produit = produits[choix-1]
    print(f"\nProduit sélectionné : {produit['nom']}")
    print(f"Quantité actuelle : {produit['quantite']}")
    
    nouvelle_quantite = demander_entier("Nouvelle quantité : ", 0)
    produit["quantite"] = nouvelle_quantite
    
    if sauvegarder_produits(produits):
        print("✅ Produit modifié avec succès !")

def supprimer_produit():
    """Supprime un produit du stock"""
    produits = lire_produits()
    
    if not produits:
        print("\n📭 Aucun produit à supprimer")
        return
    
    print("\n🗑️  SUPPRESSION DE PRODUIT")
    print("-" * 30)
    
    for i, produit in enumerate(produits, 1):
        print(f"{i}. {produit['nom']} : {produit['quantite']} unités")
    
    choix = demander_entier("\nQuel produit supprimer ? (numéro) : ", 1, len(produits))
    
    produit_supprime = produits[choix-1]
    confirmation = input(f"Êtes-vous sûr de supprimer '{produit_supprime['nom']}' ? (o/n) : ")
    
    if confirmation.lower() in ['o', 'oui', 'y', 'yes']:
        # Recréer la liste sans le produit supprimé
        nouveaux_produits = [p for i, p in enumerate(produits) if i != choix-1]
        
        if sauvegarder_produits(nouveaux_produits):
            print(f"✅ Produit '{produit_supprime['nom']}' supprimé !")
    else:
        print("❌ Suppression annulée")

def voir_alertes():
    """Affiche uniquement les produits avec alertes"""
    produits = lire_produits()
    alertes = [p for p in produits if p["quantite"] < 5]
    
    if not alertes:
        print("\n✅ Aucune alerte - tous les stocks sont bons !")
        return
    
    print(f"\n{'='*50}")
    print(f"{'⚠️  ALERTES STOCK':^50}")
    print(f"{'='*50}")
    
    for produit in alertes:
        quantite = produit["quantite"]
        if quantite == 0:
            print(f"🔴 RUPTURE DE STOCK : {produit['nom']}")
        elif quantite < 3:
            print(f"🟠 STOCK CRITIQUE : {produit['nom']} ({quantite} unités)")
        else:
            print(f"🟡 STOCK FAIBLE : {produit['nom']} ({quantite} unités)")
    
    print(f"\n📊 Total des alertes : {len(alertes)}")

def afficher_statistiques():
    """Affiche des statistiques sur le stock"""
    produits = lire_produits()
    
    if not produits:
        print("\n📭 Aucune statistique - le stock est vide")
        return
    
    print(f"\n{'='*50}")
    print(f"{'📊 STATISTIQUES DU STOCK':^50}")
    print(f"{'='*50}")
    
    total_produits = len(produits)
    total_quantite = sum(p["quantite"] for p in produits)
    moyenne_stock = total_quantite / total_produits if total_produits > 0 else 0
    
    # Compter les statuts
    rupture = len([p for p in produits if p["quantite"] == 0])
    critique = len([p for p in produits if 0 < p["quantite"] < 3])
    faible = len([p for p in produits if 3 <= p["quantite"] < 5])
    bon = len([p for p in produits if p["quantite"] >= 5])
    
    # Produits les plus et moins stockés
    produit_plus_stock = max(produits, key=lambda x: x["quantite"]) if produits else None
    produit_moins_stock = min(produits, key=lambda x: x["quantite"]) if produits else None
    
    print(f"📦 Produits différents : {total_produits}")
    print(f"🧮 Total unités en stock : {total_quantite}")
    print(f"📈 Moyenne de stock : {moyenne_stock:.1f} unités/produit")
    print(f"\n📋 RÉPARTITION :")
    print(f"  ✅ Stock bon : {bon} produit(s)")
    print(f"  🟡 Stock faible : {faible} produit(s)")
    print(f"  🟠 Stock critique : {critique} produit(s)")
    print(f"  🔴 Rupture : {rupture} produit(s)")
    
    if produit_plus_stock:
        print(f"\n🏆 PRODUIT LE MIEUX STOCKÉ :")
        print(f"  {produit_plus_stock['nom']} : {produit_plus_stock['quantite']} unités")
    
    if produit_moins_stock and produit_moins_stock["quantite"] < 5:
        print(f"\n💡 PRODUIT À RECOMMANDER :")
        print(f"  {produit_moins_stock['nom']} : {produit_moins_stock['quantite']} unités")

def exporter_csv():
    """Exporte le stock en fichier CSV avec date"""
    produits = lire_produits()
    
    if not produits:
        print("\n📭 Aucun produit à exporter")
        return
    
    date_export = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nom_fichier = f"stock_export_{date_export}.csv"
    
    try:
        with open(nom_fichier, 'w', newline='', encoding='utf-8') as fichier:
            writer = csv.writer(fichier)
            writer.writerow(["Nom", "Quantité", "Statut", "Date_Export"])
            
            for produit in produits:
                quantite = produit["quantite"]
                if quantite == 0:
                    statut = "RUPTURE"
                elif quantite < 3:
                    statut = "CRITIQUE"
                elif quantite < 5:
                    statut = "FAIBLE"
                else:
                    statut = "OK"
                
                writer.writerow([produit["nom"], quantite, statut, date_export])
        
        print(f"✅ Stock exporté vers : {nom_fichier}")
        print(f"📊 Produits exportés : {len(produits)}")
        
    except Exception as e:
        print(f"❌ Erreur lors de l'export : {e}")

# PROGRAMME PRINCIPAL
def main():
    print("🎉 Bienvenue dans le Gestionnaire de Stock Professionnel V2.0 !")
    
    while True:
        afficher_menu()
        choix = input("\nVotre choix (1-9) : ").strip()
        
        actions = {
            "1": afficher_stock,
            "2": rechercher_produit,
            "3": ajouter_produit,
            "4": modifier_produit,
            "5": supprimer_produit,
            "6": voir_alertes,
            "7": afficher_statistiques,
            "8": exporter_csv
        }
        
        if choix in actions:
            actions[choix]()
        elif choix == "9":
            print("\n👋 Merci d'avoir utilisé le Gestionnaire de Stock !")
            break
        else:
            print("❌ Choix invalide ! Veuillez choisir entre 1 et 9.")

if __name__ == "__main__":
    main()