# ----------------------------------------
# -- Decorators => practical speed test --
# ----------------------------------------

def my_decorator(func) :

    def nested_func(*numbers) :

        for number in numbers :

            if number < 0 :

                print("Number is less than 0")
    
        func(*numbers)

    return nested_func

@my_decorator
def calculation(n1, n2, n3, n4) :
    print(n1 + n2 + n3 + n4)

calculation(-5, 10, 15, 20)

# =========================================

from time import time 

def speed_test(func) :

    def wrapper() :

        start = time()

        func()

        end = time()

        print(f"Funciton running time is : {end - start}")

    return wrapper

@speed_test
def loop() :

    for number in range(1, 21) :

        print(number)

loop()
