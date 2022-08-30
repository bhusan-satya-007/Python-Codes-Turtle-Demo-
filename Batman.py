import turtle
import math

satya = turtle.Turtle()
satya.speed(500)

window = turtle.Screen()
window.bgcolor("#000000")
satya.color("yellow")

sb = 20

satya.left(90)
satya.penup()
satya.goto(-7 * sb, 0)
satya.pendown()

for a in range(-7 * sb, -3 * sb, 1):
    x = a / sb
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    satya.goto(a, y * sb)

for a in range(-3 * sb, -1 * sb - 1, 1):
    x = a / sb
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    satya.goto(a, y * sb)

satya.goto(-1 * sb, 3 * sb)
satya.goto(int(-0.5 * sb), int(2.2 * sb))
satya.goto(int(0.5 * sb), int(2.2 * sb))
satya.goto(1 * sb, 3 * sb)
print("Batman Logo with Python Turtle")
for a in range(1 * sb + 1, 3 * sb + 1, 1):
    x = a / sb
    rel = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
        math.fabs(rel - 1) / (rel - 1))
    satya.goto(a, y * sb)

for a in range(3 * sb + 1, 7 * sb + 1, 1):
    x = a / sb
    rel = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
    satya.goto(a, y * sb)

for a in range(7 * sb, 4 * sb, -1):
    x = a / sb
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    satya.goto(a, y * sb)

for a in range(4 * sb, -4 * sb, -1):
    x = a / sb
    rel = math.fabs(x)
    y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(rel - 2) - 1) ** 2)
    satya.goto(a, y * sb)

for a in range(-4 * sb - 1, -7 * sb - 1, -1):
    x = a / sb
    rel = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
    satya.goto(a, y * sb)

satya.penup()
satya.goto(300, 300)
turtle.done()
