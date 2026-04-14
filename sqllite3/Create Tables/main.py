######################
# JUST CREATED A TABLE
######################


import sqlite3

conn=sqlite3.connect("database1.db")
cur=conn.cursor()

cur.execute("""
CREATE TABLE example(
        employee_id INTEGER,
        First_name TEXT,
        last_name TEXT,
        hourly_pay REAL,
        hire_date  TEXT
)
""")


