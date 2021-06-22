# --------------------------------------------------
# -- Object oriented programming => encapsulation --
# --------------------------------------------------
# Encapsulation
# - Restrict access to the data stored in attributes and methods 
# Public
# - Every attribute and method that we used so far is public 
# - Attributes and methods can be modified and run from everywhere 
# - Inside or outside the class
# Protected
# - Attributes and methods can be accessed from within the class and sub classes
# -- Sub classes => derived => classes that inherets from this class 
# - Attributes and methods prefixed with one underscore _ 
# Private 
# - Attirbutes and methods can be accessed from with in the calss or object only 
# - Attributes cannot be modified from outside the class 
# - Attributes and methods prefixed with two underscores __
# -------------------------------------------------------------------------------
# - Attributes = variables = properties
# -------------------------------------------------------------------------------


# class Member:

#     def __init__(self, name):

#         self.name = name    # Public

# one = Member("Ahmed")
# print(one.name)

# one.name = "Hasan"
# print(one.name)


# class Member:

#     def __init__(self, name):

#         self._name = name    # Protected

# one = Member("Ahmed")
# print(one._name)

# one._name = "Hasan"
# print(one._name)


class Member:

    def __init__(self, name):

        self.__name = name    # Private

    def my_name(self):

    	return f"My name is {self.__name}"

one = Member("Ahmed")
# print(one.__name)		# Error => attribute cannot be accessed from outside class

print(one.my_name())


# In python the underscores are only name convention for you and team but not do the job of public and private and protected key words like other languages
print(one._Member__name)
