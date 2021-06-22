# -----------------------------------------------
# -- Object oriented programming => inhertance --
# -----------------------------------------------

class Food : # Base class 

    def __init__(self, name, price) :

        self.name = name 

        self.price = price

        print(f"{self.name} Food is created from base class")

    def eat(self) :

        print("Eat method from base class")

class Apple(Food) : # Derived class 

    def __init__(self, name, price, amount) :

        # Food.__init__(self, name)   # Create instance from base class

        super().__init__(name, price)

        # self.name = name              
        # self.price = price + 20   # The new attributes overwrite the base class attributes

        self.amount = amount

        print(f"{self.name} Apple is created from derived class and price is {self.price} and amount is {amount}")

    def get_from_tree(self) :

        print("Get from tree from derived class")

# food_one = Food("Pizza")

food_two = Apple("Pizza", 150, 500)
food_two.eat()
food_two.get_from_tree()
