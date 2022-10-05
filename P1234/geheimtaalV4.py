import string

lijst=""
lijst=str(input("voor uw code in: ").lower())
lijst2=""
for letter in lijst:
    if letter ==" " :
        lijst2=lijst2+" "
    else:
        if ord(letter) in range(ord('a'),ord('z')+1):
            lijst2=lijst2+letter
#@check        
print("Lijst is : "+lijst)        
print("Lijst2 is : "+lijst2)

print(len(lijst2))
def converter(list):
    lengte=len(list)
    codelijst=""
    teller=0
    for letter in list:    
        if letter!=" ":
            codelijst=codelijst+ str(ord(letter)-96)+" " # append(ord(letter)-97)
        else:
            if teller<lengte :
                codelijst=codelijst+'- '
        teller+=1
    return codelijst
    
geheimtaal=converter(lijst2)
print("De geheime code is : " +geheimtaal)
#------------------------
alfabet=list(string.ascii_lowercase)
print(alfabet)
index=alfabet.index("h")
print("index van h in alfabet is : "+str(index))
#----------------
getal=ord("a")-97
print("getal van a : "+str(getal))

