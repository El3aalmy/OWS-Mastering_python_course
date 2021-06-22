# ---------------------
# --- File handling ---
# ---------------------
# "a" Append    open file for appending values, create file if not exists
# "r" Read      ( default value ) open file for read and give error if file is not exists 
# "w" Write     open file for writing, create file if not exists 
# "x" Create    Create file, give error if file exists 
# -------------------------------------------------------------------------------------------

import os 

# Main current working directory 
print(os.getcwd()) 

# Directory for the opened file 
print(os.path.dirname(os.path.abspath(__file__)))

# Change current working directory 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print(os.getcwd())

print(os.path.abspath(__file__))


# file = open(r"C:\Users\حسن صلاح\Google Drive\1. Projects_\Python course (Osama)\Learning code\hasan.txt")
# r => Ignore any command in the dirctory like scape sequence 

file = open(r"C:\Users\حسن صلاح\Google Drive\1. Projects_\Python course (Osama)\Learning code\hasan.txt")

