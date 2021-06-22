# -------------------------------------------------------
# -- Database => SQLite => Retrieve data from database --
# -------------------------------------------------------
# - fetchone => Returns a single record or none if not more rows are available
# - fetchall => Returns all the rows of a query result. it returns all the rows
#               as a list of tuples. an empty list is returned if there is no record to fetch
# - fetchmany(size) =>
# --------------------------------------------------------------------------------------------

# Import SQLite module
import sqlite3

# Create database and connect
db = sqlite3.connect("app.db")

# Setting up the cursor
cr = db.cursor()

# Create the tables and fields
cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)")
cr.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")

# Inserting data
# cr.execute("INSERT INTO users(user_id, name) VALUES(1, 'Ahmed')")
# cr.execute("INSERT INTO users(user_id, name) VALUES(2, 'Hasan')")
# cr.execute("INSERT INTO users(user_id, name) VALUES(3, 'Osama')")

# Fetch data
cr.execute("SELECT * FROM users")

# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())  # Returns none => there's no more records

# print(cr.fetchall())

print(cr.fetchmany(2))  # Fitch two records only

# Save (commit) changes
db.commit()

# Closa database
db.close()
