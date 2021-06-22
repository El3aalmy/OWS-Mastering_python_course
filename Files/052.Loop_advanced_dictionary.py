# ------------------------------
# -- Advanced dictionary loop --
# ------------------------------

Skills = {
    "HTML" : "80%",
    "CSS" : "90%",
    "Js" : "70%",
    "PHP" : "80%"
}

# print(Skills.items())


for skill in Skills :

    print(f"{skill} => {Skills[skill]}")

# -----------------------

for skill_key, skill_value in Skills.items() :

    print(f"{skill_key} => {skill_value}")

# ------------------------

Skills2 = {
    "HTML" : {
        "main" : "80%",
        "Pugjs" : "80%"
    }, 
    "CSS" : {
        "main" : "90%",
        "Sass" : "70%"
    }
}

for main_key, main_value in Skills2.items() :

    print(f"{main_key} Progress is :")

    for nested_key, nested_value in main_value.items() :

        print(f"{nested_key} => {nested_value}")

