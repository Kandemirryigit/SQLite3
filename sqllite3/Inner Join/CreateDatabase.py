import sqlite3

conn=sqlite3.connect("school2.db")
cur=conn.cursor()


# Students table
cur.execute("""
CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
            )
""")


# Courses table
cur.execute("""
CREATE TABLE IF NOT EXISTS courses(
            id INTEGER PRIMARY KEY,
            name TEXT,
            teacher TEXT
            )
""")



# Enrollments table (which student is in which course)
cur.execute("""
CREATE TABLE IF NOT EXISTS enrollments(
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER
            )
""")



# Insert data
cur.execute("INSERT INTO students (name,age) VALUES ('Alice',20)")
cur.execute("INSERT INTO students (name,age) VALUES ('Bob',21)")
cur.execute("INSERT INTO students (name,age) VALUES ('Charlie',22)")

cur.execute("INSERT INTO courses (name,teacher) VALUES ('Math','Mr. Smith')")
cur.execute("INSERT INTO courses (name,teacher) VALUES ('Physics','Dr. Brown')")
cur.execute("INSERT INTO courses (name,teacher) VALUES ('Chemistry','Mrs. Green')")


cur.execute("INSERT INTO enrollments (student_id, course_id) VALUES (1,1)") # Alice -> Math
cur.execute("INSERT INTO enrollments (student_id, course_id) VALUES (1,2)") # Alice -> Physics
cur.execute("INSERT INTO enrollments (student_id, course_id) VALUES (2,2)") # Bob -> Physics
cur.execute("INSERT INTO enrollments (student_id, course_id) VALUES (3,3)") # Charlie -> Chemistry

conn.commit()