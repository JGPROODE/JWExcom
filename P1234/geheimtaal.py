import string
lijst=["abc","def"]
lijst=str(input("voor uw code in: ").lower())
#print(lijst)
def converter(list):
    i=0
    for word in list:
        #print(word)
        for letter in word:
            print(str(i)+" : "+ letter)
            i+=1
converter(lijst)
alfabet=list(string.ascii_lowercase)
print(alfabet)
index=alfabet.index("a")
print("index is : "+str(index))
getal=ord("a")-97
print("getal : "+str(getal))
