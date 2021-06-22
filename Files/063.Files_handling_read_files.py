# ------------------------------------
# --- Files handling => read files ---
# ------------------------------------

my_file = open("C:\Users\حسن صلاح\Google Drive\1. Projects_\Python course (Osama)\Learning code", "r")

print(my_file)  # File data object
print(my_file.name)
print(my_file.mode)
print(my_file.encoding)

print(my_file.read())   # Default value =>  -1  ( Read all bytes in the file ) 
print(my_file.read(5))  # Read 5 bytes

print(my_file.readline(3))  # If number is smaller than the number of bytes in the first line => Print the number of bytes you give it and continue the line in the new line 
print(my_file.readline())
print(my_file.readline())

print(my_file.readlines())      # Read all lines as a list
print(my_file.readlines(50))    # Read 50 bytes of all lines 
print(type(my_file.readlines()))      # Type => list


for line in my_file :

    print(line)

    if line.startswith("2") :

        break


# Close the file 

my_file.close()

