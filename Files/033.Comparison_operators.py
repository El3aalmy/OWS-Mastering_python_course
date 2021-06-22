# ------------------------------------
# ----- Comparison operators ----
# [==]  equal
# [!=]  No equal 
# [>]   Greatar than
# [<]   Less than 
# [>=]  Greater than or equal 
# [<=]  Less than or equal 
# ------------------------------------

# Equal + not equal 

print(100 == 100)   # True
print(100 == 200)   # False
print(100 == 100.00)    # True

print(100 != 100)   # False
print(100 != 200)   # True
print(100 != 100.00)    # False


# Greater than + Less than  

print(100 > 100)   # False
print(100 > 200)   # False
print(100 > 100.00)    # False
print(100 > 40)    # True

print(100 < 100)   # False
print(100 < 200)   # True
print(100 < 100.00)    # False
print(100 < 40)    # False


# Greater than or equal + Less than or equal   

print(100 >= 100)   # True
print(100 >= 200)   # False
print(100 >= 100.00)    # True
print(100 >= 40)    # True

print(100 <= 100)   # True
print(100 <= 200)   # True
print(100 <= 100.00)    # True
print(100 <= 40)    # False

