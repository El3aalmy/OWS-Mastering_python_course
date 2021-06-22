name = input("Enter your name ").strip().capitalize()

print(f"My name is {name}")

# # -------------------

age = int(input("Enter your age : ").strip())

if age < 16 : 
    
    print("Cannot join")

else :

    print("Can join")

# -------------------

fName = input("Enter your first name : ").strip().capitalize()
lName = input("Enter your last name : ").strip().capitalize()

print(f"My first name is : {fName} and my first char of last name is : {lName[0]}")

# -------------------

email = input("Enter your email : ").strip().lower()

emailName = email[:email.index("@")]
emailWebsite = email[email.index("@")+1:email.index(".")]
emailDomain = email[email.index(".") + 1:]

print(emailName)
print(emailWebsite)
print(emailDomain)

