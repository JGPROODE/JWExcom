getal=int(input("wat is uw geluksgetal ? "))

if getal<5:
    if getal%2==0:
        bonus=100
    else :
        bonus=20
    bonus=bonus*50
else :
    if getal<100: 
        if getal>50: 
            bonus =40
        else: bonus= 20
    else :
        if getal < 1000 and getal%25==0:
            bonus=500
        bonus=bonus+1
    bonus=bonus+3

print("gefeliciteerd u heeft gewonnen, uw bomus is :"+str(bonus))
