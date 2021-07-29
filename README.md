# Slitherlink
<div align="center">

![](https://img.shields.io/badge/Version-2.0-brightgreen)
![](https://img.shields.io/badge/Library-Turtle_and_Random-green)
![](https://img.shields.io/badge/Language-Python-yellow)
![](https://img.shields.io/badge/Size-2Mo-red)

![:nalili_Slitherlink](https://count.getloli.com/get/@s:nalili_Slitherlink?theme=rule34)

</div>

# Français

Ce programme permet de générer une grille vierge et génère une boucle aléatoire à plusieurs segment unique de slitherlink.
Il a été créé dans le cadre de l'évènement "Maths En Jean" pour mon lycée. Il n'y aura pas de publication officiel à cause de la pandémie actuelle.<br>

## <ins>Introduction au Slitherlink</ins> :

Le Slitherlink (ou loppy en Français) est un jeu de réflexion solitaire. Le but du jeu est de former une courbe fermée dans une grille comportant des nombres dans des cases indiquant le nombre de côtés où la courbe passe.<br>

<div align="center">

Non résolue                         | Résolue 
:----------------------------------:|:-------------------------------:
<img src="Picture/no_resolved.jpg"> | <img src="Picture/resolved.jpg">

</div>

Il y a cependant quelques règles à respecter : </div>

* La courbe ne doit pas se croiser (ce qui veut dire qu'il n’y a pas de chiffres supérieur à 3)
* La courbe doit toucher les 4 bords de la grille
* La grille doit être unique (qu'elle a qu'une solution)

## <ins>Objectif</ins> :

L'objectif qui nous avait été donné était de générer une grille de slitherlink, nous avons malheureusement fait que la moitié du problème car nous avion pas eu le temps de finir la génération des chiffres dans la grille suite à des problèmes comme le COVID-19 qui nous a compliqué énormément la tâche avec te temps. 
<br>

*Remarque* : Je ne continuerai pas ce programme pour le finir, dû a mon manque de temps et surtout que j'ai fais ça avec des camarades. Vous pouvez tout de même vous en inspiré ou le reprendre pour le finir.

## <ins>Explication</ins> :  

L'algorithme ici présent permet de généré une courbe aléatoire. Il y a une [première version](https://github.com/naliliV2/Slitherlink/tree/1.0) qui a été abandonné car elle présentait de nombreuse désaventage. 

Notre algorithme est une sorte de ``"mineur"``, je m'explique : 
En premier lieu, il faut prendre une grille totalement vierge et pleine avec aucun nombre, puis retirer petit à petit des carrés aléatoirement mais avec certaines règles. Après avoir “miner” un certain nombre de carrés, on trace un trait entre les carrés non miner et ceux miner, nous obtenons bien une courbe.

<div align="center"> 

**Exemple en image** <br/>

<img src="Picture/mine_grid.gif" width="300"> 
</div>

## <ins>Information</ins> :

* main.py : Programme principal.
* console.py : Permet de faire les commandes pour lancé le programme. 
* draw.py : Gère l'interface graphique.
* mine.py : Mine un carré qui peut être pris aléatoirement. 
* check_rule.py : Permet de défénir quel carré peut être miné avec certaine règle. 
* parameter.py : paramètre la turtle (librairie python). 

</br>

## <ins>Information supplémentaire</ins> :  

Nous avons commencé un algorithme pour généré les chiffres, le but était de faire des paternes de 3 par 3 déjà préfait (avec les chiffres et des morceaux de courbe) qu'on collerai sur la grille. Le problème et que cette méthode est peut être fiable, mais très long à mettre en place car il faut traité un par un les possibilitées de minimum de chiffre, il y a probablement plusieurs **millions** de cas a traité. Dans le dossier ``abandonned files`` il y a :

* Un programme qui fait la génération tout les morceaux de grilles possibles grâce a de la récursivité 
* un autre programme juste pour rajouté des chiffres. 

Je n'expliquerai pas leurs fonctionnement car ils ne sont pas utiles pour l'algorithme final mais ils étaient là juste pour nous aidés à notre tâche ainsi qu'ils sont très dur à prendre en main sans une explication rigoureuse. 

## <ins>FAQ</ins> : 

> Question : Ai-je le droit d'utilisé pour des fins personnels ?

Réponse : Bien-sûr ! C'est le principe d'Open source. 

>  J'ai une erreur quand je lance le programme, que dois-je faire ?

Dans ce genre de situation, merci de créé un issue et j'essayerai de voir le problème avec vous.

> Pourquoi le github est en 3.0 alors que la release est en 2.0 ?

Car la 3.0 est surtout une version d'organisation suur github, il y a effectivement quelques petites nuances dans les fichiers mais tellement minime que vous ne verrez pas la différence en tant qu'utilisateur. 

# EN : 
Not yet translated. In the futur, I translate every file and the explication of this.
