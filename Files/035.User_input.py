# -----------------------------
# ------- User input ----------
# -----------------------------

fName = input('What\'s your first name')
mName = input('What\'s your middle name')
lName = input('What\'s your last name')

fName = fName.strip().capitalize()      # Remove spaces around string and make the first character capital 
# mName = mName.strip().capitalize()    # Remove spaces around string and make the first character capital 
lName = lName.strip().capitalize()      # Remove spaces around string and make the first character capital 

print(f"My name is {fName} {mName.strip().capitalize():.1s} {lName}")
