from turtle import Turtle, Screen
from random import random


tim = Turtle()
tom = Turtle()
tam = Turtle()

tim.shape("turtle")
tom.shape("triangle")
tam.shape("circle")

def drawDashLine(x: Turtle, distance):
    distanceCovered = 0
    while distanceCovered < distance:
        x.forward(10)
        x.penup()
        x.forward(10)
        x.pendown()
        distanceCovered += 20    
    
def drawSquare():
    for i in range(4): 
        drawDashLine(tim, 110)   
        # tim.forward(100)
        tom.forward(200)
        tam.forward(300)
        
        tim.left(90)
        tom.left(90)
        tam.left(90)
        
drawSquare()


screen = Screen()
screen.exitonclick()