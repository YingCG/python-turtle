import turtle as t
import random

screen = t.Screen()
screen.bgcolor("black")
screen.setup(1200, 800)
screen.title("Circle-circle-circles")
screen.colormode(255)

c = t.Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def drawMandala(gapsize):
    numOfCircles = 0
    while numOfCircles < (360/gapsize):
        if numOfCircles % 36 == 0 and numOfCircles != 0:
            c.penup()
            c.forward(300)
            c.pendown()
        c.speed("fastest")
        c.color(random_color())
        c.circle(100)
        # current = c.heading()
        # c.setheading(current + 10)
        c.setheading(c.heading() + gapsize)
        c.circle(100)
        numOfCircles += 1

drawMandala(5)
screen.exitonclick()
