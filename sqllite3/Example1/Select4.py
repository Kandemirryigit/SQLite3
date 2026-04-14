###################
# SELECT WITH WHERE
###################


import sqlite3

conn=sqlite3.connect("school.db")
cur=conn.cursor()

cur.execute("""
SELECT * FROM students
        WHERE department="Computer Engineering"
""")

rows=cur.fetchall()

for row in rows:
    print(row)