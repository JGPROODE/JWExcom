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
