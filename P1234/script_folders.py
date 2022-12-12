'''
Description: Opdracht B, weekopdracht 6: Folders
Autor: Cas Beute - 25606OSLD0A1

Opdracht:
Je hebt al gewerkt met bestanden. In deze opdracht ga je daarmee verder en je gaat ook directories aanmaken.
Om een webserver te beheren moet je steeds folders aanmaken voor subdomeinen. De namen van deze domeinen worden aangeleverd in een tekstbestand. 
Dit proces ga je automatiseren. Voor elk subdomein wordt een map aangemaakt. In elke map wordt een 'readme.txt' bestand aangemaakt en een map 'htdocs'.
'''
#import OS
import os
foldernaam = input("Hoe wilt u de folder noemen ? ")
extentie = '.txt'

#Het 'pad' waar de files worden opgeslagen
                   
#naarbestand = 'C:\\Users\\casbe\\OneDrive\\Bureaublad\\School\\Programmeren\\Opdracht 6 - Folders voor web\Foldermap'
naarbestand="c:/test/Cas/"
try:
    os.chdir(naarbestand)
except :
    print("foutje : ")
nieuwe_map = foldernaam
bestandsnaam=foldernaam+extentie
try:
    if not os.path.exists(nieuwe_map):
        os.makedirs(nieuwe_map)
        #Folders in een andere map plaatsen:
        #naarbestand2=naarbestand+'\\'+nieuwe_map
        #os.chdir(naarbestand2)
        #nieuwe_map2='htdocx'
        #os.makedirs(nieuwe_map2)
        #Tekstbestand in de folder
        tekstbestandmoethier=naarbestand+'/'+nieuwe_map
        tekstbestand=open(tekstbestandmoethier + "/"+bestandsnaam, "at")
        tekstbestand.write("Read Me")
        tekstbestand.close()

        print("Mappen zijn aangemaakt!")
except OSError:
    print("Error: Deze map bestaat al, verander de foldernaam!")
