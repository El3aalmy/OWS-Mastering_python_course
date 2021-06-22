# --------------------------

mylist = ["Hasan", "Ahmed", "Fatima", "Omar", "Khaled"]

print(mylist[0])
print(mylist[-5])
print(mylist[-1])
print(mylist[4])

print(mylist[0] + ", " + mylist[2] + ", " + mylist[4])
print(mylist[1] + ", " + ", " + mylist[3])

# print("'Ahmed', 'Fatima', 'Omar'")
# print("'Omar', 'Khaled'")

mylist[-2] = "hasan"
mylist[-1] = "hasan"
print(mylist)

mylist[0] = "firstname"
mylist[-1] = "secondname"
print(mylist)

mylist.remove("firstname")
mylist.remove("secondname")
print(mylist)

mylist.remove("hasan")
print(mylist)

mylist2 = ["Yousef", "Mouaz"]
mylist3 = ["Kareem", "salah"]

mylist.extend(mylist2)
mylist.extend(mylist3)

print(mylist)


mylist.sort(reverse=False)
print(mylist)

mylist.sort(reverse=True)
print(mylist)

print(len(mylist))

mylist4 = ["HTML", "CSS", "Javascript", "Python", ["Django", "Flask", "Web"]]


print(mylist4[4][0])
print(mylist4[4][2])








