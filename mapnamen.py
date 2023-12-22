import os

# Stap 1: Definieer de locatie van de mappen die je wilt doorzoeken
directory = "C:/tmp/Studentendossiers/"#c:\\K0767\\"/
# Stap 2: Loop door alle submappen en bestanden in de opgegeven map
for root, dirs, files in os.walk(directory):
    # Stap 3: Loop door elk bestand in elke map
    for file in files:
        # Stap 4: Wijzig de bestandsnaam door de mapnaam toe te voegen
        # Split de bestandsnaam en extensie
        filename, extension = os.path.splitext(file)
        # Voeg de mapnaam toe aan de bestandsnaam
        lijst=(root.split(" "))


        gevonden_getal = None  # Initialiseer de variabele met None

        for element in lijst:
            print(element)
            if isinstance(element, (int)):
                gevonden_getal = element
                break  # Stop de lus zodra een getal is gevonden
        
       
            new_filename = os.path.join(root, os.path.basename(root) + '_' +str(gevonden_getal)+"---"+filename + extension)
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, new_filename)
            # Stap 5: Opslaan van de nieuwe bestandsnamen
        os.rename(old_path, new_path)
