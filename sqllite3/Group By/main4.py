import sqlite3

def show():
    for row in cur.fetchall():
        print(row)


conn = sqlite3.connect("Example13.db")
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


# cur.execute("""
#     SELECT
#         department,
#         COUNT(*)              AS     total_patients,
#         ROUND(AVG(bill),2)    AS     avg_bill,
#         SUM(days_stayed)      AS     total_days
#     FROM patients
#     GROUP BY department
#     ORDER BY avg_bill DESC
# """)
# show()



# cur.execute("SELECT department,SUM(bill) FROM patients GROUP BY department ORDER BY SUM(bill) DESC")
# show()



# Show the average days stayed per department, ordered from highest to lowest
# cur.execute("""
#     SELECT 
#         department,
#         ROUND(AVG(days_stayed),2)   AS   avg_days
#     FROM patients
#     GROUP BY department
#     ORDER BY avg_days DESC
# """)
# show()



# Show the oldest patient age per department
# cur.execute("""
#     SELECT 
#         department,
#         MAX(age)     AS   oldest
#     FROM patients
#     GROUP BY department
#     ORDER BY oldest DESC     
# """)
# show()








