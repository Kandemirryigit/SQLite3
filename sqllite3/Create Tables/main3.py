#########################
# ADD NEW COLUMN TO TABLE
#########################


import sqlite3

conn=sqlite3.connect("database1.db")
cur=conn.cursor()

cur.execute("ALTER TABLE example ADD COLUMN phoneNumber TEXT")

conn.commit()
conn.close()