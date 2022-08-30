import turtle
from turtle import *

screen = turtle.Screen()

t=turtle.Turtle()
speed(0)

t.penup()
t.goto(-400,250)
t.pendown()

#Orange color
t.color("orange")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(80)
t.right(90)
t.forward(400)
t.end_fill()
t.left(90)
t.forward(80)

#Green color
t.color("green")
t.begin_fill()
t.forward(80)
t.left(90)
t.forward(400)
t.left(90)
t.forward(80)
t.end_fill()

#Blue circle
t.penup()
t.goto(-155,130)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(40)
t.end_fill()

#White circle
t.penup()
t.goto(-161,130)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(34)
t.end_fill()

#Spokes
t.penup()
t.goto(-195,130)
t.pendown()
t.color("navy")
t.pensize(2)
for i in range(24):
    t.forward(34)
    t.backward(34)
    t.left(15)

#Pole
t.penup()
t.goto(-400,250)
t.pendown()
t.color("black")
t.pensize(15)
t.backward(500)

#Pole Stand
def rectangle():
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)

rectangle()
t.right(90)
t.forward(40)
rectangle()
t.forward(120)
rectangle()
t.right(90)
t.forward(40)
t.left(90)
t.forward(40)

turtle.done()
