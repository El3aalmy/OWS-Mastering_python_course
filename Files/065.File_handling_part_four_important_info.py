# ---------------------------------------
# --- File handling => important info ---
# ---------------------------------------

my_file = open("C:\Users\حسن صلاح\Google Drive\1. Projects_\Python course (Osama)\Learning code\hasan.txt", "a")
my_file.truncate(5) # Take 5 bytes and remove other characters

my_file = open("C:\Users\حسن صلاح\Google Drive\1. Projects_\Python course (Osama)\Learning code\hasan.txt", "a")
print(my_file.tell())   # Give a number of bytes of the place of the cursor 
# The new line => 2 bytes 

# Text in file => Hasan salah
my_file = open("C:\Users\حسن صلاح\Google Drive\1. Projects_\Python course (Osama)\Learning code\hasan.txt", "r")
my_file.seek(6)    # Move cursor to position ( byte ) 6 
print(my_file.read())
# Output => salah


# Remove file 

import os 
os.remove("C:\Users\حسن صلاح\Google Drive\1. Projects_\Python course (Osama)\Learning code\hasan.txt")
