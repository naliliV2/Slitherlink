from turtle import Turtle, Screen

from time import sleep
import os
import canvasvg 
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

def draw_grid(turtle):
    for x in range(-150, 151, 100):
        for y in range(-150, 151, 100):
            turtle.penup()
            turtle.setposition(x, y)
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(15)
            turtle.end_fill()

def nord(turtle):
    tpos = turtle.position()
    turtle.pendown()
    turtle.setposition(tpos[0], tpos[1] + 100 )
    turtle.penup()   
def est(turtle): 
    tpos = turtle.position()
    turtle.pendown()
    turtle.setposition(tpos[0] + 100, tpos[1])
    turtle.penup()
def sud(turtle):
    tpos = turtle.position()
    turtle.pendown()
    turtle.setposition(tpos[0], tpos[1] - 100 )
    turtle.penup()
def ouest(turtle):
    tpos = turtle.position()
    turtle.pendown()
    turtle.setposition(tpos[0] - 100, tpos[1])
    turtle.penup() 

def execution(turtle, path, start_x, start_y): 
    turtle.penup()
    turtle.setposition(-150 + (100*start_x), 165+(0-100*start_y))

    for i in range(len(path)):
        if path[i] == "N":
            nord(turtle)
        elif path[i] == "E":
            est(turtle)
        elif path[i] == "S":
            sud(turtle)    
        elif path[i] == "O":
            ouest(turtle)

def get_image(screen, path):
    try:
        os.mkdir("Grille")
        os.mkdir("temp")
    except:
        1+1 #Pas le choix
    canvasvg.saveall("temp/test.svg", screen.getcanvas())
    drawing = svg2rlg("temp/test.svg")
    pathfile = "Grille/"
    for i in range(len(path)):
        pathfile += path[i]+"/"
        try: 
            os.mkdir(pathfile)
        except: 
            continue
    renderPM.drawToFile(drawing, pathfile+"grid.png", fmt="PNG")
    
def main_draw_grid(path, start_x, start_y):
    screen = Screen()
    turtle = Turtle()
    turtle._tracer(1, 1)
    turtle.speed(0)
    turtle.pensize(5)
    turtle.ht()

    draw_grid(turtle)
    execution(turtle, path, start_x, start_y)
    get_image(screen, path)
    
    turtle._update()
    turtle.clear()