# ----------------------------------
# -- Built in functions => reduce --
# ----------------------------------
# [1] Reduce take a funciton + iterator 
# [2] Reduce run a function on first and second element and give result
# [3] Then run function on result and third element
# [4] Then run function on result and fourth element and so on 
# [5] Till one lement is left and this is the result of the reduce 
# [6] The function can be pre-defined function or lambda funciton 
# ----------------------------------------------------------------------

from functools import reduce 

def sum_all(num1, num2) :

    return num1 + num2

my_numbers = [1, 8, 2, 9, 100]

# result = reduce(sum_all, my_numbers)
result = reduce(lambda num1, num2 : num1 + num2, my_numbers)

print(result)

# ((((1 + 8) + 2) + 9) + 100)
