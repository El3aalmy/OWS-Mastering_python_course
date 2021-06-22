# ----------------------
# -- Lists methods 1 ---
# ----------------------

# Append()

Myfrinds = ["Ahmed", "hasan", "Osama"]
Myoldfrinds = ["Haytham", "Samy", "Ali"]

Myfrinds.append("Alaa")
Myfrinds.append(100)
Myfrinds.append(150.200)
Myfrinds.append(True)
Myfrinds.append(Myoldfrinds)

print(Myfrinds)
print(Myfrinds[2])
print(Myfrinds[6])
print(Myfrinds[7])  # The list inside the list is a one element in the main list 
print(Myfrinds[7][2])


# extend()

a = [1, 2, 3, 4]
b = ["a", "b", "c"]
c = ["one", "two"]

a.extend(b) # Add the new list elements is the main list not as a one element
a.extend(c) # Add the new list elements is the main list not as a one element

print(a)

# remove()

x = [1, 2, 3, 4, 5, "hasan", True, "hasan", "hasan"]
x.remove("hasan")
print(x)

# sort()

y = [1, 2, 100, 120, -10, 17, 29]
y = ["a", "z", "c"]
y.sort(reverse= False)  # Cannot sort int and str together 
y.sort(reverse=True)    # Cannot sort int and str together 
print(y)

# reverse()

z = [10, 40, -12, 40, 100]
z.reverse()
print(z)