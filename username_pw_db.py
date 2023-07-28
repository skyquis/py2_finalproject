# This python file will be used to create the username and password database

# Imports
import sqlite3

# Creating / establishing connection to database
con = sqlite3.connect("username_pw.db")
cur = con.cursor()

# Creating or just adding data into logins table
try:
    cur.execute("CREATE TABLE logins(username, password)")
    print("logins table created in username_pw.db")
except:
    print("logins table already existed in in username_pw.db")
finally:
    cur.execute("""
        INSERT INTO logins VALUES
        ('smarquis', 'password1!')
        """)
    con.commit()

# Need to turn this into a function where username and password are input via Django app

# Make separate function to do input validation of appropriate username and password

# Also check and see if username already exists, if so output message to user
