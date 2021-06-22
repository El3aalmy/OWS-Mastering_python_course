# ---------------------------
# -- Braek, continue, pass --
# ---------------------------
# Continue  => Ignore the current item in the loop and continue loop from the next item
# Break     => Stop the loop at point 
# Pass      => Ignore the condition of function .. etc 
# ----------------------------------------------------------------------------------------


Numbers = [1, 2, 3, 5, 6, 7, 10, 13, 14, 15, 19]

# Continue 

for number in Numbers :

    if number == 13 :

        continue
    
    print(number)


print("=" * 20)

# Break 

for number in Numbers :

    if number == 13 :

        break

    print(number)


print("=" * 20)

# Pass

for number in Numbers :

    if number == 13 :

        pass

    print(number)

