# --------------------
# -- Function scope --
# --------------------

# x = 1   # Global scope 

def one() :

    global x

    x = 2

    print(f"Print variable from function scope {x}")

def two() :

    x = 10

    print(f"Print variable from function scope {x}")


one()
print(f"Print variable from global scope {x}")
two()
print(f"Print variable from global scope after function is called {x}")
