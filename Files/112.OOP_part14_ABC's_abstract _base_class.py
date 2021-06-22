# -----------------------------------------------------------------
# -- Object oriented programming => AbC's => abstract vase class --
# -----------------------------------------------------------------
# - Class called abstract class if it has one or more abstract methods
# - abc module in python provides infrastructure for defining custom abstract vase classes
# - By adding @absttractmethod decorator on the methods 
# - ABCMeta class is a metaclass used for defining absttract vase class
# -----------------------------------------------------------------------------------------------

from abc import ABCMeta, abstractmethod

class Programming(metaclass=ABCMeta):

    @abstractmethod
    def has_oop(self):

        pass

    @abstractmethod # If it abstractmethod => must be in the instance too
    def has_name(self):

        pass

class Python(Programming):

    def has_oop(self):

        return "Yes"

class Pascal(Programming):

    def has_oop(self):

        return "No"

        # pass  # Can make it don't return any thing (none) => what matters is the method like the parent class

    def has_name(self):

        return "Pascal"

one = Pascal()

print(one.has_oop())
print(one.has_name())
