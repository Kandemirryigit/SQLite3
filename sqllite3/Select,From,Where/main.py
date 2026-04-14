import sqlite3

conn=sqlite3.connect("Example6.db")
cur=conn.cursor()

cur.execute("DROP TABLE employees")

cur.execute("""
CREATE TABLE employees(
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



# Select name and salary from table
# cur.execute("SELECT name,salary FROM employees")
# for row in cur.fetchall():
#     print(row)


# Selecty name and salary who works as an engineer
# cur.execute("""
#     SELECT name,salary FROM employees 
#     WHERE department='Engineering'
# """)
# for row in cur.fetchall():
#     print(row)



# Select name,department,salary where the salary is above than 80000
# cur.execute("""
#     SELECT name,department,salary FROM employees
#     WHERE salary >80000
# """)
# for row in cur.fetchall():
#     print(row)



# Select name and department who lives in istanbul
# cur.execute("""
#     SELECT name,department FROM employees
#     WHERE city='Istanbul'
# """)
# for row in cur.fetchall():
#     print(row)



# Select all employees younger than 30
# cur.execute("""
#     SELECT * FROM employees 
#     WHERE age<30
# """)
# for row in cur.fetchall():
#     print(row)



# Get only the name and department of employees in HR
# cur.execute("""
#     SELECT name,department FROM employees 
#     WHERE department='HR'
            
# """)
# for row in cur.fetchall():
#     print(row)



# Get all employees from Ankara
# cur.execute("SELECT * FROM employees WHERE city='Ankara'")
# for row in cur.fetchall():
#     print(row)



# Get employees who work in Marketing and live in Istanbul
# cur.execute("SELECT * FROM employees WHERE department='Marketing' and city='Istanbul'")
# for row in cur.fetchall():
#     print(row)



# Get the name, department, and salary of employees who work in Engineering or live in Izmir
# cur.execute("""
#     SELECT name,department,salary FROM employees
#     WHERE department='Engineering' or city='Izmir'
# """)
# for row in cur.fetchall():
#     print(row)










