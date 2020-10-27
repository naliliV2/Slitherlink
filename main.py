#import la turtle
from turtle import Screen, Turtle
screen = Screen()
turtle = Turtle()

#import les fichiers externe. 
from draw import *
from parameter import *
from robot import *

#Reset la grille
##A amélioré dans la 1.1 qui permettra d'effacer que le trait rouge.
def reset():
    turtle.clear()

#Lance le progamme entier
def start(size = 5, size_square = 50):
    grid = def_grid_bot(size, grid=[]) #robot.py
    grid = start_bot_h(size, grid) #robot.py
    grid = start_bot_v(size, grid) #robot.py
    grid = verification(size, grid) #robot.py

    parameter(turtle, size, size_square) #parameter.py
    draw_grid(turtle, size, size_square) #draw.py
    draw_shape(turtle, grid, size, size_square) #draw.py

def main():
    cmd = input(">>> ")
    if cmd == "":
        reset()
        start()
    elif cmd == "h" or "help":
        print(" '' = Lance l'algorithme avec un carré 5*5")
        print(" 'size' = Lance un programme avec une taille que vous définisez")
        print(" 'exit' = Ferme le programme")
    elif cmd == "s" or "size":
        reset()
        start(int(input("Quelle taille voulez-vous pour votre grille ? ")))
    elif cmd == "exit":
        print(9/0)
    else:
        print("Vous avez rentrer une valeur invalide.")
    screen.mainloop


if __name__ == "__main__":
    print("Faite 'help' pour avoir plus d'information, sinon faite enter")
    while True:
        main()    
