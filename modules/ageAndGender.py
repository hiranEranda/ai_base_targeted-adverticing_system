import random

def ageAndGender(age,gender):
    if(gender == "Male"):
        predGender=1
    else:
        predGender=0
        
    if(age == "(0-2)"):
        predAge=random.randint(0,2)
    elif(age == "(4-6)"):
        predAge=random.randint(4,6)
    elif(age == "(8-14)"):
        predAge=random.randint(8,14)
    elif(age == "(15-24)"):
        predAge=random.randint(15,24)
    elif(age == "(25-37)"):
        predAge=random.randint(25,37)
    elif(age == "(38-47)"):
        predAge=random.randint(38,47)
    elif(age == "(48-59)"):
        predAge=random.randint(48,59)
    elif(age == "(60-100)"):
        predAge=random.randint(60,100)
 
    return predAge,predGender

