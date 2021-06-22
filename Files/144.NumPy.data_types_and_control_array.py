# ---------------------------------------
# -- NumPy => data types control array --
# ---------------------------------------
# https://numpy.org/devdocs/user/basics.types.html
# https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html$specifying-and-constructing-data-types
# ---------------------------------------
# ?     boolean 
# b     (signed) byte
# B     unsigned byte
# i     signed integer
# u     unsigned integer 
# f     floating-point
# c     complex-floating point 
# m     timedelta
# M     datetime
# O     (python) objects 
# S, a  zero terminated bytes (not recommended)
# U     unicode string
# V     raw data (void)
# ---------------------------------------- 

import numpy as np

# Show array data type 

my_array1 = np.array([1, 2, 3])
my_array2 = np.array([1.5, 20.15, 3.601])
my_array3 = np.array(["Hasan Salah", "B", "Ahmed"])

print(my_array1.dtype)
print(my_array2.dtype)
print(my_array3.dtype)


print("=" * 20) # -----------------------------


# Create array with specific data type

my_array4 = np.array([1, 2, 3], dtype='float') # float or "float" or "f"  => f is float 32, other is float64
my_array5 = np.array([1.5, 20.15, 3.601], dtype=int) # int or "int" or "i"
# my_array6 = np.array(["Hasan Salah", "B", "Ahmed"], dtype=int) # Value error

print(my_array4.dtype)
print(my_array5.dtype)
# print(my_array6.dtype) # Error


print("=" * 20) # -------------------------------


# Change data type of existing array 

my_array7 = np.array([0, 1, 2, 3, 0, 4])
print(my_array7.dtype)
print(my_array7)

print("=" * 20)

my_array7 = my_array7.astype('float')
print(my_array7.dtype)
print(my_array7)

print("=" * 20)

my_array7 = my_array7.astype('bool')
print(my_array7.dtype)
print(my_array7)


print("=" * 20) # ------------------------------

 
# Test capacity

my_array8 = np.array([100, 200, 300, 400], dtype="f")
print(my_array8.dtype)
print(my_array8[0].itemsize) # 4 bytes => because of array float32

my_array8 = my_array8.astype('float')
print(my_array8.dtype)
print(my_array8[0].itemsize) # 8 bytes => because of array float64
