#[15:34] Melle Huibers
    
import turtle
t=turtle.Pen()
ystep=-200
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(0,6):
    t.penup()
    t.goto(0,ystep)
    t.pendown()
    t.fillcolor(colors[x])#x%6])
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    ystep+=100
    
   
 
