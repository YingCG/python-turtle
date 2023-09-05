import turtle as t
import random

screen = t.Screen()
screen.title("Dot-Dot-Dot")

t.colormode(255)
polka = t.Turtle()
polka.penup()
polka.hideturtle()

polka.setposition(-220, -220)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

polka.setheading(0)
def hirstArt():
    for i in range(10):
        for _ in range(10):
            polka.dot(15, random_color())
            polka.forward(50)

        if i % 2 == 0:
            # if we are at even line turn left twice
            polka.left(90)
            polka.forward(50)
            polka.left(90)
            polka.forward(50)
            
        else:
            # if we are at odd line turn left twice
            polka.right(90)
            polka.forward(50)
            polka.right(90)
            polka.forward(50)



        

hirstArt()
    
screen.exitonclick()