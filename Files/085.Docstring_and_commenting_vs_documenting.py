# --------------------------------------------
# -- Doc string & commenting vs documenting --
# --------------------------------------------
# [1] Documentaion string for calss, module or function 
# [2] Can be accessed from the help and doc attributes 
# [3] Made for understanding the funcionality of the complex code 
# [4] There is one line and multiple line doc string 
# ----------------------------------------------------------------

def my_name(name) :
    # '''This is a function to print name'''  # Single line documentation
    """
    my_name function 
        it print the name 
    parameter :
        name => person name 
    return : 
        return => my name is 
    """
    print(f"My name is : {name}")

my_name("Hasan")


# print(dir(my_name))


# Show the documentation 

print(my_name.__doc__)
help(my_name)
