# ---------------------------------
# -- Function default parameters --
# ---------------------------------

# If the argument not found , print default parametar you defind it

def details(name="Unknown", age="Unknown", country="Unknown") :

    print(f"My name is {name} and my age is {age} and my country is {country}")

details("Hasan", 16, "Egypt")
details("Ahmed", 20, "KSA")
details("Ahmed")
details()
