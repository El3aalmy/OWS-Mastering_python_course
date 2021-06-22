# --------------------------------------------------------
# -- Object oriented programming => @proprety decorator --
# --------------------------------------------------------

class Member:

    def __init__(self, name, age):

        self.name = name

        self.age = age 

    def my_name(self):

        return f"My name is {self.name}"

    @property   # Make it like properties (attributes) => return the value of it and not print the data of it 
    def age_in_days(self):

        return self.age * 364

one = Member("Hasan", 16)

print(one.name)
print(one.age)
print(one.my_name())
# print(one.age_in_days())  # Error

print(one.age_in_days)
