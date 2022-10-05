import turtle

t = turtle.Pen()
s = turtle.getscreen()
t.speed(0)
turtle.bgcolor('black')



for i in range(5):
 for colours in ['red', 'yellow', 'magenta', 'blueviolet', 'lime', 'springgreen', 'cyan', 'blue']:
    t.color(colours)
    t.pensize(3)
    t.left(12)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
