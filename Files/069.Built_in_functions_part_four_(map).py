# ---------------------------------
# --- Built in functions => map ---
# ---------------------------------
# [1] Mape take a function + iterator 
# [2] Map called map because it map the function on every element
# [3] The function can be pre-defined function or lambda function 
# -----------------------------------------------------------------

# Use map with pre-defined function 

def format_text(text) :

	return f"- {text.strip().capitalize()} -"

my_texts = ["Osama", "Ahmed", "Sayed"]

my_formated_data = map(format_text, my_texts)

print(my_formated_data)

for name in my_formated_data :

	print(name)

# Or

for name in map(format_text, my_texts) :

	print(name)

# Or 

for name in list(map(format_text, my_texts)) :

	print(name)




print("=" * 10)




# Use map with lambda funciton 

# def format_text(text) :

	# return f"- {text.strip().capitalize()} -"

my_texts = ["Osama", "Ahmed", "Sayed"]

# for name in my_formated_data :

# 	print(name)

# Or

for name in map(lambda text : f"- {text.strip().capitalize()} -", my_texts) :

	print(name)

# Or 

for name in list(map(lambda text : f"- {text.strip().capitalize()} -", my_texts)) :

	print(name)


def format_text(text) :

	return f"- {text.capitalize()}"

my_texts = ["aHMEd", "haSAn"]

for name in map(format_text, my_texts) :

	print(f"= {name}")

