# DECORATOR provides a simple way to modify the behavior of a function without necessarily changing it
def decorator(func):
    def wrapper():
        print ("I am before the execution of the function passed as an argument")
        func()
        print ("I am after the execution of the function passed as an argument")

    return wrapper

def another_func():
    print (">>>>>>>>>>>>>>>>>>>>I'm a beautiful argument!<<<<<<<<<<<<<<<<<<<<<<<<<<<")

decorator_func = decorator(another_func)
decorator_func() # decorators returns a the wrapper function
