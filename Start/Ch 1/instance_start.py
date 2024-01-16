# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secretDiscount = 0.5
    # TODO: create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, discountVal):
        self._discount = discountVal

# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 745, 44.50)
b2 = Book("The Catcher in the Rye", "JD Salinger", 260, 25.99)

# TODO: print the price of book1
print(f'Cena przed obniżką: {b1.getprice()}')

# TODO: try setting the discount (20%)
b1.setdiscount(0.2)
print(f'Cena po obniżce: {b1.getprice()}')

# TODO: properties with double underscores are hidden by the interpreter
#can't access secret discount
try:
    print(b1.__secretDiscount)
except:
#but ofc there's a trick to acces secretDiscount
    print(b1._Book__secretDiscount)