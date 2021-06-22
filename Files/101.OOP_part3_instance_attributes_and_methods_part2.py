# --------------------------------------------------------------------
# -- Object oriented programming => instance attributes and methods --
# --------------------------------------------------------------------
# self : point to instance created from class
# instance attributes : instance attributes defined inside the constructor
# --------------------------------------------------------------------
# Instance methods : take self parameter which point to instance created from class
# Instance methods can have more than one parameter like any function
# Instance methods can freely access attributes and methods on the same object
# Instance methods cass access the class itself
# --------------------------------------------------------------------

class Member : 

    def __init__(self, first_name, middle_name, last_name) :

        # self.name = "Hasan"     # => attribute => name
         
        self.fname = first_name     
        self.mname = middle_name     
        self.lname = last_name     

member_one = Member("Osama", "Mohamed", "Ali")
member_two = Member("Ahmed", "Ali", "Mahmoud")
member_three = Member("Mona", "Ali", "Mahmoud")

# print(dir(member_one))  # => Has attribute name

# Access attribute of instance
print(member_one.fname, member_one.mname, member_one.lname)
print(member_two.fname)
print(member_three.fname)
