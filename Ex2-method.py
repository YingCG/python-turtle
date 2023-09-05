from turtle import Turtle, Screen

drawing = Turtle()
drawing.shape("circle")
# https://docs.python.org/3/library/turtle.html#turtle.shape

drawing.color("red")
# color pallete: https://trinket.io/docs/colors

drawing.pensize(width=3)

# Some steps for one square
def drawSquare():
    drawing.forward(100)
    drawing.left(90)
    drawing.forward(100)
    drawing.left(90)
    drawing.forward(100)
    drawing.left(90)
    drawing.forward(100)
    drawing.left(90)


drawSquare()
drawing.color("hot pink")
drawSquare()
drawing.color("gold")
drawSquare()
drawing.color("lawn green")
drawSquare()
drawing.color("medium spring green")
drawSquare()

screen = Screen()
screen.title("Drawing some square")
screen.exitonclick()