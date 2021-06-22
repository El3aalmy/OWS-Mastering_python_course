# -------------------------------------------------------------
# ------ Object oriented programming => class attributes ------
# -------------------------------------------------------------
# Class attibutes: attributes defined outside the constructor
# -------------------------------------------------------------

class Member : 

    not_allowed_names = ["Mem", "Shit", "Baloot"]

    users_num = 0

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

# print(member_three.get_full_info())

# print(dir(Member))
