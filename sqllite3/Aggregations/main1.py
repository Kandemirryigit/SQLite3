import sqlite3

conn=sqlite3.connect(":memory:")
cur=conn.cursor()


# Simple employees table
cur.execute("""
CREATE TABLE employees10(
            id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            salary REAL
            )
""")


# Insert information to the table
cur.execute("INSERT INTO employees10 VALUES(?,?,?,?)",(101,"Yigit","Engineering",90000))
cur.execute("INSERT INTO employees10 VALUES(?,?,?,?)",(102,"Ahmet","Doctor",80000))
cur.execute("INSERT INTO employees10 VALUES(?,?,?,?)",(103,"Hüseyin","Nurse",70000))
cur.execute("INSERT INTO employees10 VALUES(?,?,?,?)",(104,"Barış","Nurse",70000))
cur.execute("INSERT INTO employees10 VALUES(?,?,?,?)",(105,"Türker","empty",150000))
cur.execute("INSERT INTO employees10 VALUES(?,?,?,?)",(106,"Efe","Engineering",90000))
cur.execute("INSERT INTO employees10 VALUES(?,?,?,?)",(107,"Ömer","Engineering",50000))


# COUNT - how many employees?
cur.execute("SELECT COUNT(*) FROM employees10")
print("Total employees:",cur.fetchone()[0])

# SUM - total salary budget
cur.execute("SELECT SUM(salary) FROM employees10")
print("Total salary budget: $",cur.fetchone()[0])

# AVG - average salary
cur.execute("SELECT AVG(salary) FROM employees10")
print("Average salary: $",round(cur.fetchone()[0],2))

# MIN / MAX
cur.execute("SELECT MIN(salary),MAX(salary) FROM employees10")
row=cur.fetchone()
print("Lowest salary: $",row[0])
print("Highest salary: $",row[1])

# Average salary of engineers
cur.execute("SELECT AVG(salary) FROM employees10 WHERE department='Engineering'")
print("Average salary of engineerse are: $",round(cur.fetchone()[0],2))

# How many person earns above than $60.000
cur.execute("SELECT COUNT(*) FROM employees10 WHERE salary>60000")
print("How many person earns above than $60.000: ",cur.fetchone()[0])












