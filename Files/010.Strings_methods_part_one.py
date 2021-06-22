# ----------------------------------------
# ------------ Strings methods -----------
# ----------------------------------------

# len()  => Return the number of elements in the object 
a = "I love python"               
b = "     I love python  "       # Spaces are elements 
print(len(a))
print(len(b))

# ----------------------------------------

# strip() rstrip() lstrip()  # Remove spaces 

c = "   I love python   " 
print(c.strip())        # Remove spaces from right and left
print(c.rstrip())       # Remove spaces from right only 
print(c.lstrip())       # Remove spaces from left only 

c = "#####I love python####" 
print(c.strip("#"))        # Remove # from right and left
print(c.rstrip("#"))       # Remove # from right only 
print(c.lstrip("#"))       # Remove # from left only 

c = "#@#@#I love python#@#@#" 
print(c.strip("#@"))        # Remove #@ from right and left
print(c.rstrip("#@"))       # Remove #@ from right only 
print(c.lstrip("#@"))       # Remove #@ from left only 

# --------------------------------------------

# title()       # Make first characters from all words capital and chracters after numbers capital

b = "I love 2d graphics and 3g technology and python"
print(b.title())

# -------------------------------------------

# capitalize()  # Make first characters from all words capital
b = "I love 2d graphics and 3g technology and python"
print(b.capitalize())

# -------------------------------------------

# zfill() 

d, f, u, w = "1", "11", "111", "1111"
print(d.zfill(4))
print(f.zfill(4))
print(u.zfill(4))
print(w.zfill(4))

# -------------------------------------------

# upper()  => Make all characters capital

g = "hasan"
print(g.upper())

# ------------------------------------------

# lower()    => Make all characters small

l = "HaSan"
print(l.lower())

# ----------------------------------------------------