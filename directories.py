import os
dirPath = r"C:\tmp\Diego-"
#alle bestanden, geen dirs.
result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
print(result)
lijst=[]
lijst.append(result)
print("------------------------") 
result = next(os.walk(dirPath))[2]
print(result)
print("de lijst is "+ str(lijst))