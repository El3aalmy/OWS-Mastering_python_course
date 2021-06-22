# ------------------------
# -------- Tuples --------
# ------------------------

# Tuples with one element 
# To make a tuple with one element from string to tuple , put "," after the element

mytuple1 = ("hasan",)
mytuple2 = "hasan",

print(mytuple1)
print(mytuple2)

print(type(mytuple1))
print(type(mytuple2))

print(len(mytuple1))
print(len(mytuple2))


# Tuple concatinate

a = (1, 2, 3, 4, 5)
b = (6, 7)

c = a + b
d = a + ("a", "b", True) +b

print(c) 
print(d) 

# Tuple, list, string repeat (*)

mystring = "hasan"
mylist = [1, 2]
mytuple = ("a", "b")

print(mystring * 6)
print(mylist * 6)
print(mytuple * 6)

# --------------------------------------

# Methods => count()

my = (1, 2, 7, 8, 4, 9, 8)
print(my.count(8))

# Method => index()

my2 = (1, 3, 7, 8, 2, 6, 5)
# print("The position is : " + my2.index(7))  # Error Cannot concatinate string with number
print("The position is : {} " .format(my2.index(7)))  
print(f"The position is : {my2.index(7)}")  

# --------------------------------------

# Tuple destruct 

my3 = ("a", "b", 4, "c")

x, y, _, z = my3

print(x)
print(y)
print(z)