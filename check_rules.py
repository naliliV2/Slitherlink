def rules(size, grid):
    grid = acces_void(size, grid) #Qui met des 1 ##Corriged
    grid = between_two_square(size, grid) 
    
    grid = void_diago(size, grid) #Qui met des 0 ##Corriged 
    grid = max_take(size, grid) #Corriged
    return grid

def acces_void(size, grid): #Verified 
    for line in range(1, size-1, 1):
        for column in range(1, size-1, 1):
            if grid[line][column] == 2:
                break
            elif grid[line-1][column] == 2 or grid[line+1][column] == 2 or grid[line][column-1] == 2 or grid[line][column+1] == 2:  
                grid[line][column] = 1
                print("AV : ", "grid =(", line, column, ")", "=1")
                for i in range(len(grid)):
                    print(grid[i])
    return grid

def between_two_square(size, grid): #Verified ##A refiare en plus propre
    for line in range(0, size, 1):
        for column in range(0, size, 1):
            if grid[line][column] == 2:
               break 
            
            #En angle 
            try: #Haut droite 
                if grid[line-1][column+1] == 2 and grid[line-1][column] == 2 and grid[line][column+1]==2:
                    grid[line][column] = 1
                    succes_bts = 1
                    print("BTS AHD : ", "grid =(", line, column, ")", "=1")
                    for i in range(len(grid)):
                        print(grid[i])
            except IndexError:
                ussless = 0
            finally:
                try: #Haut gauche
                    if grid[line-1][column-1] == 2 and grid[line-1][column] == 2 and grid[line][column-1]==2:
                        grid[line][column] = 1
                        succes_bts = 1
                        print("BTS AHG : ", "grid =(", line, column, ")", "=1")
                        for i in range(len(grid)):
                            print(grid[i])
                except IndexError:
                    ussless = 0
                finally:
                    try: #Bas droite
                        if grid[line+1][column+1] == 2 and grid[line+1][column] == 2 and grid[line][column+1]==2:
                            grid[line][column] = 1
                            succes_bts = 1
                            print("BTS ABD : ", "grid =(", line, column, ")", "=1")
                            for i in range(len(grid)):
                                print(grid[i])
                    except IndexError:
                        ussless = 0
                    finally:
                        try: #Bas gauche
                            if grid[line+1][column-1] == 2 and grid[line+1][column] == 2 and grid[line][column-1]==2:
                                grid[line][column] = 1
                                succes_bts = 1
                                print("BTS ABG : ", "grid =(", line, column, ")", "=1")
                                for i in range(len(grid)):
                                    print(grid[i])
                        except IndexError:
                            ussless = 0
                if succes_bts == 1:
                    continue
           
            try: 
                if grid[line-1][column] == 2 and grid[line+1][column] == 2: #Vertical
                    if 
                    
            except IndexError:



    return grid

def void_diago(size, grid): #Verified
    for line in range(0, size, 1):
        for column in range(0, size, 1):
            if grid[line][column] == 2: #Déjà manger
                continue
            
            if line > 0 and column < size-1 : 
                if grid[line-1][column+1] == 2: #Haut droite
                    if grid[line][column+1] == 2 or grid[line-1][column] == 2:
                        grid[line][column] = 1 
                        print("VD HD : ", "grid =(", line, column, ")", "=1")
                        for i in range(len(grid)):
                            print(grid[i])
                    else:
                        grid[line][column] = 0
                        print("VD HD : ", "grid =(", line, column, ")", "=0")
                        for i in range(len(grid)):
                            print(grid[i])
                        continue
            
            if line > 0 and column > 0:
                if grid[line-1][column-1] == 2: #Haut gauche
                    if grid[line][column-1] == 2 or grid[line-1][column] == 2:
                        grid[line][column] = 1 
                        print("VD HG : ", "grid =(", line, column, ")", "=1")
                        for i in range(len(grid)):
                            print(grid[i])
                    else:
                        grid[line][column] = 0
                        print("VD HG : ", "grid =(", line, column, ")", "=0")
                        for i in range(len(grid)):
                            print(grid[i])
                        continue
    
            if line < size-1 and column < size-1:
                if grid[line+1][column+1] == 2: #Bas droite
                    if grid[line][column+1] == 2 or grid[line+1][column] == 2:
                        grid[line][column] = 1
                        print("VD BD : ", "grid =(", line, column, ")", "=1")
                        for i in range(len(grid)):
                            print(grid[i]) 
                    else:
                        grid[line][column] = 0
                        print("VD BD : ", "grid =(", line, column, ")", "=0")
                        for i in range(len(grid)):
                            print(grid[i])
                        continue

            if column > 0 and line < size-1:
                if grid[line+1][column-1] == 2: #Bas gauche
                    if grid[line][column-1] == 2 or grid[line+1][column] == 2:
                        grid[line][column] = 1 
                        print("VD BG : ", "grid =(", line, column, ")", "=1")
                        for i in range(len(grid)):
                            print(grid[i])
                    else:
                        grid[line][column] = 0
                        print("VD BG : ", "grid =(", line, column, ")", "=0")
                        for i in range(len(grid)):
                            print(grid[i])
                        continue
    return grid
                                        
def max_take(size, grid): #Verified ##Manque vertical x
    for i in range(0, size, 1): #Horizontal
        if grid[i].count(2) == size-1:
            for n in range(0, size, 1):
                if grid[i][n] == 1:
                    grid[i][n] = 0
            print("MTH ligne :", i)
            for i in range(len(grid)):
                print(grid[i])

    for column in range(0, size, 1):
        temp = 0
        for line in range(0, size, 1):
            if grid[line][column] == 2:
                temp += 1
        if temp == size-1:
            for line in range(0, size, 1):
                if grid[line][column] == 1:
                    grid[line][column] = 0
            print("MTH ligne :", i)
            for i in range(len(grid)):
                print(grid[i])
    return grid

if __name__ == "__main__":
    print("Vous avez lancer le mauvais fichier, merci de lancer 'main.py'")