import sqlite3

def show():
    for row in cur.fetchall():
        print(row)

conn = sqlite3.connect("Example10.db")
cur = conn.cursor()

cur.execute("DROP TABLE employees")

cur.executescript("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL,
    age INTEGER,
    city TEXT
);

INSERT INTO employees VALUES
(1,  'Ali',     'Engineering', 85000, 28, 'Istanbul'),
(2,  'Ayse',    'Marketing',   62000, 35, 'Ankara'),
(3,  'Burak',   'Engineering', 91000, 32, 'Istanbul'),
(4,  'Zeynep',  'HR',          48000, 26, 'Izmir'),
(5,  'Can',     'Engineering', 78000, 30, 'Ankara'),
(6,  'Deniz',   'Marketing',   55000, 29, 'Istanbul'),
(7,  'Ece',     'HR',          51000, 33, 'Ankara'),
(8,  'Fatih',   'Engineering', 95000, 40, 'Istanbul'),
(9,  'Gul',     'Marketing',   67000, 27, 'Izmir'),
(10, 'Hakan',   'HR',          44000, 24, 'Istanbul');
""")



# cur.execute("""
#     SELECT name FROM employees
#     WHERE name LIKE 'A%'
# """)
# show()




# cur.execute("""
#     SELECT name FROM employees
#     WHERE name LIKE 'Ay%'
# """)
# show()




# cur.execute("""
#     SELECT name FROM employees
#     WHERE name LIKE 'B%'
# """)
# show()




# cur.execute("""
#     SELECT name FROM employees
#     WHERE name LIKE '%n'
# """)
# show()



# cur.execute("""
#     SELECT name FROM employees
#     WHERE name LIKE '%a%'
# """)
# show()




# cur.execute("""
#     SELECT name FROM employees
#     WHERE name LIKE '___'
# """)
# show()




# cur.execute("""
#     SELECT name,city FROM employees
#     WHERE city NOT LIKE 'Is%'
# """)
# show()



# cur.execute("""
#     SELECT name FROM employees
#     WHERE name LIKE '%an'
# """)
# show()




# cur.execute("""
#     SELECT name FROM employees
#     WHERE name LIKE '____'
# """)
# show()



# cur.execute("""
#     SELECT * FROM employees
#     WHERE department LIKE '%ing'
# """)
# show()



