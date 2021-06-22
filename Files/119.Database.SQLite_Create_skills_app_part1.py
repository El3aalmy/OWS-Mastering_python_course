# ----------------------------------------------------
# -- Database => SQLite => Create skills app part 1 --
# ----------------------------------------------------

# Input big message 
input_message = """
What do you want ? 
"s" => Show all skills
"a" => Add new skill
"d" => Delete a skill
"u" => Update a skill
"q" => Quit the app 
Choose option: 
"""

# Input option choose 
user_input = input(input_message).strip().lower()

# Commands list 
commands_list = ["s", "a", "d", "u", "q"]

# Define methods

def show_skill():

    print("Show skill")

def add_skill():

    print("Add skill")

def delete_skill():

    print("Delete skill")

def update_skill():

    print("Update skill progress")

# Check if command is exists 
if user_input in commands_list:

    # print(f"Command found {user_input}")

    if user_input == "s":

        show_skill()

    elif user_input == "a":

        add_skill()

    elif user_input == "d":

        delete_skill()

    elif user_input == "u":

        update_skill()

    else:

        print("App is closed.")

else:

    print(f"Sorry this command \"{user_input}\" is not found")
