# Vooraf gemaakte variablen
#initialisatie
isDeelnemer=False
invoerLand=False
gender="x"
isRoker=False
aantalGlazenAlcoholPerWeek=0
opt=-100

def vraagLengte(mv):
    geslacht =mv
    status=True
    lengte=0
    while lengte<50 or lengte >250:
        try :
            lengte = int(input("Wat is uw Lengte ? Opgeven in cm en tussen 50-250 cm."))
        except ValueError:
                print("Could not convert data to an integer.")
    if geslacht=="V":
        if lengte <178 or lengte >210:
            status =False
            print("U heeft niet de juiste lengte.")
    else:
        if lengte <150 or lengte >210:
            status =False
            print("U heeft niet de juiste lengte.")
        
    return status  

def vraagBMI(mv):
    geslacht =mv
    status=True
    bmi=0
    while bmi<1 or bmi >100:
        try :
            bmi = int(input("Wat is uw BMI ? Een getal opgeven 2-100 cm."))
        except ValueError:
                print("Could not convert data to an integer.")
    if geslacht=="V":
        if bmi>28:
            status =False
            print("Uw bmi is te hoog.")
    else:
        if bmi >25:
            status =False
            print("Uw bmi is te hoog.")       
    return status  
#print(status)


# loop voor de eerste vraag land van herkomst
#start main
while invoerLand==False:
    
    # Vraag naar woonplaats
    # Verkrijg user input
    #opt=-100
    try:
        opt = int(input("In welk land woont u ?\n\n1) Rusland\n2) China\n3) Noord-Korea\n4)) Ander land.\n\nLocatie: "))
    except ValueError:
        print("Invoer verkeerd, moet 1,2,3 of 4 zijn")
    except :
        print("onverwachte fout opgetreden!")
    # Check of het nummer 4 is
    if opt >0 and opt< 5:
              invoerLand=True
              if opt==4 :
                  isDeelnemer=True
  
#stel volgende vraag naar geslacht
if isDeelnemer :
    print(" ga door")
    #man of vrouw ?
    while gender not in ["M","V"]: 
        gender=input("Bent u man of vrouw ?  m/v").upper()
        

if isDeelnemer:
    print("Beantwoord de volgende vragen: ")
    isDeelnemer=vraagLengte(gender)
if isDeelnemer :
    isDeelnemer=vraagBMI(gender)

    if gender=="V":
        print("vragen vrouw")
       
    else:
        print("vragen Man")


        
#eindconclusie       
if isDeelnemer :
    print("Gefeliciteerd, U gaat een ruimtereis maken. ")
else:
    print("Helaas nemen we afscheid van U.")


 
