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
            
def maakInhoudMapStudent(pad,kds,gitems,bitems):
    items=["/Beroepsgericht","/BPV","/Generiek","/L&B","/Keuzedelen"]
    for item in items:
        maakMap(pad+str(item))
    for keuzedeel in kds:
        maakMap(pad+items[-1]+"/"+str(keuzedeel))
    for gitem in gitems:
        #generiek is index 2
        maakMap(pad+items[2]+"/"+str(gitem))
    for bitem in bitems:
        #beroepsspecifiek is index 0
        maakMap(pad+items[0]+"/"+str(bitem))
        
        
        
        
def haalGeneriekOp(opleiding):
    if opleiding=="25192":
        gen=["Nederlands", "Rekenen"]
    else:
        gen=["Engels","Nederlands", "Rekenen"]
    return gen





    #haalBeroepsgericht op !
#####################################

def haalBeroepsgerichtOp(opleiding):
    #opleiding=ol[0:5]
    #niet meer per 2020
    #CT
    if opleiding =="25187":
        bg=["B1-K1","B1-K2","B1-K3","P1-K1","CEF Engels"]   
    elif opleiding =="25188":
        bg=["B1-K1","B1-K2","B1-K3","P1-K1","CEF Engels"]   
    elif opleiding =="25265":
        bg=["B1-K1","B1-K2","B1-K3"]      
    elif opleiding =="25604":
        bg=["B1-K1","B1-K2"]           
    #DANS
    #niet meer per 2022
    elif opleiding =="25495":
        bg=["B1-K1","B1-K2","B1-K3","P1-K1","CEF Engels"]  
    #ICT
    elif opleiding =="25189":
        bg["B1-K1","B1-K2","B1-K3","P1-K1","P1-K2","CEF Engels"]  
    elif opleiding =="25191":
        bg=["B1-K1","B1-K2","B1-K3","P2-K1","CEF Engels"]  
    elif opleiding =="25192":
        bg=["B1-K1","B1-K2","CEF Engels"]  
    #vanaf2020
    elif opleiding =="25605":
        bg=["B1-K1","B1-K2","B1-K3"]                    
    elif opleiding =="25606":
        bg=["B1-K1","B1-K2","B1-K3","P2-K1","P2-K2"]                 
    elif opleiding =="25607":
        bg=["B1-K1","B1-K2"]     
    #F&V
    elif opleiding =="25158":
        bg=["B1-K1","B1-K2","B1-K3"]     
    elif opleiding =="25159":
        bg=["B1-K1","B1-K2"]           
    elif opleiding =="25163":
        bg=["B1-K1","B1-K2","B1-K3"]        
    elif opleiding =="25164":
        bg=["B1-K1","B1-K2","B1-K3","P2-K1"]  
    elif opleiding =="25212":
        bg=["B1-K1","P2-K1","P2-K2","P2-K3"]        
    elif opleiding =="25526":
        bg=["B1-K1","B1-K2","B1-K3","P1-K1","P1-K2","P1-K3","CEF Engels"] 
    elif opleiding =="25527":
        bg=["B1-K1","B1-K2","B1-K3","P2-K1","P2-K2","CEF Engels"] 
    #vanaf 2020  
    #LLLLLAAATSTE
    elif opleiding =="23207":
        bg=["B1-K1","B1-K2","B1-K3","P2-K1"]      
    elif opleiding =="25684":
        bg=["B1-K1","P2-K1","P2-K2","P2-K3"]     
    elif opleiding =="25686":
        bg=["B1-K1","B1-K2","B1-K3"]   
    elif opleiding =="25687":
        bg=["B1-K1","B1-K2"] 
    elif opleiding =="25688":
        bg=["B1-K1","B1-K2","B1-K3","P1-K1","P1-K2","P1-K3","CEF Engels"]  
    elif opleiding =="25689":
        bg=["B1-K1","B1-K2","B1-K3"]  
    elif opleiding =="25771":
        bg=["B1-K1","B1-K2","B1-K3"]    
    elif opleiding =="25811":
        bg=["B1-K1","B1-K2","B1-K3"]  
    #MEDIA
    elif opleiding =="25199":
        bg=["B1-K1","B1-K2","B1-K3"]  
    elif opleiding =="25200":
        bg=["B1-K1","B1-K2","B1-K3"]       
    elif opleiding=="25201":
        bg=["B1-K1","B1-K2","B1-K3"]  
    elif opleiding=="25633":
        bg=["B1-K1","B1-K2"]  
    else:
        bg="bg-foutje"
    return bg




