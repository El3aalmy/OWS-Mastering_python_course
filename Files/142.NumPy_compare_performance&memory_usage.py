# ------------------------------------------------
# -- NumPy => Compare performace and memory use --
# ------------------------------------------------
# - Performance
# - Memory use
# ------------------------------------------------

import numpy as np 
import time
import sys 

elements = 1500000

my_list1 = range(elements)
my_list2 = range(elements)

my_array1 = np.arange(elements)
my_array2 = np.arange(elements)


list_start = time.time()
list_result = [(n1 + n2) for n1, n2 in zip(my_list1, my_list2)]
print(f"List time is {time.time() - list_start}")

array_start = time.time()
array_result = my_array1 + my_array2
print(f"Array time is {time.time() - array_start}")


# for n1, n2 in zip(my_list1, my_list2):
#     print(n1 + n2)

# print(list_result)
# print(array_result)


print("=" * 15) # ---------------------------------


my_array = np.arange(100)

print(my_array)
print(my_array.itemsize)  # Size of element of the array in memory
print(my_array.size)  # Size of elements of the array (100) => number of elements 

print(f"All bytes: {my_array.itemsize * my_array.size}")
# The size of all elements of the array (bytes)


print("=" * 20)


my_list = range(100)

print(sys.getsizeof(my_list[0]))   
# Only number 0 is different than all elements in the list (less than them)

print(len(my_list))
print(f"All bytes: {sys.getsizeof(my_list[1]) * len(my_list)}")
