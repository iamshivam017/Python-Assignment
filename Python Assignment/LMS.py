import datetime

class Book:
    def __init__(self, BookId, title, author, quantity):
        self.BookId = BookId
        self.title = title
        self.author = author
        self.quantity = quantity

class User:
    def __init__(self, UserId, name):
        self.UserId = UserId
        self.name = name
        self.BooksCheckedout = []

class Library:
    def __init__(self):
        self.catalog = {}
        self.users = {}
        self.transactions = {}

    def AddBook(self, BookId, title, author, quantity):
        self.catalog[BookId] = Book(BookId, title, author, quantity)

    def RegisterUser(self, UserId, name):
        self.users[UserId] = User(UserId, name)

    def DisplayCatalog(self):
        print("Catalog:")
        for BookId, book in self.catalog.items():
            print(f"ID: {book.BookId}, Title: {book.title}, Author: {book.author}, Available: {book.quantity}")

    def CheckoutBook(self, UserId, BookId):
        if BookId not in self.catalog:
            print("Book is not found")
            return
        if len(self.users[UserId].BooksCheckedout) >= 3:
            print("User's checked out limit reached")
            return
        if self.catalog[BookId].quantity <= 0:
            print("Book not available")
            return

        self.catalog[BookId].quantity -= 1
        self.users[UserId].BooksCheckedout.append(BookId)
        self.transactions[(UserId, BookId)] = datetime.datetime.now()

    def ReturnBook(self, UserId, BookId):
    	if BookId not in self.catalog:
        	print("Book not found.")
        	return
    	if BookId not in self.users[UserId].BooksCheckedout:
        	print("Book not checked out by the user.")
        	return

    	self.catalog[BookId].quantity += 1
    	self.users[UserId].BooksCheckedout.remove(BookId)
    	checkout_date = self.transactions[(UserId, BookId)]
    	due_date = checkout_date + datetime.timedelta(days=14)
    	if datetime.datetime.now() > due_date:
        	days_overdue = (datetime.datetime.now() - due_date).days
        	fine = days_overdue
        	print(f"Fine for overdue: ${fine}")
    	print("Book returned successfully.")


library = Library()
library.AddBook('786', 'Book1', 'MyFutureGF', 5)
library.AddBook('132', 'Book2', 'MyFutureWife', 3)
library.AddBook('216', 'Book3', 'MyFutureSon', 2)

library.RegisterUser('786', 'Rohit')

library.DisplayCatalog()

library.CheckoutBook('786', '786')
library.ReturnBook('786', '786')
library.CheckoutBook('786', '786')
library.CheckoutBook('786', '132')
library.CheckoutBook('786', '216')