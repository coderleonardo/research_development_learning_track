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

    # TODO: create instance methods
    def getprice(self):
        return self.price


# TODO: create some book instances
b1 = Book("War and Peace", "Leo", 1225, 39)
b2 = Book("The Catcher in the Rye", "Joe", 234, 30)

# TODO: print the price of book1
print(b1.getprice())


# TODO: try setting the discount


# TODO: properties with double underscores are hidden by the interpreter
