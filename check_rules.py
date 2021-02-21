def rules(size, grid):
    grid = acces_void(size, grid) 
    grid = around(size, grid)
    grid = max_take(size, grid) 
    return grid

def around(size, grid):
    for line in range(0, size, 1):
        for column in range(0, size, 1):
            print(line, column)
            if grid[line][column] == 2:
                continue
            try:
                temp = []
                if line == 0 or column == 0:#Provoque un IndexError
                    temp = temp[1]
                temp[len(temp):] = [grid[line-1][column-1], grid[line-1][column], grid[line-1][column+1]]
                temp[len(temp):] = [grid[line][column+1]]
                temp[len(temp):] = [grid[line+1][column+1], grid[line+1][column], grid[line+1][column-1]]
                temp[len(temp):] = [grid[line][column-1]]
            except IndexError:
                temp = []
                if column == 0:
                    if line == 0:
                        temp[len(temp):] = [2, 2, 2]
                        temp[len(temp):] = [grid[line][column+1]]
                        temp[len(temp):] = [grid[line+1][column+1], grid[line+1][column], 2]
                        temp[len(temp):] = [2]
                    elif line == size-1:
                        temp[len(temp):] = [2, grid[line-1][column], grid[line-1][column+1]]
                        temp[len(temp):] = [grid[line][column+1]]
                        temp[len(temp):] = [2, 2, 2]
                        temp[len(temp):] = [2]
                    else: 
                        temp[len(temp):] = [2, grid[line-1][column], grid[line-1][column+1]]
                        temp[len(temp):] = [grid[line][column+1]]
                        temp[len(temp):] = [grid[line+1][column+1], grid[line+1][column], 2]
                        temp[len(temp):] = [2]
                elif column == size-1:
                    if line == 0:
                        temp[len(temp):] = [2, 2, 2]
                        temp[len(temp):] = [2]
                        temp[len(temp):] = [2, grid[line+1][column], grid[line+1][column-1]]
                        temp[len(temp):] = [grid[line][column-1]]
                    elif line == size-1:
                        temp[len(temp):] = [grid[line-1][column-1], grid[line-1][column], 2]
                        temp[len(temp):] = [2]
                        temp[len(temp):] = [2, 2, 2]
                        temp[len(temp):] = [grid[line][column-1]]
                    else:
                        temp[len(temp):] = [grid[line-1][column-1], grid[line-1][column], 2]
                        temp[len(temp):] = [2]
                        temp[len(temp):] = [2, grid[line+1][column], grid[line+1][column-1]]
                        temp[len(temp):] = [grid[line][column-1]] 
                elif line == 0:
                    temp[len(temp):] = [2, 2, 2]
                    temp[len(temp):] = [grid[line][column+1]]
                    temp[len(temp):] = [grid[line+1][column+1], grid[line+1][column], grid[line+1][column-1]]
                    temp[len(temp):] = [grid[line][column-1]] 
                elif line == size-1:
                    temp[len(temp):] = [grid[line-1][column-1], grid[line-1][column], grid[line-1][column+1]]
                    temp[len(temp):] = [grid[line][column+1]]
                    temp[len(temp):] = [2, 2, 2]
                    temp[len(temp):] = [grid[line][column-1]] 
            
            temp2 = temp.count(2)
            temp3 = temp.copy()
            nb = 0
            enclenched = 0

            if temp2 == 0: #Pas de 2 au allentour.
                continue

            elif temp[1] !=2 and temp[3] !=2 and temp[5] !=2 and temp[7] !=2: #Si il y a des 2 et aucun adjaçant = forcément faux
                continue

            while True: # Décallage
                if temp3[7] == 2:
                    temp4 = temp3.copy()
                    for i in range(8):
                        temp3[i] = temp4[i-1]
                else:
                    temp = temp3 
                    break
      
            for i in range(8): #verification
                if enclenched == 1:
                    if nb == temp2:
                        grid[line][column] = 1
                        break #C'est bon
                    elif temp[i] == 2:
                        nb+=1  
                    else:  
                        grid[line][column] = 0
                        break #C'est pas bon
                else:
                    if temp[i] == 2:
                        enclenched = 1
                        nb+=1   
    return grid

def acces_void(size, grid): #Verified 
    for line in range(1, size-1, 1):
        for column in range(1, size-1, 1):
            if grid[line][column] == 2:
                continue
            
            elif grid[line-1][column] == 2 or grid[line+1][column] == 2 or grid[line][column-1] == 2 or grid[line][column+1] == 2:  
                grid[line][column] = 1
                continue
            
            elif grid[line-1][column] == 0 or 1 and grid[line+1][column] == 0 or 1 and grid[line][column-1] == 0 or 1 and grid[line][column+1] == 0 or 1:
                grid[line][column] = 0
                continue
            
    return grid

def max_take(size, grid): #Verified 
    for line in range(0, size, 1): #Horizontal
        if grid[line].count(2) == size-1:
            for column in range(0, size, 1):
                if grid[line][column] == 1:
                    grid[line][column] = 0
                    
    for column in range(0, size, 1): #Vertical
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