###################################
def haalKeuzedelenOp(opleiding):
    #opleiding=ol[0:5]
    #niet meer per 2020
    #CT
    if opleiding =="25187":
        kds=["K0059","K0080","K0125","K0497","K0505","K0529"]   
    elif opleiding =="25188":
        kds=["K0059","K0080","K0125","K0497","K0505","K0529"]   
    elif opleiding =="25265":
        kds=["K0059","K0080","K0125","K0226","K0512","K0781"]      
    elif opleiding =="25604":
        kds=["K0059","K0356","K0481","K0497","K0519","K0529","K0542","K0717","K0730","K0767","K0781","K0788"]        
    #DANS
    #niet meer per 2022
    elif opleiding =="25495":
        kds=["K0165"]
    #ICT
    elif opleiding =="25189":
        kds=["K0226","K0400","K0444","K0505"]
    elif opleiding =="25191":
        kds=["K0400","K0505","K0665","K0721"]
    elif opleiding =="25192":
        kds=["K0224","K0665","K0719","K0721","K1030"]
    #vanaf2020
    elif opleiding =="25605":
        kds=["K0225","K0505","K0721","K0803","K1030"]                       
    elif opleiding =="25606":
        kds=["K0125","K0226","K0360","K0505"]                        
    elif opleiding =="25607":
        kds=["K0665","K0721","K1030"]       
    #F&V
    elif opleiding =="25158":
        kds=["K0125","K0206","K0461","K0725"]      
    elif opleiding =="25159":
        kds=["K007","K0209","K0211"]          
    elif opleiding =="25163":
        kds=["K0206","K0461","K0725"]            
    elif opleiding =="25164":
        kds=["K0125","K0206","K0461","K0725"]        
    elif opleiding =="25212":
        kds=["K0031","K0184","K0189","K0766"]    
    elif opleiding =="25526":
        kds=["K0031","K0080","K0125","K0206"]      
    elif opleiding =="25527":
        kds=["K0031","K0080","K0125","K0206"]      
    #vanaf 2020  
    #LLLLLAAATSTE
    elif opleiding =="23207":
        kds=["K0125","K0206","K0461","K0725"]  
    elif opleiding =="25684":
        kds=["K0031","K0184","K0189","K0766"]   
    elif opleiding =="25686":
        kds=["K0031","K0080","K0125","K0156"]   
    elif opleiding =="25687":
        kds=["K007","K0209","K0211"] 
    elif opleiding =="25688":
        kds=["K0031","K0080","K0125","K0206"]   
    elif opleiding =="25689":
        kds=["K0031","K0080","K0125","K0156"]  
    elif opleiding =="25771":
        kds=["K0031","K0080","K0125","K0156"]    
    elif opleiding =="25811":
        kds=["K0031","K0080","K0125","K0156"] 
    #MEDIA
    elif opleiding =="25199":
        kds=["K0031","K0125","K0361","K0389","K0528","K0765","K0769","K0781","K0881"]   
    elif opleiding =="25200":
        kds=["K0031","K0125","K0361","K0389","K0528","K0765","K0769","K0781","K0881"]       
    elif opleiding=="25201":
        kds=["K0031","K0184","K0250","K0528","K0769","K0781"]  
    elif opleiding=="25633":
        kds=["K0031","K0125","K0361","K0389","K0528","K0765","K0769","K0781","K0881"]  
    else:
        kds="kds-foutje"
    return kds

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
        oms="F&V 25688 Fashion Product Coordinator"    
        print("nu bezig met 22688") 
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
         oms="oploms-foutje"
    return oms



#diverse parameters
cohort="1959"
soortOpleiding="QQP"
opleidingOmschrijving="NN 9999 leuke opleiding"


#dirPath = "C:/tmp/CSV"
#dirPath= "C:/ExcomCSV/CSVbron initialen"
#padNaarDoel in het nieuwe dirPath
pnd = "C:/Beoordelingen CI"
padNaarDoel=pnd+"/"+opleidingOmschrijving+"/"+soortOpleiding+"/"+cohort+"/"+"Studentendosiers"
#test
maakMap(padNaarDoel)

#bronMap="c:/tmp/CSVbron"
bronMap="C:/ExcomCSV/testcsv"
cohortenOverzicht= ["2020","2021","2022","2023"]
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
            #crebo=opl
            crebo=row[4][0:5]
            #test
            print(crebo)
            
            if cohort in cohortenOverzicht : #["2020","2021","2022"]:
                #test
                print(row[5]+ row[4])
                if crebo in opleidingenOverzicht:
                    # info ophalen als het nodig is
                    opleidingOmschrijving=haalOpleidingOmschrijvingOp(crebo) # row[4][0:5]
                    #crebo en cohort als parametre?
                    keuzedelen=haalKeuzedelenOp(crebo)
                    generiekItems=haalGeneriekOp(crebo)
                    beroepsItems=haalBeroepsgerichtOp(crebo)
                    soortOpleiding=row[4][5:8]
                    
                    
                   
                    
                    # is er een tussenvoegsel ?
                    if row[1]=="" :
                        studentMapnaam=row[0]+" "+row[2]+" "+row[3]
                    else:
                        studentMapnaam=row[0]+" "+row[1]+" "+row[2]+" "+row[3]
                    #test
                    print(studentMapnaam)
                   
                    #aanpassen voor beoordelingen CI
                    padNaarDoel=pnd+"/"+opleidingOmschrijving+"/"+soortOpleiding+"/"+cohort+"/"+"Studentendosiers"
                    padEnMapnaam=padNaarDoel+"/"+studentMapnaam
                    maakMap(padEnMapnaam)
                    maakInhoudMapStudent(padEnMapnaam,keuzedelen,generiekItems, beroepsItems)
                    
#einde            
    
