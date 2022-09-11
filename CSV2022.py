import csv
import os
klas='25188OLVM9A2'
padnaarbestand= 'C:/Examens/Klassen 2020/cohort 2019/'+klas+'.csv'
padnaarbestand2= 'c:/Examens/klassen 2020/cohort 2019/'+klas

if (os.path.isdir(padnaarbestand2)==False) :
            os.mkdir(padnaarbestand2)


# Open het csv-bestand in leesmodus 'r'                                                                                                                                              
with open(padnaarbestand, 'r') as f:
    # lees het bestand                                                                                                                                                               
    csvReader = csv.reader(f,delimiter=';')
#csvfile, delimiter=' ', quotechar='|'
    # elke lijn in een lus uitlezen                                                                                                                                               
    for regel in csvReader:
        print(regel)

        #C:/Examens/Klassen 2020/25265OLVM0A1/25265OLVM0A1.csv
        #'c:/tmp/voorbeeld.csv'
with open(padnaarbestand,'rt')as f:
  data = csv.reader(f,delimiter=';')
 
  #[3,6,9]
  for row in data:
        print(row[0])
        # is er een tussenvoegsel ?
        if row[2]=="" :
            mapnaam=row[3]+"-"+row[0]+"-"+row[4]
        else:
            mapnaam=row[3]+"-"+row[0]+"-"+row[2]+"-"+row[4]
        print(mapnaam)
        mapnaam=padnaarbestand2+"/"+mapnaam
        if (os.path.isdir(mapnaam)==False) :
            os.mkdir(mapnaam)

        

#  column  = [i[1] for i in row]
 # print(column[1] )

        

path="C:/tmp/hoi"
if (os.path.isdir(path)==False) :
    os.mkdir(path)
#else:os.mkdir(path+"2233")

