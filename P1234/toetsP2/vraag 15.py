def get_rating(age):
    rating=""
    if age<13: rating="C"
    elif age < 18: rating="T"
    else : rating ="A"
    return rating


print(get_rating(18))
print(get_rating(17))
print(get_rating(13))
print(get_rating(12))

