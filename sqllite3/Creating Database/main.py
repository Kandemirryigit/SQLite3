##################
# CREATED DATABASE
##################


import sqlite3

conn=sqlite3.connect("myDatabase.db")
conn.commit()


# If a database named myDatabase not exists this code creates it
# If exists this code connects to it

