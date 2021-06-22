# --------------------------
# --- Built in functions ---
# --------------------------
# all()
# any()
# bin()
# id()
# --------------------------

# all()

x = [1, 2, 3, 4]        # Condition true
x = [1, 2, 3, 4, []]    # Condition false 

if all(x) :

    print("All elements is true")

else :

    print("There is at least one elements is false")


# any()

i = [1, 2, 3, []]   # Condition true
i = [0, 0, []]      # Condition false 

if any(i) :
    
    print("There at least one elements is true")

else :

    print("Thre's no any element is true")


# bin()
# Transform to binary => Computer language (0, 1)

print(bin(100))


# id()
# Return id of the object in the memory

a = 1
b = 2 

print(id(a))
print(id(b))
