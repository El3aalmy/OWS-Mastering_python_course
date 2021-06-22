# -----------------------
# ----- Set methods -----
# -----------------------

# clear()

a = {1, 2, 3, 4}
a.clear()
print(a)

# union 

b = {"one", "two", "three"}
c = {"1", "2", "3"}
x = {"zero", "hasan"}

print(b | c | x)
print(b.union(c, x))

# add()

d = {1, 2, 3, 4}
d.add(5)
d.add(6)    # Cannot give 2 elements to add in the same method : (d.add(5, 6)) => Error
print(d)

# copy()

e = {1, 2, 3, 4}
f = e.copy()

print(e)
print(f)

e.add(6)

print(e)
print(f)    # The copied set doesnot related to the main set 

# remove()

g = {1, 2, 3, 4}
g.remove(1)
# g.remove(7)   # Give error if not exsist
print(g)

# discard()

h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)    # Don't Give error if not exsist
print(g)

# pop()

i = {"a", True, 1, 2, 3, 4, 5}
print(i.pop())  # Print random element from the set 

# update()

j = {1, 2, 3}
k = {1, "a", "b", 2}
j.update(["HTML", "CSS"])
j.update(k) # Replace j with k and remove the repeated elements

print(j)

