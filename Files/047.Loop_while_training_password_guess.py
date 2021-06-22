# ---------------------------------
# ----- Loop => While training ----
# ----- Simple password guess -----
# ---------------------------------

tries = 4

MainPassword = "Hasan@123"

InputPassword = input("Write your password: ")

while InputPassword != MainPassword :   # true

    tries -= 1      # tries = tries - 1 

    print(f"Wrong password, { 'last' if tries == 1 else tries } chance left")

    InputPassword = input("Write your password: ")

    if tries == 1 :

        print("All tries is finished")

        break 
    
else :

    print("Correct password")




