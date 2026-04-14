import sqlite3

conn=sqlite3.connect("library.db")
cur=conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            year INTEGER
            )
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
            )
""")


cur.execute("""
CREATE TABLE IF NOT EXISTS borrows(
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            book_id INTEGER,
            borrow_date TEXT,
            return_date TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(book_id) REFERENCES books(id)
)
""")

conn.commit()


def add_book():
    title=input("Enter book title: ")
    author=input("Enter author: ")
    year=int(input("Enter publication year: "))
    cur.execute("INSERT INTO books(title,author,year) VALUES (?,?,?)",(title,author,year))
    conn.commit()
    print(f"Book '{title}' added!")


def add_user():
    name=input("Enter username: ")
    email=input("Enter user email: ")
    cur.execute("INSERT INTO users (name,email) VALUES (?,?)",(name,email))
    conn.commit()
    print(f"User '{name}' added!")

def borrow_book():
    user_id=int(input("Enter user ID: "))
    book_id=int(input("Enter book ID: "))
    borrow_date=input("Enter borrow date (YYYY-MM-DD): ")
    return_date=input("Enter return date (YYYY-MM-DD): ")
    cur.execute("INSERT INTO borrows (user_id,book_id,borrow_date,return_date) VALUES(?,?,?,?)",(user_id,book_id,borrow_date,return_date))
    conn.commit()
    print(f"Book ID {book_id} borrowed by usrr ID: {user_id}")



def show_borowed_books():
    cur.execute("SELECT * FROM borrows")
    for borrow in cur.fetchall():
        print(borrow)


def show_books():
    cur.execute("SELECT * FROM books")
    for book in cur.fetchall():
        print(book)

def show_users():
    cur.execute("SELECT * FROM users")
    for user in cur.fetchall():
        print(user)




while True:
    print("\nLibrary Menu:")
    print("1. Add Book")
    print("2. Add User")
    print("3. Borrow Book")
    print("4. Show Borrowed Books")
    print("5. Show Books")
    print("6. Show Users")
    print("7. Exit")

    choice=int(input("Choose an option: "))

    if choice==1:
        add_book()
    elif choice==2:
        add_user()
    elif choice==3:
        borrow_book()
    elif choice==4:
        show_borowed_books()
    elif choice==5:
        show_books()
    elif choice==6:
        show_users()
    elif choice==7:
        print("Exiting program...")
        break   
    else:
        print("Invalif option.Try again.")


conn.close()


