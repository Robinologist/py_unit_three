"""
For this project, use the assignment_three.py file.
Your program should first prompt the user for three pieces of information:
the length of a side of the hexagon
the color of the flower’s “petals”
the color of the center of the circle.
Your program should have at least the following functions:
get_side_length() - no parameters, returns a float.
get_center_color() - no parameters, returns a string
get_petal_color() - no parameters, returns a string
draw_hexagon(size, color) - has size (float) and color (string) as parameters, does not return anything.
a main() function that calls all the other functions.
Each of those functions (except for main) must include a brief document string (docstring) that describes the purpose of the function.
Make sure that each function other than main() has a document string detailing information about the purpose of the function, the parameters, and what is returned.
There should be header comments at the top of your file with your name, date last modified and overall purpose of the program. Throughout your code, you should have comments explaining pieces of code that are not immediately obvious.
You must try to use Unit Tests, but if they don’t work it won’t affect your grade. You should try creating tests for the get_side_length() and get_color() functions. Rather than using the self.assertEquals() function, you are going to use self.assertTrue() which makes sure that whatever is in the parentheses is a true statement. In these cases, you want to test that what is coming back from those functions is the correct type (either float or string). As a hint, to test if two things are equal, use two equal signs:
5 == 5 is True, "apple" == "banana" is False, type("banana") == str is True, type(34.5) == int is false.
Since these functions are getting user input, we need a way to test that input. There is a part of Python testing called Mock that will let you do this. A test using mock would look like this:
def test_input(self):
        with mock.patch('builtins.input', return_value="3"):
            assert type(assignment_three.get_side_length()) == float
	The important thing to note here is that the return_value parameter represents what the user input would be. Add another test to make sure that if the return value is a float, the function still returns a float. You can modify this to test for a string for the get_color() functions.
"""

import turtle

turtle.hideturtle()
turtle.speed(0)

def getSideLength():
    sideLength=input("What is the side length?\n")
    sideLength=int(sideLength)
    return sideLength
def getCenterColor():
    centerColor=input("What is the center color?\n")
    return centerColor
def getPetalColor():
    petalColor=input("What is the petal color?\n")
    return petalColor

def drawHexagons(sideLength,centerColor,petalColor):
    turtle.setheading(0)
    turtle.forward(sideLength/2)
    for x in range(6):
        turtle.left(360/6)
        turtle.forward(sideLength)
        drawSideHexagon(sideLength,petalColor)
    turtle.setheading(0)
    turtle.fillcolor(centerColor)
    turtle.begin_fill()
    for x in range(6):
        turtle.left(360/6)
        turtle.forward(sideLength)
    turtle.end_fill()


def drawSideHexagon(sideLength,petalColor):
    turtle.fillcolor(petalColor)
    turtle.begin_fill()
    for x in range(6):
        turtle.right(360 / 6)
        turtle.forward(sideLength)
    turtle.end_fill()

def main():
    sideLength = getSideLength()
    centerColor = getCenterColor()
    petalColor = getPetalColor()
    drawHexagons(sideLength,centerColor,petalColor)


main()

turtle.exitonclick()