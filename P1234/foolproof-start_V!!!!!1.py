'''
Bereken de entreeprijs
Volwassenen betalen 2,50 euro
Kinderen betalen 7,50 euro
Elk kind word door tenminste 1 volwassene begeleid
Per volwassene zijn 2 kinderen toegestaan
De groepsgrootte mag niet groter zijn dan 10
'''
while True:

    # Hoeveel kinderen?
    kinderen = 0
    while kinderen <= 0:
        try:
            kinderen = int(input("Hoeveel kinderen?\n"))
            if kinderen >= 7:
                raise Exception 

        except ValueError:
            print("Dit is geen getal!")
        except Exception :
            print("Met zoveel kinderen mogen er niet meer genoeg ouders binnen komen!(Voor elke 2 kinderen is 1 volwassenen nodig.)")
            kinderen = 0
        except:
            Print("er is een andere fout opgetreden !")   


    # Hoeveel volwassenen?
    volwassenen = 0
    while volwassenen <= 0:
        try:
            volwassenen = int(input("Hoeveel volwassenen?\n"))
        except ValueError:
            print("Dit is geen getal!")

    # Check aantal kinderen per volwassene
    if kinderen / 2 > volwassenen:
        print("Voor elke twee kinderen is een volwassene nodig. Voer de aantallen opnieuw in.")

    # Check totale groepsgrootte
    elif kinderen + volwassenen > 10:
        print("Dit zijn teveel mensen. Voer de aantallen opnieuw in.")
        
    else:
        break

# Bereken het bedrag
bedrag = kinderen * 7.5 + volwassenen * 2.5

# Retour
print("U moet ", bedrag, " euro betalen voor ", kinderen, " kinderen en ", volwassenen, "volwassenen.")
