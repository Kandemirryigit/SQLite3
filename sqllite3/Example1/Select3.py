######################################
# SELECT SPECIFIC COLUMS FROM DATABASE
######################################


import sqlite3

conn=sqlite3.connect("school.db")
cur=conn.cursor()

cur.execute("SELECT name,gpa FROM students")
rows=cur.fetchall()

for row in rows:
    print(row)