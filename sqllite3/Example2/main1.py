################################
# SELECT EVERYTHING FROM DATABASE
#################################

import sqlite3

conn=sqlite3.connect("shop.db")
cur=conn.cursor()

cur.execute("""
SELECT * FROM products
""")

for row in cur.fetchall():
    print(row)



