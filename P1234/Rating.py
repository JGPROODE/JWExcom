def get_rating(age):
    rating=""
    if age <13 : rating="C"
    elif age<18 : rating="T"
    #if age<18 and age >13 : rating="T"
    else : rating="A"
    return rating

print(get_rating(13))   
print(get_rating(12))   
print(get_rating(6))   
print(get_rating(18)) 
