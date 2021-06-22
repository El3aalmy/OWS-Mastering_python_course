# -------------------------------------------
# --- Dictionary ---
# ------------------
# [1] Dict items are enclosed in curly braces 
# [2] Dict items are contains key : value
# [3] Dict key must be imutable => (number, string, tuple) list no allowed
# [4] Dict value can be any type of data
# [5] Dict key must be unique
# [6] Dict is not ordered , you can access its element with key
# -------------------------------------------

# Dictionary 

user = {
    "name" : "Hasan",
    "Age" : 16,
    "Country" : "Egypt",
    "Skills" : ["HTML", "CSS", "JS"],
    "Rating" : 10.5,
}

print(user)
print(user['Country'])
print(user.get("Country"))

print(user.keys())
print(user.values())

# Two-dimentional dictionary 

languages = {
    "One" : {
        "name" : "HTML",
        "Progress" : "80%"
    },
    "Two" : {
        "name" : "CSS",
        "Progress" : "90%"
    },
        "Three" : {
        "name" : "JS",
        "Progress" : "90%"
    }
}

print(languages)
print(languages['One'])
print(languages['Three']['Progress'])

# Dictionary length

print(len(languages))
print(len(languages["Two"]))

# Make dictionary from variables 

frameworkOne = {
    "name" : "Vuejs",
    "Progress" : "80%"
}
frameworkTwo = {
    "name" : "Reactjs",
    "Progress" : "80%"
}
frameworkThree = {
    "name" : "Angular",
    "Progress" : "80%"
}


allframeworks = {
    "One" : frameworkOne,
    "Two" : frameworkTwo,
    "Three" : frameworkThree
}

print(allframeworks)

