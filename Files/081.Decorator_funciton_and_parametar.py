# --------------------------------------------
# -- Decorators => function with parameters --
# --------------------------------------------

def my_decorator(func) :    # Decorator 

    def nested_func(num1, num2) :     # Any name it's just for decoration

        # print("before") # Message from decorator 

        if num1 < 0 or num2 < 0 :

            print("One of the numbers is less than 0")

        func(num1, num2)  # Execute function

    return nested_func  # Return all data


def my_decorator_two(func) :

    def nested_func(num1, num2) :

        print("Comming from decorator two")

        func(num1, num2)

    return nested_func

# Error : 
# @my_decorator
# def calculation(n1, n2) :
#     print(n1 + n2)

@my_decorator
@my_decorator_two
def calculation(n1, n2) :

    print(n1 + n2)

calculation(-5, 90)
