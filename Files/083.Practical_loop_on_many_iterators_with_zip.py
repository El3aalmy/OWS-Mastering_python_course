# ----------------------------------------------------
# -- Practical => loop on many iterators with zip() --
# ----------------------------------------------------
# zip() return a zip object cantains all objects
# zip() length is the length of lowest object
# ----------------------------------------------------

list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d"]
tuple1 = ("Man", "Woman", "Girl", "Boy")
dict1 = {"Name" : "Hasan", "Age" : 16, "Country" : "Egypt", "Skill" : "Python"}

for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1) :

    print("List 1 item is => ", item1)
    print("List 2 item is => ", item2)
    print("Tuple 1 item is => ", item3)
    print("Dict 1 key is => ", item4, "value => ", dict1[item4])


zip_list = zip(list1, list2)

print(zip_list)

for item in zip_list :

    print(item)
