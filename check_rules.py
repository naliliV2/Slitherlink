def rules(size, grid):
    grid = acces_void(size, grid) 
    grid = around(size, grid)
    grid = max_take(size, grid) 
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

def around(size, grid):
    '''
    2ème règle
    
    Explication :
    Prenons tout les 8 carrés a coté de celui qu'on veut test : 
    Si tout les X (2) sont collés; il est possible de le prendre
    Si ils sont pas tous collés, il est impossible de le prendre
    Si le carré qu'on veut tester est sur le bord, on met des X là ou il y a pas de carré.    
    '''
    for line in range(0, size, 1): 
        for column in range(0, size, 1):
            
            if grid[line][column] == 2: #Passe si c'est déjà pris
                continue
            
            try: #Fait une suite de tout les carrés pour savoir si les X sont allignés. 
                suit = []
                if line == 0 or column == 0:#Provoque un IndexError car sur le bord
                    suit = suit[1]
                suit[len(suit):] = [grid[line-1][column-1], grid[line-1][column], grid[line-1][column+1]]
                suit[len(suit):] = [grid[line][column+1]]
                suit[len(suit):] = [grid[line+1][column+1], grid[line+1][column], grid[line+1][column-1]]
                suit[len(suit):] = [grid[line][column-1]]
            except IndexError: #Gère les exceptions (bord).
                suit = []
                if column == 0:
                    if line == 0:
                        suit[len(suit):] = [2, 2, 2]
                        suit[len(suit):] = [grid[line][column+1]]
                        suit[len(suit):] = [grid[line+1][column+1], grid[line+1][column], 2]
                        suit[len(suit):] = [2]
                    elif line == size-1:
                        suit[len(suit):] = [2, grid[line-1][column], grid[line-1][column+1]]
                        suit[len(suit):] = [grid[line][column+1]]
                        suit[len(suit):] = [2, 2, 2]
                        suit[len(suit):] = [2]
                    else: 
                        suit[len(suit):] = [2, grid[line-1][column], grid[line-1][column+1]]
                        suit[len(suit):] = [grid[line][column+1]]
                        suit[len(suit):] = [grid[line+1][column+1], grid[line+1][column], 2]
                        suit[len(suit):] = [2]
                elif column == size-1:
                    if line == 0:
                        suit[len(suit):] = [2, 2, 2]
                        suit[len(suit):] = [2]
                        suit[len(suit):] = [2, grid[line+1][column], grid[line+1][column-1]]
                        suit[len(suit):] = [grid[line][column-1]]
                    elif line == size-1:
                        suit[len(suit):] = [grid[line-1][column-1], grid[line-1][column], 2]
                        suit[len(suit):] = [2]
                        suit[len(suit):] = [2, 2, 2]
                        suit[len(suit):] = [grid[line][column-1]]
                    else:
                        suit[len(suit):] = [grid[line-1][column-1], grid[line-1][column], 2]
                        suit[len(suit):] = [2]
                        suit[len(suit):] = [2, grid[line+1][column], grid[line+1][column-1]]
                        suit[len(suit):] = [grid[line][column-1]] 
                elif line == 0:
                    suit[len(suit):] = [2, 2, 2]
                    suit[len(suit):] = [grid[line][column+1]]
                    suit[len(suit):] = [grid[line+1][column+1], grid[line+1][column], grid[line+1][column-1]]
                    suit[len(suit):] = [grid[line][column-1]] 
                elif line == size-1:
                    suit[len(suit):] = [grid[line-1][column-1], grid[line-1][column], grid[line-1][column+1]]
                    suit[len(suit):] = [grid[line][column+1]]
                    suit[len(suit):] = [2, 2, 2]
                    suit[len(suit):] = [grid[line][column-1]] 
            
            suit_copy, nb, enclenched = suit.copy(), 0, 0 

            if suit.count(2) == 0: #Pas de 2 au allentour.
                continue
            elif suit[1] !=2 and suit[3] !=2 and suit[5] !=2 and suit[7] !=2: #Si il y a des 2 et aucun adjaçant = forcément imp.
                continue

            while True: # Décallage
                if suit_copy[7] == 2:
                    offset = suit_copy.copy()
                    for i in range(8):
                        suit_copy[i] = offset[i-1]
                else:
                    suit = suit_copy 
                    break
      
            for i in range(8): #verification
                if enclenched == 1:
                    if nb == suit.count(2):
                        grid[line][column] = 1
                        break #C'est bon
                    elif suit[i] == 2:
                        nb+=1  
                    else:  
                        grid[line][column] = 0
                        break #C'est pas bon
                else:
                    if suit[i] == 2:
                        enclenched = 1
                        nb+=1   
    return grid

def max_take(size, grid): 
    '''
    Règle N°3 

    On ne peut prendre size-1 carré car sinon on coupe la figure en 2 ou on ne peut plus atteindre un
    des 4 bords. 
    '''
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
    print("Vous avez lancé le mauvais fichier, merci de lancer 'main.py'")