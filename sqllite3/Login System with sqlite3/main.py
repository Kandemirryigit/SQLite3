import sqlite3

conn=sqlite3.connect("Login.db")
cur=conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
            )
""")

conn.commit()

def register():
    username=input("Enter a username: ")
    password=input("Enter a password: ")
    try:
        cur.execute("INSERT INTO users(username,password) VALUES (?,?)",(username,password))
        conn.commit()
        print(f"User '{username}' registered successfully!")
    except:
        print("Username already exists.Try a different one")

    
def login():
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    cur.execute("SELECT * FROM users WHERE username= ? AND password= ?",(username,password))
    user=cur.fetchone()
    if user:
        print(f"Welcome back, {username}")
    else:
        print("Invalid username or password")

def show():
    cur.execute("SELECT * FROM users")
    for row in cur.fetchall():
        print(row)


while True:
    print("\nMenu:")
    print("1. Register")
    print("2. Login")
    print("3. Show")
    print("4. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        register()
    elif choice == 2:
        login()
    elif choice==3:
        show()
    elif choice == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid option. Try again.")

conn.close()
