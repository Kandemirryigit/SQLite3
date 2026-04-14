import sqlite3

def show():
    for row in cur.fetchall():
        print(row)


conn = sqlite3.connect("Example7.db")
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




# Select name and salary and order salary in decreasing format
# cur.execute("""
#     SELECT name,salary FROM employees
#     ORDER BY salary DESC
# """)
#show()




# Select name and salary and order salary in ascending format
# cur.execute("""
#     SELECT name,salary FROM employees
#     ORDER BY salary ASC
# """)
# show()





# Top 3 highest paid
# cur.execute("""
#     SELECT name,salary FROM employees
#     ORDER BY salary DESC
#     LIMIT 3
# """)
# show()





# Get all employees ordered by name A-Z
# cur.execute("""
#     SELECT name FROM employees
#     ORDER BY name DESC
# """)
# show()




# Get all employees ordered by name Z-A
# cur.execute("""
#     SELECT name FROM employees
#     ORDER BY name ASC
# """)
# show()




# Get the top 5 highest paid employees from Istanbul only
# cur.execute("""
#     SELECT name,salary,city FROM employees
#     WHERE city='Istanbul'
#     ORDER BY salary DESC
#     LIMIT 5
# """)
# show()











