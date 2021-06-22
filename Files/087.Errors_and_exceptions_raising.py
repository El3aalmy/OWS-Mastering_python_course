# ------------------------------------
# --- Errors and exeptions raising ---
# ------------------------------------
# [1] Exeptions is a runtime error reporting mechanism
# [2] Exeption gives you the message to understand the problem 
# [3] Traceback gives you the line to look for the code in this line 
# [4] Exeptions have types (SyntaxError, IndexError, KeyError, ValueErro, etc...)
# [5] Exeptions list https://docs.python.org/3/library/exceptions.html
# [6] Raise keyword used to raise your own exceptions
# ---------------------------------------------------------------------

x = -10 

if x < 0 :

    raise Exception(f"The number {x} is less than zero")  

    print("This is not printed because of the exception")  

else :

    print(f"{x} is good number and ok")

print("Pirnt message after if condition")


y = "Hasan"   # Add exception
y = 10        # Not add exception

if type(y) != int :

    raise ValueError("Only numbers allowed")

print("Print message after if condition")   # Not printed because of exception
