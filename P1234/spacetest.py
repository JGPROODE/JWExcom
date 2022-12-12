invoerLand=False

# loop voor de eerste vraag land van herkomst
while invoerLand==False:
    
    # Vraag naar woonplaats
    # Verkrijg user input
    opt=-1
    try:
        opt = int(input("In welk land woont u ?\n\n1) Rusland\n2) China\n3) Noord-Korea\n4)) Ander land.\n\nLocatie: "))
    except :
        print("er is een fout")
    # Check of het nummer 4 is
    if opt >0 and opt< 5:
              invoerLand=True
              if opt==4 :
                  isDeelnemer=True
    #test
    #print(isDeelnemer)

