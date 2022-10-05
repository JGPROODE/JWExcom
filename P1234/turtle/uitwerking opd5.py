import turtle
import random
x=0
y=0
rnd = 0
s = turtle.getscreen()
turtle.bgcolor("black")
turtle.title("Java bouncer part 2: Python boogaloo")


def vak():

    vt = turtle.Turtle()
    vt.pencolor('white')
    vt.pensize(10)
    vt.penup()
    vt.goto(-300, 300)
    vt.pendown()
    vt.forward(600)
    vt.rt(90)
    vt.fd(600)
    vt.rt(90)
    vt.fd(600)
    vt.rt(90)
    vt.fd(600)

def bounce():
    global rnd
    global x
    global y

    rnd = random.randint(5,85)
    print(str(rnd))
    
    lt = turtle.Turtle()
    lt.pencolor("purple")
    lt.forward(300)
    print(lt.ycor())

    if lt.pos() >= (280.00, lt.ycor()):
        lt.rt(rnd)
        lt.bk(1200)
    if lt.pos() <= (lt.xcor(), 200.00):
        lt.rt(rnd)
        lt.fd(1200)
    if lt.pos() <= (-280.00 , lt.ycor()):
        lt.rt(rnd)
        lt.fd(1200)
    if lt.pos() >= (lt.xcor(), -280.00):
        lt.lt(rnd)
        lt.fd(1200)
vak()
bounce()
turtle.done()
