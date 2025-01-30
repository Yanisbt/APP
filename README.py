donnees={"Order ID":"","Product":"","Quantity Ordered":"","Price Each":"","Order Date":"","Purchase Address":""}
def lire(donnees,fichier):
    with open(fichier,"w") as f:
        for keys in donnees.keys():
            f.write(keys,"\n")
    affichage = print(fichier)
    return affichage
print(lire(donnees,"PME.csv"))
