########################
# SELECT WITH CONDITIONS
########################


import sqlite3

conn=sqlite3.connect("school.db")
cur=conn.cursor()

cur.execute("""
SELECT name,gpa FROM students
            WHERE gpa>3
""")

rows=cur.fetchall()

for row in rows:
    print(row)