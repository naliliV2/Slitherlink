# Slitherlink
Version : 2.0 
Author : nalili

# Français 

<div style="text-indent: 30px;">Ce programme permet de générer une grille vierge et génère une boucle aléatoire à plusieurs segment unique de slitherlink.
Il a été créé dans le cadre de l'évènement "Maths En Jean" pour mon lycée.</div><br>

## <ins>Introduction du Slitherlink</ins> :

<div style="text-indent: 30px;">Le Slitherlink (ou loppy en Français) est un jeu de réflexion solitaire. Le but du jeu est de former une courbe fermée dans une grille comportant des nombres dans des cases indiquant le nombre de côtés où la courbe passe.</div><br>



Non résolue|Résolue
:---|---:
<img src="Picture/no_resolved.jpg"> | <img src="Picture/no_resolved.jpg">


Il y a cependant quelques règles à respecter : </div>

* La courbe ne doit pas se croisé (ce qui veut dire qu'il n’y a pas de chiffres supérieur à 3)
* La courbe doit toucher les 4 bords de la grille
* La grille doit être unique (qu'elle a qu'une solution)

## <ins>Objectif</ins> :




### Explication :  

Ce programme créé une figure dite "pleine" qui va miner des carrés aléatoire petit à petit. 
Cependant, on ne peut pas manger n'importe quel carré, il y a 3 règles : 

**Première règle**: \  
Si un carré n'à pas accès a l'exterieur de la grille, il ne peut pas être miné.\
**Deuxième règle**:  \
Prenons tout les 8 carrés a coté de celui qu'on veut miner : \
Si tout les carré déjà mangé sont collés; il est possible de le prendre\
Sinon ça veux dire qu'ils sont pas tous collés, il est impossible de le prendre \
Remarque : Si le carré qu'on veut tester est sur le bord, on met des X là où il y a du vide.

## <ins>Information</ins> :

* main.py : Programme principal.
* console.py : Permet de faire les commandes pour lancé le programme. 
* draw.py : Gère l'interface graphique.
* mine.py : Mine un carré qui peut être pris aléatoirement. 
* check_rule.py : Permet de défénir quel carré peut être miné avec certaine règle. 
* parameter.py : paramètre la turtle (librairie python). 



# EN : 
Not yet translated.
