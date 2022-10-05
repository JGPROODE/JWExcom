# using calendar module 
# using time module 
import calendar; 
import time; 
  
# gmt stores current gmtime 
localtime = time.localtime() # gmtime() 
print("Local time:-", localtime) 
print("----------------------")
# ts stores timestamp 
ts = calendar.timegm(localtime) 
print("timestamp:-", ts) 
