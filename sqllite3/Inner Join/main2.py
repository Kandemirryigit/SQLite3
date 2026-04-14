# Imagine two tables as two circles. INNER JOIN gives you only the overlapping part — rows that exist in both tables!

import sqlite3


def show():
    for row in cur.fetchall():
        print(row)


conn=sqlite3.connect("Example15.db")
cur=conn.cursor()

cur.execute("DROP TABLE departments")
cur.execute("DROP TABLE employees")

cur.execute("""
CREATE TABLE departments(
        id INTEGER PRIMARY KEY,
        name TEXT
)
""")


cur.execute("""
CREATE TABLE employees(
        id INTEGER PRIMARY KEY,
        name TEXT,
        department_id INTEGER,
        salary REAL
)
""")


cur.execute("""
INSERT INTO departments VALUES
            (1, 'Engineering'),
            (2, 'Marketing'),
            (3, 'HR'),
            (4, 'Finance')
""")


cur.execute("""
INSERT INTO employees VALUES
            (1, 'Ali',    1, 85000),
            (2, 'Ayse',   2, 62000),
            (3, 'Burak',  1, 91000),
            (4, 'Zeynep', 3, 48000),
            (5, 'Can',    1, 78000),
            (6, 'Deniz',  2, 55000),
            (7, 'Ece',    3, 51000),
            (8, 'Fatih',  1, 95000),
            (9, 'Gul',    NULL, 67000); 
""")






# cur.execute("""
#     SELECT
#         e.name     AS    employee,
#         d.name     AS    department,
#         e.salary
#     FROM employees e
#     INNER JOIN departments d ON e.department_id=d.id
#     ORDER BY d.name
# """)
# show()




cur.execute("""
    SELECT e.name,d.name   AS department
    FROM employees e
    INNER JOIN departments d ON e.department_id=d.id
""")
show()


