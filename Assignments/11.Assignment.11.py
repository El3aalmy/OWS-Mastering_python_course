Numbers = [15, 81, 5, 17, 20, 21, 13]

Numbers.sort(reverse= True)

for number in Numbers :

    print(f"{Numbers.index(number) + 1} => {number}")
        
else :

    print("Loop is done")

# ----------------------------------

Range = range(1, 21)

for num in Range :

    if num == 6 or num == 8 or num == 12 :

        continue
    
    print(str(num).zfill(2))      # Cannot add zfill to number => Solved , zfill() is a method for string not for int 

else :

    print("Loop is done")

# ---------------------------------

my_ranks = {
    "Math" : "rank1",       # => 100
    "Science" : "rank2",    # => 80 
    "Football" : "rank1",   # => 100
    "Sports" : "rank3"      # => 40
}

for item in my_ranks.items() :

    for item_value in item :

        if item_value is "rank1" :

            print(f"My rank in {my_ranks[item]} is {100}")

        elif item_value is "rank2" :

            print(f"My rank in {my_ranks[item]} is {80}")

        else :

            print(f"My rank in {my_ranks[item]} is {40}")

    # Cannot do it

# --------------------------------

students = {
  "Ahmed": {
    "Math": "1",
    "Science": "4",
    "Draw": "2",
    "Sports": "3",
    "Thinking": "1"
  },
  "Sayed": {
    "Math": "2",
    "Science": "2",
    "Draw": "2",
    "Sports": "4",
    "Thinking": "1"
  },
  "Mahmoud": {
    "Math": "4",
    "Science": "1",
    "Draw": "1",
    "Sports": "2",
    "Thinking": "2"
  }
}
        
for student, degrees in students.items() :

    print("-" * 20)

    print(f"Student name is => {student}")

    print("-" * 20)

    for subject, degree in degrees.items() :

        if degree is "1" :

            print(f"- {subject} => {100}")

        elif degree is "2" :

            print(f"- {subject} => {80}")

        elif degree is "3" :

            print(f"- {subject} => {60}")

        elif degree is "4" :

            print(f"- {subject} => {40}")

else : 

    print("Loop is done")




students = {
  "Ahmed": {
    "Math": "1",
    "Science": "4",
    "Draw": "2",
    "Sports": "3",
    "Thinking": "1"
  },
  "Sayed": {
    "Math": "2",
    "Science": "2",
    "Draw": "2",
    "Sports": "4",
    "Thinking": "1"
  },
  "Mahmoud": {
    "Math": "4",
    "Science": "1",
    "Draw": "1",
    "Sports": "2",
    "Thinking": "2"
  }
}
        
for student in students :

    print("-" * 20)

    print(f"Student name is => {student}")

    print("-" * 20)

    for subject in students[student] :


        if students[student][subject] == "1" :

            print(f"- {subject} => {100}")

        elif students[student][subject] == "2" :

            print(f"- {subject} => {80}")

        elif students[student][subject] == "3" :

            print(f"- {subject} => {60}")

        elif students[student][subject] == "4" :

            print(f"- {subject} => {40}")

else : 

    print("Loop is done")

