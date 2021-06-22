# ------------------------
# -- Built in functions --
# ------------------------
# enumerate()
# help()
# reversed()
# ------------------------

# enumerate(iterable, start=0)

my_skills = ["HTML", "CSS", "JS", "PHP"]

my_skills_with_Counter = enumerate(my_skills, 20)

print(type(my_skills_with_Counter))

for counter, skill in my_skills_with_Counter :

    print(f"{counter} - {skill}")



# help()

print(help(print))



# reversed()

my_string = "Hasan"
print(reversed(my_string))  # Object
# print(list(reversed(my_string)))  # List

for letter in my_string :

    print(letter)


for s in reversed(my_skills) :

    print(s)
