import sqlite3

conn=sqlite3.connect("school4.db")
cur=conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            department TEXT,
            gpa REAL
)
""")


cur.execute("INSERT INTO students (name,age,department,gpa) VALUES ('Alice',20,'CS',3.5)")
cur.execute("INSERT INTO students (name,age,department,gpa) VALUES ('Bob',21,'Math',3.0)")
cur.execute("INSERT INTO students (name,age,department,gpa) VALUES ('charlie',22,'Physics',2.8)")

cur.execute("""
DELETE FROM students WHERE name='Bob'
""")

conn.commit()


cur.execute("""
SELECT *  FROM students
""")
rows=cur.fetchall()
for row in rows:
    print(row)
