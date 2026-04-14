import sqlite3


ADMIN_USERNAME="admin"
ADMIN_PASSWORD="admin"



conn=sqlite3.connect("bank.db")
cur=conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            balance REAL DEFAULT 0
)
""")

conn.commit()

def register():
    username=input("Enter a username: ")
    password=input("enter a password: ")
    try:
        cur.execute("INSERT INTO users(username,password) VALUES (?,?)",(username,password))
        conn.commit()
        print("Registration successful! Your balance is 0")
    except:
        print("Username already exists!")
    
def login():
    username=input("Username: ")
    password=input("Password: ")

    if username==ADMIN_USERNAME and password==ADMIN_PASSWORD:
        print("Welcome admin")
        admin_menu()
        return

    cur.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
    user=cur.fetchone()
    if user:
        print(f"Welcome {username}!")
        user_menu(user[0])
    else:
        print("Invalid credentials!")

    

def user_menu(user_id):
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Logout")
        choice = int(input("Choose an option: "))

        if choice==1:
            cur.execute("SELECT balance FROM users WHERE id=?",(user_id,))
            balance=cur.fetchone()[0]
            print(f"Your balance is: ${balance:.2f}")
        elif choice==2:
            amount=float(input("Enter deposit amount: "))
            cur.execute("UPDATE users SET balance = balance + ? WHERE id=?",(amount,user_id))
            conn.commit()
            print(f"${amount:.2f} deposited successfully!")
        elif choice==3:
            amount=float(input("Enter withdrawal amount: "))
            cur.execute("SELECT balance FROM users WHERE id=?",(user_id,))
            balance=cur.fetchone()[0]
            if amount>balance:
                print("Not enough balance'")
            else:
                cur.execute("UPDATE users SET balance =balance -? WHERE id=?",(amount,user_id))
                conn.commit()
                print(f"${amount:.2f} withdrawn successfully!")
        
        elif choice==4:
            recipient=input("Enter recipient username: ")
            amount=float(input("Enter transfer amount: "))
            cur.execute("SELECT balance FROM users WHERE id=?",(user_id,))
            balance=cur.fetchone()[0]
            if amount>balance:
                print("Not enough balance!")
            else:
                cur.execute("SELECT id FROM users WHERE username=?",(recipient,))
                rec=cur.fetchone()
                if rec:
                    rec_id=rec[0]
                    cur.execute("UPDATE users SET balance = balance - ? WHERE id=?",(amount,user_id))
                    cur.execute("UPDATE users SET balance = balance + ? WHERE id=? ",(amount,rec_id))
                    conn.commit()
                    print(f"${amount:.2f} transferred to {recipient} successfully!")
                else:
                    print("Recipient not found!")

        elif choice==5:
            print("Logged out!")
            break
        else:
            print("Invalid choice!")





def admin_menu():
    while True:
        print("\n--- ADMIN PANEL ---")
        print("1. View All Users")
        print("2. View Richest User")
        print("3. Delete User")
        print("4. Total Bank Money")
        print("5. Exit Admin Panel")

        choice = int(input("Choose an option: "))

        if choice==1:
            cur.execute("SELECT id,username,balance FROM users")
            users=cur.fetchall()
            print("\n---USERS---")
            for user in users:
                print(f"ID: {user[0]} | Username: {user[1]} | Balance: ${user[2]:.2f}")

        elif choice==2:
            cur.execute("SELECT username,balance FROM users ORDER BY balance DESC LIMIT 1")
            richest=cur.fetchone()
            if richest:
                print(f"Richest user: {richest[0]} with ${richest[1]:.2f}")
            else:
                print("No users found.")
        
        elif choice==3:
            username=input("Enter username to delete: ")
            cur.execute("DELETE FROM users WHERE username=?",(username,))
            conn.commit()
            print("User deleted (if existed)")
        
        elif choice==4:
            cur.execute("SELECT SUM(balance) FROM users")
            total=cur.fetchone()[0]
            total=total if total else 0
            print(f"Total money in bank: ${total:.2f}")
        
        elif choice == 5:
            print("Exiting admin panel.")
            break

        else:
            print("Invalid choice.")
            



                















while True:
    print("\n--- Mini Banking App ---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")


                    



