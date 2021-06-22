# -----------------------------------------------
# -- Function paciking and unpacking arguments *Args --
# -----------------------------------------------

print(1, 2, 3, 4)

my_list = [1, 2, 3, 4]

print(my_list)
print(*my_list)


def my_name_is(*peoples) :

    for name in peoples :

        print(f"My name is : {name}")

my_name_is("Ahmed", "Hasan", "Khaled", "Mahmoud", "Fitma")


def show_details(name, *skills) :

    print(f"{name}, your skills is : ")

    for skill in skills :

        print(skill)

show_details("Hasan", "HTML", "CSS", "JS", "Python", "MySQL")
show_details("Ahmed", "HTML", "CSS", "JS", "Python", "MySQL")

