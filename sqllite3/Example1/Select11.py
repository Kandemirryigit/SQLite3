##################
# SELECT WITH LIKE
##################


import sqlite3

conn=sqlite3.connect("school.db")
cur=conn.cursor()

cur.execute("""
SELECT * FROM students
            WHERE name LIKE "A%"
""")

rows = cur.fetchall()
for row in rows:
    print(row)