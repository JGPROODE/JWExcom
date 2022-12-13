import os
import csv


#omzetten van csv bestanden met studentgegeven in mappen van studenten in het juiste cohort en opleiding
# de bronbestanden staan in bronMap. alle csv bestanden die daar in staan worden gelezen en indien het een cohort uit cohortenOverzicht betfet omgezet in de map op de plaats .
# C:\Users\ROOJ\Aventus\Creatieve Industrie Examencommissie - Documenten\Examendossiers\CT 25187 Applicatie- en mediaontwikkelaar\BOL\2019\Studentendossiers\
# voor het testen:C:\Examendossiers\CT 25187 Applicatie- en mediaontwikkelaar\BOL\2019\Studentendossiers\
# padNaarDoel+opleidingOmschrijving+soortOpleiding+cohort+"Studentendosier\"
# hier de kolommen en volgorde van het csv bestand en vb



def maakMap(path):
    bestaatAl= True
    try:
        if (os.path.isdir(path)==False) :
            bestaatAl=False
            os.makedirs(path)
            
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        if bestaatAl==False:
            print ("Successfully created the directory %s" % path)
        else:
            print ("The directory %s existed already." % path)
            

def haalOpleidingOmschrijvingOp(opleiding):
    #opleiding=ol[0:5]
    #CT
    if opleiding =="25187":
        oms="CT 25187 Applicatie- en mediaontwikkelaar"
    elif opleiding =="25188":
        oms="CT 25188 Gamedeveloper"   
    elif opleiding =="25265":
        oms="CT 25265 Technicus human technology"      
    elif opleiding =="25604":
        oms="CT 25604 Softwaredeveloper"       
    #DANS
    elif opleiding =="25495":
        oms="Dans 25495 Danser"
    #ICT
    elif opleiding =="25189":
        oms="ICT 25189 ICT-Beheerder"   
    elif opleiding =="25191":
        oms="ICT 25191 Medewerker Beheer ICT"      
    elif opleiding =="25192":
        oms="ICT 25192 Medewerker ICT"       
    elif opleiding =="25605":
        oms="ICT 25605 Allround Medewerker IT systems & devices"                              
    elif opleiding =="25606":
        oms="ICT 25606 Expert IT systems & devices"                  
    elif opleiding =="25607":
        oms="ICT 25607 Medewerker ICT support"       
    #F&V
    elif opleiding =="25158":
        oms="F&V 25158 Interieuradviseur"   
    elif opleiding =="25159":
        oms="F&V 25159 Basismedewerker mode"      
    elif opleiding =="25163":
        oms="F&V 25163 Allround medewerker mode maatkleding"       
    elif opleiding =="25164":
        oms="F&V 25164 Specialist mode maatkleding"   
    elif opleiding =="25212":
        oms="F&V 25212 Ruimtelijk vormgever"      
    elif opleiding =="25526":
        oms="F&V 25526 Junior stylist"     
    elif opleiding =="25527":
        oms="F&V 25527 Junior productmanager fashion"   
    #vanaf 2020ev  
    elif opleiding =="23207":
        oms="F&V 23207 Fashion design & productmanagement"     
    elif opleiding =="25684":
        oms="F&V 25684 Assitant Fashion Tailor"   
    elif opleiding =="25686":
        oms="F&V 25686 Fashion Tailor"     
    elif opleiding =="25687":
        oms="F&V 25687 Fashion Designer"   
    elif opleiding =="25688":
        oms="F&V 25688 Fashion Product Coordinator "     
    elif opleiding =="25689":
        oms="F&V 25689 Basismedewerker fashion"   
    elif opleiding =="25771":
        oms="F&V 25771 Interieuradviseur"     
    elif opleiding =="25811":
        oms="F&V 25811 Ruimtelijk vormgever"   
    #MEDIA
    elif opleiding =="25199":
        oms="Media 25199 Mediamanager"   
    elif opleiding =="25200":
        oms="Media 25200 Mediaredactiemedewerker"      
    elif opleiding=="25201":
        oms="Media 25201 Mediavormgever"   
    elif opleiding=="25633":
        oms="Media 25633 Mediavormgever"    
    else:
         oms="99999-foutje"
    return oms

