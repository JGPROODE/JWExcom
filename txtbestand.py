import csv
import os
klas='25188OLVM9A2'
pad1='C:/Excom-csv/'
pad2='C:/Excom-csv/'
extentie1='.csv'
extentie2='.txt'
bestand1='studenten_2022-09-01_143230'
bestand2='studenten_2022-09-01_143230'


#padnaarbestand= 'C:/Examens/Klassen 2020/cohort 2019/'+klas+'.csv'
#padnaarbestand2= 'c:/Examens/klassen 2020/cohort 2019/'+klas

padnaarbestand= pad1+bestand1+extentie2
padnaarbestand2= pad2+bestand2


if (os.path.isdir(padnaarbestand2)==False) :
            os.mkdir(padnaarbestand2)


# Open het csv-bestand in leesmodus 'r'                                                                                                                                              
with open(padnaarbestand, 'r') as f:
    # lees het bestand                                                                                                                                                               
   # csvReader = csv.reader(f,delimiter=';')
#csvfile, delimiter=' ', quotechar='|'
    # elke lijn in een lus uitlezen                                                                                                                                               
    for regel in f:#csvReader:
        print(regel.split())

      

        #C:/Examens/Klassen 2020/25265OLVM0A1/25265OLVM0A1.csv
        #'c:/tmp/voorbeeld.csv'
    print(regel[2].split())

#close(f)
"""
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
"""