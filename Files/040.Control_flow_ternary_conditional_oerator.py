# ----------------------------------------
# ----- Ternary conditional operator -----
# ----------------------------------------

country = "A"

if country == "Egypt" : print(f"The weather in {country} is 25")
elif country == "KSA" : print(f"The weather in {country} is 30")
else : print("This country isnot in the list")          # This code is valied

# Short if 

Rate = 20 
age = 16 

if age < Rate : 

    print("No")     # Condition if True

else : 

    print("Yes")    # Condition if false 

print("No" if age < Rate else "Yes")

# If condition True | If condition | Else condition | Condition if False