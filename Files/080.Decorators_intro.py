# ---------------------------
# --- Decorators => intro ---
# ---------------------------
# [1] Sometimes called meta programming 
# [2] Everything in python is object even functions
# [3] decorator take a function and add some functionality and return it 
# [4] Decorator wrap other function and enhance their behaviur
# [5] Decorator is higher order funciton (function accept function as a parameter)
# ---------------------------------------------------------------------------------------

def my_decorator(func) :    # Decorator 

    def nested_func() :     # Any name it's just for decoration

        print("before") # Message from decorator 

        func()  # Execute function

        print("After")  # Message from decorator

    return nested_func  # Return all data


@my_decorator
def my_name_is() :

    print("My name is hasan")


@my_decorator
def my_age_is() :

    print("My age is 16")

# after_decoration = my_decorator(my_name_is)
# after_decoration()


my_name_is()
print("=" * 10)
my_age_is()
