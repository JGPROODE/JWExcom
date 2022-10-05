#[15:34] Melle Huibers
    
import turtle
t=turtle.Pen()
xpos=-300
ypos=-200
t.speed(0)
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(0,24):
    if (x%6==0):
        xpos+=110
        ypos= -200
        print(str(x)+ "-->"+str(ypos))
    t.penup()
    t.goto(xpos,ypos)
    t.pendown()
    t.fillcolor(colors[x%6])
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    ypos+=100
    
print(str(x)+"---"+str(xpos)+" - "+str(ypos)) 
 
