from random import randint, choice

#Créé une liste qui permet que chaque carré a une valeur.
def def_grid_bot(size, grid = []):
    for _ in range(size*size):
        grid.append(0)
    return grid


# Détermine l'action du "robot"
### J'ai décidé de pas faire de la "vrai aléatoire" car les figures ne sont pas assez varrié.
### A modifié pour la 1.1
def random_action(): 
    ra = randint(1, 100) 
    if ra > 0 and ra <= 40: 
        return "left"
    elif ra > 40 and ra <= 80:
        return "right"
    elif ra > 80 and ra <=100:
        return "forward"

#Lance un "robot" qui trace une ligne (modifie la liste en transformant les 0 en 1) de gauche à droite
def start_bot_h(size, grid, temp = 0):
    start_h = []
    for _ in range(size): #Détermine où le robot va apparaitre.
        start_h.append(temp) ##A changé car j'ai plus appris sur la boucle for entre temps dans la 1.05
        temp+=size
    next_act = choice(start_h)

    while True: 
        if  next_act < 0: #Détecte si le robot sort de la grille et le fait prendre la direction opp.
            next_act += (size*2) 
        if next_act > (size**2)-1:
            next_act -= (size*2)
        grid.pop(next_act)
        grid.insert(next_act, 1)

        ra = random_action() #"Déplace" le robot
        if ra == "left":
            next_act -= size
        elif ra == "right":
            next_act += size
        elif ra == "forward":
            next_act += 1
            
            for i in range(size): #Si le robot est à l'opp. de la grille et qu'il en sort, il est arrêté.
                if next_act == size*(i+1):
                    return grid

#Fait de même mais avec un autre "robot" de haut en bas.     
def start_bot_v(size, grid): #Up to down
    next_act = randint(1, size) #Détermine où va apparaitre le robot.
    column = 1
    
    while True:
        if next_act >= size * column: #Idem que l'horizontal mais avec des ajustements.
            next_act -= 2
        elif next_act <= size * (column-1):
            next_act +=  2
        
        if next_act >= size**2: #Stop le robot comme dans l'honrizontal.
            return grid
        
        grid.pop(next_act)
        grid.insert(next_act, 1)

        ra = random_action() #"Déplace" le robot.
        if ra == "left":
            next_act += 1
        if ra == "right":
            next_act -= 1
        if ra == "forward":
            next_act += size
            column += 1

#Il se peut que des bulles dans la figure se créé, il va les détécter et les bouchés.
##Problème : Il bouche que les bulles qui font 1 carré. Si il y en a plus il les bouches pas.
###A régler dans la 1.1 ou + 
def verification(size, grid):
    for lign in range(1, size-1): #X ligne
        for column in range(1, size-1): #Y colone. 
            ts = (column)+((size*lign)) # ts = Test square
            if grid[ts-size] and grid[ts-1] and grid[ts+1] and grid[ts+size] == 1: #Vérifie que les 4 carrés allentour son plein.
                grid.pop(ts)
                grid.insert(ts, 1)
    return grid