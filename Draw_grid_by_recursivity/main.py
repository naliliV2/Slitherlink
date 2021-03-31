import turtle

from draw import *

class struct(object):
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)

sens = struct(name = ["Nord", "Est", "Sud", "Ouest"], name_invert = ["Sud", "Ouest", "Nord", "Est"], x = [0, 1, 0, -1], y = [-1, 0, 1, 0])

def recursif(x, y, origine_sens, start, final, round, grid, path = []):
    grid[y][x] = round
    if final.x == x and final.y == y:
        print(path)
        for lign in range(4):
            print(grid[lign])
        print("------------")
        pathc = path.copy()
        main_draw_grid(pathc)
        path.pop()
        grid[y][x] = 0
        return

    for i in range(4):
        try:
            if origine_sens == sens.name[i]: #Vérifié qu'il vient pas de là
                continue
            elif sens.name[i] == "Nord" and y == 0 or sens.name[i] == "Ouest" and x == 0: #Pour évité qu'il se TP de l'autre côté
                continue 
            elif grid[sens.y[i]+y][sens.x[i]+x] == 0: #Vérifié que le point futur existe et qu'il est égal a 0
                path.append(sens.name[i][0]) 
                recursif(sens.x[i]+x, sens.y[i]+y, sens.name_invert[i], start, final, round+1, grid, path) 
        except IndexError: #Sort de la grille, n'existe pas
            1+1 #Parce que WHALA
    grid[y][x] = 0
    if len(path) !=0: 
        path.pop()
    return

def main():
    grid = [[0 for i in range(4)] for j in range(4)]
    print("0 0 est en haut a gauche")
    point_start = struct(x = int(input("Coordonnée X de votre point d'entré : ")), y=int(input("Coordonnée Y de votre point d'entré : ")))
    point_exit = struct(x = int(input("Coordonnée X de votre point de sortie : ")), y= int(input("Coordonnée Y de votre point de sortie : ")))
    
    recursif(point_start.x, point_start.y, "null", point_start, point_exit, 1, grid)

if __name__ == "__main__":
    main()