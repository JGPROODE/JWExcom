import os
import csv
dirPath = "C:/tmp/CSV"
bronMap="c:/tmp/CSVbron"
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
            if row[5] in ["2020","2021","2022"]:
                print(row[5]+ row[4])
            # is er een tussenvoegsel ?
            if row[1]=="" :
                mapnaam=row[0]+"-"+row[2]+"-"+row[3]
            else:
                mapnaam=row[0]+"-"+row[1]+"-"+row[2]+"-"+row[3]
            print(mapnaam)
            mapnaam=dirPath+"/"+mapnaam
            if (os.path.isdir(mapnaam)==False) :
                os.mkdir(mapnaam)

#  column  = [i[1] for i in row]
 # print(column[1] )

 

path="C:/tmp/hoi"
if (os.path.isdir(path)==False) :
    os.mkdir(path)
