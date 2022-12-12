# Vooraf gemaakte variablen
 
isDeelnemer=False
invoerLand=False
gender="x"
# loop voor de eerste vraag land van herkomst
while invoerLand==False:
    
    # Vraag naar woonplaats
    # Verkrijg user input
    opt = int(input("In wel land woont u ?\n\n1) Rusland\n2) China\n3) Noord-Korea\n4)) Ander land.\n\nLocatie: "))
    # Check of het nummer 4 is
    if opt >0 and opt< 5:
              invoerLand=True
              if opt==4 :
                  isDeelnemer=True
              
  #stel volgende vraag
if isDeelnemer :
    print(" ga door")
    #man of vrouw ?
    while gender not in ["M","V"]: 
        gender=input("Bent u man of vrouw ?  m/v").upper()
    print("Beantwoord de volgende vragen: ")    
    if gender=="V":
        print("vragen vrouw")
    else:
        print("vragen Man")
        

if isDeelnemer :
    print("Gefeliciteerd, U gaat een ruimtereis maken. ")
else:
    print("Helaas nemen we afscheid van U.")



        
        
