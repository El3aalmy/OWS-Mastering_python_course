# ---------------------------------
# -- Dictionary methods part two --
# ---------------------------------

# setdefault()

user = {
    "name" : "Hasan"
}

print(user)
print(user.setdefault("name" , "Ahmed")) # Bring the value of "name" , if not exsist => add new key and value

print(user.setdefault("Age" , 16))  # Age not exsist => add a key and value 
print(user)

print(user.setdefault("Country"))   # No value => none
print(user)

# popitem()

member = {
    "name" : "Hasan",
    "Skill" : "HTML"
}

print(member)
member.update({"age" : 36})
print(member.popitem()) # Returen the last added key and value

# items()

view = {
    "name" : "Hasan",
    "Skills" : "CSS"
}

allitems = view.items()
print(view)
view["Age"] = 16

print(allitems) # Return all items in dict , however new items added to it 

# dict.fromkeys()

a = ("MyKeyOne", "MyKeyTwo", "MyKeyThree")
b = "x"
b = ("x", "z")

print(dict.fromkeys(a, b))  # Take keies from a and values from b


