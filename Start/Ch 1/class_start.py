# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    book_types = ('e-book', 'paperback','hardcover')
    # TODO: double-underscore properties are hidden from other classes
    __bookList = None
    # TODO: create a class method - class method gets whole class as parameter
    @classmethod
    def getBookTypes(cls):
        return cls.book_types

    # TODO: create a static method - to implement singleton design pattern
    @staticmethod
    def getBookList():
        if Book.__bookList == None:
            Book.__bookList = []
        return Book.__bookList

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.book_types):
            raise ValueError(f'{booktype} is not a valid booktype')
        else:
            self.booktype = booktype


# TODO: access the class attribute
print(f'Book types: {Book.getBookTypes()}')

# TODO: Create some book instances
b1 = Book('Strong winds', 'hardcover')
b2 = Book('Book of jokes', 'paperback')

# TODO: Use the static method to access a singleton object
theBooks = Book.getBookList()
theBooks.append(b1)
theBooks.append(b2)
print(theBooks)