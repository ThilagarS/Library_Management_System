import mysql.connector as s

class Db:

    conn = 0
    cursor = 0

    def db_connect(self):
        self.conn = s.connect(
            host="localhost",
            user="root",
            password="Thila@123",
            database="library_db"
        )

        self.cursor = self.conn.cursor()

    def db_disconnect(self):
        self.conn.close()

class Book:

    db_op = 0

    def __init__(self,db):
        self.db_op = db

    def search_book(self,name):

        query = f"""select book_name,total_count from Books where book_name='{name}'"""
        self.db_op.cursor.execute(query)
        row = self.db_op.cursor.fetchone()

        if row is None:
            print("\nBook is Not Available in our Library")
            return False
        name = row[0]
        total = row[1]

        if(total > 0):
            print("\nBook is Available")
            return True
        else:
            print("\nThere is no Stock Available Now Visit Later")
            return False

    def issue_book(self,name):

        check = self.search_book(name)

        if(check):

            query = f"update Books set total_count = total_count-1 where book_name='{name}'"
            self.db_op.cursor.execute(query)
            self.db_op.conn.commit()
            print(f"\nGet the {name} Book")
            return True

        return False

    def return_book(self,name):

        query = f"update Books set total_count = total_count+1 where book_name = '{name}'"
        self.db_op.cursor.execute(query)
        self.db_op.conn.commit()
        print(f"\n{name} returned Successfully")

    def request(self,name):
        query = f"""insert into requested_books (name) values ('{name}')"""
        self.db_op.cursor.execute(query)
        self.db_op.conn.commit()
        print("\n Request Sent")

    def add_new_books(self,name):
        count = 10
        query = f"""INSERT INTO Books (book_name, total_count, available_count) VALUES('{name}',10,10)"""
        self.db_op.cursor.execute(query)
        self.db_op.conn.commit()
        print("Books Added Successfully")

class Credentials:

    db_op = 0
    current_name = 0
    current_reg_no = 0

    def __init__(self,db):
        self.db_op = db

    def log_in(self):

        name = input("\nEnter Your Name as per ID Card : ")
        reg_no = input("Enter the Register_Number : ")

        self.current_name = name
        self.current_reg_no = reg_no

        query = f"""select reg_no from Student where reg_no = '{reg_no}'"""
        self.db_op.cursor.execute(query)
        row = self.db_op.cursor.fetchone()

        if row is not None:
            print("\nVerified Successfully....")
            return True

        print("\nInvalid Register Number")
        print("\nIf -> Not Registered with Library Get Sign In")
        return False

    def sign_in(self):

        name = input("\nEnter name as id_Card : ")
        reg_no = input("Enter your College Register Number : ")
        email = input("Enter your email id : ")

        check = f"""select reg_no from Student where reg_no = '{reg_no}'"""
        self.db_op.cursor.execute(check)
        row = self.db_op.cursor.fetchone()

        if row is None:
            query = f"""insert into Student (name,reg_no,email) values('{name}','{reg_no}','{email}')"""
            self.db_op.cursor.execute(query)
            self.db_op.conn.commit()
            print("\nLogin to continue the process")
            self.log_in()
        else:
            print("\nThis reg_no is already registerd So just Log In")
            self.log_in()




    def current_name_fun(self):
        return self.current_name
    def current_reg_no_fun(self):
        return self.current_reg_no

class Library:

    db_op = 0
    cre = 0
    def __init__(self,db,credentials):
        self.db_op = db
        self.cre = credentials

    def menu(self):
        print("\n1.Book\n2.Digital Library\n3.Interview Preparation")
        option = int(input("\nEnter your option : "))
        book = Book(self.db_op)

        c = self.cre
        name = c.current_name_fun()
        reg = c.current_reg_no_fun()
        activity = "Restricted Access"
        book_name = 0

        if(option == 1):
            print("\n1.Search_book\n2.Issue_book\n3.Return_book\n4.Request_to_add\n5.Add_Books")
            option = int(input("\nEnter your option : "))
            book_name = input("\nEnter the Name of the book : ")
            if(option == 1):
                activity = "Search_book"
                book.search_book(book_name)
            elif(option == 2):
                val = book.issue_book(book_name)
                if(val):
                    activity = "Issue_book"
                else:
                    activity = "Book_not_available in library"

            elif(option == 3):
                activity = "Return_book"
                book.return_book(book_name)
            elif(option == 4):
                activity = "Request_to_add"
                book.request(book_name)
            elif(option == 5):

                if(c.current_name_fun() == 'Admin' or c.current_name_fun() == 'admin'):
                    activity = "Add_Books"
                    book.add_new_books(book_name)

                else:
                    print("Restricted Access")
            else:
                print("\nEnter Proper Value")


        elif(option == 2):
            activity = "Digital Library"
            print("\nDigital Library")
        elif(option == 3):
            activity = "Interview Prep"
            print("\nInterview Preparation")
        else:
            activity = "Genral Reasons"
            print("\nGenaral Reasons")

        query = f"""insert into Legture (name,reg_no,book_name,Activity,time)
                    values('{name}','{reg}','{book_name}','{activity}',CURRENT_TIMESTAMP)"""
        self.db_op.cursor.execute(query)
        self.db_op.conn.commit()



db = Db()
db.db_connect()
credentials = Credentials(db)
print("\n1.Already Registered with Library the Log In\n2.Didn't Registered Sign In")
option = int(input("\nEnter Your Option : "))

if(option == 1):
    credentials.log_in()
else:
    credentials.sign_in()

library = Library(db,credentials)
library.menu()

db.db_disconnect()

