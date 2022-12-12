# Python3 code to  calculate age in years
from datetime import date
 
def calculateAge(birthDate):
    days_in_year = 365.2425   
    age = float((date.today() - birthDate).days / days_in_year)
    return age
         
# Driver code
print(calculateAge(date(1959, 7, 25)), "years")
# Output: 21 years
