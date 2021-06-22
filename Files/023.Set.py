# ----------------------------------------
# ---- Set ----
# -------------
# [1] Set items are enclosed in curly braces 
# [2] Set items are not ordered and not indexed 
# [3] Indexing and slicing cannot be done 
# [4] Set has only immutable data types (numbers, strings, tuples) list and dict are not
# [5] Set items is unique
# ----------------------------------------

# not ordered and not indexed 

MySetOne = {"Osama", "Ahmed", 100}
print(MySetOne)
# print(MySetOne[0])    Error => Set not indexed 

# slicing cannot be done 

MySetTwo = {1, 2, 3, 4, 5}
# print(MySetTwo[0:3]) Error => Cannot slicing in set 

# MySetTree = {"Hasan", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
MySetTree = {"Hasan", 100, 100.5, True, (1, 2, 3)} # Can only has imutable datatypes
print(MySetTree)

# items is unique

MySetFour = {1, 2, "Hasan", "one", "Hasan", 1}
print(MySetFour)
# Output print => {1, 2, "Hasan", "one"}