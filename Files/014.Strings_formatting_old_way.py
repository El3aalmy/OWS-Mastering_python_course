# -----------------------------
# Strings formatting ----------
# -----------------------------

name = "hasan"
age = 16
rank = 10

print("My name is: " + name)
# print("My name is: " + name + "and my age is: " + age) # Error => Cannot concatinate string with number

print("My name is : %s" % "hasan")
print("My name is : %s" % name)
print("My name is : %s and my age is %d" % (name, age))
print("My name is : %s and my age is %d and my rank is %f" % (name, age, rank))

# %s => String
# %d => Number 
# %f => Float 

n = "hasan"
l = "python"
y = 10 

print("My name is %s i'm %s developer with %d years exp" % (n, l, y))

# Control floating point number 

num = 10 
print("My number is %d" % num)
print("My number is %f" % num)
print("My number is %.2f" % num)

# Truncate string 

var = "Hasan salah"
print("My name is %s" % var)
print("My name is %.2s" % var)  # print 2 elements of the string [ Ha ]
