# --------------------------
# --- Function => lambda ---
# --- Anonymous function ---
# --------------------------
# [1] It has no name 
# [2] You can call it inline without defining it 
# [3] You can use it in return data from anthor function 
# [4] Lambda used for simple function and def handle the large tasks 
# [5] Lambda is one single expression not block of code 
# [6] Lambda type is function 
# --------------------------------------------------------------------

def my_name(name, age) : return f"My name is {name} and my name is {age}"

MyName = lambda name, age : f"My name is {name} and my name is {age}"

print(my_name("Hasan", 16))
print(MyName("Hasan", 17))


print(my_name.__name__)
print(MyName.__name__)

print(type(MyName))

