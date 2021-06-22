# -------------------------------------
# -- Boolean operators --
# -----------------------
# and
# or 
# not
# -------------------------------------

age = 16 
country = "Egypt"
rank = 10

print(age > 15 and country == "Egypt" and rank > 5)  # True 
print(age > 15 and country == "KSA" and rank > 5)  # False 

print(age > 15 or country == "Egypt")   # True
print(age > 17 or country == "KSA" or rank > 20)   # False
print(age > 17 or country == "Egypt" or rank > 20)  # True

print(age > 16) # True
print(not age > 16)  # Not True = False

