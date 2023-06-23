import os
import shutil
import datetime


padBeoordelingen=["Beoordelingsformulieren CI - General\\F&V(archief Dans)\\Cohort 2020\\", "Beoordelingsformulieren CI - General\\ICT\\Cohort 2020\\","Beoordelingsformulieren CI - General\\CT\\Cohort 2020\\", "Beoordelingsformulieren CI - General\\MED\\Cohort 2020\\"]
padTK8=["Taakgroep 08 (examenresultaten)\\Vastgestelde resultaten\\2022-2023\\F&V\\","Taakgroep 08 (examenresultaten)\\Vastgestelde resultaten\\2022-2023\\ICT\\" ,"Taakgroep 08 (examenresultaten)\\Vastgestelde resultaten\\2022-2023\\MED\\" , "Taakgroep 08 (examenresultaten)\\Vastgestelde resultaten\\2022-2023\\CT\\", ]



for pad in padBeoordelingen :
    print(pad)
    print("------------------")
for pad in padTK8:
    print(pad)
    if "CI" in pad:
        print("gevonden CI")
    if "F&V"in pad:
        print("gevonden F&V")
    if "MED" in pad:
            print("gevonden MED")
    if "ICT" in pad:
        print("gevonden ICT")
    source = "C:\\Users\\ROOJ\\Aventus\\"+str(pad)
    dir(source)
    print(source)


def toon_inhoud_map(map_pad):
    inhoud = os.listdir(map_pad)
    for item in inhoud:
        item_pad = os.path.join(map_pad, item)
        if os.path.isfile(item_pad):
            print("Bestand:", item)
        elif os.path.isdir(item_pad):
            print("Map:", item)

# Deel van het pad dat zal worden toegevoegd aan "C:\\test\\"
variabele = "25265 BOL\\"

# Volledige map-pad
map_pad = "C:\\twee\\" + variabele

# Inhoud van de map weergeven
toon_inhoud_map(map_pad)
