import string
lijst=["abc","def"]
lijst=str(input("voor uw code in: ").lower())
print(lijst)
def converter(list):
    #i=0
    codelijst=""#[]
    for word in list:
        print(word)
        i=0
        for letter in word:
            print(str(i)+" : "+ letter)
            i+=1
            if letter!=" ":
                codelijst=codelijst+ str(ord(letter)-97)# append(ord(letter)-97)
    #codelijst.append("-")
        codelijst=codelijst+'-'
    return codelijst
    
converter(lijst)
geheimtaal=converter(lijst)
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
