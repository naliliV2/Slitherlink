from random import choice, randint

def create_grid(size, grid = []):
    '''
    Créé le tableau a double dimension (line, column)

    0 = Ne peut être pris
    1 = Peut être pris 
    2 = A été déjà pris 
    '''
    grid = [[0 for i in range(size)] for j in range(size)]
 
    return grid

def random_round(size):
    '''
    Défini le nombre de carré qu'on va mange
    '''
    return randint(size, (size**2)-size*2)

def defined_mine(size, grid):   
    '''
    Prend un carré qui peut être mangé aléatoirement
    '''
    mine = []
    for line in range(0, size, 1): #Stock ceux qui peut être pris. 
        for column in range(0, size, 1):
            if grid[line][column]==1: 
                mine.append([line, column])

    if len(mine) == 0: #Si on ne peut plus miner, on arrête tout.
        return "Stop"
    return choice(mine)

def mine(size, grid):
    '''
    Mine un carré
    '''
    mine = defined_mine(size, grid)
    if mine != "Stop":
        grid[mine[0]][mine[1]] = 2
        return grid, "Good"
    else:
        return grid, "Stop"

if __name__ == "__main__":
    print("Vous avez lancer le mauvais fichier, merci de lancer 'main.py'")    