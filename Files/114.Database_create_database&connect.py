# -------------------------------------------------------
# -- Database => SQLite => create database and connect --
# -------------------------------------------------------
# - Connect 
# - Execute
# - Close
# -------------------------------------------------------

# Import SQLite module 
import sqlite3

# Create database and connect
db = sqlite3.connect("app.db")

# Create tables and fields
db.execute("CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER, user_id INTEGER)")

# Close database 
db.close()
