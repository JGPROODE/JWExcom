import turtle
t=turtle.Pen()
ystep=-200
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
x=4
t.penup()
t.goto(0,ystep)
t.pendown()
t.fillcolor(colors[x])#x%6])
t.begin_fill()
t.circle(50)
t.end_fill()
ystep+=100
x=1
t.penup()
t.goto(0,ystep)
t.pendown()
t.fillcolor(colors[x])#x%6])
t.begin_fill()
t.circle(50)
t.end_fill()
ystep+=100
x=2
t.penup()
t.goto(0,ystep)
t.pendown()
t.fillcolor(colors[x])#x%6])
t.begin_fill()
t.circle(50)
t.end_fill()
ystep+=100
        
