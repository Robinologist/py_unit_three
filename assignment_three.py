"""
Robin Engdahl, 10/20/22

This project creates 6 hexagons surrounding a center hexagon,
prompting the user for a side length and colors for the center and edge hexagons.
"""

import turtle

turtle.hideturtle()
turtle.speed(0)

"""Prompts the user for the side length of the hexagons and returns the value"""
def getSideLength():
    sideLength=input("What is the side length?\n")
    sideLength=int(sideLength)
    return sideLength

"""Prompts the user for the color of the center hexagon and returns the value"""
def getCenterColor():
    centerColor=input("What is the center color?\n")
    return centerColor

"""Prompts the user for the color of the side hexagons and returns the value"""
def getPetalColor():
    petalColor=input("What is the petal color?\n")
    return petalColor

"""Uses the values the user inputted (sideLength, centerColor, & petalColor)
to draw a main hexagon and draw side hexagons at each point on the main one"""
def drawHexagons(sideLength,centerColor,petalColor):
    turtle.setheading(0)
    turtle.forward(sideLength / 2)
    turtle.fillcolor(centerColor)
    turtle.begin_fill()
    for x in range(6):
        turtle.left(360 / 6)
        turtle.forward(sideLength)
    turtle.end_fill()
    turtle.setheading(0)
    for x in range(6):
        turtle.left(360/6)
        turtle.forward(sideLength)
        drawSideHexagon(sideLength,petalColor)

"""Draws a side hexagon"""
def drawSideHexagon(sideLength,petalColor):
    turtle.fillcolor(petalColor)
    turtle.begin_fill()
    for x in range(6):
        turtle.right(360 / 6)
        turtle.forward(sideLength)
    turtle.end_fill()

"""Runs the other functions in order"""
def main():
    sideLength = getSideLength()
    centerColor = getCenterColor()
    petalColor = getPetalColor()
    drawHexagons(sideLength,centerColor,petalColor)
    turtle.exitonclick()


main()