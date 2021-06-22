# -------------------------
# ----- Set methods -------
# -------------------------

# difference()

a = {1, 2, 3, 4}
b = {1, 2, 3, "Hasan", "Ahmed"}
print(a)
print(a.difference(b)) # a - b  => (Print what in the first set and not in the second set)
print(a)

# difference_update()

c = {1, 2, 3, 4}
d = {1, 2, "Hasan", "Ahmed"}
print(c)
c.difference_update(d)  # c - d  => (Print what in the first set and not in the second set , and update the first set with the difference)
print(c)

# intersection()

e = {1, 2, 3, 4, "x", "Hasan"}
f = {"Hasan", "x", 2}
print(e)
print(e.intersection(f))  # e & f   => (Print the repeated elements in the two sets without update the main one)
print(e)

print("=" * 40) # Separator

# intersection_update()

g = {1, 2, 3, 4, "x", "Hasan"}
h = {"Hasan", "x", 2}
print(g)
g.intersection_update(h)  # e & f   => (Print the repeated elements in the two sets with update the main one)
print(g)

print("=" * 40) # Separator

# symmetric_difference()

i = {1, 2, 3, 4, 5, "x"}
j = {"Hasan", "zero", 1, 2, 4, "x"}
print(i)
print(i.symmetric_difference(j)) # i ^ j    => (Find what isnot in the both sets (In one set only))
print(i)

print("=" * 40) # Separator

# symmetric_difference_update()

k = {1, 2, 3, 4, 5, "x"}
l = {"Hasan", "zero", 1, 2, 4, "x"}
print(k)
k.symmetric_difference_update(l) # k ^ l    => (Find what isnot in the both sets (In one set only) and update the main set with these elements)
print(k)




