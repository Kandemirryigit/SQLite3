import sqlite3

conn = sqlite3.connect("Example2.db")
cur = conn.cursor()

# cur.execute("DROP TABLE products")

cur.executescript("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL,
    stock INTEGER
);

INSERT INTO products VALUES
(1, 'iPhone 15',    'Electronics', 999.99, 50),
(2, 'Samsung TV',   'Electronics', 599.99, 30),
(3, 'Nike Shoes',   'Clothing',     89.99, 200),
(4, 'Levi Jeans',   'Clothing',     59.99, 150),
(5, 'Coffee Maker', 'Kitchen',      49.99, 75),
(6, 'Blender',      'Kitchen',      39.99, 60),
(7, 'Headphones',   'Electronics', 199.99, 100),
(8, 'T-Shirt',      'Clothing',     19.99, 500);
""")


cur.execute("""
    SELECT
            category,
            COUNT(*)               AS    num_products,
            ROUND(AVG(price),2)    AS    avg_price,
            SUM(stock)             AS    total_stock
    FROM products
    GROUP BY category  
""")



print(f"{'Category':<15} {'# Products':<12} {'Avg Price':<12} Total Stock")
print("-" * 50)
for row in cur.fetchall():
    print(f"{row[0]:<15} {row[1]:<12} ${row[2]:<11} {row[3]}")
    




