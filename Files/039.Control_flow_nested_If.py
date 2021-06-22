# --------------------
# ----- Nested if ----
# --------------------

uName = "Hasan"
isStudent = "Yes"
uCountry = "KSA"
cName = "Python course"
cPrice = 100

if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "ALgasaier": 

    if isStudent == "Yes" : 

        print(f"{uName} because you from {uCountry} and a student")
        print(f"the course \"{cName}\" price is : {cPrice - 60 } pounds")

    else : 
        
        print(f"{uName} because you from {uCountry}")
        print(f"the course \"{cName}\" price is : {cPrice - 70 } pounds")


elif uCountry == "Kuwait" or uCountry == "Bahrain":

    print(f"{uName} because you from {uCountry}")
    print(f"the course \"{cName}\" price is : {cPrice - 80} pounds")

else :

    print(f"{uName} because you from {uCountry}")
    print(f"the course \"{cName}\" price is : {cPrice - 30} pounds")

