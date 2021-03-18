#import les librairies
from turtle import Screen, Turtle
from random import choice

#Créé la turtle
screen = Screen()
turtle = Turtle()

#import les fichiers externe. 
from mine import *
from parameter import *
from draw import *
from check_rules import *
from console import *

#Reset la grille
def reset():
    turtle.clear()

#Lance le progamme entier
def start(size, size_square):
    grid = create_grid(size) #mine.py
    for i in range(size):
        grid[0][i], grid[size-1][i], grid[i][0], grid[i][size-1] = 1, 1, 1, 1
    
    for _ in range(random_round(size)):
        grid, state = mine(size, grid)
        if state == "Stop":
            break
        grid = rules(size, grid)
    
    number_grid = create_grid(size)

    parameter(turtle, size, size_square) #parameter.py
    draw_grid(turtle, size, size_square) # draw.py
    grid = transform_grid(size, grid)
    number_grid = draw_shape(turtle, grid, size, size_square, number_grid)
    draw_number(turtle, size, size_square, number_grid)
    turtle._update()

def main():
    #Taille par défaut
    size = 7
    size_square = 40
    while not False:
        size, size_square = console(size, size_square)
        reset()
        start(size, size_square)

if __name__ == "__main__":
    print("Faite 'help' pour avoir plus d'information, sinon appuyez sur entrer pour lancer le programme")
    main()    
