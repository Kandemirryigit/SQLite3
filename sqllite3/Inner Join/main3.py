import sqlite3

def show():
    for row in cur.fetchall():
        print(row)

conn = sqlite3.connect("Example16.db")
cur = conn.cursor()

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



cur.execute("""
    SELECT 
        students.name,
        classes.name,
        classes.teacher
    FROM students
    INNER JOIN classes ON students.class_id=classes.id
""")
show()