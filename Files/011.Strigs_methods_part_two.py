# ------------------------- 
# ---- Strings methods ----
# -------------------------

# split() rsplit() # Return string as a list of elements 

a = "I love python and PHP"
print(a.split())

b = "I-love-python-and-PHP"
print(b.split("-"))

c = "I-love-python-and-PHP"
print(c.split("-", 3))

d = "I-love-python-and-PHP"
print(d.rsplit("-", 3))     # Split from right 

# -------------------------------------------------------

# center()

e = "Hasan"
print(e.center(9))  # Spaces
print(e.center(9, "#"))  # #
print(e.center(15, "@"))  # @

# -------------------------------------------------------

# count()       # Return the number of parametar

f = "I love python and PHP because PHP is easy"
print(f.count("PHP"))   # 2 PHP words
print(f.count("PHP", 0, 25))   # Only one PHP word

# -------------------------------------------------------

# swapecase()   # Transform capital to small , small to capital 

g = "I love python" 
h = "i LoVe pYTHON"
print(g.swapcase()) 
print(h.swapcase()) 

# -------------------------------------------------------

# startstwith()  Return => bool

i = "I love python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("p", 7, 12))

# -------------------------------------------------------

# endstwith()   Return => bool

j = "I love python"
print(g.endswith("n"))
print(g.endswith("S"))
print(g.endswith("e", 3, 6))

# -------------------------------------------------------