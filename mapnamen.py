import os

# Stap 1: Definieer de locatie van de mappen die je wilt doorzoeken
directory = "c:\\K0767\\"

# Stap 2: Loop door alle submappen en bestanden in de opgegeven map
for root, dirs, files in os.walk(directory):
    # Stap 3: Loop door elk bestand in elke map
    for file in files:
        # Stap 4: Wijzig de bestandsnaam door de mapnaam toe te voegen
        # Split de bestandsnaam en extensie
        filename, extension = os.path.splitext(file)
        # Voeg de mapnaam toe aan de bestandsnaam
        new_filename = os.path.join(root, os.path.basename(root) + '_' + filename + extension)
        old_path = os.path.join(root, file)
        new_path = os.path.join(root, new_filename)
        # Stap 5: Opslaan van de nieuwe bestandsnamen
        os.rename(old_path, new_path)
