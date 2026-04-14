
import sqlite3

conn=sqlite3.connect("shop.db")
cur=conn.cursor()

cur.execute("""
SELECT customers.name,SUM(products.price * orders.quantity) AS totalSpend FROM orders
            JOIN customers ON orders.customer_id=customers.id
            JOIN products ON orders.product_id=products.id
            GROUP BY customers.id
""")

for row in cur.fetchall():
    print(row)



