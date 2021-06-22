# -----------------------------------------------
# -------- Escape sequence characters -----------
# \b => Back space
# \newline => Escape the new line + \
# \ => Escape back slash
# \' => Escape single qoute
# \" => Escape double qoutes
# \n => Line feed
# \r => Carriage return
# \t => Horizontal tab
# \xhh => Characters's hex code
# -----------------------------------------------

# Back space 
print("hasan\b salah") # Remove " n "

# \new line 
print("My \
name is \
hasan")

# Escape back slash
print("hasan salah\\") # <= escape back slash

# Escape single qoute
print('my name is \'hasan\' ')

# Escape Double qoute
print("my name is \"hasan\" ")

# Line feed 
print("My name is hasan and this is\nnew line")

# Carriage return 
print("123456\rabcd") # Replace The number of characters and characters of thng before \r with the number and characters of thing that is after \r

# Horizontal tab
print("hasan\tsalah")

# Character hex value 
print("\x4F\x73")  # Print " Os "