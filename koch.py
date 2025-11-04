import turtle
from turtle import Turtle

def drawFractalLine(t, distance, angle, level):
    """Recursively draws a Koch fractal line."""
    if level == 0:
        t.forward(distance)
    else:
        distance /= 3.0
        drawFractalLine(t, distance, angle, level - 1)
        t.left(60)
        drawFractalLine(t, distance, angle + 60, level - 1)
        t.right(120)
        drawFractalLine(t, distance, angle - 60, level - 1)
        t.left(60)
        drawFractalLine(t, distance, angle, level - 1)

def main():
    t = Turtle()
    t.speed()
    t.penup()
    t.goto(-150, 100)
    t.pendown()

    distance = 300
    level = 3

    for angle in [0, -120, 120]:
        drawFractalLine(t, distance, angle, level)
        t.right(120)

if __name__ == "__main__":
    main()
