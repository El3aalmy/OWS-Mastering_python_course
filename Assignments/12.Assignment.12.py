def calculation(num1, num2, operator="a") :

    if operator.lower() == "add" or operator == "A" or operator == "a" :

        print(num1 + num2)

    elif operator.lower() == "subtract" or operator == "S" or operator == "s" :

        print(num1 - num2) 

    elif operator.lower() == "muliply" or operator == "M" or operator == "m" :

        print(num1 * num2) 

    else : 

        print("Invaliad operator")

calculation(5, 3, "m")

# -----------------------------------------

def addition(*num) :

        num.remove(10)

        for number in num :

            if number != 10 and number != 5 :

                print(sum(num))

                break


addition(10, 4,)      # Cannot do it 

# -----------------------------------

def show_skills(name="Unkown", *skills = "You have no skills") :

    print(f"{name}, Your skills are :")

        for skill in skills :

            print(f"- {skill}")


show_skills("Name", "HTML", "CSS")  

# ------------------------------------

def details(name="Unknown", age="Unknown", country="Unknown") :

    print(f"My name is {name} , my age is {age} , my country is {country}")

details("Hasan", 16)