#diverse parameters
cohort="1959"
soortOpleiding="QQP"
opleidingOmschrijving="NN 9999 leuke opleiding"


#dirPath = "C:/tmp/CSV"
dirPath= "C:/ExcomCSV/CSVbron initialen"
#padNaarDoel in het nieuwe dirPath
pnd = "C:/Examendossiers"
padNaarDoel=pnd+"/"+opleidingOmschrijving+"/"+soortOpleiding+"/"+cohort+"/"+"Studentendossiers"
#test
maakMap(padNaarDoel)

#bronMap="c:/tmp/CSVbron"
bronMap="C:\ExcomCSV\CSVbron initialen"
cohortenOverzicht= ["2020","2021","2022"]
opleidingenlijstICT=["25189","25191","25605","25606","25607"]
opleidingenlijstMedia=["25199","25200","25201","25633"]
opleidingenlijstFenV=["23207","25158","25159","25212","25526","25527","25163","25164","25684","25686","25687","25688","25689","25771","25811"]
opleidingenlijstDans=["25495"]
opleidingenlijstCT=["25187","25188","25604","25265"]
opleidingenOverzicht=opleidingenlijstICT+opleidingenlijstMedia+opleidingenlijstCT+opleidingenlijstFenV+opleidingenlijstDans
#["25187","25188","25604","25265","25199","25200","25201","25633","25189","25191","25605","25606","25607", ]



#alle bestanden, geen dirs.
result = [f for f in os.listdir(bronMap) if os.path.isfile(os.path.join(bronMap, f))]
print(result)
lijst=[]
lijst.append(result)
print("------------------------") 
result = next(os.walk(bronMap))[2]
print("de dir bevat de volgende bestanden: "+str(result))
print("de lijst is "+ str(lijst))
for bestand in lijst :
    print("bestand = "+str(bestand)+"\n")

dirs = os.listdir( bronMap )
"""
# This would print all the files and directories
for file in dirs:
   print(file)
   ff=open(dirPath+"/"+str(file), 'r')
   for regel in ff:
      print(regel) #+"\n")  
      #de eerste letter
      #print(regel[0])
    
      print(regel.split())
"""


#padnaarbestand= 'C:/Examens/Klassen 2020/cohort 2019/'+klas+'.csv'
#padnaarbestand2= 'c:/Examens/klassen 2020/cohort 2019/'+klas

#padnaarbestand= pad1+bestand1+extentie1
#padnaarbestand2= pad2+bestand2


for file in dirs:
    
    with open(bronMap+"/"+str(file), 'r') as f:
        # lees het bestand
        csvReader = csv.reader(f,delimiter=';')
        #csvfile, delimiter=' ', quotechar='|'
        # elke lijn in een lus uitlezen                                                                                                                                               
        for regel in csvReader:
            print(regel)

    with open(bronMap+"/"+str(file),'rt')as f:
        data = csv.reader(f,delimiter=';')
 
        #[3,6,9]
        for row in data:
            print(row[0])
            cohort=row[5]
            crebo=row[4][0:5]
            
            
            if cohort in cohortenOverzicht : #["2020","2021","2022"]:
                #test
                print(row[5]+ row[4])
                if crebo in opleidingenOverzicht:
                    #test
                    print(crebo)
                    
                    # is er een tussenvoegsel ?
                    if row[1]=="" :
                        studentMapnaam=row[0]+" "+row[2]+" "+row[3]
                    else:
                        studentMapnaam=row[0]+" "+row[1]+" "+row[2]+" "+row[3]
                    #test
                    print(studentMapnaam)
                    opleidingOmschrijving=haalOpleidingOmschrijvingOp(crebo) # row[4][0:5]
                    soortOpleiding=row[4][5:8]
                    #cohort=row[5]
                    padNaarDoel=pnd+"/"+opleidingOmschrijving+"/"+soortOpleiding+"/"+cohort+"/"+"Studentendossiers"
                    padEnMapnaam=padNaarDoel+"/"+studentMapnaam
                    maakMap(padEnMapnaam)
                    
                    
#einde            
    
