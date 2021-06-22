# ----------------------------
# -- NumPy => create arrays --
# ----------------------------

import numpy as np

# print(dir(np))

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

print(my_list)
print(my_array)

print("=" * 50) # ======================================

# Type 
print(type(my_list))
print(type(my_array))   # <class 'numpy.ndarray'> numpy.number of dimensoinal array 

print("=" * 50) # ======================================

# Accessing elements 
print(my_list[0])
print(my_array[0])

print("=" * 50) # ======================================

a = np.array(10)  # Zero dimensional array 
b = np.array([10, 10])  # One dimensional array 
c = np.array( [ [1, 2], [1, 2] ] )   # Two dimensional array 
d = np.array( [ [ [5, 6], [7, 9] ], [ [1, 3], [4, 8] ] ] )   # Three dimensional array 

print(d[1][1][-1])
print(d[1, 1, 1])
print(d[1, 1, -1])

print("=" * 50) # ======================================

# Number of dimensions

print(a.ndim)  # ndim => number of dimensions
print(b.ndim)
print(c.ndim)
print(d.ndim)

print("=" * 50) # ======================================

# Costum dimensions 

my_costum_array = np.array([1, 2, 3], ndmin=3)  # Deal with array as three dimensions array 
print(my_costum_array)
print(my_costum_array.ndim)

print(my_costum_array[0][0][0])
print(my_costum_array[0, 0, 0])
