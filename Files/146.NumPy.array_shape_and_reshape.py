# ------------------------------------
# -- NumPy => Array shape & reshape --
# ------------------------------------
# Shape returns a tuple contains the number of elements in each dimension
# ------------------------------------

import numpy as np

my_array1 = np.array([1, 2, 3, 4])
print(my_array1.ndim)
print(my_array1.shape)  # Return the number of elements in the dimension


print("=" * 20) # -------------------------------------


my_array2 = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
print(my_array2.ndim)
print(my_array2.shape)


print("=" * 20) # ------------------------------


my_array3 = np.array([[[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]], [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]])
print(my_array3.ndim)
print(my_array3.shape)


print("=" * 20) # -----------------------------


my_array4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(my_array4.ndim)
print(my_array4.shape)

reshaped_array4 = my_array4.reshape(3, 4)
print(reshaped_array4.ndim)
print(reshaped_array4.shape)
print(reshaped_array4)


print("=" * 20) # --------------------------------------


my_array5 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
print(my_array5.ndim)
print(my_array5.shape)

print("=" * 10)

# reshaped_array5 = my_array5.reshape(-1) # -1 => make all elements in 1 dimension
# reshaped_array5 = my_array5.reshape(4, 5) 
reshaped_array5 = my_array5.reshape(2, 5, 2) 
print(reshaped_array5.ndim)
print(reshaped_array5.shape)
print(reshaped_array5)
