# ---------------------------------------------
# -- NumPy => Compare data lacation and type --
# ---------------------------------------------

import numpy as np 

my_list = [1, 2, 3, 4, 5]
my_array = np.array([1, 2, 3, 4, 5])

print(my_list[0])
print(my_list[1])

print(my_array[0])
print(my_array[1])


print("=" * 20) # --------------------------------


print(id(my_list[0]))
print(id(my_list[1]))

print(id(my_array[0]))
print(id(my_array[1]))  # Array elements in the same place in memory 


print("=" * 20) # --------------------------------


my_list_of_data = [1, 2, "A", "B", True, 10.50]
my_array_of_data = np.array([1, 2, "A", "B", True, 10.50])

print(my_list_of_data)
print(my_array_of_data) # Deal with all elements as a string if array has string 

print(my_list_of_data[0])
print(my_array_of_data[0])

print(type(my_list_of_data[0]))
print(type(my_array_of_data[0])) # Deal with int as a string because the array has sting on it 


print("=" * 20) # ----------------------------------

my_list_of_data_two = [1, 2, "A", "B", True, 10.50]
my_array_of_data_two = np.array([1, 2, 10.50])

print(my_list_of_data_two)
print(my_array_of_data_two)

print(my_list_of_data_two[0])
print(my_array_of_data_two[0])

print(type(my_list_of_data_two[0]))
print(type(my_array_of_data_two[0]))
