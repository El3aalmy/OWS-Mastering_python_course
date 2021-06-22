# ------------------------------------------------------
# -- Advanced lessons => timing your code with timeit --
# ------------------------------------------------------
# - timeit - Get execution time of code by running 1M time and give you minimal time  
# -        - It used for performance by testing all functionality 
# - timeit(stmt, setup, time, number)
# - timeit(pass, pass, default, 1.000.000) default values
# --------------------------------------------------------------------------------------------
# - stmt: code you want to measure the execution time 
# - setup: setup done before the code execution (import module or anything)
# - timer: the timer value 
# - number: how many execution that will run
# --------------------------------------------------------------------------------------------

import timeit

# print(dir(timeit))


# print(timeit.timeit("'Hasan' * 1000"))


# name = "Hasan"
# print(name * 1000)

# print(timeit.timeit("name = 'Hasan'; name * 1000"))


# print(random.randint(0, 50))

# print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random"))



print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=4))
# ( test 1M timte and get result ) * 4 => give 4 results 

