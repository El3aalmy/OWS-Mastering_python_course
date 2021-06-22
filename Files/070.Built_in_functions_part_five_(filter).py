# ----------------------------------
# -- Built in functions => filter --
# ----------------------------------
# [1] Filter take a function + iterator 
# [2] Filter run a function on every element 
# [3] The function can be pre-defined function of lambda function 
# [4] Filter out all elements for which the function return true
# [5] The function need to return boolean value
# -------------------------------------------------------------------

# Example 1 

def check_number(num):

    if num > 10:

        return num 

    # or :

    return num > 10  

    # -----------

    # if num == 0 :

        # return num => not print 0 => 0 is false ( filter use true only )
        # return True => print 0 

    # return num == 0   => return true => print 0 


my_numbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]

my_result = filter(check_number, my_numbers)

for number in my_result:

    print(number)



# Example 2 


def check_name(name) :

    return name.startswith("O")


my_strings = ["Osama", "Omar", "Ahmed", "Othman"]

my_result_of_strings = filter(check_name, my_strings) 

for person in my_result_of_strings :

    print(person)



# Example 3 

my_names = ["Hasan", "Ahmed", "Osama", "Amer", "Atef"]

my_result_of_names = filter(lambda name : name.startswith("A"), my_names)

for name in my_result_of_names :

    print(name)

# Or :

my_names = ["Hasan", "Ahmed", "Osama", "Amer", "Atef"]

for name in filter(lambda name : name.startswith("A"), my_names) :

    print(name)