import csv # pour manipuler les données du .csv
import os # pour se diriger dans les dossiers
import pandas as pd # permet d'analyser les données

# on importe le fichier
fichier = "Sales_April_2019.csv"
df = pd.read_csv(fichier, sep=",", quotechar='"', engine="python", on_bad_lines='skip', header=0)

print(df.head())  # Vérifie les premières lignes
print(df.columns)  # Vérifie si toutes les colonnes sont bien détectées


# fonction qui charge les données du fichier csv
def charger_donnees(fichier):
    try:
        df = pd.read_csv(fichier, sep=",", quotechar='"', engine="python", on_bad_lines='skip')
        df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')  # Conversion correcte
        return df
    except FileNotFoundError:
        print("Fichier non trouvé.")
        return None
    
# fonction qui filtre les ventes par date
def filtrer_par_date(df, date):
    date = pd.to_datetime(date, errors='coerce')  
    return df[df['Order Date'].dt.date == date.date()]  

# fonction qui filtre les ventes par produit
def filtrer_par_produit(df, produit):
    return df[df['Product'].str.strip().str.lower() == produit.strip().lower()]  # pour ignorer les espaces et les majuscules

# fonction qui ajoute une vente
def ajouter_vente(df, nouvelle_vente, fichier):
    df = df.append(nouvelle_vente, ignore_index=True)
    df.to_csv(fichier, index=False)
    print("Nouvelle vente ajoutée !")

# fonction qui modifie une vente
def modifier_vente(df, order_id, nouvelle_quantite, nouveau_prix, fichier):
    df.loc[df['Order ID'].astype(str) == str(order_id), ['Quantity Ordered', 'Price Each']] = [nouvelle_quantite, nouveau_prix]
    df.to_csv(fichier, index=False)
    print("Vente mise à jour !")

# fonction qui calcule chiffre d'affaires total
def calculer_ca_total(df):
    df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'], errors='coerce')
    df["Price Each"] = pd.to_numeric(df["Price Each"], errors='coerce')
    return (df['Quantity Ordered'] * df['Price Each']).sum()

# le menu principal
def menu():
    df = charger_donnees(fichier)
    if df is None:
        return
    
    while True:
        print("\n1. Filtrer par date")
        print("2. Filtrer par produit")
        print("3. Ajouter une vente")
        print("4. Modifier une vente")
        print("5. Chiffre d'affaires total")
        print("6. Quitter")
        
        choix = input("Choisissez une option : ")
        
        if choix == '1':
            date = input("Entrez la date (MM/JJ/YY Heure:Minutes) : ")
            print(filtrer_par_date(df, date))
        elif choix == '2':
            produit = input("Entrez le produit : ")
            print(filtrer_par_produit(df, produit))
        elif choix == '3':
            order_id = input("Order ID : XXXXXX ")
            produit = input("Produit : ")
            quantite = int(input("Quantité : "))
            prix = float(input("Prix : "))
            date = input("Date (MM/JJ/YY Heure : Minutes) : ")
            adresse = input("Adresse d'achat : ")
            nouvelle_vente = {'Order ID': order_id, 'Product': produit, 'Quantity Ordered': quantite, 'Price Each': prix, 'Order Date': date, 'Purchase Address': adresse}
            ajouter_vente(df, nouvelle_vente, fichier)
        elif choix == '4':
            order_id = input("Entrez l'Order ID à modifier : ")
            quantite = int(input("Nouvelle quantité : "))
            prix = float(input("Nouveau prix : "))
            modifier_vente(df, order_id, quantite, prix, fichier)
        elif choix == '5':
            print("Chiffre d'affaires total :", calculer_ca_total(df))
        elif choix == '6':
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    menu()
