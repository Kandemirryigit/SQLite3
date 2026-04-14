import sqlite3

def show():
    for row in cur.fetchall():
        print(row)

conn = sqlite3.connect("Example18.db")
cur = conn.cursor()

cur.execute("DROP TABLE students")

cur.executescript("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade INTEGER,
    class TEXT
);

INSERT INTO students VALUES
(1,  'Ali',    85, 'Math'),
(2,  'Ayse',   92, 'Science'),
(3,  'Burak',  78, 'Math'),
(4,  'Zeynep', 95, 'Science'),
(5,  'Can',    88, 'Math'),
(6,  'Deniz',  72, 'Science'),
(7,  'Ece',    91, 'Math'),
(8,  'Fatih',  65, 'Science'),
(9,  'Gul',    83, 'Math'),
(10, 'Hakan',  77, 'Science');
""")




# cur.execute("""
#     SELECT name,grade FROM students
#     WHERE grade > (SELECT AVG(grade) FROM students)
#     ORDER BY grade DESC
# """)
# show()




# Who has the highest grade?
# cur.execute("""
#     SELECT name,grade FROM students
#     WHERE grade=(SELECT MAX(grade) FROM students)
# """)
# show()




# Find students whose grade is below the average
# cur.execute("""
#     SELECT name,grade FROM students
#     WHERE grade < (SELECT AVG(grade) FROM students)
# """)
# show()




# Find the student with the lowest grade
# cur.execute("""
#     SELECT name,grade FROM students
#     WHERE grade=(SELECT MIN(grade) FROM students)
# """)
# show()




# Find students whose grade is above the average of Math class only
# cur.execute("""
#     SELECT name,grade FROM students
#     WHERE class='Math' AND grade>(SELECT AVG(grade) FROM students WHERE class='Math')
# """)
# show()





