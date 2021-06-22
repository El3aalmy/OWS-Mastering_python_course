# ---------------------------

mytuple = "Hasan",

print(mytuple)
print(type(mytuple))

# ---------------------------

mytuple2 = ("Osama", "Ahmed", "Salah")
mytuple2 = ("Hasan", "Ahmed", "Salah")

print(mytuple2)
print(type(mytuple2))

print("{:d}" .format(len(mytuple2)) + " elements")

# ----------------------------

nums = (1, 2, 3)
letters = ("a", "b", "c")

con = nums + letters

print(con)
print(len(con))

# ----------------------------

my_tuple = (1, 2, 3, 4)
x, y, _, z = my_tuple

print(x)
print(y)
print(z)
