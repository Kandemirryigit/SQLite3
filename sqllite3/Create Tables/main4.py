#################################
# INSERT INFORMATION TO THE TABLE
#################################

import sqlite3

conn=sqlite3.connect("database1.db")
cur=conn.cursor()

cur.execute("INSERT INTO example (employee_id,first_name,surname,hourly_pay,hire_date,phoneNumber) VALUES (?,?,?,?,?,?)",
            (101,'Yiğit',"Kandemir",100,'2026-10-25',"05346246409")
            )

conn.commit()
conn.close()