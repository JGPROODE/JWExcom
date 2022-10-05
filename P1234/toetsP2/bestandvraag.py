import sys
try:
    file_in=open("in.txt",'r')
    file_out=open("out.txt",'w+')
except IOError:
    print("Ik kan bestand niet openen :", file_name)
else:
    i=1
    for line in file_in:
        print(line.rstrip())
        file_out.write("line"+str(i)+": "+line)
        i=i+1
    file_in.close()
    file_out.close()
