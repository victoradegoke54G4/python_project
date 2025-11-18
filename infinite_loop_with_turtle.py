# upgraded 

import math
import turtle as t
import random

screen = t.Screen()
screen.bgcolor('black')
screen.tracer(0)
screen.colormode(255)

t.colormode(255)
my_turtle = t.Turtle()
my_turtle.speed(0)
my_turtle.pensize(3)
my_turtle.hideturtle()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

a=150
trail = t.Turtle()
trail.hideturtle()
trail.speed(0)
trail.pensize(2)

max_trail =100
points = []

while True:
    if a ==150:
        a-=2
    elif 100 <= a:
        a +=2
    for i in range(720):
        angle = math.radians(i)
        x = (a*math.sin(angle))
        y = (a*math.sin(angle) * math.cos(angle))

        t.pencolor(random_color())
        t.goto(x,y)

        points.append((x,y,random_color()))

        if len(points)> max_trail:
             points.pop(0)

        trail.clear()
        for idx, (px,py,color) in enumerate(points[-120:]):
             fade = int(idx/120)
             r,g,b = color
             trail.pencolor(r,g,b)
             trail.goto(px,py)  
        if i % 2 ==0:
             screen.update()
        i+=1     
t.done



# import math
# import turtle as t
# import random

# my_turtle = t.Turtle()
# screen = t.Screen()

# t.colormode(255)
# my_turtle.speed(0)
# my_turtle.pensize(3)
# screen.bgcolor('white')


# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return r,g,b

# a=150
# my_turtle.penup()
# my_turtle.goto(0,0)
# my_turtle.pendown()

# while True:
#     a-=1
#     for i in range(720):
#         angle = math.radians(i)
#         x = (a*math.sin(angle))
#         y = (a*math.sin(angle) * math.cos(angle))

#         r = int((math.sin(i*0.03)+1)/2)
#         g = int((math.sin(i*0.05+2)+1)/2)
#         b = int((math.sin(i*0.07+4)+1)/2)
        
#         my_turtle.pencolor(random_color())
#         my_turtle.goto(x,y)
# t.done
