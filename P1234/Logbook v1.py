
# Globale variable
log = ''

# Functie
def new_log():
    # Maak variable globaal
    global log

    # Verkrijg user input
    temp = input("log text: ")

    # Als stop is
    if temp == "stop":
        print('Stopped')
        
        # OPSLAAN NAAR HET BESTAND
        bestand = open('bestand.txt', 'a')
        bestand.write(log)
        bestand.close()

    else:
        # Toevoegen aan log variable
        log += "\n" +temp
        # Log laten zien
        print(log)
        # Functie opnieuw runnen
        new_log()

# Functie starten
new_log()


log = ''
def logger():
    global log
    get = input('Text to be logged: ')
    if get == 'stop':
        f = open('file.txt', 'a')
        f.write(log)
        f.close()
    else:
        log += '\n'+get
        logger()
logger()

let log = '', logger = () => get = input('Text: '),



