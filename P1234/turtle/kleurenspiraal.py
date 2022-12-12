#from turtle import *
import turtle
import random

t=turtle.Pen()

def tekenCirkels(d1, d2):
    t.speed(0)
    t.up()
    t.goto(0,-200)
    t.down()
    colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
    for x in range(100):
        diameter = random.randint(d1, d2 )
        kleur=random.randint(0,5)
        t.pencolor(colors[kleur])
        t.up()
        t.goto(0,-diameter)
        t.down()
        t.circle(diameter)
 
tekenCirkels(10,300)
