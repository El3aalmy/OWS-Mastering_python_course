values = (0, 1, 2)

if any(values):     # 1 value is true at least => true

  my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
# first condition only is true , others no true because my_var is false (0)

    print("Good")

else:

    print("Bad")

# Good 

# ==========================================

v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v))  # 820

# ==========================================

n = 20

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")

else :

	print("no")

# Output => Good

# ==========================================

# all()
def get_all(arg) :
	counter = 0
	for item in arg :
		if item == False :
			counter += 1 
		else :
			continue
	if counter > 0 :
		print("False")
	else :
		print("True")
my_list = [1, 2, 3, 4]	# True
# my_list = [1, 2, 3, 0]	# False

get_all(my_list)


# sum()
my_list = [5, 7, 0]

def get_sum(my_list) -> list :

	the_value = my_list[0]

	my_list = my_list[1:]

	for number in my_list :

		the_value = the_value + number

	return the_value
			
print(get_sum(my_list))


# min()
my_list = [3, 7, 2, 1, 10, 0]

def get_min(my_list) -> list :

	the_value = my_list[0]

	for number in my_list :

		if number < the_value :

			the_value = number

		else :

			continue 

	print(the_value)

get_min(my_list)


# max()
my_list = [3, 7, 2, 1, 10, 0]

def get_min(my_list) -> list :

	the_value = my_list[0]

	for number in my_list :

		if number > the_value :

			the_value = number

		else :

			continue 

	print(the_value)

get_min(my_list)
