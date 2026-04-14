##################################
# INSERT INFROMATION TO THE TABLE2
##################################


import sqlite3

conn=sqlite3.connect("database1.db")
cur=conn.cursor()


cur.execute("DELETE FROM example")
employees=[
    (101, 'Ahmet', "Kandemir", 100, '2026-10-25', "05346246409"),
    (102, 'Ali', "Yılmaz", 120, '2026-11-01', "05340000000"),
    (103, 'Ayşe', "Demir", 110, '2026-12-01', "05341111111")
]

cur.executemany("INSERT INTO example (employee_id, first_name, surname, hourly_pay, hire_date, phoneNumber) VALUES (?,?,?,?,?,?)", employees)

conn.commit()

cur.execute("SELECT * FROM example")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()











