# -----------------------
# ----- Set methods -----
# -----------------------

# issuperset()

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b))   # True => Is all elements in the second set in the first set ?
print(a.issuperset(c))   # False  => Is all elements in the second set in the first set ?

print("=" * 50) # Separator

# issubset()

d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}

print(d.issubset(e))    # False => Is the elements in the first set in the second set ?
print(d.issubset(c))    # True  => Is the elements in the first set in the second set ?

print("=" * 50) # Separator

# isdisjoint()

g = {1, 2, 3, 4}
h = {1, 2 ,3}
i = {10, 11, 12}

print(g.isdisjoint(h)) # False  => Is the elements in the first set related to second set ?
print(g.isdisjoint(i)) # True   => Is the elements in the first set related to second set ?

