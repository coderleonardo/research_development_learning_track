# one function inside another function: nested functions

def party():
    print("I'm out =[")

    def start_party():
        return "We are in! Uhullll!"

    def finish_party():
        return "Finish! =["

    print(start_party())
    print(finish_party())

party()