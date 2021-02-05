# Algorithme V2

Le but de cet algorithme V2 est de prendre un carré plein qu'on va mangé petit à petit selon certaines règles.

Actuellement nous avons trouvé 4 règles a notre algorithme pour qu'il puisse mangé sans faire un cas qui casserait la boucle unique : 

# Règle N°1 : Maximum sur une même ligne

On ne peut pas prendre plus de N-1 carré (N étant la taille du carré complet) car sinon on coupe la figure en 2 ou on ne peut plus atteindre tout les bords du carré.

Exemple :
O  X  O     X = Carré déjà manger
O  X  O     O = Carré qui peut être mangé
O  Y  O     Y = Carré qu'on veut prendre

Dans ce cas, il est impossible de le prendre car sinon on coupe la figure en 2. 

# Règle N°2 : Accès au vide

On ne peut pas prendre un carré si il n'a pas accès au vide 

Exemple :
O  O  O     X = Carré déjà manger
O  Y  O     O = Carré qui peut être mangé
O  O  O     Y = Carré qu'on veut prendre

Dans ce cas, il est impossible de le prendre car il a pas accès au "vide".


# Règle N°3 : Diagonal 

On ne peut prendre un carré si il a un carré déjà mangé en diagonal 

Exemple :
O  O  X     X = Carré déjà manger
X  Y  O     O = Carré qui peut être mangé
O  O  O     Y = Carré qu'on veut prendre

Dans ce cas, il est pas possible car il y a un carré déjà pris en diagonal 
**Par contre**, il peut avoir une exception a cette règle, si il y a un carré adjacant entre ses 2 carré, il peut être mangé 

Exemple :
O  X  X     X = Carré déjà manger
O  Y  O     O = Carré qui peut être mangé
O  O  O     Y = Carré qu'on veut prendre

Dans ce cas, il peut être mangé.

# Règle N°4 : Entre 2 carré 

On ne peut prendre un carré qui se situe entre 2 carré déjà mangé (en angle ou en vertical / honrizontal)

Exemple (en ignorant la règle de la diagonal) :
O  X  O     X = Carré déjà manger
O  Y  X     O = Carré qui peut être mangé
O  O  O     Y = Carré qu'on veut prendre

Exemple 2 :
O  X  O     X = Carré déjà manger
O  Y  O     O = Carré qui peut être mangé
O  X  O     Y = Carré qu'on veut prendre

Dans ces cas, ce n'est pas possible de le prendre car il coupe la figure en 2

**Exception :**
Il peut avoir une exception, en effet, pour les angles, si le carré en diagonal entre les deux carrés, il peut être mangé. Pour les verticales / horizontales, il faut que il y a 3 carré prit a coté (droite ou gauche pour honrizontal, haut / bas pour honrizontal)

Exemple 1 :
O  X  X     X = Carré déjà manger
O  Y  X     O = Carré qui peut être mangé
O  O  O     Y = Carré qu'on veut prendre

Exemple 2 : 
X  X  O  O     X = Carré déjà manger
X  Y  O  O     O = Carré qui peut être mangé
X  X  O  O     Y = Carré qu'on veut prendre
O  O  O  O

Dans ces cas, il est possible de le manger.

