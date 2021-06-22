# --------------------------------------------------
# -- Object oriented programming => magic methods --
# --------------------------------------------------
# Everything in python is object 
# __init__ called automatically when instantiating class
# self.__class__ the class to which a class instance belongs
# __str__   gives a human-readable output of the object 
# __len__   returns the length of the container 
#           Called when we use the built-in len() function on the object 
# --------------------------------------------------

class Skill : 

    def __init__(self) :

        self.skills = ["HTML", "CSS", "JS"]

    def __str__(self) :

        return f"My skills are : {self.skills}"

    def __len__(self) :

        return len(self.skills)

profile = Skill()
print(profile)
print(len(profile))

profile.skills.append("PHP")
profile.skills.append("MySQL")

print(len(profile))


# print(profile.__class__)


# my_string = "Hasan"
# print(type(my_string))
# print(my_string.__class__)
# print(dir(str))     # => Class 
# print(dir(type))    # => Class
# print(str.upper(my_string))

# print(member_one.full_name())
# print(member.full_name(member_one))
