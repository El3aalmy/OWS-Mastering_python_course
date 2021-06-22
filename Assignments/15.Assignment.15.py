def remove_chars(text) :

    if text[0] == text[1] :

        return text[1:].replace(text[-1], "") 
    
    else :

        return text.replace(text[0], "").replace(text[-1], "")

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_list = map(remove_chars, friends_map)

for name in cleaned_list :

    print(name)

# ========================================

def get_names(text) :

    if text[-1] == "m" :

        return text 
        
friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

names = filter(get_names, friends_filter)

for name in names :

    print(name) 

# =========================================

from functools import reduce

def multiplication(num1, num2) :

    return num1 * num2

numbers = [1, 2, 3, 2]

nums = reduce(multiplication, numbers)

print(nums)

# ===========================================

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

my_skills = list(skills)

my_skills.pop(2)
my_skills.pop(4)
my_skills.reverse()

skills = tuple(my_skills)

new_tuple = enumerate(skills, 50)

for counter, skill in new_tuple :

    print(f"{counter} - {skill}")

# ============================================
