import os
import shutil
#lest op Osiris kleine letters!! omzetten naar hoofdletters
def zoek_en_kopieer_osiris(bron_pad, doel_pad):
    # Zorg ervoor dat de doelmap bestaat
    if not os.path.exists(doel_pad):
        os.makedirs(doel_pad)

    # Loop door de directories en zoek naar mappen genaamd 'Osiris'
    for root, dirs, files in os.walk(bron_pad):
        if 'Osiris' in dirs:
            osiris_pad = os.path.join(root, 'Osiris')

            # Kopieer de inhoud van de Osiris map naar de doelmap
            for item in os.listdir(osiris_pad):
                s = os.path.join(osiris_pad, item)
                d = os.path.join(doel_pad, item)
                if os.path.isdir(s):
                    # Als een directory met dezelfde naam al bestaat in de doelmap, voeg een nummer toe om naamconflicten te voorkomen
                    counter = 1
                    base_name = item
                    while os.path.exists(d):
                        d = os.path.join(doel_pad, f"{base_name}_{counter}")
                        counter += 1
                    shutil.copytree(s, d)
                else:
                    # Als een bestand met dezelfde naam al bestaat in de doelmap, voeg een nummer toe om naamconflicten te voorkomen
                    counter = 1
                    base_name, extension = os.path.splitext(item)
                    while os.path.exists(d):
                        d = os.path.join(doel_pad, f"{base_name}_{counter}{extension}")
                        counter += 1
                    shutil.copy2(s, d)

if __name__ == "__main__":
    bron_pad = input("Geef het pad op waar gezocht moet worden: ")
    doel_pad = input("Geef het doelpad op waar de inhoud van alle Osiris mappen gekopieerd moet worden: ")
    zoek_en_kopieer_osiris(bron_pad, doel_pad)
    print("Kopieerproces voltooid.")
