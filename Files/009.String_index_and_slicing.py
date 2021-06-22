# -------------------------------------------------------------
#
# ---------------- String indexing and slicing ----------------
#
# [1] All data in python is object 
# [2] Object contain elements 
# [3] Every element has its own index 
# [4] python use zero based indexing ( Index start from zero )
# [5] Use Square brackets to access elements 
# [6] Enable accessing parts of strings , tuples or lists
#
# --------------------------------------------------------------

# Indexing ( Access single element )

myString = "I love python"

print(myString[0])  # Index 0 => I
print(myString[9])  # Index 9 => t

print(myString[-1]) # Index -1 => First character from end 
print(myString[-6]) # Index -6 => 6th character from end 


# Slicing ( Access multipule sequence elements )
# [Start:End]  => End not included
# [Start:End:Steps]

print(myString[8:11])  # =>yth
print(myString[3:5])  # =>ov

print(myString[:10])  # If start isnot here , start from 0 ( I love pyt )
print(myString[5:])  # If end isnot here , go to end ( e  python )

print(myString[:])  # Full data


print(myString[0::1])   #Full data
print(myString[::1])   #Full data

print(myString[::2]) # Take char and ignore next char
print(myString[::3]) # Take char and ignore next two char