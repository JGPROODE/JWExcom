'''
# Description: Logboek script, made by Cas Beute
# Niveau: Medium
'''
#import csv
import os
bestandsnaam = input("Hoe wilt u het bestand noemen?")
extentie='.txt'
bronmap='C:/testP/'
#doelmap='C:/testP'
naarbestand= bronmap+bestandsnaam+extentie
#verwijzing naar het juiste bestand = doelmap+bestandsnaam+extentie



def schrijfBestand(targetfile,herhaal):
    bestand=open(targetfile,"at")
   
    if herhaal:       
        bestand.write(input("Wat wilt u schrijven?\n"))
        bestand.write("\n")
    else:
        bestand=open(targetfile,"r")
        print(bestand.read())
        print("Einde")
    bestand.close()    
    #return True
# Functie die de mogelijkheid bied om meerdere regels te kunnen laten afdrukken in het tekstbestand

def controleerMapEnBestand(bronmap,bestandsnaam):
    naarbestand=bronmap+bestandsnaam
    if (os.path.isdir(bronmap)==False) :
        
    #kan maar 1 map aanmaken geen waslijst van mappen achter elkaar
        os.mkdir(bronmap)
        print("Map : "+ bronmap+" is aangemaakt.")
    else:
        print("Map : "+ bronmap+" bestaat al.")

    if (os.path.isfile(naarbestand)==False) :
        bestand=open(naarbestand,"at")
        print("Map : "+ naarbestand+" is aangemaakt.")
        bestand.write(input("Wat is de titel?\n"))
        bestand.write("\n")
        bestand.close()
    else:
        print("Map : "+ naarbestand+" bestaat al.")

def vraagNogEenRegel():
    doorgaan=True
    antw="Z"
    while antw not in ["N","J"]:
        antw = str(input("Wil je nog een bericht typen? (ja/nee)")).upper()
    if antw=="N":
        doorgaan=False
    return doorgaan

controleerMapEnBestand(bronmap,bestandsnaam)

keuze=True
while keuze:
    
    schrijfBestand(naarbestand,keuze)
    keuze=vraagNogEenRegel()
# Functie activering
    

    
    
        
