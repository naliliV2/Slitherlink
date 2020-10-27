#Dessine la grille de taille X
def draw_grid(turtle, size, size_square = 50): 
    for _ in range(size): #Nombre de collone
        for _ in range(size): #Nombre de carré dans la collone 
            for _ in range(4): #Dessine les carrés ###A optimiser dans la 1.05
                turtle.forward(size_square)
                turtle.left(90)
            turtle.left(90)
            turtle.forward(size_square)
            turtle.right(90)
        turtle.right(90)
        turtle.forward(size*size_square)
        turtle.left(90)
        turtle.forward(size_square)

#Dessine la figure qui a été généré.
def draw_shape(turtle, grid, size, size_square = 50):
    #Mise en place au point 0 et parametre la turtle. ##A mettre dans parameter.py dans la 1.05
    turtle.penup()
    turtle.setpos((0-(size*size_square))/2, (0-(size*size_square))/2)
    turtle.left(90)
    turtle.forward((size*size_square)-size_square)
    turtle.right(90)
    turtle.pencolor("red")
    turtle.pensize(5)
    
    #Dessine des traits rouges quand un carré de val 0 est a coter d'un carré de val 1. (Vertical)
    for i0 in range(0, size**2, size):
        for i1 in range(1, size):
            if grid[(i0+i1)-1] == 0 and grid[i0+i1] == 1 or grid[(i0+i1)-1] == 1 and grid[i0+i1] == 0:
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
    for i0 in range(0, (size**2)-size, size):
        for i1 in range(0, size):
            if grid[i0+i1] == 0 and grid[i0+i1+size] == 1 or grid[i0+i1] == 1 and grid[i0+i1+size] == 0:
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
    for i in range((-(size*size)+size), 1, size): #Coté droit
        if grid[-i] == 1:
            turtle.pendown()
            turtle.forward(size_square)
            turtle.penup()
        else:
            turtle.forward(size_square)
    turtle.right(90)

    for i in range(0, size): #Coté haut
        if grid[i] == 1:
            turtle.pendown()
            turtle.forward(size_square)
            turtle.penup()
        else: 
            turtle.forward(size_square)
    turtle.right(90)

    for i in range(size-1, size*size, size): #Coté gauche
        if grid[i] == 1:
            turtle.pendown()
            turtle.forward(size_square)
            turtle.penup() 
        else:
            turtle.forward(size_square)
    turtle.right(90)

    for i in range(-(size*size)+1, -(size*size)+(size+1)):#Coté bas
        if grid[-i] == 1:
            turtle.pendown()
            turtle.forward(size_square)
            turtle.penup()
        else:
            turtle.forward(size_square)
    turtle.right(180)