import math
from turtle import Turtle

def drawCircle(t,x, y, radius):
    """Draws the specified circle."""
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.pencolor("blue")

    step_length = 2.0 * math.pi * radius / 120.0

    for i in range(120):
        t.forward(step_length)
        t.left(3)
