# --------------------------------------------------
# -------- Tuple ---------------
# ------------------------------
# [1] Tuple items are enclosed in parentheses 
# [2] You can remove the parentheses if you want 
# [3] Tuple are ordered, to use index to access items 
# [4] Tuple are imutable => you cannot add or delete 
# [5] Tuple items are not uniqe 
# [6] Tuple can have different data types 
# [7] Operators used in strings and lists available in tuples
# --------------------------------------------------

# Tuple syntax & type 

mytuple1 = ("Osama", "Ahmed")
mytuple2 = "Osama", "Ahmed"

print(mytuple1)
print(mytuple2)

print(type(mytuple1))
print(type(mytuple2))

# Tuple indexing 

mytuple3 = (1, 2, 3, 4, 5)
print(mytuple3[0])
print(mytuple3[-1])
print(mytuple3[-3])

# Tuple assign values 

mytuple4 = (1, 2, 3, 4, 5)
# mytuple4[2] = "three"
# print(mytuple4)     # 'tuple' object does not support item assignment

# Tuple items 

mytuple5 = ("hasan", "hasan", 1, 2, 3, 100,5, True)
print(mytuple5[1])
print(mytuple5[-1])

