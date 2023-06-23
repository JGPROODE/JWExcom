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



#bestand om bestanden na een bepaalde datum te kopieren. Zowel voor de beoordelingensite als voor TK)*

# De bronmap waar je wilt zoeken !! 4x med, ict, ct en F&V, voor beoordelingen
#source = "C:\\Users\\ROOJ\\Aventus\\Beoordelingsformulieren CI - General\\F&V(archief Dans)\\Cohort 2020\\"
#source = "C:\\Users\\ROOJ\\Aventus\\Beoordelingsformulieren CI - General\\CT\\Cohort 2020\\"
#dit is voor tk8 docs
source = "C:\\Users\\ROOJ\\Aventus\\Creatieve Industrie Examencommissie - Documenten\\Taakgroep 08 (examenresultaten)\\Vastgestelde resultaten\\2022-2023\\CT\\"


#_"c:\\een\\"

# De doelmap waar je wilt kopiëren
# twee is voor beoordelingen tk8 is voor tk8
#target = "c:\\twee\\"
target = "c:\\tk8\\"

# De datum waar je mee wilt vergelijken (jaar, maand, dag)
date = datetime.datetime(2023, 6, 3,0,0,0)

# Loop door de bronmap en zijn submappen
for root, dirs, files in os.walk(source):
    # Loop door de bestanden in de huidige map
    for file in files:
        # Krijg het volledige pad van het bestand
        file_path = os.path.join(root, file)
        # Krijg de wijzigingsdatum van het bestand
        file_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        # Vergelijk de wijzigingsdatum met de opgegeven datum
        print("file datum  ", str(file_date))
        print("---")
        print(str(date))
        if file_date > date:
            # Krijg het relatieve pad van het bestand ten opzichte van de bronmap
            relative_path = os.path.relpath(file_path, source)
            # Krijg het volledige pad van het bestand in de doelmap
            target_path = os.path.join(target, relative_path)
            # Maak de doelmap als die nog niet bestaat
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            # Kopieer het bestand naar de doelmap
            shutil.copy(file_path, target_path)
            # Print een bericht dat het bestand is gekopieerd
            print(f"{file_path} gekopieerd naar {target_path}")
    print("klaar-1")
print("klaar-2")
    
