import turtle
import random

random.random()
 


t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.color("green")
a = 0
b = 0
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()

turtle.colormode(255)

while True:

    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    t.pencolor(red,green,blue)
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b ==210:
        break
    t.hideturtle()

turtle.done()
