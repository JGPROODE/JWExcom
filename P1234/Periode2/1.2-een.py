import random

#worpen bevat 3 worpen met 1 dobbelsteen
worpen=[random.randint(1,6),random.randint(1,6),random.randint(1,6)]
#worpen=random.sample(range(1,7),21)

#controle 
for worp in worpen:
    print(str(worp))
print(worpen)

#functie telt het aantal ogen van drie worden, 1 doet niet mee en 6 telt dubbel
def bereken_score(dobbelsteen):
    totaal=0
    for aantal in dobbelsteen:
        if aantal >1 :
            if aantal==6:
                aantal=aantal*2
            totaal=totaal+aantal
    return totaal

#geef 3 worpen mee
print("Het totaal aantal punten is : "+ str(bereken_score(worpen)))
