import csv
import os

print("hello world")
path="C:/tmp/hoi/hallo/etc/pp"

try:
    if (os.path.isdir(path)==False) :
        os.makedirs(path)
    
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)
