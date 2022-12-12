#import csv
import os
bestandsnaam='voorbeeld1'
extentie='.txt'
bronmap='C:/testP/'
#doelmap='C:/testP'
padnaarbronbestand= bronmap+bestandsnaam+extentie
#padnaardoelbestand= doelmap+bestandsnaam+extentie

if (os.path.isdir(bronmap)==False) :
    #kan maar 1 map aanmaken geen waslijst van mappen achter elkaar
    os.mkdir(bronmap)
    print("Map : "+ bronmap+" is aangemaakt.")
else:
    print("Map : "+ bronmap+" bestaat al.")
    
# ik weet nu zeker dat de map bestaat

if (os.path.isfile(padnaarbronbestand)==False) :
    bestand=open(padnaarbronbestand,"wt")
    print("Map : "+ padnaarbronbestand+" is aangemaakt.")
    bestand.write("eerste regel"+"\n")
    bestand.close()
else:
    print("Map : "+ padnaarbronbestand+" bestaat al.")
    #bestand=open(padnaarbronbestand,"wt")
    #hierboven overschrijft de eerste regel
    bestand=open(padnaarbronbestand,"at")
    bestand.write("Nog een  regel dit doet ie echt nU fdssdfdfs!!!"+"\n")
    bestand.close()


    
    

    
    
        
