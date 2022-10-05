
weekdagen=["MAANDAG","DINSDAG", "WOENSDAG","DONDERDAG", "VRIJDAG"]
weekend=["ZATERDAG","ZONDAG"]

dag=input( "welke dag is het vandaag ? ").upper()
print(dag)
if dag in weekend:
    print(dag)
    print ("weekend !")
if dag in weekdagen:
    print(dag)
    print ("week dag !")
