# Slitherlink
Version : 2.0 \
Author : nalili

# FR : 

Ce programme permet de générer une grille vierge et génère une boucle aléatoire à plusieurs segment unique de slitherlink.
Il a été créé dans le cadre de l'évènement "Maths En Jean" pour mon lycée. (Publication pas encore sorti) 

  # Information:

main.py : Programme principal.

console.py : Permet de faire les commandes pour lancé le programme. 

draw.py : Gère l'interface graphique.

mine.py : Mine un carré qui peut être pris aléatoirement. 

check_rule.py : Permet de défénir quel carré peut être miné avec certaine règle. 

parameter.py : paramètre  la turtle (librairie python). 

  # Explication: 

Ce programme créé une figure dite "pleine" qui va miner des carrés aléatoire petit à petit. 
Cependant, on ne peut pas manger n'importe quel carré, il y a 3 règles : 

**Première règle**: \  
Si un carré n'à pas accès a l'exterieur de la grille, il ne peut pas être miné.\
**Deuxième règle**:  \
Prenons tout les 8 carrés a coté de celui qu'on veut miner : \
Si tout les carré déjà mangé sont collés; il est possible de le prendre\
Sinon ça veux dire qu'ils sont pas tous collés, il est impossible de le prendre \
Remarque : Si le carré qu'on veut tester est sur le bord, on met des X là où il y a du vide.


# EN : 
Not yet translated.
