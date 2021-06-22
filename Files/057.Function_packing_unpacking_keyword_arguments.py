# ------------------------------------------------------------
# -- Function packing, unpacking keyword arguments **KWArgs --
# ------------------------------------------------------------

# **parametar => Make the arguments dictionary not tuple

def show_skills(*skills) :

    print(type(skills))

    for skill in skills :

        print(f"{skill}")

show_skills("HTML", "CSS", "JS")


skills = {
    'HTML' : "80%", 
    'CSS' : "70%", 
    'JS' : "50%", 
    'Python' : "80%",
    "Go" : "70%"
}

def show_skills(**skills) : # Must add arguments as a dictinary

    print(type(skills))

    for skill, value in skills.items() :

        print(f"{skill} => {value}")

show_skills(**skills)




