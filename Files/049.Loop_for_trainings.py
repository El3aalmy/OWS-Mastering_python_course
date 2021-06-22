# -------------------
# --- Loop => for ---
# ---  Trainings  ---
# -------------------

# Range 

Range = range(1, 101)

for number in Range :

    print(number)

# Dictionary 

Skills = {
    "HTML" : "80%",
    "CSS" : "60%",
    "PHP" : "70%",
    "Js" : "80%",
    "Python" : "90%",
    "MySQL" : "60%"
}

# print(Skills['Js'])
# print(Skills.get('Python'))

for skill in Skills :

    # print(skill)

    # print(f"My progress in lang {skill} is {Skills[skill]}")
    print(f"My progress in lang {skill} is {Skills.get(skill)}")



