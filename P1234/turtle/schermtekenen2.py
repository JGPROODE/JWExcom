import turtle
import random

#random.random()
 

#pen object en screenobject aanmaken
pen = turtle.Turtle()
screen = turtle.Screen()
#turtle.mainloop()
#niet meet nodig vanaf 3.0
screen.screensize(800,800)
screen.colormode(255)


pen.speed(0)
pen.penup()
pen.pendown()


#screen.bgpic()
#'nopic'
#screen.bgpic('landschap.gif')
#screen.bgpic()
# "landscape.gif"

screen.bgcolor("green")
screen.bgcolor(90,180,70) 
print(str(screen.bgcolor()))


screen.update()

#initialiseren
lengte = 0
hoek = 0
pen.speed(0)
pen.penup()
pen.goto(0,100)
pen.pendown()



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
print("klaar")

"""
niet meer nodig vanaf versie 3.0
#turtle.done()
#screen.done()
"""
