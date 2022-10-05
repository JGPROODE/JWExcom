import random
import copy

hoevaakSpelen = input("Hoeveel keer wilt u dobbelen? Geeft het aantal keren op : ")
print("____________________________________________________________________")
print("____________________________________________________________________")
print("")
print("Een ‘1’ brengt ongeluk: de volgende worp is 0 punten waard.")
print("Een ‘6’ brengt geluk: de volgende worp telt dubbel." )
print("Note: als een ‘6’ na een ‘1’ wordt gegooid, dan telt de zes niet,")
print("maar het effect van de ‘6’ op de volgende worp wel.")
print("____________________________________________________________________")
print("____________________________________________________________________")
print("")

#input("Druk 'ENTER' om verder te gaan")

gedobbeld=[]
for x in range (0, int(hoevaakSpelen)):
    gedobbeld.append(random.randint(1, 6))
 
#check
print (gedobbeld)


def berekenscore(gedobbeld2):
    # ik maak en kopie van het origineel.
    # nav de kopie wijzig ik het origineel bij een 1 en een 6
    # ik tel dan het aantal punten van het origineel
    gedobbeld3=[]
    #echt kopieren !!
    gedobbeld3=gedobbeld2.copy()
    #werkt niet ???
    print("NR 3: "+str(gedobbeld3))
    print("NR 2: "+str(gedobbeld2))
    index=0#int(-1) 
    for x in gedobbeld3 :
        if x==1 and index<len(gedobbeld3)-1:
            gedobbeld2[index+1]=0                
        elif x==6 and index<len(gedobbeld3)-1:
            gedobbeld2[index+1]=2*gedobbeld2[index+1]        
        index+=1
    aantalpunten=0
    for x in gedobbeld2 :
        aantalpunten=aantalpunten+x
        
    print("NR 3: "+str(gedobbeld3))
    print("NR 2: "+str(gedobbeld2)+"----"+ str(sum(gedobbeld2)))
    return aantalpunten



print("De score is : "+ str(berekenscore(gedobbeld)))

#print("De score is : "+ str(aantalpunten))
