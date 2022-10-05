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
        dag = input("Welke dag is het?: ").upper()
        
    #ik heb nu goede invoer
    #nu bepalen of het een werkdag is of een weekenddag
    if dagen.index(dag) <= 4:
        return True
    else:
        return False

def vraagabo():
    # Systeem vraagt of de bezoeker een abonnement heeft (ja/nee), en Actor voert in of hij/zij een abbonement heeft.
    abo = ""
    while abo is not "JA" and abo is not "NEE":
        abo = input("Heeft u een abbonement? (ja/nee): ").upper()
        if abo == "NEE":
            return False
        elif abo == "JA":
            return True
        else:
            print("verkeerde invoer...ja of nee invoeren graag !")
    #return heeftabonnement


def vraagleeftijd():
    # Systeem vraagt wat de leeftijd van de bezoeker is, en Actor voert de leeftijd in.
    leeftijd=int(-1)
    while leeftijd<0 or leeftijd > 120:
        leeftijd = int(input("Hoe oud bent u?: "))
    return leeftijd   





def berekenprijs(iseenwerkdag,deleeftijd,heefteenabonement):
    # Systeem berekent de prijs en geeft deze terug aan de gebruiker
    prijs=0
    #test
    print("werkdag = "+str(iseenwerkdag))
    print("leeftijd = "+str(deleeftijd))
    print("heeftabonnement = "+str(heefteenabonement))
    
    if iseenwerkdag == True:
        if heefteenabonement == True:
            prijs=2.50
    else:
        if int(deleeftijd) >=8 and int(deleeftijd) <=11 and heefteenabonement:
            prijs=2.50
        elif int(deleeftijd) >=8 and int(deleeftijd) <=11:
            prijs=5.00
        elif int(deleeftijd) >=13 and heefteenabbonement:
            prijs=5.00
        elif int(deleeftijd) >=12:
            prijs=7.50
    print("De entreeprijs is : " +str(prijs)+" euro.")
    return prijs

#dit is nu het programma met aanroep van 4 functies
iswerkdag=vraagdag()
heeftabonement=vraagabo()
leeftijd=vraagleeftijd()
berekenprijs(iswerkdag,leeftijd,heeftabonement)
