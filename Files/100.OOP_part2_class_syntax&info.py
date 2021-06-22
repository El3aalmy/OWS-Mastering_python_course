# --------------------------------------------------------
# -- Object oriented programming => class syntax & info --
# --------------------------------------------------------
# [01] Class is the blueprint or constructor of the object 
# [02] Class instantiate means create instance of a class 
# [03] Instance => onject created from class and have his methods and attributes 
# [04] Class defined with keyword class 
# [05] Class name written with PascalCase (UpperCamelCase) style 
# [06] Class may contains methods and attributes 
# [07] When creating object python look for the built in __int__ method 
# [08] __init__ method called every time you create object from class
# [09] __init__ method is initialize the data for the object
# [10] Any method with two underscore in the stat and end called dunder or magic method 
# [11] self refer to the current instance created from the class and must be first param
# [12] self can be named anything
# [13] In python you don't neet to call new() keyword to create object
# ------------------------------------------------------------------------------------ 
# syntax 
# class Name :
#   constructor => do instantiation (create instance from a class)
#   each instance is separate object 
#   def __init__(self, other_data) :
#       body of functoin 

class Member:

    def __init__(self) :

        print("A new member has been added")

Member()
Member()
Member()

# print(dir(Member))

member_one = Member()
member_two = Member()
member_three = Member()

print(member_one.__class__) # Show the class of the data


my_dictionary = {
    'name' : "Hasan",
    'age' : 16,
    'monthly_salary' : 5000,
    'yearly_salary' : ''    # something 
}
