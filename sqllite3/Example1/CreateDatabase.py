####################################
# CREATE AND INSERT DATA TO DATABASE
####################################


import sqlite3

 # If school.db not exists it creates
 # If exists connets to it
conn=sqlite3.connect("school.db") 


# Cursor lets you send SQL commands to the database
# conn = Database
# cur = the pen you use to write SQL commands
cur=conn.cursor()



# It creates a table called students with 5 colums
# Prımary key:
# Each row must have a uniqe id
# SQLite automaticly increments it(1,2,3,4)
cur.execute("""
CREATE TABLE students(
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            department TEXT,
            gpa REAL
            );
""")


students_data = [
    ("Ali", 20, "Computer Engineering", 3.2),
    ("Ayşe", 22, "Mathematics", 3.8),
    ("Mehmet", 19, "Computer Engineering", 2.9),
    ("Zeynep", 21, "Physics", 3.5)
]


# executemany()
# This runs the same SQL command for every tuple in students_data.
# Instead of writing 4 insert commands manually, it loops automatically.
cur.executemany(
    "INSERT INTO students(name,age,department,gpa) VALUES(?,?,?,?)",
    students_data
)

conn.commit()
