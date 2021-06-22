# -------------------------------------------------
# --- File handling => write and append in file ---
# -------------------------------------------------

# Write => Replace the new value with the old value 

my_file = open("C:\Users\حسن صلاح\Google Drive\1. Projects_\Python course (Osama)\Learning code\hasan.txt", "w")
my_file.write("This is a first line\n")
my_file.write("Second line")

my_file = open(r"C:\Users\حسن صلاح\Google Drive\1. Projects_\Python course (Osama)\Learning code", "w")
my_file.write("Hasan salah\n" * 1000)

my_list = ["Osama\n", "Ahmed\n", "Sayed"]
my_file = open("C:\Users\حسن صلاح\Google Drive\1. Projects_\Python course (Osama)\Learning code", "w")
my_file.writelines(my_list)


# Append => Don't replace the new values with the old values 
# Start typing from the last line typed

my_file = open("C:\Users\حسن صلاح\Google Drive\1. Projects_\Python course (Osama)\Learning code", "a")
my_file.write("hasan")
my_file.write("hasansalah\n") # Write after the word hasan not in the new line because there is no \n in the last line 
my_file.write("hasansalaheisa") # Write in the new line because there is a \n in the last line
