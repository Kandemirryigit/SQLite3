import sqlite3

conn=sqlite3.connect("school2.db")
cur=conn.cursor()

cur.execute("""
SELECT students.name,courses.name,courses.teacher FROM students
            INNER JOIN enrollments ON students.id=enrollments.student_id
            INNER JOIN courses ON enrollments.course_id=courses.id
""")

results=cur.fetchall()
for row in results:
    print(row)