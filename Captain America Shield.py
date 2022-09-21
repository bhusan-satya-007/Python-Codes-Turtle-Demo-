import turtle
import math

satya = turtle.Turtle()


def func_1(x, y):
    satya.penup()
    satya.goto(x, y)
    satya.pendown()
    satya.setheading(0)
    satya.pensize(2)
    satya.speed(10)


def circle(r, color):
    x_point = 0
    y_pont = -r
    func_1(x_point, y_pont)
    satya.pencolor(color)
    satya.fillcolor(color)
    satya.begin_fill()
    satya.circle(r)
    satya.end_fill()


def star(r, color):
    func_1(0, 0)
    satya.pencolor(color)
    satya.setheading(162)
    satya.forward(r)
    satya.setheading(0)
    satya.fillcolor(color)
    satya.begin_fill()
    for i in range(5):
        satya.forward(math.cos(math.radians(18)) * 2 * r)
        satya.right(144)
    satya.end_fill()
    satya.hideturtle()


if __name__ == '__main__':
    circle(288, 'crimson')
    circle(234, 'snow')
    circle(174, 'crimson')
    circle(114, 'blue')
    star(114, 'snow')
    turtle.done()
