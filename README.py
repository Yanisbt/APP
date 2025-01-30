donnees={"Order ID":[],"Product":[],"Quantity Ordered":[],"Price Each":[],"Order Date":[],"Purchase Address":[]}
def charger(donnees,fichier):
    with open(fichier,"w") as f:
        for keys in donnees.keys():
            f.write(f"{keys}\n")
    affichage = print(fichier)
    return affichage
print(charger(donnees,"PME.csv"))
        

date=input("Entrez une date en str")
produit= input("Entrez un produit en str")
vente_prix=tuple.int("Entrez un minimum et un maximum pour le prix")
vente_qtite=tuple.int("Entrez un minimum et un maximum pour la quantité")

def filtre(date,produit,prix,qtite):
    filtrage=input("Choisissez entre : date, produit, prix, quantité")
    if filtrage=="date":
        print(date)
        #Ajouter des instructions
    elif filtrage=="produit":
        print(produit)
    elif filtrage=="prix":
        print(vente_prix)
        #Ajouter des instructions
    elif filtrage=="quantité":
        print(qtite)
        #Ajouter des instructions
