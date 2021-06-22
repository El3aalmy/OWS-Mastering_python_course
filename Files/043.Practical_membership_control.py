# ------------------------------------------
# ------ Practical membership control ------
# ------------------------------------------

# List contains admins 
admins = ["Ahmed", "Osama", "sameh", "Manal", "Rahma", "Mahmoud", "Enas"]

# Login 
print("-" * 40)
name = input("---- Please type your name : ").strip().capitalize()

# If name in admins 

if name in admins :

    print(f"---- Your name is {name}")

    option = input("---- Delete or update name ? ").strip().capitalize()

    
    # Update option 
    if option == 'Update' or option == "U": 

        TheNewName = input("---- Your new name is ").strip().capitalize()

        admins[admins.index(name)] = TheNewName

        print("---- Name updated")

        print(admins)

        print("-" * 27)

    
    # Delete option
    elif option == 'Delete' or option == "D":

        admins.remove(name)

        print("---- Name deleted")

        print(admins)

        print("-" * 27)

    
    # Wrong option 
    else :

        print("---- Wrong option choosed")

        print("-" * 27)

else :

    status = input("---- Not admin, add you Y, N ? ")

    if status == 'Yes' or status == 'Y' :

        print("---- You have been added")

        admins.append(name)

        print(admins)

        print("-" * 27)

    else :

        print("---- You are not added")

        print("-" * 27)

print("------ Program ended ------")

