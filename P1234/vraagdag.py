#Bereken entreeprijs van een zwembad met functies
#25-11-2020
#J.G.P. Roode

#functie returnt True als het een werkdag is en False als het weekend is.
def vraagdag():
    # Systeem vraagt welke dag het is, en Actor voert de dag van de week in.
    dag=""
    dagen = ["MAANDAG", "DINSDAG", "WOENSDAG", "DONDERDAG", "VRIJDAG", "ZATERDAG", "ZONDAG"]
    #controleer of invoer passend is
    while dag not in dagen:
        dag = input("Welke dag is het?: ")#.upper()
        print(dag)
    #ik heb nu goede invoer
    #nu bepalen of het een werkdag is of een weekenddag
    if dagen.index(dag) <= 4:
        return True
    else:
        return False

#hoofdprogramma
iswerkdag=vraagdag()    
print(iswerkdag)
#print(vraagdag())
