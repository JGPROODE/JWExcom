import datetime
dt = '26/11/2020'
day, month, year = (int(x) for x in dt.split('/'))    
ans = datetime.date(year, month, day)
print (ans.strftime("%A"))


#intDay = datetime.date(year=2000, month=12, day=1).weekday()
intDay = datetime.date(year, month, day).weekday()
days = ["MAANDAG", "DINSDAG", "WOENSDAG", "DONDERDAG", "VRIJDAG", "ZATERDAG", "ZONDAG"]
print(days[intDay])


#--------------------------------------------
from datetime import datetime

now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
print("date and time: date+time",date_time)

#---------------------------------
from datetime import date
import calendar
my_date = date.today()
print (calendar.day_name[my_date.weekday()] ) #'Wednesday'



