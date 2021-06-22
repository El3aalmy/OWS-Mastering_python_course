# ---------------------------------------------------------
# -- Object oriented programming => multiple inheritance --
# ---------------------------------------------------------

# class Food:  # Base class
#
#     def __init__(self, name, price):
#
#         self.name = name
#
#         self.price = price
#
#         print(f"{self.name} Food is created from base class")
#
#     def eat(self):
#
#         print("Eat method from base class")
#
# class Apple(Food):  # Derived class
#
#     def __init__(self, name, price, amount):
#
#         # Food.__init__(self, name)   # Create instance from base class
#
#         super().__init__(name, price)
#
#         # self.name = name
#         # self.price = price + 20   # The new attributes overwrite the base class attributes
#
#         self.amount = amount
#
#         print(f"{self.name} Apple is created from derived class and price is {self.price} and amount is {amount}")
#
#     def get_from_tree(self):
#
#         print("Get from tree from derived class")
#
#     def eat(self):     # This method override the method of the base class
#
#         print("Eat method from derived class")
#
# # food_one = Food("Pizza")
#
# food_two = Apple("Pizza", 150, 500)
# food_two.eat()
# food_two.get_from_tree()

# ====================================

class BaseOne:

    def __init__(self):

        print("Base one")

    def func_one(self):

        print("One")


class BaseTwo:

    def __init__(self):

        print("Base Two")

    def func_two(self):

        print("Two")


class Derived(BaseOne, BaseTwo):

    pass

var_one = Derived()     # Print  Base one  because of the order of the inhertance classes

print(Derived.mro())    # Print the order of classes that this class inhertance methods from it


print(var_one.func_one)
print(var_one.func_two)

var_one.func_one()
var_one.func_two()


class Base:

    pass 

class DerivedOne(Base):

    pass 

class DerivedTwo(DerivedOne):   # Inhertance from Base class two

    pass    