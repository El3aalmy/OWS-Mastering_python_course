# ------------------
# --- Generators ---
# ------------------
# [1] Generators is a function with (yield) keyword instead of (return)
# [2] It support iteration and return generator iterator by calling (yield)
# [3] Generator funciton can have one or more (yield)
# [4] By using next() it resume from where it called (yeild) not from begining 
# [5] When called, it's not start automatically, it's only give you the control
# ----------------------------------------------------------

def my_generator() :

    yield 1
    yield 2
    yield 3
    yield 4

# print(my_generator())

my_gen = my_generator()

print(next(my_gen))

print("Hasan salah")

print(next(my_gen))

print("Hasan salah")

print(next(my_gen))

print("Hasan salah")

print(next(my_gen))

# If print the next of the function not the variable :
# print the first element always

# for number in my_gen :

#     print(number)
# This code don't print any thing because the next() method printed all iterator ..
# if remove one next() method => for loop print the last element => 4 (Continue after the next(method))
 
# Print all yields 
for number in my_generator() :

    print(number)

