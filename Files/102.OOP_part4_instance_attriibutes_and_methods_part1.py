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

    def __init__(self, first_name, middle_name, last_name, gender) :

        # self.name = "Hasan"     # => attribute => name
         
        self.fname = first_name    

        self.mname = middle_name  

        self.lname = last_name  

        self.gender = gender   

    def full_name(self) :

        return f"{self.fname} {self.mname} {self.lname}"

    def name_with_title(self) :

        if self.gender == "male" :

            return f"Hello ms {self.fname}"

        elif self.gender == "female" :

            return f"Hello miss {self.fname}"

        else :

            return f"{self.fname}"

    def get_full_info(self) :

        return f"{self.name_with_title()}, your full name is : {self.full_name()}"

member_one = Member("Osama", "Mohamed", "Ali", "male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "male")
member_three = Member("Mona", "Ali", "Mahmoud", "female")

# Use function :
# print(member_one.full_name())
# print(member_three.name_with_title())

print(member_one.get_full_info())
