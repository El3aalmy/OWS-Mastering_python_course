# -----------------------------------------------------------
# -- Database => SQLite => Update and delete from database --
# -----------------------------------------------------------

import sqlite3

# Connect to database 
db = sqlite3.connect("app.db")

# Setting up the cursor
cr = db.cursor()

# Update data
# cr.execute("UPDATE users SET name = 'Mahmoud' WHERE user_id = 1")
# cr.execute("UPDATE users SET name = 'Hasan' WHERE user_id = 2")
# cr.execute("UPDATE users SET name = 'Ammer' WHERE user_id = 3")

# Delete data
# cr.execute("DELETE FROM users") # Delete all records 
cr.execute("DELETE FROM users WHERE user_id = 4")

# Fetch data
cr.execute("SELECT * FROM users")  

print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())

# Save (commit) changes 
db.commit()

# Close database 
db.close()
