#################################
# SELECT EVERYTHING FROM DATABASE
#################################


import sqlite3

# We created a school.db so it connets to it
conn=sqlite3.connect("school.db")
cur=conn.cursor()

cur.execute("SELECT * FROM students")

# execute() runs the query BUT it does NOT automatically give you the data.
# You must fetch it.
rows=cur.fetchall()

for row in rows:
    print(row)