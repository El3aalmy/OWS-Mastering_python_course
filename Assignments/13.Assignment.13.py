def get_score(**skills) :

    for skills_key, skill_value in skills.items() :

        print(f"\"{skills_key}\" => \"{skill_value}\"") 

get_score(arabic="80", hasan="90", Math="70")

# ========================================

def get_score2(*name, **skills2) :

    while name is not None :

        print(f"{name}, Your skills are : ")

        for skill_key2, skill_value2 in skills2.items() :

            print(f"{skill_key2} => {skill_value2}")

        break

    while name is None :

        for skill_key2, skill_value2 in skills2.items() :

            print(f"{skill_key2} => {skill_value2}")

        break

get_score2(arabic="90", english="80")

# =======================================

my_skills = {
    "Math" : "90",
    "Arabic" : "80",
    "Science" : "70",
    "fsjdlfa" : "50"
}

def get_score3(name, **skills3) :

    print(f"{name}, Your skills are : ")

    for skill_key3, skill_value3 in skills3.items() :

        print(f"{skill_key3} => {skill_value3}")

get_score3("Hasan", **my_skills)

# ========================================
