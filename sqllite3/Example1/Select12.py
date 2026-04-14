#####################
# SELECT WITH DISTINCT
######################


import sqlite3

conn=sqlite3.connect("school.db")
cur=conn.cursor()

cur.execute("""
SELECT DISTINCT department FROM students
""")

rows = cur.fetchall()
for row in rows:
    print(row)