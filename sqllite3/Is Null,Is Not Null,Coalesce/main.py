import sqlite3

def show():
    for row in cur.fetchall():
        print(row)

conn = sqlite3.connect("Example11.db")
cur = conn.cursor()

cur.execute("DROP TABLE employees")

cur.executescript("""
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL,
    phone TEXT,
    manager TEXT
);

INSERT INTO employees VALUES
        (1,  'Ali',    'Engineering', 85000, '+90 555 111', 'Fatih'),
        (2,  'Ayse',   'Marketing',   62000, NULL,          'Gul'),
        (3,  'Burak',  'Engineering', 91000, '+90 555 333', NULL),
        (4,  'Zeynep', 'HR',          NULL,  '+90 555 444', 'Ece'),
        (5,  'Can',    'Engineering', 78000, NULL,          'Fatih'),
        (6,  'Deniz',  'Marketing',   55000, '+90 555 666', NULL),
        (7,  'Ece',    'HR',          51000, '+90 555 777', NULL),
        (8,  'Fatih',  'Engineering', 95000, '+90 555 888', NULL),
        (9,  'Gul',    'Marketing',   67000, NULL,          'Ayse'),
        (10, 'Hakan',  'HR',          NULL,  '+90 555 000', 'Ece')
""")




# Employees with no phone number
# cur.execute("""
#     SELECT name,phone FROM employees
#     WHERE phone IS NULL
# """)
# show()



# Employees who has phone number
# cur.execute("""
#     SELECT name,phone FROM employees
#     WHERE phone IS NOT NULL
# """)
# show()



# Change the text 
# cur.execute("""
#     SELECT
#             name,
#             COALESCE(phone,'No phone registered')    AS  phone,
#             COALESCE(manager,'No manager')           AS  manager
#     FROM employees
# """)
# show()





# cur.execute("""
#     SELECT name FROM employees
#     WHERE salary IS NULL
# """)
# show()




# cur.execute("""
#     SELECT name FROM employees
#     WHERE manager IS NOT NULL
# """)
# show()




# cur.execute("""
#     SELECT name,COALESCE(salary,0) FROM employees
# """)
# show()



# cur.execute("""
#     SELECT name,COALESCE(phone,'No phone number') FROM employees
# """)
# show()



# cur.execute("""
#     SELECT name,COALESCE(manager,name) FROM employees
# """)
# show()





