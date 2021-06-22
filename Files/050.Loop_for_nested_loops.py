# ---------------------
# ---- Loop => for ----
# ---  Nested loops ---
# ---------------------

people = ["Osama", "Ahmed", "Sayed", "Ali"]

skills = ["HTML", "CSS", "Js"]

for name in people :  # Outer loop

    print(f"{name} skills is :")

    for skill in skills : # Iner loop

        print(f"- {skill}")

# --------------

peoples = {

    "Osama" : {
        "HTML" : "70%",
        "CSS" : "80%",
        "Js" : "50%"
    }, 

    "Ahmed" : {
        "HTML" : "90%",
        "CSS" : "80%",
        "Js" : "90%"
    },

    "Sayed" : {
        "HTML" : "70%",
        "CSS" : "60%",
        "Js" : "90%"
    }

}

# print(peoples["Osama"])
# print(peoples["Ahmed"])
# print(peoples["Sayed"])
# print(peoples["Sayed"]['CSS'])

for name in peoples :

    print(f"Skills and progress for {name} is : ")

    for skill in peoples[name] :

        print(f"{skill} => {peoples[name][skill]}")



        