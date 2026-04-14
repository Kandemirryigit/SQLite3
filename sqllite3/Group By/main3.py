import sqlite3

conn=sqlite3.connect("Example4.db")
cur=conn.cursor()


cur.execute("DROP TABLE orders101")


cur.execute("""
CREATE TABLE orders101(
            id INTEGER PRIMARY KEY,
            customer TEXT,
            drink TEXT,
            size TEXT,
            price REAL
)
""")

cur.execute("""
INSERT INTO orders101 VALUES
            (1,  'Ali',   'Latte',      'Small',  3.00),
            (2,  'Ayse',  'Espresso',   'Small',  2.00),
            (3,  'Ali',   'Cappuccino', 'Large',  5.00),
            (4,  'Burak', 'Latte',      'Large',  5.00),
            (5,  'Ayse',  'Latte',      'Medium', 4.00),
            (6,  'Burak', 'Espresso',   'Small',  2.00),
            (7,  'Ali',   'Espresso',   'Small',  2.00),
            (8,  'Ayse',  'Cappuccino', 'Large',  5.00),
            (9,  'Burak', 'Cappuccino', 'Medium', 4.00)
""")


cur.execute("""
    SELECT
            customer,
            COUNT(*)      AS    num_orders101,
            SUM(price)    AS    total_spent
    FROM orders101
    GROUP BY customer
    ORDER BY total_spent ASC
""")


print("👤 Customer Spending")
print("-" * 35)
for row in cur.fetchall():
    print(f"  {row[0]:<8} {row[1]} orders → ${row[2]:.2f}")



