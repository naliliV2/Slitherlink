def rules(size, grid):
    grid = acces_void(size, grid) 
    grid = max_take(size, grid) 
    return grid

def around(size, grid):
    for line in range(1, size-1,1):
        for comlumn in range(1, size-1, 1):
            try:
                temp = []
                temp[len(temp):] = [grid[line-1][comlumn-1], grid[line-1][comlumn], grid[line-1][comlumn+1]]
                temp[len(temp):] = [grid[line][comlumn+1]]
                temp[len(temp):] = [grid[line+1][comlumn+1], grid[line+1][comlumn], grid[line+1][comlumn-1]]
                temp[len(temp):] = [grid[line][comlumn-1]]
            except IndexError:
                temp = []
                if comlumn == 0:
                    if line == 0:
                        temp[len(temp):] = [2, 2, 2]
                        temp[len(temp):] = [grid[line][comlumn+1]]
                        temp[len(temp):] = [grid[line+1][comlumn+1], grid[line+1][comlumn], 2]
                        temp[len(temp):] = [2]
                    elif line == size-1:
                        temp[len(temp):] = [2, grid[line-1][comlumn], grid[line-1][comlumn+1]]
                        temp[len(temp):] = [grid[line][comlumn+1]]
                        temp[len(temp):] = [2, 2, 2]
                        temp[len(temp):] = [2]
                    else: 
                        temp[len(temp):] = [2, grid[line-1][comlumn], grid[line-1][comlumn+1]]
                        temp[len(temp):] = [grid[line][comlumn+1]]
                        temp[len(temp):] = [grid[line+1][comlumn+1], grid[line+1][comlumn], 22]
                        temp[len(temp):] = [2]
                if comlumn == size-1:
                    if line == 0:
                        temp[len(temp):] = [grid[line-1][comlumn-1], grid[line-1][comlumn], grid[line-1][comlumn+1]]
                        temp[len(temp):] = [grid[line][comlumn+1]]
                        temp[len(temp):] = [grid[line+1][comlumn+1], grid[line+1][comlumn], grid[line+1][comlumn-1]]
                        temp[len(temp):] = [grid[line][comlumn-1]]
                    elif line == size-1:
                    else: 
                if line == 0:
                    if comlumn == 0:
                    elif comlumn == size-1:
                    else: 
                if line == size-1:
                    if comlumn

def acces_void(size, grid): #Verified 
    for line in range(1, size-1, 1):
        for column in range(1, size-1, 1):
            if grid[line][column] == 2:
                break
            elif grid[line-1][column] == 2 or grid[line+1][column] == 2 or grid[line][column-1] == 2 or grid[line][column+1] == 2:  
                grid[line][column] = 1
    return grid

def max_take(size, grid): #Verified ##Manque vertical x
    for i in range(0, size, 1): #Horizontal
        if grid[i].count(2) == size-1:
            for n in range(0, size, 1):
                if grid[i][n] == 1:
                    grid[i][n] = 0

    for column in range(0, size, 1):
        temp = 0
        for line in range(0, size, 1):
            if grid[line][column] == 2:
                temp += 1
        if temp == size-1:
            for line in range(0, size, 1):
                if grid[line][column] == 1:
                    grid[line][column] = 0
    return grid

if __name__ == "__main__":
    print("Vous avez lancer le mauvais fichier, merci de lancer 'main.py'")