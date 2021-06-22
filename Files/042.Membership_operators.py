# ------------------------------------------
# --------- Membership operators -----------
# ------------------------------------------
# in
# not in 
# ------------------------------------------

# String

name = "Hasan"

print("s" in name)
print("a" in name)
print("A" in name)  # Characters case sensetive 

print("-" * 40)

# List 

friends = ["Ahmed", "Sayed", "Mahmoud"]

print("Osama" in friends)
print("Sayed" in friends)
print("Mahmoud" not in friends)

print("-" * 50)

# Using in and not in with condition 

countriesOne = ["Egypt", "KSA", "Kuwait", "Bahrain"]
countriesOneDiscount = 80

contriesTwo = ["Jordon", "Alsomal"]
contriesTwoDiscount = 50

myCountry = "Jordon"

if myCountry in countriesOne : 

    print(f"You have discount {countriesOneDiscount}")

elif myCountry in contriesTwo :

    print(f"You have discount {contriesTwoDiscount}")

else : 

    print("You have no discount")
