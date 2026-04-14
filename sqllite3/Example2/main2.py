
import sqlite3

conn=sqlite3.connect("shop.db")
cur=conn.cursor()

cur.execute("""
SELECT name,age FROM customers WHERE age >25
""")

for row in cur.fetchall():
    print(row)



