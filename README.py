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
vente_quantite=tuple.int("Entrez un minimum et un maximum pour la quantité")
