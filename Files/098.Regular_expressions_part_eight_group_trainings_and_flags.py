# ------------------------------------------------------
# -- Regular expressions => group trainings and flags --
# ------------------------------------------------------

import re

# Flages :
# - DOTALL - D => Match all characters 
# - Multiline - M => Match the new line too however you type ^ and $ 
# - IGNOTRECASE - I => Ignore case sensitive => o match o & O
# - VERBOS - V => Ignore comments in regular expressions. ex: \w+#comment 

my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

search = re.search(r"(\w+)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web, re.DOTALL)
# .+ => . : match character but new line | .+  : Match all characters but new line

print(search.group(1))
print(search.groups())

for group in search.groups() :

	print(group)


# Print all peices of URL 

print(f"Protocol: {search.group(1)}")
print(f"Sub domain: {search.group(2)}")
print(f"Domain name: {search.group(3)}")
print(f"Top level domain: {search.group(4)}")
print(f"Port: {search.group(5)}")
print(f"Query string: {search.group(6)}")

