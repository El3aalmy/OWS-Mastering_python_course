# ---------------------------------------------------------
# -- Regular expressions => re module search and fileall --
# ---------------------------------------------------------
# search()  => Search a string for a match and return a first match only
# findall() => Returns a list of all matches and empty list if no match
# -----------------------------------------------------------------------
# Email pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# -----------------------------------------------------------------------

import re 

# ----- search(pattern, string)

my_search = re.search(r"[A-Z]{2}", "HHasan Salah")

print(my_search)
# print(dir(my_search))
print(my_search.span()) # Return the span only 
print(my_search.string) # Return the string 
print(my_search.group())    # Return the matched characters or character


is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net|)", "hs@hasan.com")

if is_email :

    print("This is a valiade email")

    print(is_email.span())
    print(is_email.string)
    print(is_email.group())

else :

    print("This is not a valiade email")



# ------ findall()

email_input = input("Enter your email : ")

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)

emply_list = []

if search != [] :

	emply_list.append(search)

	print("Email added")

else :

	print("Invalid email")

for email in emply_list :

	print(email)

