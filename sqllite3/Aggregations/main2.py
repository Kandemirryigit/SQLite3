import sqlite3

conn=sqlite3.connect("Example1.db")
cur=conn.cursor()

cur.execute("DROP TABLE products101")

cur.execute("""
CREATE TABLE products101(
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            price REAL,
            stock INTEGER
)
""")

cur.execute("INSERT INTO products101 VALUES(?,?,?,?,?)",(101,"Iphone 15","Electronics",999.99,50))
cur.execute("INSERT INTO products101 VALUES(?,?,?,?,?)",(102,"Samsung TV","Electronics",599.99,30))
cur.execute("INSERT INTO products101 VALUES(?,?,?,?,?)",(103,"Nike Shoes","Clothing",89.99,200))
cur.execute("INSERT INTO products101 VALUES(?,?,?,?,?)",(104,"Levi Jeans","Clothing",59.99,150))
cur.execute("INSERT INTO products101 VALUES(?,?,?,?,?)",(105,"Coffe Maker","Kitchen",49.99,75))
cur.execute("INSERT INTO products101 VALUES(?,?,?,?,?)",(106,"Blender","Kitchen",39.99,60))
cur.execute("INSERT INTO products101 VALUES(?,?,?,?,?)",(107,"Headphones","Electronics",199.99,100))
cur.execute("INSERT INTO products101 VALUES(?,?,?,?,?)",(108,"T-Shirt","Clothing",19.99,500))


# Total product count
cur.execute("SELECT COUNT(*) FROM products101")
print("Total products: ",cur.fetchone()[0])

# Total inventorty value
cur.execute("SELECT SUM(price*stock) FROM products101")
print("Total inventory value: $",cur.fetchone()[0])

# Average product price
cur.execute("SELECT ROUND(AVG(price),2) FROM products101")
print("Average product price: $",cur.fetchone()[0])

# Cheapest products name and price
cur.execute("""
    SELECT name,price FROM products101 WHERE price = (SELECT MIN(price) FROM products101)
""")
row=cur.fetchone()
print(f"Cheapest: {row[0]} at ${row[1]}")


cur.execute("""
    SELECT name,price FROM products101 WHERE price =(SELECT MAX(price) FROM products101)
""")
row=cur.fetchone()
print(f"Most expensive: {row[0]} at ${row[1]}")


# How many products in Electronics category
cur.execute("SELECT COUNT(*) FROM products101 WHERE category='Electronics'")
print("How many products are in Electronics category: ",cur.fetchone()[0])


# Total stock of clothing items
cur.execute("SELECT SUM(stock) FROM products101 WHERE category='Clothing'")
print("Total stock of clothing items: ",cur.fetchone()[0])


cur.execute("SELECT AVG(price) FROM products101 WHERE category='Kitchen'")
print("Average price of kitchen products: $",cur.fetchone()[0])





