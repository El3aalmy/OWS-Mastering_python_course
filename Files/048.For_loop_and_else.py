# --------------------------------
# ---------- Loop => for ---------
# --------------------------------
# for item in iterable_object : 
#   do something with item 
# --------------------------------
# item is a variable you create and call whatever you want 
# item refer to the current position and will run and visit all items to the end
# iterable_objects => sequence ( list, tuple, set, dict, string of characters, etc ... )

MyNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in MyNumbers :

    # print(number * 10) 

    if number % 2 == 0 :    # Even

        print(f"The number {number} is even")

    else :

        print(f"The number {number} is odd")

else : 

    print("Loop is finished")

# --------------------

MyName = "hasan"

for letter in MyName :

    print(f"[ {letter.upper()} ]")

