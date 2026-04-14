import sqlite3

def show():
    for row in cur.fetchall():
        print(row)



conn = sqlite3.connect("Example8.db")
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
)
""")



cur.execute("""
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
            (10, 'Hakan',   'HR',          44000, 24, 'Istanbul')
""")




# cur.execute("""
#     SELECT name,department,salary FROM employees
#     WHERE department='Engineering' AND salary>80000
# """)
# show()



# cur.execute("""
#     SELECT name,city FROM employees
#     WHERE city='Istanbul' OR city='Izmir'
# """)
# show()



# cur.execute("""
#     SELECT name,department FROM employees
#     WHERE NOT department = 'HR'
# """)
# show()




# cur.execute("""
#     SELECT name,department,salary,city FROM employees
#     WHERE (department='Engineering' OR department='Marketing')
#     AND NOT city='Ankara'
#     AND salary>60000
# """)
# show()




# cur.execute("""
#     SELECT * FROM employees
#     WHERE department='HR' AND salary<50000
# """)
# show()




# cur.execute("""
#     SELECT * FROM employees 
#     WHERE city='Ankara' OR age>33
# """)
# show()




# cur.execute("""
#     SELECT * FROM employees
#     WHERE NOT city='Istanbul' AND salary>60000
# """)
# show()



