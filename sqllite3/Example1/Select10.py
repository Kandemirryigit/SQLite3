#####################
# SELECT WITH BETWEEN
#####################



import sqlite3

conn=sqlite3.connect("school.db")
cur=conn.cursor()

cur.execute(""" 
SELECT name,age FROM students
            WHERE age BETWEEN 20 AND 22
""")

rows=cur.fetchall()
for row in rows:
    print(row)