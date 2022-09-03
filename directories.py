import os
dirPath = "C:/tmp/CSV"
#alle bestanden, geen dirs.
result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
print(result)
lijst=[]
lijst.append(result)
print("------------------------") 
result = next(os.walk(dirPath))[2]
print("de dir bevat de volgende bestanden: "+str(result))
print("de lijst is "+ str(lijst))
for bestand in lijst :
    print("bestand = "+str(bestand)+"\n")

dirs = os.listdir( dirPath )

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
      for letter in regel:
        print(letter)
      """



""""
with open(dirPath+"/"+str(lijst[0]), 'r') as f:
    # lees het bestand                                                                                                                                                               
   # csvReader = csv.reader(f,delimiter=';')
#csvfile, delimiter=' ', quotechar='|'
    # elke lijn in een lus uitlezen                                                                                                                                               
    for regel in f:#csvReader:
        print(regel.split())


"""