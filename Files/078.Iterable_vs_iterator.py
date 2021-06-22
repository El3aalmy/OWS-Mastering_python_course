# ----------------------------
# --- Interable vs terator ---
# ----------------------------
# Iterable 
# [1] Object cantains data that can be iterated upon
# [2] Examples => (Strings, Lists, Set, Tuple, Dictionary)
# -------------------------------------------------------
# Iterator 
# [1] Object used to iterate ober iterable using next() method return 1 element at a time 
# [2] You can generate iterator from iterable when useing iter() method
# [3] For loop already calls iter() method on the iterable behind the scence
# [4] Gives ( StopIteratoin ) if there's no next element  
# --------------------------------------------------------

my_string = "Hasan"

my_list = [1, 2, 3, 4, 5]

# my_number = True     
# # Error => Int object and float object and bool object are not iterable

for letter in my_string :

    print(letter, end=" ")

for number in my_list :

    print(number, end=" ")

print("\n")

# for n in my_number :

#     print(n, end=" ")



my_iterator = iter(my_string)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
# print(next(my_iterator))  # Error => StopIteratoin => There's is no next element in the iterator

# ----------------------------

# For loop generate iterator from iterable auto

for letter in "Hasan" :

    print(letter, end=" ")

# This equal following :

for letter in iter("Hasan") :

    print(letter)
