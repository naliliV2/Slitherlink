def console(size, size_square):
    while True:
        awser = input(">>> ") 
        if awser == '':
            return size, size_square
        elif awser == 'help':
            print()
            print("Size (s)")
            print("Permet de définir une nouvelle taille pour la grille") 
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("SizeSquare (ss)")
            print("Permet de définir une nouvelle taille pour les carrés")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("Exit")
            print("Ferme le programme")
            print()
        elif awser == 'Size' or awser == 'size' or awser == 's':
            awser = int(input("Saisisez la nouvelle taille de grille \n>>> "))
            size = awser
        elif awser == 'SizeSquare' or awser == 'sizesquare' or awser == 'ss':
            awser = int(input("Saisisez la nouvelle taille de vos carrés \n>>> "))
            size_square = awser
        elif awser == "exit":
            10/0 #Provoque une division par 0 pour fermer le programme
        else: 
            print("Error : Aucune commande a été trouvé\n")

if __name__ == "__main__":
    print("Vous avez lancé le mauvais fichier, merci de lancer 'main.py'")