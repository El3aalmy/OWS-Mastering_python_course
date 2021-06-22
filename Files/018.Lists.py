# ---------------------------------------
# ---- Lists ----------------------------
# ------------
# [1] Lists items are enclosed in square brackets 
# [2] Lists are aordered, to use index to access item 
# [3] Lists are mutable => add, delete, edit
# [4] Lists items is not unique
# [5] Lists can have different data types
# ---------------------------------------

mylist = ["one", "two", "one", 1, 100.5, True]

print(mylist)   # All list
print(mylist[1])    # "one"   # Data type => str (String)
print(mylist[-1])    # True
print(mylist[-3])    # 1

print(mylist[1:4])  # ["two", "one", 1]
print(mylist[:4])   # ['one', 'two', 'one', 1]
print(mylist[1:])   # ['two', 'one', 1, 100.5, True]

print(mylist[::1]) # Steps : 1 (default)   # ['one', 'two', 'one', 1, 100.5, True]
print(mylist[::2]) # Steps : 2  # ['one', 'one', 100.5]

# List is mutable

print(mylist)
# mylist[1] = 2
# mylist[-1] = False
# mylist[0:2] = []
# mylist[0:3] = ["a", "b", "c"]
mylist[0:2] = ["a"]
print(mylist)

