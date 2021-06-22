# -----------------------------------------------
# -- Database => SQLite => Very important info -- 
# -----------------------------------------------

# Import SQLite module 
import sqlite3

# Create database and connect 
db = sqlite3.connect("app.db")

# Setting up the cursor 
cr = db.cursor()

my_tuple = ('Pascal', '65', 4)

# Inserting data 
# cr.execute("INSERT INTO skills VALUES(?, ?, ?)", my_tuple)

# Fetch data from database 
cr.execute("SELECT * FROM skills WHERE user_id NOT IN(1, 2, 3)")
# - ORDER BY
#   - ASC    => 1, 2, 3, ..
#   - DESC   => 3, 2, 1 
# - LIMIT 
#   - number of recored to fitch
# - OFFSET 
#   - number of record to ignore
# - WHERE 
#   - user_id > 1
#   - user_id NOT IN(1, 2, 3)   => fitch user_id 4 only    

# Assign data to variable 
results = cr.fetchall()

# Loop on results 
for row in results:

    print(f"Skill name => {row[0]},", end=" ")
    print(f"skill progress => {row[1]},", end=" ")
    print(f"User ID => {row[2]}")

# Save (commit) changes 
db.commit()

# Cloase connection 
db.close()
