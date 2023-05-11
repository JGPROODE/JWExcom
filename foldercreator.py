import os
import datetime

# Maak een map aan voor elk domein
# https://www.tutorialspoint.com/How-to-create-a-directory-using-Python

# Open het bestand
f = open("files/list.txt", "r")

# Lees de lijst in
string = f.read()

# Plaats de regels in een lijst
lijst = string.split("\n")


doel = input("In welke map wilt u de bestanden maken?")
f.close()


# Loop door de lijst en maak de mappen aan
for item in lijst:
    if item != "":
        pad = doel+"/"+item
        try:
            os.makedirs(pad)
        except OSError as e:
            print("De map "+pad+"bestaat al!" )

        # Plaats de readme in de map
        f = open(pad+"/readme.txt", "w")
        f.write("Deze map is aangemaakt door het script van Laura, op " + str(datetime.datetime.now()) + ".")
        f.close()
