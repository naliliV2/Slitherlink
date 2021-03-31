def draw_grid(turtle, size, size_square = 50): 
    for _ in range(size): #Nombre de collone
        for _ in range(size): #Nombre de carré dans la collone 
            for _ in range(4): #Dessine les carrés 
                turtle.forward(size_square)
                turtle.left(90)
            turtle.left(90)
            turtle.forward(size_square)
            turtle.right(90)
        turtle.right(90)
        turtle.forward(size*size_square)
        turtle.left(90)
        turtle.forward(size_square)

def transform_grid(size, grid):
    '''
    Transforme les 0-1 en 1 et les 2 en 0 

    0 signifiant vide
    1 signifiant plein
    '''
    for line in range(0, size, 1):
        for column in range(0, size, 1):
            if grid[line][column] == 0 or grid[line][column] == 1:
                grid[line][column] = 1
            elif grid[line][column] == 2:
                grid[line][column] = 0
    return grid

#Dessine la figure qui a été généré.
def draw_shape(turtle, grid, size, size_square = 50):
    '''
    Dessine la figure qui a été généré en mettant un trait entre les carrés vide / plein. 
    '''
    #Mise en place au point 0 et parametre la turtle. ##A mettre dans parameter.py dans la 1.05
    turtle.penup()
    turtle.setpos((0-(size*size_square))/2, (0-(size*size_square))/2)
    turtle.left(90)
    turtle.forward((size*size_square)-size_square)
    turtle.right(90)
    turtle.pencolor("red")
    turtle.pensize(5)
    
    #Dessine des traits rouges quand un carré de val 0 est a coter d'un carré de val 1. (Vertical)
    for line in range(0, size, 1):
        for column in range(1, size, 1):
            if grid[line][column-1] == 0 and grid[line][column] == 1 or grid[line][column-1] == 1 and grid[line][column] == 0:
                turtle.forward(size_square)
                turtle.left(90)
                turtle.pendown()
                turtle.forward(size_square)
                turtle.penup()
                turtle.left(180)
                turtle.forward(size_square)
                turtle.left(90)
            else:
                turtle.forward(size_square)
        turtle.right(180)
        turtle.forward((size*size_square)-size_square)
        turtle.left(90)
        turtle.forward(size_square)
        turtle.left(90)
    
    #Remise en place
    turtle.setpos((0-(size*size_square))/2, (0-(size*size_square))/2)
    turtle.left(90)
    turtle.forward((size*size_square)-size_square)
    turtle.right(90)

    #Fait pareil mais honrizontalement.
    for line in range(0, size-1, 1):
        for column in range(0, size, 1):
            if grid[line][column] == 0 and grid[line+1][column] == 1 or grid[line][column] == 1 and grid[line+1][column] == 0:
                turtle.pendown()
                turtle.forward(size_square)
                turtle.penup()
            else: 
                turtle.forward(size_square)
        turtle.right(180)
        turtle.forward(size*size_square)
        turtle.left(90)
        turtle.forward(size_square)
        turtle.left(90)

    #Remise en place
    turtle.setpos((0-(size*size_square))/2, (0-(size*size_square))/2)
    turtle.left(90)
    
    #Détecte si un carré qui est au bord de la grille à une valeur de 1 pour tracé un trait.
    for line in range(-(size-1), 1, 1): #Coté droit 
        if grid[-line][0] == 1:
            turtle.pendown()
            turtle.forward(size_square)
            turtle.penup()
        else:
            turtle.forward(size_square)
    turtle.right(90)

    for column in range(0, size, 1): #Coté haut
        if grid[0][column] == 1:
            turtle.pendown()
            turtle.forward(size_square)
            turtle.penup()
        else: 
            turtle.forward(size_square)
    turtle.right(90)

    for line in range(0, size, 1): #Coté gauche 
        if grid[line][size-1] == 1:
            turtle.pendown()
            turtle.forward(size_square)
            turtle.penup() 
        else:
            turtle.forward(size_square)
    turtle.right(90)

    for column in range(-(size-1), 1, 1):#Coté bas ###erreur
        if grid[size-1][-column] == 1:
            turtle.pendown()
            turtle.forward(size_square)
            turtle.penup()
        else:
            turtle.forward(size_square)
    turtle.right(180)

if __name__ == "__main__":
    print("Vous avez lancer le mauvais fichier, merci de lancer 'main.py'")