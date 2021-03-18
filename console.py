def console(size, size_square):
    '''
    Fait des commandes
    '''
    while True:
        awser = input(">>> ") 
        if awser == '':
            return size, size_square
        elif awser == 'help':
            print()
            print("Size (s)")
            print("Défini la taille de la grille")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("SizeSquare (ss)")
            print("Défini la taille d'affichage des carrés")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("Exit")
            print("Ferme le programme")
            print()
        elif awser == 'Size' or awser == 'size' or awser == 's':
            awser = int(input("Saisisez votre nouvelle taille de grille \n>>> "))
            size = awser
        elif awser == 'SizeSquare' or awser == 'sizesquare' or awser == 'ss':
            awser = int(input("Saisisez votre nouvelle taille de vos carrés \n>>> "))
            size_square = awser
        elif awser == "exit":
            10/0 #Provoque une division par 0 pour fermer le programme
        else: 
            print("Error : Aucune commande a été trouvé\n")

if __name__ == "__main__":
    print("Vous avez lancer le mauvais fichier, merci de lancer 'main.py'")