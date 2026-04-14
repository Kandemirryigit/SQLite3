import sqlite3

conn=sqlite3.connect("shop.db")
cur=conn.cursor()


# Products table
cur.execute("""
CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL,
        category TEXT
)
""")


# Customers table
cur.execute("""
CREATE TABLE IF NOT EXISTS customers(
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
)
""")


# Orders table
cur.execute("""
CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        order_date TEXT,
        FOREIGN KEY(customer_id) REFERENCES customers(id)
        FOREIGN KEY(product_id) REFERENCES products(id)
)
""")


# Insert data to products
cur.executemany("INSERT INTO products(name,price,category) VALUES (?,?,?)",
            [
                ("Laptop",1000,"Electronics"),
                ("Mouse",25,"Electronics"),
                ("Keyboard",50,"Electronics"),
                ("Book",15,"Stationery"),
                ("Pen",2,"Stationery")
            ])



# Insert data to customers
cur.executemany("INSERT INTO customers(name,age) VALUES (?,?)",
                [
                    ("Ali",28),
                    ("Ayşe",22),
                    ("Mehmet",35),
                    ("Zeynep",30)
                ])



# Insert data to products
cur.executemany("INSERT INTO orders(customer_id,product_id,quantity,order_date) VALUES (?,?,?,?)",
                [
                    (1, 1, 1, "2026-03-01"),  # Ali bought 1 Laptop
                    (1, 2, 2, "2026-03-01"),  # Ali bought 2 Mice
                    (2, 4, 3, "2026-03-02"),  # Ayşe bought 3 Books
                    (3, 3, 1, "2026-03-03"),  # Mehmet bought 1 Keyboard
                    (3, 5, 10, "2026-03-03"), # Mehmet bought 10 Pens 
                ])



conn.commit()