#Définie les param. de la turtle.
def parameter(turtle, size, size_square = 50): 
    turtle._tracer(0, 0)

    turtle.speed(0)
    turtle.hideturtle()
    turtle.pensize(1)
    turtle.pencolor('black')

    #Ajustement du carré au milieu de la fenêtre.
    turtle.penup()
    turtle.setpos((0-(size*size_square))/2, (0-(size*size_square))/2)
    turtle.pendown()

if __name__ == "__main__":
    print("Vous avez lancer le mauvais fichier, merci de lancer 'main.py'")