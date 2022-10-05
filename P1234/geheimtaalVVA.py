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

#--------------------------------------------------------
alfabet=list(string.ascii_lowercase)
print(alfabet)
index=alfabet.index("z")

print("index is : "+str(index))
getal=ord("a")#-97
print("getal : "+str(getal))
for letter in alfabet:
    print("De letter is : "+str(letter)+" en de positie is: "+ str (alfabet.index(letter)))
