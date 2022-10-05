import turtle
import random

#random.random()
 

#pen object en screenobject aanmaken
pen = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("black")
pen.color("green")
a = 0
b = 0
pen.speed(9)
pen.penup()
pen.goto(0,200)
pen.pendown()

turtle.colormode(255)

while True:

    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    pen.pencolor(red,green,blue)
    pen.forward(a)
    pen.right(b)
    a+=3
    b+=1
    if b ==210:
        break
    pen.hideturtle()

turtle.done()
