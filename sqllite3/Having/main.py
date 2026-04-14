import sqlite3

conn = sqlite3.connect("Example5.db")
cur = conn.cursor()


cur.execute("DROP TABLE orders")

cur.executescript("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer TEXT,
    drink TEXT,
    size TEXT,
    price REAL
);

INSERT INTO orders VALUES
(1,  'Ali',   'Latte',      'Small',  3.00),
(2,  'Ayse',  'Espresso',   'Small',  2.00),
(3,  'Ali',   'Cappuccino', 'Large',  5.00),
(4,  'Burak', 'Latte',      'Large',  5.00),
(5,  'Ayse',  'Latte',      'Medium', 4.00),
(6,  'Burak', 'Espresso',   'Small',  2.00),
(7,  'Ali',   'Espresso',   'Small',  2.00),
(8,  'Ayse',  'Cappuccino', 'Large',  5.00),
(9,  'Burak', 'Cappuccino', 'Medium', 4.00);
""")



cur.execute("""
    SELECT
            customer,
            SUM(price)   AS    total_spent
    FROM orders
    GROUP BY customer
    HAVING SUM(price) > 10
""")

print("💰 Big Spenders (over $10)")
print("-" * 30)
for row in cur.fetchall():
    print(f"  {row[0]}: ${row[1]:.2f}")
