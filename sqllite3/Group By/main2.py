import sqlite3

conn=sqlite3.connect("Example3.db")
cur=conn.cursor()

cur.execute("""
CREATE TABLE players(
            id INTEGER PRIMARY KEY,
            name TEXT,
            team TEXT,
            points INTEGER,
            assists INTTEGER,
            rebounds INTEGER
)
""")

cur.execute("""
INSERT INTO players VALUES
            (1, 'LeBron',   'Lakers',   28, 8, 7),
            (2, 'AD',       'Lakers',   24, 3, 12),
            (3, 'Austin',   'Lakers',   14, 2, 3),
            (4, 'Curry',    'Warriors', 32, 6, 5),
            (5, 'Klay',     'Warriors', 22, 3, 4),
            (6, 'Green',    'Warriors', 8,  9, 10),
            (7, 'Luka',     'Mavs',     35, 10, 8),
            (8, 'Kyrie',    'Mavs',     28, 6, 4),
            (9, 'Gafford',  'Mavs',     12, 1, 9)
""")


cur.execute("""
    SELECT
            team,
            COUNT(*)              AS    num_players,
            SUM(points)           AS    total_points,
            ROUND(AVG(points))    AS    avg_points,
            MAX(points)           AS    best_scorer
    FROM players
    GROUP BY team
    ORDER BY total_points DESC
""")

print(f"{'Team':<12} {'Players':<10} {'Total Pts':<12} {'Avg Pts':<10} Best Scorer")
print("-" * 55)
for row in cur.fetchall():
    print(f"{row[0]:<12} {row[1]:<10} {row[2]:<12} {row[3]:<10} {row[4]}")
