import datetime

class Student:

    # Constructor
    def __init__(self, dag:int, maand:int, jaar:int):
        try:
            self.geboortedatum = datetime.date(jaar, maand, dag)
        except: 
            raise ValueError

    # Bereken de leeftijd
    def bereken_leeftijd(self):
        nu = datetime.datetime.now()
        # bepaal of de student al jarig is geweest
        #check logica
        if (nu.month > self.geboortedatum.month or (nu.month == self.geboortedatum.month and nu.day >= self.geboortedatum.day)) :
            # Verjaardag is geweest. 
            return nu.year - self.geboortedatum.year
        else:
            #Verjaardag is nog niet geweest
            return nu.year - self.geboortedatum.year - 1

    def __str__(self):
        return f"Student is {self.bereken_leeftijd()} jaar oud."