#💡 LEFT JOIN gives you all rows from the left table, even if there is no match on the right table. No match = NULL on the right side!


import sqlite3

def show():
    for row in cur.fetchall():
        print(row)


conn = sqlite3.connect("Example17.db")
cur = conn.cursor()

cur.execute("DROP TABLE students")
cur.execute("DROP TABLE classes")

cur.executescript("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    class_id INTEGER
);

CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    name TEXT,
    teacher TEXT
);

INSERT INTO classes VALUES
(1, 'Math',    'Mr. Smith'),
(2, 'Science', 'Mrs. Jones'),
(3, 'History', 'Mr. Brown'),
(4, 'Art',     'Mrs. White');

INSERT INTO students VALUES
(1, 'Ali',    1),
(2, 'Ayse',   2),
(3, 'Burak',  1),
(4, 'Zeynep', 3),
(5, 'Can',    2),
(6, 'Deniz',  NULL);
""")






# cur.execute("""
#     SELECT
#         students.name,
#         classes.name,
#         classes.teacher
#     FROM students
#     LEFT JOIN classes ON students.class_id=classes.id
# """)
# show()





cur.execute("""
    SELECT
        students.name,
        COALESCE(classes.name,'Not assigned')    AS   class
    FROM students
    LEFT JOIN classes ON students.class_id=classes.id
""")
show()










