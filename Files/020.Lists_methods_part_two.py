# ----------------------
# -- Lists methods 2 ---
# ----------------------

# clear()

a = [1, 2, 3, 4]
a.clear()
print(a)

# copy()

b = [1, 2, 3, 4]
c = b.copy()

print(b)    # Main list
print(c)    # Copied list

b.append(5)

print(b)
print(c)    # The copied list doesnot related to the mailn list

# count()

d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))

# index()

e = ["Hasan", "Ahmed", "Sayed", "Osama", "Ahmed", "Osama"]
print(e.index("Osama"))

# insert()

f = [1, 2, 3, 4, 5, "a", "b"]
f.insert(0, "test")     # Must add the index number of the element you want to add the new element (before) it
f.insert(-1, "test")
print(f)

# pop()

g = [1, 2, 3, 4, 5, "a", "b"]
print(g.pop(-3))    # Print 5