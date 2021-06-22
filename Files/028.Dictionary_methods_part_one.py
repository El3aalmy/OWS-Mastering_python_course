# ---------------------------------
# ------- Dictionary methods ------
# ---------------------------------

# clear()

user = {
    "name" : "Hasan"
}

print(user)
user.clear()
print(user)

# update()

member = {
    "name" : "Hasan"
}
print(member)

member['Age'] = 16
print(member)

member.update({"Country" : "Egypt"})
print(member)

# copy()

main = {
    "name" : "Hasan"
}

b = main.copy()
print(b)

main.update({"Skills": "HTML"})
print(main)
print(b)

# Keys() + values()

print(main.keys())
print(main.values())


