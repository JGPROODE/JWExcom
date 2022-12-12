import turtle
import random
"""
Demo programma om wat turtlefuncties te laten zien.
Er wordt geen gebruik gemaakt van TKinter.
5-10-2021
J.G.P. Roode
"""
#pen object en screenobject aanmaken
pen = turtle.Turtle()
screen = turtle.Screen()

#pen aanmaken
pen.speed(0)
pen.penup()
pen.pendown()
#scherm instellen
screen.screensize(800,800)
screen.colormode(255)
screen.bgcolor("green")
print(str(screen.bgcolor()))
screen.bgcolor(90,60,160) 
print(str(screen.bgcolor()))

#initialiseren (beginwaarden instellen voor de tekening)
lengte = 0
hoek = 0
pen.speed(0)
pen.penup()
pen.goto(0,100)
pen.pendown()

#de tekening
while True:
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    pen.pencolor(red,green,blue)
    pen.forward(lengte)
    pen.right(hoek)
    lengte+=2
    hoek+=1
    if hoek ==210:
        break
    pen.hideturtle()

#bericht voor de user
print("klaar")
