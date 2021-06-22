# ------------------------------------
# ---      Exceptions handling     ---
# -- Try | except | else | finally  --
# ------------------------------------
# Try       => test the code for errors 
# Except    => handle the erorrs
# ------------------------------------
# Else      => If no errors 
# Finally   => run the code 
# ------------------------------------

number = int(input("Enter your age : "))

print(number)
print(type(number))


try :   # Try the code and test errors

    number = int(input("Enter your age :"))

    print("Good, this is integer from try")

except :  # Handle errors if its found

    print("Bad, This is not integer")

else :  # If there is no errors 

    print("Good, this is integer from else")
    # You can replace the else with try like second line in try

finally :   # Print whatever happens

    print("Print from finally whatever happens")


try :

    # print(10/ 0)
    # print(x)
    print(int("hasan"))

except ZeroDivisionError :

    print("Cannot devide")

except NameError :

    print("Identifier not found")

except :    # This is a global except for any error not equal last types of errors

    print("Error happens")

# except ValueError :

#     print("Value error")
