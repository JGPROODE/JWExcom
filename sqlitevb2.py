import sqlite3

class Vbsql:
    # In de constructor wordt het te raden woord gedefinieerd
    def __init__(self):
        #self.woord = str.lower("Lingo")
        self.woord = str.lower(self.kies_woord())
        self.beurt = 0



    #Functie om woord te selecteren uit database
    def kies_woord(self):
        connection =sqlite3.connect('lingo.sqlite3')
        lijst=connection.execute('SELECT * FROM vijfletters ORDER BY RANDOM()')
        for rij in lijst:
            print(rij)
            woord=rij[0]
            print(woord)
        connection.close()
        return(woord)


vb=Vbsql()
print('dit is het gekozen woord: '+ vb.woord)