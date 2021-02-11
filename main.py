#import la turtle
from turtle import Screen, Turtle
screen = Screen()
turtle = Turtle()
turtle._tracer(0, 0)
from random import choice

#import les fichiers externe. 
from mine import *
from parameter import *
from draw import *
from check_rules import *

#Reset la grille
##A amélioré dans la 2.1 qui permettra d'effacer que le trait rouge.
def reset():
    turtle.clear()

#Lance le progamme entier
def start(size = 5, size_square = 50):
    grid = create_grid(size, grid=[]) #mine.py
    for _ in range(random_round(size)):
        grid, state = mine(size, grid)
        if state == "Stop":
            break
        grid = rules(size, grid)
    print()
    parameter(turtle, size, size_square)
    draw_grid(turtle, size, size_square)
    grid = transform_grid(size, grid)
    
    for i in range(len(grid)):
        print(grid[i])
    draw_shape(turtle, grid, size, size_square)
    input("finish")
    turtle._update()

def main():
    while not False:
        reset()
        start()

if __name__ == "__main__":
    print("Faite 'help' pour avoir plus d'information, sinon faite enter")
    main()    
