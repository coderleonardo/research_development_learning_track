# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
    def __init__(self, title) -> None: # initializer
        self.title = title


# TODO: create instances of the class
b1 = Book("Brave new World")
b2 = Book("War and Peace")


# TODO: print the class and property
print(b1)
print(b1.title)
