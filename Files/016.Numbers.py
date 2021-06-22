# ----------------------
# Numbers --------------
# ----------------------

# Integer 

print(type(1))
print(type(100))
print(type(-21))
print(type(-2221))

# Float 

print(type(1.52))
print(type(-4.588))
print(type(0.511))
print(type(-0.53))

# Complex 

mynum = 5+6j

print(type(mynum))

print("Real part is : {}".format(mynum.real))
print("Imaginary part is : {}".format(mynum.imag))

# [1] Can convert from int to float or complex 
# [2] Can convert from float to int or complex
# [3] Cannot convert conplex to any type 

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

# print(10+9j)
# print(int(10+9j))     # Error

