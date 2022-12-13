import turtle

"""
Programmeur: JW Roode
Datum: 19-10-2022
1 import voor de tekenfuncties
Doel: demo voor commentaar en for-loop
"""

t=turtle.Pen()

#0 is het snelst 9 het langzaamst
t.speed(0)

# variabele hoek en lengte worden gebruikt om 
# een lijn te tekenen onder een bepaalde hoek met een bepaalde lengte
# de variabele tekst wordt gebruikt om info op het scherm af te kunnen drukken
hoek=10
lengte = 100
tekst=str(hoek)+'°'

# de eerste lijn
t.setheading(hoek)
t.forward(lengte)
t.write(str(hoek)+'°')
t.backward(lengte)

# hoek vergroten
hoek+=10

# de tweede lijn
t.setheading(hoek)
t.forward(lengte)
t.write(str(hoek)+'°')
t.backward(lengte)

hoek+=10
t.setheading(hoek)
t.forward(lengte)
t.write(str(hoek)+'°')
t.backward(lengte)

hoek+=10
t.setheading(hoek)
t.forward(lengte)
t.write(str(hoek)+'°')
t.up()
t.backward(lengte)


hoek+=10
t.setheading(hoek)
t.down()
t.forward(lengte)
t.write(str(hoek)+'°')
t.up()
t.backward(lengte)


"""
POrogrammeur : JW Roode
datum: 19-10-2022
Functie om een lijn van een bepaalde lengte te tekenen omnder een bepaalde hoek
met twee paremeters
input:  int en  int
return value: geen (none)
"""

def tekenstreep(hoek, lengte):
    t.setheading(hoek)
    t.down()
    t.forward(lengte)
    t.write(str(hoek)+'°')
    t.up()
    t.backward(lengte)
    
"""
For loop waar mee heel vaak de functie wordt aangeroepen zodat er veel lijnen
onder een bepaalde hoek worden getekend.
"""
for hoek in range(0,360,10):
    tekenstreep(hoek,120)



"""

for angle in range(0, 360, 15):
    t.setheading(angle)
    t.forward(100)
    t.write(str(angle) + '°')
    t.backward(100)

""" 



# statement bedoelt om het scherm te laten zien. Mag weg na de testfase

print("tekening klaar")
wacht=input("")
            