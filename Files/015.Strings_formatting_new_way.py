# -----------------------------
# Strings formatting ----------
# -----------------------------

name = "hasan"
age = 16
rank = 10

print("My name is: " + name)
# print("My name is: " + name + "and my age is: " + age) # Error => Cannot concatinate string with number

print("My name is : {}" .format("hasan"))
print("My name is : {}" .format(name))
print("My name is : {} and my age is {}" .format(name, age))
print("My name is : {:s} and my age is {:d} and my rank is {:f}" .format(name, age, rank))

# {:s} => String
# {:d} => Number 
# {:f} => Float 

n = "hasan"
l = "python"
y = 10 

print("My name is {} i'm {} developer with {:f} years exp" .format(n, l, y))

# Control floating point number 

num = 10 
print("My number is {:d}" .format(num))
print("My number is {:f}" .format(num))
print("My number is {:.2f}" .format(num))

# Truncate string 

var = "Hasan salah"
print("My name is {:s}" .format(var))
print("My name is {:.5s}" .format(var))  # print 5 elements of the string [ Ha ]
print("My name is {:.11s}" .format(var))  # print 11 elements of the string [ Hasan salah ]

# Format money 

money = 578439248394

print("My money is {:d}" .format(money))
print("My money is {:_d}" .format(money))
print("My money is {:,d}" .format(money))
# print("My money is {:&d}" .format(money)) #   Wrong

# Rearrange items 

a, b, c = "one", "two", "three"
print("hasan {} {} {}".format(a, b, c)) # hasan one two three
print("hasan {1} {2} {0}".format(a, b, c)) # hasan two three one
print("hasan {2} {0} {1}".format(a, b, c)) # hasan tree one two

x, y, z = 10, 20, 30
print("hasan {} {} {}".format(x, y, z)) # hasan 10 20 30
print("hasan {1:d} {2:d} {0:d}".format(x, y, z)) # hasan 20 30 10 
print("hasan {2:f} {0:f} {1:f}".format(x, y, z)) # hasan 30 10 20
print("hasan {2:.2f} {0:.4f} {1:.5f}".format(x, y, z)) # hasan 30 10 20

# Format version 3.6 and new versions

myname = "hasan"
myage = 16 

print("My name is {myname} and my age is {myage}")  # Error 
print(f"My name is {myname} and my age is {myage}")

print("=" * 40)

