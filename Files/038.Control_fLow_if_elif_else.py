# --------------------
# --  Control flow  --
# -- if, elif, dlse --
# -- Make decisions --
# --------------------

uName = "Hasan"
uCountry = "Kuwait"
cName = "Python course"
cPrice = 100

if uCountry == "Egypt" : 
    
    print(f"{uName} because you from {uCountry}")
    print(f"the course \"{cName}\" price is : {cPrice - 40} pounds")

elif uCountry == "KSA" :

    print(f"{uName} because you from {uCountry}")
    print(f"the course \"{cName}\" price is : {cPrice - 40} pounds")

elif uCountry == "Kuwait" :

    print(f"{uName} because you from {uCountry}")
    print(f"the course \"{cName}\" price is : {cPrice - 80} pounds")

else :

    print(f"{uName} because you from {uCountry}")
    print(f"the course \"{cName}\" price is : {cPrice - 30} pounds")

