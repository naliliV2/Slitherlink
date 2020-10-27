# Slitherlink
Version : 1.0 
Author : nalili

# FR : 

  Ce programme permet de générer une grille vierge et génère la boucle unique aléatoire de slitherlink.
Il a été créé dans le cadre de l'évènement "Maths En Jean" pour mon lycée. (Sujet pas encore sorti) 

  # Information:

main.py : Programme principal qui lance tout.

grid.py : Gère tout ce qui touche à l'affichage.

robot.py : Lance des "robots" et fais des vérifications dans l'algo.

parameter.py : paramétrage de la turtle (librairy python). 

  # Explication: 

  Ce programme génère une grille de taille X (imaginons 5) et fait en sorte que chaque carré à une "variable" entre 0 et 1. Le but de ce programme est comme j'ai dit de générer une boucle unique aléatoire. Le programme va donc lancer des "robots" (un vertical et un autre horizontal) qui vont laisser une "trainé" derrière (Change les 0 en 1 de la variable du carré où il se trouve). Une fois ça fait et atteint le bord opposé où il a commencé, je fais en sorte que les carrés avec 0 (ou pas de carré) et 1 ont un trait. Cela permet de générer une boucle unique. Cependant il se peut que cette technique laisse des trous et donc fait une 2ème boucle, j'applique donc une vérification que si les carrés vide sont entourés par des carrés contenant 1 comme variable soit "rebouché". 

  # Problème encore existant: 
  
  Ce programme a effectivement encore de nombreux problème. Comme sa lenteur pour faire la grille, cela ne vient pas de moi mais de la librairy turtle. Pour la 1.1 j'essayerai d'optimiser un peu plus mon programme. 
  Il y a aussi un problème avec ma vérification, elle marche que sur des bulles qui ont que 1 carré. Je réfléchis encore à un moyen pour régler ce problème.  

  # Remerciement
  
  Je remercie Glcraft (https://github.com/glcraft) qui m’a énormément aidé pour savoir comment j'allais m'y prendre pour faire le programme. Sans lui, je doute que j'aurai réussi) à faire ça. 

# EN : 
Not yet translated.
