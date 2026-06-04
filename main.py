

class Db:

    def db_connect(self):
        pass
    def db_disconnect(self):
        pass
    def db_execute(self):
        pass

class Book:
    def search_book(self,name):
        pass
    def issue_book(self,name):
        pass
    def return_book(self,name):
        pass

class Members:

    def add_members(self,value):
        # add that member to the db
        pass
    def remove_members(self,reg_no):
        #remove that member from the db
        pass
    def view_members(self):
        pass

class Credentials:

    def log_in(self):
        name = input("Enter Your Name as per ID Card")
        reg_no = input("Enter the Register_Number")

        query = True
        if(query):
            print("Verified Successfully")
            return True
        print("\nInvalid Register_Number")
        return False
    def sign_in(self):
        name = input("Enter name as id_Card")
        reg_no = input("Enter your College Register Number")
        email = input("Enter your email id")

        self.log_in()

class Library:

    def menu(self):
        print("\n1.Book\n2.Digital Library\n3.Interview Preparation")
        option = int(input("\nEnter your option : "))
        book = Book()

        if(option == 1):
            print("\n1.Search_book\n2.Issue_book\n3.Return_book")
            option = int(input("\nEnter your option : "))
            name = input("\nEnter the Name of the book")
            if(option == 1):
                book.search_book(name)
            elif(option == 2):
                book.issue_book(name)
            elif(option == 3):
                book.return_book(name)
            else:
                print("\nEnter Proper Value")


        elif(option == 2):
            print("\nDigital Library")
        elif(option == 3):
            print("\nReturn Book")
        else:
            print("\nGenaral Reasons")


credentials = Credentials()
validity = credentials.log_in()
if(validity):
    library = Library()
    library.menu()

