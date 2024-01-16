# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
#initializing function
  def __init__(self, title):
    self.title = title

# TODO: create instances of the class
book1 = Book("Harry Potter and Prisoner of Azkaban")
book2 = Book("History of Art for Dummies")

# TODO: print the class and property
print(book1)
print(book1.title)
