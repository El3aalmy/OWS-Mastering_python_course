# -------------------------------------------------------
# -- Function packin and unpacking arguments trainings --
# -------------------------------------------------------

my_skills = ("HTML", "CSS", "JS")

SkillProgress = {
    "HTML" : "70%",
    "Python" : "90%",
    "MySQL" : "60%"
}

def show_skills(name, *skills, **SkillsWithProgress) :

    print(f"My name is {name} \nSkills without progress are :")

    for skill in skills :

        print(f"- {skill}")

    print("Skills with progress are :")

    for skill_key, skill_value in SkillsWithProgress.items() :

        print(f"- {skill_key} => {skill_value}")

show_skills("Hasan", *my_skills, **SkillProgress)
