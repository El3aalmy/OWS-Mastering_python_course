# ----------------------------------------
# ----- Loop => While training -----------
# ----------------------------------------
# While condeition is true 
#   Code run until condition become false 
# ----------------------------------------

MyF = ["Os", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa", "Ha"]

# print(len(MyF)) # List length ( 10 )

a = 0 

while a < len(MyF) :    # a < 10

    print(f"{str(a + 1).zfill(2)}. {MyF[a]}")

    a += 1  # a = a + 1

else :

    print("Loop is done")


# print(f"1. {MyF[0]}")
# print(MyF[1])
# print(MyF[2])
# print(MyF[3])
# print(MyF[4])
# print(MyF[5])
# print(MyF[6])
# print(MyF[7])
# print(MyF[8])
# print(MyF[9])

