# --------------------------
# --- Built in functions ---
# --------------------------
# abs()
# pow()
# min()
# max()
# slice()
# -------------------------

# abs()
# Return distance between number and zero 

print(abs(100))
print(abs(-100))
print(abs(10.19))
print(abs(-10.19))


# pow(base, exp, mod) => power 

print(pow(2, 5))	# 2 * 2 * 2 * 2 * 2
print(pow(2, 5, 10))	# (2 * 2 * 2 * 2 * 2) % 10 


# min(item, item, item, or iterator)
# Returen the minimum elements 

my_numbers = (1, 20, -50, -100, 100)
print(min(1, 10, -50, 20, 30))
print(min("a", "z", "x", "osama")) # => a
print(min("z", "x", "osama"))	# osama => firist letter (o) is the minimum
print(min(my_numbers))


# max(item, item, item, or iterator)
# Returen the maximum elements 

my_numbers = (1, 20, -50, -100, 100)
print(max(1, 10, -50, 20, 30))
print(max("a", "z", "x", "osama")) # => a
print(max("z", "x", "osama"))	# osama => firist letter (o) is the minimum
print(max(my_numbers))


# slice(start, stop, step)	
# stop is no optional => if give it one parameter => make it the stop
a = ["a", "b", "c", "d", "e", "f"]
print(a[:5])
print(a[slice(5)])
print(a[slice(2, 5)])
