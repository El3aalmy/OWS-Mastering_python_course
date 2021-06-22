# --------------------------------------------------
# -- Database => SQLite => training on everything --
# --------------------------------------------------

import sqlite3

def get_all_data():

    try:

        # Connect to database
        db = sqlite3.connect("app.db")

        # Print success message
        print("Connected to database successfully")

        # Setting up the cursor
        cr = db.cursor()

        # Fetch data from database
        cr.execute("SELECT * FROM users")

        # Assign data to variable
        results = cr.fetchall()

        # Print number of rows
        print(f"Database has {len(results)} rows")

        # Print message
        print("Showing data ..")

        # Loop on data
        for row in results:

            print(f"User ID => {row[0]},", end=" ")

            print(f"Username => {row[1]}")

    except sqlite3.Error as er:

        print(f"Error reading data {er}")

    finally:

        if (db):

            # Close database
            db.close()

            print("Connection to database is closed")


get_all_data()
