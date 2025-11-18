import math
import turtle as t
import random

my_turtle = t.Turtle()
screen = t.Screen()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b


t.colormode(255)
my_turtle.pensize(3)
my_turtle.speed(0)

directions = [0, 90, 180, 270]
step_size = random.randint(20,30)
my_turtle.setheading(random.choice(directions))


while True:
    my_turtle.color(random_color())

    my_turtle.fd(step_size)
    my_turtle.setheading(random.choice(directions))

t.done