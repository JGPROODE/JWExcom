import turtle

t=turtle.Pen()
t.speed(0)

hoek=10
lengte = 100
tekst=str(hoek)+'°'

def tekenstreep(hoek, lengte):
    t.setheading(hoek)
    t.down()
    t.forward(lengte)
    t.write(str(hoek)+'°')
    t.up()
    t.backward(lengte)
    

for hoek in range(0,360,10):
    tekenstreep(hoek,120)


print("tekening klaar")
wacht=input("")
        
