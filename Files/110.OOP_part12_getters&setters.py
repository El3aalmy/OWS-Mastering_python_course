# ------------------------------------------------------
# -- Object oriented programming => getters & setters --
# ------------------------------------------------------

class Member:

	def __init__(self, name):

		self.__name = name 	# Private

	def my_name(self):

		return f"My name is {self.__name}"

	def get_name(self):		# Getter 

		return self.__name

	def set_name(self, new_name):		# Setter 

		self.__name = new_name

one = Member("Hasan")

# one._Member__name = "Ahmed"	# Setter 
# print(one._Member__name)		# Getter 	
# Not good way to get attribute because of it private and python don't use public and private and protected keywords right, it's just name convention


print(one.get_name())

print("=" * 10)

one.set_name("Ahmed")
print(one.get_name())
