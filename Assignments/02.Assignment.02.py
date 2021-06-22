name = "hasan"
age = 16 
country = "Egypt"

print("\'" + name + "\'" + ", how you doing \\ \"\"\" your age is \"{}"  .format(age) + "\" + and your country is :" + country)

# ------------ 

print("\'" + name + "\'" + ", how you doing \\ \n \"\"\" your age is \"{}"  .format(age) + "\" + \n and your country is :" + country)

# ------------

var = "hasan" 

print(var[1])
print(var[2])
print(var[4])
# ------------

print(var[0:3])
print(var[0] + var[2] + var[4])
print(var[3] + var[2] + var[0])

# ------------

var2 = "#@#@hasan#@#@"

print(var2.strip("#@"))

# ------------

num = "9"
num = "15"
num = "130"
num = "550"
num = "3111"

print(num.zfill(4))

# ------------

var3 = "hasan"
var4 = "hasan salah"

print(var3.rjust(20, "@"))
print(var4.rjust(20, "@"))

# ------------

name1 = "HAsaN"
name2 = "haSAn"

print(name1.swapcase())
print(name2.swapcase())

# -----------

msg = "I love python and i love html"

print(msg.count("love"))

# ----------- 

name3 = "hasan"

print(name3.index("s"))

# ----------

var5 = "I j pyhton and j html"

print(var5.replace("j", "love", 1))

# ----------

var5 = "I j pyhton and j html"

print(var5.replace("j", "love", 2))

# ----------

namef = "hasan"
agef = 16
countryf = "Egypt"

print(f"My name is {namef} , and my age is {agef} , and my country is {countryf}" )