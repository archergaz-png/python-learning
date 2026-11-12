class book:
    def __init__(self, title, author, year):
        self._title = title
        self._author = author
        self._year = year
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def return_book (self):
        self.is_borrowed = False

    def __str__(self):
        return f"\"{self._title}\" - {self._author}, {self._year}. {'выдана' if self.is_borrowed else 'в библ'}"

book1 = book("мастер и марг", "мих булг", 1967)
book2 = book("мастер и мар 2 г", "мих 2 булг", 1966) 
print(book1)
print(book2)
book1.borrow ()
print(book1)
print(book2)
book1.return_book ()

