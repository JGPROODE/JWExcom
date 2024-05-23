import os
import shutil

def zoek_en_kopieer_osiris(bron_pad, doel_pad):
    # Zorg ervoor dat de doelmap bestaat
    if not os.path.exists(doel_pad):
        os.makedirs(doel_pad)

    # Loop door de directories en zoek naar mappen genaamd 'Osiris'
    for root, dirs, files in os.walk(bron_pad):
        if 'Osiris' in dirs:
            osiris_pad = os.path.join(root, 'Osiris')
            doel_osiris_pad = os.path.join(doel_pad, os.path.relpath(osiris_pad, bron_pad))

            # Zorg ervoor dat de doelsubmap bestaat
            if not os.path.exists(doel_osiris_pad):
                os.makedirs(doel_osiris_pad)

            # Kopieer de inhoud van de Osiris map naar de nieuwe locatie
            for item in os.listdir(osiris_pad):
                s = os.path.join(osiris_pad, item)
                d = os.path.join(doel_osiris_pad, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)

if __name__ == "__main__":
    bron_pad = input("Geef het pad op waar gezocht moet worden: ")
    doel_pad = input("Geef het doelpad op waar de inhoud van alle Osiris mappen gekopieerd moet worden: ")
    zoek_en_kopieer_osiris(bron_pad, doel_pad)
    print("Kopieerproces voltooid.")
