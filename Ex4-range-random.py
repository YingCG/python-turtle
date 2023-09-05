from turtle import Turtle, Screen
import random

tim = Turtle()
tim.pensize(3)
# triangle have 3 side, square of 4 side, pentagon - 5 side, hexagon - 6 side, heptagon - 7 side, octagon - 8side ...
sideNums = 5
colorPallete = ['dodger blue', 'dark cyan', 'medium aquamarine', 'orange', 'deep pink' , 'dark orchid']

def drawShape(sideNums):
    angle = 360 / sideNums
    for i in range(sideNums):
        tim.forward(100)
        tim.right(angle)

# drawShape(3)

for i in range(3, 11):
    tim.color(random.choice(colorPallete))
    drawShape(i)

screen = Screen()
screen.exitonclick()