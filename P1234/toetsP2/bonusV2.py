#getal=int(input("wat is uw geluksgetal ? "))

def bepaalBonus(getal):
    bonus=0
    if getal<5:
        if getal%2==0:
            bonus=bonus+100
        else :
            bonus=bonus+20
        bonus=bonus*50
    else :
        if getal<100: 
            if getal>50: 
                bonus =bonus+40
            else: bonus=bonus+20
        else :
            if getal < 1000 and getal%25==0:
                bonus=bonus+500
            bonus=bonus+1
        bonus=bonus+3
    return bonus

lijst=[1,4,33,25, 66,500,3000]
for getal in lijst :
    print("gefeliciteerd,uw bonus voor "+str(getal) +" is :"+str(bepaalBonus(getal)))
