# -------------------------------------------------------------------
# -- Object oriented programming => class methods & static methods --
# -------------------------------------------------------------------
# Class methods :
# - Marked with @classmethod decorator to flag it as class method
# - It take Cls parameter not self to point to the class not the instance
# - It doesn't require creation of a class instance
# - Used when you wnat to do something with the class itself
# Static methods :
# - It takes no parameters
# - It's bound to the class not instance
# - Used when doing something doesn't have access to object or class but related to class
# -------------------------------------------------------------------

class Member : 

    not_allowed_names = ["Mem", "Shit", "Baloot"]

    users_num = 0

    @classmethod
    def show_users_count(cls) :

        print(f"We have {cls.users_num} users in our system")

    @staticmethod
    def my_name() :

        print("My name is Hasan")

    def __init__(self, first_name, middle_name, last_name, gender) :

        # self.name = "Hasan"     # => attribute => name
         
        self.fname = first_name    

        self.mname = middle_name  

        self.lname = last_name  

        self.gender = gender   

        Member.users_num += 1 # Member.users_num = Member.users_num + 1 

    def full_name(self) :

        if self.fname in Member.not_allowed_names :

            raise ValueError("Name not allowed")

        else :

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

    def delete_users(self) :

        Member.users_num -= 1 # Member.users_num = Member.users_num - 1

        return f"User {self.fname} is deleted" 

print(Member.users_num)

member_one = Member("Osama", "Mohamed", "Ali", "male")
member_two = Member("Ahmed", "Ali", "Mahmoud", "male")
member_three = Member("Mona", "Ali", "Mahmoud", "female")
member_four = Member("Shit", "Ali", "Mahmoud", "female")

print(Member.users_num)
print(member_four.delete_users())
print(Member.users_num)

print("=" * 10)
Member.show_users_count()

print("=" * 10)

# print(member_one.full_name())
# print(Member.full_name(member_one))

Member.my_name()
