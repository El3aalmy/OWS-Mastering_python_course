# ---------------------------
# ------- Strings -----------
# ---------------------------

myStringOne = 'This is single qoute'
myStringtwo = "This is double qoutes"

print(myStringOne)
print(myStringtwo)

# --------------------------------

myStringThree = 'This is single qoute "test"'  # To print double qoutes => use scape sequence or other qoutes
myStringFour = "This is single qoute 'test'"  # To print single qoutes => use scape sequence or other qoutes

print(myStringThree)
print(myStringFour)

# -------------------------------

myStringFive = '''First 
Second 
Third '''
# myStringFive = 'First\nSecond\nThird '

myStringSix = """First 
Second
Third """
# myStringSix = """First\nSecond\Third

print(myStringFive)
print(myStringSix)

# --------------------------------

myStringSeven = '''First 
Second 'test' "test"
Third '''

myStringAight = """First 
Second "test" 'test' 
Third """

print(myStringSeven)
print(myStringAight)

# --------------------------------


myStringNighn = """First 
Second "test" \ \\ 'test'  \
Third """

print(myStringNighn)