import sqlite3

def show():
    for row in cur.fetchall():
        print(row)



conn = sqlite3.connect("Example14.db")
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
#         COUNT(*)      AS    total_patients
#     FROM patients
#     GROUP BY department
#     HAVING COUNT(*) >3
# """)
# show()





# cur.execute("""
#     SELECT
#         department,
#         COUNT(*)               AS    total_patients,
#         ROUND(AVG(bill),0)     AS    avg_bill
#     FROM patients
#     WHERE age>35
#     GROUP BY department
#     HAVING avg_bill >15000
#     ORDER BY avg_bill DESC
# """)
# show()





# Show departments where the total bill is more than $50,000
# cur.execute("""
#     SELECT 
#         department,
#         SUM(bill)     AS    total_bill
#     FROM patients
#     GROUP BY department
#     HAVING total_bill>50000
# """)
# show()



# Show departments where the average days stayed is more than 7, but only consider patients younger than 60
# cur.execute("""
#     SELECT
#         department,
#         ROUND(AVG(days_stayed),2)    AS   avg_days
#     FROM patients
#     WHERE age<60
#     GROUP BY department
#     HAVING avg_days>7
# """)
# show()




# Show departments where the minimum bill is above $10,000
# cur.execute("""
#     SELECT
#         department,
#         MIN(bill)     AS    min_bill
#     FROM patients
#     GROUP BY department
#     HAVING min_bill >10000     
# """)
# show()



