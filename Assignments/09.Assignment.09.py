# -------------------------------------------

num1 = int(input("---- Enter num 1 : "))
operation = str(input("Enter operation => + , - , * , / , % : "))
num2 = int(input("---- Enter num 2 : "))

if operation == '+' :

    print(num1 + num2)

elif operation == '-' :

    print(num1 - num2)

elif operation == '*' :

    print(num1 * num2)

elif operation == '/' :

    print(num1 / num2)

elif operation == '%' :

    print(num1 % num2)

else : 

    print("Invaliad operation")

# ----------------------------------------

age = 17 

print("Good" if age > 16 else "Not good")

# ------------------------------------------

age2 = int(input("Enter your age : "))

months = age2 * 12
weeks = months * 4
days = age2 * 364
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

if age2 > 10 and age2 < 100 : 

    print(f"{months} months")
    print(f"{weeks} weeks")
    print(f"{days} days")
    print(f"{hours} hours")
    print(f"{minutes} minutes")
    print(f"{seconds} seconds")

else : 

    print("No")

# --------------------------------------


country = input("Enter your country : ").strip().capitalize()
countries = ["Egypt", "Syria", "Kuwait", "Jordon"]
discount = 30
price = 100

if country in countries :

    print(f"The discount is {discount}")

else :

    print(f"The price is {price}")

# ----------------------------------------