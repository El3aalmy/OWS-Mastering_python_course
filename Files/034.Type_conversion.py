# ------------------------------
# ------- Type conversion ------
# ------------------------------

# str()

a = 10
print(type(a))  # Int
print(type(str(a))) # String 

# tuple()

c = "Hasan" # String 
d = [1, 2, 3, 4, 5] # List 
e = {"a", "b", "c"} # Set 
f = {"a" : 1, "b" : 2}  # Dictionary 

print(tuple(c))
print(tuple(d))
print(tuple(e))  # Set printed not ordered
print(tuple(f)) # Take keys only from dict


# list()

c = "Hasan" # String 
d = (1, 2, 3, 4, 5) # Tuple 
e = {"a", "b", "c"} # Set 
f = {"a" : 1, "b" : 2}  # Dictionary 

print(list(c))
print(list(d))
print(list(e))  # Set printed not ordered 
print(list(f))  # Take keys only from dict


# set()

c = "Hasan" # String 
d = (1, 2, 3, 4, 5) # Tuple 
e = ["a", "b", "c"] # List 
f = {"a" : 1, "b" : 2}  # Dictionary 

print(set(c))  # Data printed no ordered 
print(set(d))  # Data printed no ordered 
print(set(e))  # Data printed no ordered  
print(set(f))  # Data printed no ordered # Take keys only from dict

# dict()

c = "Hasan" # String 

d = (1, 2, 3, 4, 5) # Tuple # Must has keies and values , following :
d = (("a" : 1), ("b" : 2), ("c" : 3))

e = ["a", "b", "c"] # List # Must has keies and values , following :
e = [["a" : 1], ["b" : 2], ["c" : 3]]

f = {"a", "b"}  # Set   # Error 

print(dict(c))  # Error   # Cannot convert string to dict , must has keies and values 
print(dict(d))  # Error   # Cannot convert tuple to dict , must has keies and values (nested tuples) , The new d in valied
print(dict(e))  # Error   # Cannot convert list to dict , must has keies and values (nested lists) , The new e in valied  
print(dict(f))  # Error   # Cannot convert set to dict although if there is nested sets 
