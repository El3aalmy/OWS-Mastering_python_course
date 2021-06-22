# ----------------------------------------------------
# -- Regular expressions => re module split and sub --
# ----------------------------------------------------
# split(pattern, string, MaxSplit) => return a list of elements spllitted on each match 
# sub(pattern, replace, string, ReplaceCount) => Replace matches with what you want 
# --------------------------------------------------------------------------------------

import re 

# ----- split

string_one = "I love python programming language"

search_one = re.split(r"\s", string_one, 1)

print(search_one)


print("#" * 20)


string_two = "How-to_write_a_very-good-article"

search_two = re.split(r"-|_", string_two)

print(search_two)


print("#" * 20)


# Get words from URL

for counter, word in enumerate(search_two) :

	if len(word) == 1 :

		continue 

	print(f"Word number: {counter} => {word.lower()}")


print("#" * 20)


# ------ Sub 

my_string = "I love python"

print(re.sub(r"\s", "-", my_string, 1))
