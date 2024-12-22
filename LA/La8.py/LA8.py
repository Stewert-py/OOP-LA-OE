class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


book1 = book("book1", "stewert")
print(book1.title, book1.author)
del book1.author
book2 = book("book2", "yuri")
print(book1.title, book1.author)
print(book2.title, book2.author)
