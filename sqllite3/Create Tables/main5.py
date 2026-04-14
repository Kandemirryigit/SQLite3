##################
# READ FROM TABLE
#################

import sqlite3

conn=sqlite3.connect("database1.db")
cur=conn.cursor()

cur.execute("SELECT * FROM example")

rows=cur.fetchall()
for row in rows:
    print(row)