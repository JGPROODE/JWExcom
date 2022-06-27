import sqlite3

#Functie om woord te selecteren uit database

def kies_woord():
    connection =sqlite3.connect('lingo.sqlite3')
    lijst=connection.execute('SELECT * FROM vijfletters ORDER BY RANDOM()')
    for rij in lijst:
        print(rij)
        woord=rij[0]
        print(woord)
    connection.close()
    return(woord)

woord2=kies_woord()

print('dit is het woord: '+ woord2)
    
