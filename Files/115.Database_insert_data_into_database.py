# -----------------------------------------------------
# -- Database => SQLite => Insert data into database -- 
# -----------------------------------------------------
# - Cursor => All operation in SQL done by cursor not the connection itself
# - Commit => Save all changes 
# --------------------------------------------------------------------------------------

# Import SQLite module 
import sqlite3

# Creata database and connect 
db = sqlite3.connect("app.db")

# Setting up the cursor 
cr = db.cursor()

# Create the tables and fields
cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)")
cr.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")

# Inserting data
# cr.execute("INSERT INTO users(user_id, name) VALUES(1, 'Ahmed')")
# cr.execute("INSERT INTO users(user_id, name) VALUES(2, 'Sayed')")
# cr.execute("INSERT INTO users(user_id, name) VALUES(3, 'Osama')")

my_list = ["Ahmed", "Sayed", "Mahmoud", "Ali", "Hasan", "Ibrahim", "Enas"]

for key, user in enumerate(my_list):

    cr.execute(f"INSERT INTO users(user_id, name) VALUES({key + 1}, '{user}')")    

# Save (commit) changes
db.commit()

# Closa database 
db.close()
