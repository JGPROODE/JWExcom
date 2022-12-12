import turtle
import random
"""
Demo programma om wat turtlefuncties te laten zien.
Er wordt geen gebruik gemaakt van TKinter.
6-10-2021
J.G.P. Roode
"""
#pen object en screenobject aanmaken
pen = turtle.Turtle()
screen = turtle.Screen()

#pen aanmaken
pen.speed(0)
"""
pen.penup()
pen.pendown()
pen.up()
pen.down()
"""
#scherm instellen
screen.screensize(800,800)
screen.colormode(255)
for x in range(1,100,3):
    xstap=random.randint(-200,200)
    ystap=random.randint(-200,200)
    pen.up()
    pen.goto(xstap,ystap)
    pen.down()
    stap=random.randint(0,360)
    pen.circle(50,stap)
