#TurtleGraphics.py
#Name: Alex Hernandez Lopez
#Date: 2/15/25
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)

def fillCorner(bob, corner):
    drawSquare(bob, 100)
    
    if corner == 1:
        bob.begin_fill()
        drawSquare(bob, 50)
        bob.end_fill()
    elif corner == 2:
        bob.forward(50)
        bob.begin_fill()
        drawSquare(bob, 50)
        bob.end_fill()
    elif corner == 3:
        bob.right(90)
        bob.forward(50)
        bob.left(90)
        bob.begin_fill()
        drawSquare(bob, 50)
        bob.end_fill()
    else:
        bob.right(90)
        bob.forward(50)
        bob.left(90)
        bob.up()
        bob.forward(50)
        bob.down()
        bob.begin_fill()
        drawSquare(bob, 50)
        bob.end_fill()

def main():
    myTurtle = turtle.Turtle()
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
