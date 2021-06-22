# -------------------------------
# -- Strings methods 3 ----------
# -------------------------------

# index(Substring, start, end)  # If sub string not found => erorr ---------------

a = "I love python" 
print(a.index("p"))   # index => 7
print(a.index("p", 0, 10))   # index => 7
print(a.index("p", 0, 5))   # index => 7

# find(Substring, start, end)   # If sub string not found => print ("-1") -----
 
b = "I love python" 
print(b.find("p"))   # index => 7
print(b.find("p", 0, 10))   # index => 7
print(b.find("p", 0, 5))   # index => 7

# rjust(width, fill character) , ljust(width, fill character)-----------
# rjust => put fill character from the left
# ljust => put fill character from the right

c = "hasan"
print(c.rjust(10,)) # If fill character not found => print spaces
print(c.rjust(10, "#"))

d = "hasan"
print(d.ljust(10))  # If fill character not found => print spaces
print(d.ljust(10, "#"))

# splitlines()  => Return elements as a list -------------------

e = """First line
second line 
third line"""

print(e.splitlines())

f = "First line \n Second line \n third line"

print(f.splitlines())

# expandtabs() ----------------------------------------------

g = "hasan\tsalah\teisa"

print(g.expandtabs(5))

# -----------------------------------------------------------   

One = "I love python and 4F"
two ="I love python and 4f"
print(One.istitle())    # Return bool =>    true
print(two.istitle())    # Return bool =>    false


Three = " "
Four = ""
print(Three.isspace())   # Return bool =>    true
print(Four.isspace())   # Return bool =>    false


five = "i love python"
six = "I Love python"
print(five.islower())   # Return bool =>    true
print(six.islower())   # Return bool =>    false

seven = "hasansalah"
eight = "hasansalah100"
nine = "hasan--salah"

print(seven.isidentifier()) # Return bool => true
print(seven.isidentifier()) # Return bool => true
print(seven.isidentifier()) # Return bool => false


x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"

# isalpha => Is the string elements from a to z ? 

print(x.isalpha())  # Return bool =>    true
print(y.isalpha())  # Return bool =>    false


u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"

# isalnum => Is the string elements from [ a to z ] or [ a to z and contain numbers ] ? 

print(u.isalnum())  # Return bool =>    true
print(z.isalnum())  # Return bool =>    true
# ------------------------------------------------------