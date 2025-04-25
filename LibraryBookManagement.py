
class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author 
        self.available = True

    def land(self):
        self.available = False

    def return_book(self):
        self.available = True

    def __str__(self):
        return f"Tital: {self.title}, Author: {self.author}, Available: {self.available}"
    

class Library:
    def __init__(self):
        self.books = {}
        self.borrowers = {}

    def add_book(self, book):
        self.books[book.title] = book

    def land_book(self, book, borrower):
        if self.books[book.title].available:
            self.books[book.title].available = False
            self.borrowers[book.title] = borrower
            print(f"The book '{book.title}' has been lent to {borrower}.")
        else:
            print(f"The book '{book.title}' is currently not available.")
    
    def return_book(self, book):
        if book.title in self.books and not self.books[book.title].available:
            self.books[book.title].available = True
            self.borrowers.pop(book.title, None)
            print(f"The book '{book.title}' has been returned.")
        else:
            print(f"The book '{book.title}' was not borrowed or does not exist in the library.")


def main():
    book1 = book("aaa", "ppp")
    book2 = book("bbb", "qqq")
    book3 = book("ccc", "rrr")
    book4 = book("ddd", "sss")
    
    lib = Library()
    lib.add_book(book1)
    lib.add_book(book2)
    lib.add_book(book3)
    lib.add_book(book4)

    lib.land_book(book1,"xxx")
    lib.land_book(book2,"yyy")
    lib.land_book(book1,"zzz")

    lib.return_book(book1)
    lib.land_book(book1,"vvv")

main()






