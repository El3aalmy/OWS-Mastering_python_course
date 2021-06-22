# -------------------------------------------------
# -- Object oriented programming => polymorphism --
# -------------------------------------------------

n1 = 10 
n2 = 20 
print(n1 + n2)

s1 = "Hasan"
s2 = "Salah"
print(s1 + " " + s2)

print(len([1, 2, 3, 4, 5, 6]))
print(len("Hasan Salah"))
print(len({"Key_one" : 1, "Key_two" : 2}))
# Same method has different outputs depend of datatypes 


class A:

    def do_something(self):

        print("From class A")

        raise NotImplementedError("Derived class must implement this method")
        # If the following class don't have this method in it, raise error

class B(A):

    def do_something(self):
       
       print("From class B")

class C(A):

    def do_something(self):
       
       print("From class C")

my_instance = B()
my_instance.do_something()

# The method do_something do different thing depend of the my_instance class 
