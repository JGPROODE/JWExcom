import string
#lijst=["abc","def"]
lijst=""
lijst=str(input("voor uw code in: ").lower())
lijst2=""
for letter in lijst:
    if letter ==" " :
        lijst2=lijst2+" "
    else:
        if ord(letter) in range(ord('a'),ord('z')+1):
            lijst2=lijst2+letter
        
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
#for teken in geheimtaal:
#    print(teken)
print(geheimtaal)
'''
alfabet=list(string.ascii_lowercase)
print(alfabet)
index=alfabet.index("a")

print("index is : "+str(index))
getal=ord("a")-97
print("getal : "+str(getal))
'''
