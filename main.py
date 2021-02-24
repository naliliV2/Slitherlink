#import les libs
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
    grid = create_grid(size, grid=[]) #mine.py
    
    for _ in range(random_round(size)):
        grid, state = mine(size, grid)
        if state == "Stop":
            break
        grid = rules(size, grid)
    
    parameter(turtle, size, size_square)
    draw_grid(turtle, size, size_square)
    grid = transform_grid(size, grid)
    draw_shape(turtle, grid, size, size_square)
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
