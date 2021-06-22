num = int(input("Enter number : "))

if num < 0 or num == 0 :

    print("The number is not bigger than 0")

else :

    print("Printing ...")

    while num > 0 :

        num -= 1 

        if num != 6 :

            import time 

            time.sleep(1)

            print(num)

        if num == 2 :

            break


# ============================================

friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

index = 0

while len(friends) > 0 and index < len(friends) or index == len(friends):

    if friends[index].istitle() :

        print(friends[index])
        index += 1  

# ============================================

skills = ["HTML", "CSS", "Javascript", "PHP", "Python"]

while skills :

    print(f"{skills[0]}\n{skills[1]}\n{skills[2]}\n{skills[3]}\n{skills[4]}" if len(skills) == 5) 

# ============================================

my_friends = []

maxf = 4


while len(my_friends) < maxf :

    name = input("Enter friend name :").strip()

    if name.isupper() :

        print("Invailed")

    elif name.islower() :

        name.title()

        my_friends.append(name)

        print(f"First character has been convarted to capital, name is {name}")

        print(f"Name left is {maxf - len(my_friends)}")

    elif name.istitle() :

        my_friends.append(name)

        print("Name added with the first chapital letter")

        print(f"Name left is {maxf - len(my_friends)}")

else :

    print("No space")
    
# =============================================