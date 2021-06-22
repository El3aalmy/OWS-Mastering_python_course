# One : 

print(100)
print("Hasan")
print([1, 2, 3, 4])
print({"one" : 1, "two" : 2})
print(True)

print("")
print([])
print({})
print(0)
print(False)

# Two : 

html = 80
css = 60
javascript = 70

print(html > 50 and css > 50 and javascript > 50)   # True

# Three : 

num_one = 10
num_two = 20
num = 20

print(num > num_one or num_two) # True 
print(num > num_one and num_two) # False 

# Four : 

num_one = 10
num_two = 20

resault = num_one + num_two

print(resault)  # 30
print(resault**3)   # 27000
print((resault ** 3) % 2600) # 1000
print(float(((resault ** 3) % 2600) / 5))   # 200.0
print(str(((resault ** 3) % 2600) / 5))
