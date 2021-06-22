# ----------------------------------------------------
# -- Database => SQLite => Create skills app part 1 --
# ----------------------------------------------------

# Import SQLite module 
import sqlite3

# Create database and connect
db = sqlite3.connect("app.db")

# Setting up the cursor
cr = db.cursor()


def commit_and_close():
    """Commit changes and close connection to database"""
    db.commit()  # Commit (save) changes
    db.close()  # Close database
    print("Connection to database is closed.")

# My user ID
uid = 1

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

    cr.execute(f"SELECT * FROM skills WHERE user_id = '{uid}'")

    results = cr.fetchall()

    print(f"You have {len(results)} skills")

    if len(results) > 0:

        print("Showing skills with progress : ")

    for row in results:

        print(f"Skill => {row[0]},", end=" ")

        print(f"progress => {row[1]}%")

    commit_and_close()


def add_skill():

    sk = input("Write skill name : ").strip().capitalize()

    cr.execute(f"SELECT name FROM skills WHERE name = '{sk}' AND user_id = '{uid}'")

    results = cr.fetchone()

    if results == None: # There is no skill with this name in database

        prog = input("Write skill progress : ").strip()

        cr.execute(f"INSERT INTO skills(name, progress, user_id) VALUES('{sk}', '{prog}', '{uid}')")

    else: # There is a skill with this name in database

        def yes_or_no():

            print("This skill is already exists, want to update it ( yes, no) ?")

            status = input(">> ")

            if status[0] == "y":

                prog = input("Write the new skill progress : ").strip()

                cr.execute(f"UPDATE skills SET progress = '{prog}' WHERE name = '{sk}' AND user_id = '{uid}'")

            elif status[0] == "n":

                print("Skill not added")

            else:

                print("Please write yes or no")

                yes_or_no()

        yes_or_no()

    commit_and_close()


def delete_skill():

    sk = input("Write skill name : ").strip().capitalize()

    cr.execute(f"DELETE FROM skills WHERE name = '{sk}' and user_id = '{uid}'")

    commit_and_close()


def update_skill():

    sk = input("Write skill name : ").strip().capitalize()

    prog = input("Write the new skill progress : ").strip()

    cr.execute(f"UPDATE skills SET progress = '{prog}' WHERE name = '{sk}' AND user_id = '{uid}'")

    commit_and_close()


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

        commit_and_close()

else:

    print(f"Sorry this command \"{user_input}\" is not found")

