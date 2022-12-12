#Ik zorg ervoor dat ieder karakter ingelezen wordt. en letters A-Z als kleine letter in lijst
#daarna filter ik de karakters die geen letter zijn a..z er uit en spatie's laat ik staan
lijst=""
lijst2=""
lijst=str(input("voor uw code in: ").lower())
for letter in lijst:
    if letter ==" " :
        lijst2=lijst2+" "
    else:
        if ord(letter) in range(ord('a'),ord('z')+1):
            lijst2=lijst2+letter
#Ik zet letters om in een getal die hun plaats in de lijst a..z weergeeft
#en spaties vervaang ik door '-' en ik zorg voor spaties yussen de lettercodes
def converter(list):
    lengte=len(list)
    codelijst=""
    teller=0
    for letter in list:    
        if letter!=" ":
            codelijst=codelijst+ str(ord(letter)-96)+" " 
        else:
            if teller<lengte :
                codelijst=codelijst+'- '
        teller+=1
    return codelijst
    
geheimtaal=converter(lijst2)
print("De geheime code is : " +geheimtaal)
 
