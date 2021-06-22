# ---------------------------------------
# ------- Practical email slicing -------
# ---------------------------------------

email = "hasan_salah_eisa@gmail.com"

theName = input('What\'s your name ?').strip().capitalize()
theEmail = input('What\'s your email ?').strip()

userName = theEmail[:theEmail.index("@")]
theWebsite = theEmail[theEmail.index("@") + 1:]

print(f"My name is {theName} , and my email is {theEmail}")
print(f"Your username is {userName} \nand your domain is {theWebsite}")

# print(email.index("@"))
# print(email[:email.index("@")])
