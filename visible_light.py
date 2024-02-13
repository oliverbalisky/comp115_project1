import turtle 
import math

def drawCeilingLight (t):

    """draw main circles for ceiling light"""

    light_colors = ["grey10", "lemonchiffon", "FloralWhite", "cornsilk1", "beige", "LightGoldenrodYellow", "LightYellow", "white"]
    radius_change = [80, 70, 60, 50, 40, 30, 20, 10]

    for i in range (8):

        moveTurtle(t, 0, -radius_change[i])
        t.color(light_colors[i])
        t.begin_fill()
        t.circle(radius_change[i])
        t.end_fill()

        radius_change1 = int(radius_change[i])

        moveTurtle(t, 0, -radius_change[i])
     
        if radius_change [i] == 80: 
            for r in Rainbow:
                
                t.color(r)
                t.circle(radius_change1)
                t.up()
                t.right(90)
                t.forward(1)
                t.left(90)
                t.down()
                radius_change1 = radius_change1 + 1
        else:
            pass
    
    darkArea(t)

def moveTurtle (t, x, y):

    """ move turtle to x/y coordinate"""

    t.up()
    t.goto(x, y)
    t.down()

def square(t, side):

    """draw ONE of the 4 corners of the squares that make up the lightrays"""

    for i in range (1):
        t.up()
        t.forward(side)
        t.left(90)
        t.down()
    for i in range (2):
        t.forward(side)
        t.left(90)
    for i in range (1):
        t.up()
        t.forward(side)
        t.left(90)
        t.down()

def drawSquares(t, side):

    """draw the 4 parts of the square that make up the light rays"""

    for i in range (4):
        square(t, side)
        t.left(90)
        
def drawRainbow(t, side):

    """draws the rainbow light rays """

    for color in (Rainbow):
        t.color(color)
        drawSquares(t, side)
        t.left(2)

def findHyp(x):

    """find the outter circumfrence the previous circle of lightrays"""
    hyp = math.sqrt(((2*x)**2) + ((2*x)**2))
    return hyp/2
    
def darkArea(t):

    """create negative dark corners"""

    corner_x = [500,  500, -500, -500]
    corner_y = [50, -950,  50, -950]
    for i in range (4):

        moveTurtle(t, corner_x[i], corner_y[i])
        t.color("white", "black")
        t.begin_fill()
        t.circle (450)
        t.end_fill()


def drawLightRays(t, side, spin):

    """draw the series of the rainbow lightrays """

    moveTurtle(t, 0, 0)
    for _ in range (5):

        for _ in range (4):
            drawRainbow(t, side)
            t.left(360/spin)

        side = findHyp(side)

        
wn = turtle.Screen()
light = turtle.Turtle()

wn.setup(height=1000,width=1000)
light.speed(0)
turtle.screensize(canvwidth = 1000, canvheight = 1000, bg = "black")

Rainbow = ["OrangeRed", "orange", "khaki1", "gold", "SpringGreen1", "turquoise", "RoyalBlue4"]

drawCeilingLight(light)

drawLightRays(light, 90, 7)

light.hideturtle()

wn.exitonclick()



