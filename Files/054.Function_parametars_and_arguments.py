# ----------------------------------------
# --- Function parametar and arguments ---
# ----------------------------------------

a, b, c = "Osama", "Ahmed", "Sayed"

print(f"My name is : {a}")
print(f"My name is : {b}")
print(f"My name is : {c}")

# def                           => Function keyword (define)
# My_name_is                    => Function name
# name                          => Parameter 
# print(f"My name is {name}")   => Task 
# My_name_is("Ahmed")           => Ahmed is the argument

def My_name_is(name) :

    print(f"My name is {name}")

My_name_is(a)
My_name_is(b)
My_name_is(c)


def addition1(n1, n2) :

    print(n1 + n2)

# addition1(100)     # Error => Must put 2 arguments because you hava two parametars
addition1(100, 300)
# addition1(100, 300, 200)  # Error => Must put 2 arguments because you hava two parametars


def addition2(n1, n2):

    if type(n1) != int or type(n2) != int :

        print("Only integers allowed")

    else :

        print(n1 + n2)

addition2(100, 200)


def full_name(first, middle, last) :

    print(f"My name is {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")

full_name("  Hasan  ", "salah", "Eisa")


