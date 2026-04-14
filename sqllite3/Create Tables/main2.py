#################################
# RENAME ONE OF THE COLUMN'S NAME
#################################


import sqlite3

conn=sqlite3.connect("database1.db")
cur=conn.cursor()

cur.execute("ALTER TABLE example RENAME COLUMN last_name TO surname")
conn.commit()
conn.close()