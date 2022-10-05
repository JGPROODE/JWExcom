
weekdagen=["MAANDAG","DINSDAG","WOENSDAG","DONDERDAG","VRIJDAG","ZATERDAG","ZONDAG"]

dag=input( "welke dag is het vandaag ? ").upper()
while dag not in weekdagen:
    dag=input( "welke dag is het vandaag ? ").upper()

if weekdagen.index(dag)<5:
    isWeekend=False
else:
    isWeekend=True
 
if isWeekend:
    print(dag)
    print ("weekend !")
else:
    print(dag)
    print ("week dag !")
