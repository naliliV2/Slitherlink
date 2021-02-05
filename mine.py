from random import choice, randint

def create_grid(size, grid):
    '''
    Créé le tableau a double dimension (line, column)

    0 = Ne peut être pris
    1 = Peut être pris 
    2 = A été déjà pris 
    '''
    grid = [[0 for i in range(size)] for j in range(size)]

    for i in range(size):
        grid[0][i], grid[size-1][i], grid[i][0], grid[i][size-1] = 1, 1, 1, 1
 
    return grid

def random_round(size):
    return randint(size, (size**2)-size*2)

def defined_mine(size, grid):   
    mine = []
    for line in range(0, size, 1):
        for column in range(0, size, 1):
            if grid[line][column]==1: 
                mine.append([line, column])

    if len(mine) == 0:
        return "Stop"
    return choice(mine)

def mine(size, grid):
    mine = defined_mine(size, grid)
    if mine != "Stop":
        grid[mine[0]][mine[1]] = 2
        return grid, "Good"
    else:
        return grid, "Stop"

if __name__ == "__main__":
    print("Vous avez lancer le mauvais fichier, merci de lancer 'main.py'")    