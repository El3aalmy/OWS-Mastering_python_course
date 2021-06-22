my_list = [1, 2, 3, 4, 5, 1]
unique_list = [1, 2, 3, 4, 5]

print(unique_list)
print(type(unique_list))
print(unique_list[0:4])

# -------------

nums = {1, 2, 3}
letters = {"a", "b", "c"}

print(nums.union(letters))
print(nums | letters)

# -------------

my_set = {1, 2, 3}
letters2 = {"a", "b", "c"}

print(my_set)

my_set.clear()
print(my_set)

my_set.add("a")
my_set.add("b")
print(my_set)

my_set.discard("C")

# --------------

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))

# --------------

dictionary = {
    "One" : {
        "name" : "HTML",
        "Progress" : "80%"
    },
        "Two" : {
        "name" : "CSS",
        "Progress" : "70%"
    },
        "Three" : {
        "name" : "Python",
        "Progress" : "40%"
    },
        "Four" : {
        "name" : "PHP",
        "Progress" : "80%"
    }
}

print(f"{dictionary['One']['name']} progress is {dictionary['One']['Progress']}")
print(f"{dictionary['Two']['name']} progress is {dictionary['Two']['Progress']}")
print(f"{dictionary['Three']['name']} progress is {dictionary['Three']['Progress']}")
print(f"{dictionary['Four']['name']} progress is {dictionary['Four']['Progress']}")
