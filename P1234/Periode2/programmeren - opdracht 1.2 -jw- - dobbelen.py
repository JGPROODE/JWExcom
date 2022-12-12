import random
  
hoevaakSpelen = input("Hoeveel keer wilt u dobbelen?\n")

print("Een ‘1’ brengt ongeluk: de volgende worp is 0 punten waard.\n" + "Een ‘6’ brengt geluk: de volgende worp telt dubbel.\n" + "Note: als een ‘6’ na een ‘1’ wordt gegooid, dan telt de zes niet, maar het effect van de ‘6’ op de volgende worp wel.")
input("Druk 'ENTER' om verder te gaan")

gedobbeld=[]
for x in range (0, int(hoevaakSpelen)):
    gedobbeld.append(random.randint(1, 6))
    
teller=0
for a in gedobbeld:
    print("het getal is : "+str(a))
    print("het getal is : "+str(teller)+" --"+str(gedobbeld[teller]))
    teller+=1

def berekenscore(gedobbeld):
    #overslaan=false
    gedobbeld2=gedobbeld
    aantalpunten=0
    index=0#int(-1) 
    for x in gedobbeld :
        if x==1 and index<len(gedobbeld)-1: 
            gedobbeld[index+1]=0
        elif x==6 and index<len(gedobbeld)-1:
            aantalpunten=aantalpunten+gedobbeld[index+1]
        aantalpunten=aantalpunten+x
        index+=1
    return aantalpunten

print(gedobbeld)

print("De score is : "+ str(berekenscore(gedobbeld)))
