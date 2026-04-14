
import sqlite3

conn=sqlite3.connect("shop.db")
cur=conn.cursor()

cur.execute("""
SELECT customers.name,products.name,orders.quantity FROM orders
        JOIN customers ON orders.customer_id= customers.id
        JOIN products ON orders.product_id = products.id
""")

for row in cur.fetchall():
    print(row)



