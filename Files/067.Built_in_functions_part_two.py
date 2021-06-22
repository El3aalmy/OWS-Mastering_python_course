# --------------------------
# --- Built in functions ---
# --------------------------
# sum()
# round()
# range()
# print()
# --------------------------

# sum(iterable, start)  start default value is 0
a = [1, 10, 19, 40]
print(sum(a))   # => 40
print(sum(a, 40))   # Start in 40 => 40 + sum(a)


# round(number, numofdigits)
# numofdigits is the number after .
print(round(150.499))  # 150 
print(round(150.500))  # 150
print(round(150.451))  # 151 

print(round(150.554, 2))   # 150,55
print(round(150.554, 3))   # 150,554
print(round(150.556, 2))   # 150,56


# range(start, end, step)
print(list(range(0)))   # 0 is the end because it's not optional => if you give it 1 parametar , make it the end not the start(optional parametar)
print(list(range(10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(0, 20, 2)))    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# print()
print("My / name / is / hasan / salah")
print("My", "name", "is", "hasan", "salah", sep=" / ")
# Default separator is space 

print("First line", end=" ")    # Default value of the end is : \n
print("second line")
print("Third line")

# Output :

# First line second line 
# Third line

 