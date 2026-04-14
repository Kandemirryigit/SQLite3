import sqlite3

conn=sqlite3.connect("school.db")
cur=conn.cursor()

cur.execute("""
SELECT name,gpa FROM students
            ORDER BY gpa DESC
            LIMIT 2
""")

rows=cur.fetchall()

for row in rows:
    print(row)