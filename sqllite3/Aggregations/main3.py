import sqlite3

def show():
    for row in cur.fetchall():
        print(row)


conn = sqlite3.connect("Example12.db")
cur = conn.cursor()

cur.execute("DROP TABLE patients")

cur.executescript("""
CREATE TABLE patients (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    department TEXT,
    bill REAL,
    days_stayed INTEGER
);

INSERT INTO patients VALUES
(1,  'Ali',     45, 'Cardiology',  15000, 7),
(2,  'Ayse',    32, 'Neurology',   22000, 12),
(3,  'Burak',   58, 'Cardiology',  18000, 9),
(4,  'Zeynep',  27, 'Orthopedics', 9000,  4),
(5,  'Can',     61, 'Neurology',   31000, 15),
(6,  'Deniz',   39, 'Orthopedics', 7500,  3),
(7,  'Ece',     52, 'Cardiology',  21000, 11),
(8,  'Fatih',   44, 'Neurology',   28000, 13),
(9,  'Gul',     36, 'Orthopedics', 11000, 5),
(10, 'Hakan',   71, 'Cardiology',  25000, 14);
""")



# Find total patients
cur.execute("SELECT COUNT(*) FROM patients")
print("Total patiens: ",cur.fetchone()[0])


# Find sum of all bills
cur.execute("SELECT SUM(bill) FROM patients")
print("Total bills: $",cur.fetchone()[0])


# Find average age of patients
cur.execute("SELECT AVG(age) FROM patients")
print("Average age: ",cur.fetchone()[0])


# Find max and min days styaed at the hospital
cur.execute("SELECT MIN(days_stayed) , MAX(days_stayed) FROM patients")
row=cur.fetchone()
print("Shortest stay:",row[0],"days")
print("Longest stay:",row[1],"days")


# Find the total bills of only Cardiology patients
cur.execute("SELECT SUM(bill) FROM patients WHERE department='Cardiology'")
print("Total bills in cardiology:",cur.fetchone()[0])


# Find the average days stayed for patients older than 50
cur.execute("SELECT AVG(days_stayed) FROM patients WHERE age>50")
print("Average days stayed at the hospital older than 50:",cur.fetchone()[0])


# Find the highest bill among patients who stayed more than 10 days
cur.execute("SELECT MAX(bill) FROM patients WHERE days_stayed>10")
print("highest bill among patients who stayed more than 10 days:",cur.fetchone()[0])







