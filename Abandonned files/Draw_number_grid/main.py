import turtle
import os
import canvasvg 
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

def draw_grid():
    for x in range(-150, 151, 100):
        for y in range(-150, 151, 100):
            turtle.penup()
            turtle.setposition(x, y)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(15)
            turtle.end_fill()

def forward(n): #Right
    for i in range(0, n, 1):
        tpos = turtle.position()
        turtle.pendown()
        turtle.setposition(tpos[0] + 100, tpos[1])
        turtle.penup()

def back(n): #left
    for _ in range(0, n, 1):
        tpos = turtle.position()
        turtle.pendown()
        turtle.setposition(tpos[0] - 100, tpos[1])
        turtle.penup()

def down(n):
    for _ in range(0, n, 1):
        tpos = turtle.position()
        turtle.pendown()
        turtle.setposition(tpos[0], tpos[1] - 100 )
        turtle.penup()
        
def up(n):
    for _ in range(0, n, 1):
        tpos = turtle.position()
        turtle.pendown()
        turtle.setposition(tpos[0], tpos[1] + 100 )
        turtle.penup()    

def translate(awser):
    splt = awser.split(" ")
    splt2 = [[0 for i in range(len(splt[j]))] for j in range(len(splt))]
    for i in range(len(splt)):
        for i1 in range(len(splt[i])):
            splt2[i][i1] = splt[i][i1]
    return splt2
    
def execution(directive): 
    turtle.penup()
    turtle.setposition(-150, 165)

    for i in range(len(directive)):
        if directive[i][0] == "F":
            forward(int(directive[i][1]))
        elif directive[i][0] == "B":
            back(int(directive[i][1]))
        else: 
            input("ERREUR : Merci de redémarer le programme")
            10/0
        
        if directive[i][2] == "U":
            up(int(directive[i][3]))
        elif directive[i][2] == "D":
            down(int(directive[i][3]))    
        else: 
            input("ERREUR : Merci de redémarer le programme")
            10/0

def print_number(list_x):    
    style = ('Arial', 75, 'normal')
    turtle.penup()
    if list_x[0][0] != "/":
        turtle.setposition(-100, 55)
        turtle.write(str(list_x[0][0]), font=style, align='center')   
    if list_x[1][0] != "/":
        turtle.setposition(0, 55)
        turtle.write(str(list_x[1][0]), font=style, align='center')
    if list_x[2][0] != "/":
        turtle.setposition(100, 55)
        turtle.write(str(list_x[2][0]), font=style, align='center')
    if list_x[3][0] != "/":
        turtle.setposition(-100, -45)
        turtle.write(str(list_x[3][0]), font=style, align='center')
    if list_x[4][0] != "/":
        turtle.setposition(0, -45)
        turtle.write(str(list_x[3][0]), font=style, align='center')
    if list_x[5][0] != "/":
        turtle.setposition(100, -45)
        turtle.write(str(list_x[3][0]), font=style, align='center')
    if list_x[6][0] != "/":
        turtle.setposition(-100, -145)
        turtle.write(str(list_x[3][0]), font=style, align='center')
    if list_x[7][0] != "/":
        turtle.setposition(0, -145)
        turtle.write(str(list_x[3][0]), font=style, align='center')
    if list_x[8][0] != "/":
        turtle.setposition(100, -145)
        turtle.write(str(list_x[3][0]), font=style, align='center')
    
def get_image(splt, name):
    try:
        os.mkdir("Grille")
        os.mkdir("temp")
    except:
        1+1 #Pas le choix
    canvasvg.saveall("temp/test.svg", turtle.getcanvas())
    drawing = svg2rlg("temp/test.svg")
    path = "Grille/"
    for i in range(len(splt)):
        temp = ""
        for i1 in range(len(splt[i])):
            temp += splt[i][i1]
        path += temp+"/"
        try: 
            os.mkdir(path)
        except: 
            continue

    fname = ""
    for i in range(4):
        if name[i][0] != "/":
            fname += name[i][0]
        else: 
            fname += "_" 
    renderPM.drawToFile(drawing, path+fname+".png", fmt="PNG")
    
def main():
    awser = input("Paterne : ")
    awser2 = input("Chiffre : ")
    draw_grid()
    splt1 = translate(awser)
    execution(splt1)
    splt2 = translate(awser2)
    print_number(splt2)
    get_image(splt1, splt2)
    
if __name__ == "__main__":
    while True:
        turtle.speed(0)
        turtle.ht()
        main()
        input()
        turtle.reset()