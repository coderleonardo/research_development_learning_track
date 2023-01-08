from operations.operations import Operations
from art import art

print(art)

opt = input("Choose one operation: +, -, * or /: ")
# isin_opt = opt in ["+", "-", "*", "/"]

while not (opt in ["+", "-", "*", "/"]):
    again = input("You type an invalid operation. To try again type 'T' or to finish type 'F': ")
    if again == "T":
        opt = input("Choose one operation: +, -, * or /: ")
        if opt in ["+", "-", "*", "/"]:
            break
    else: 
        break

print()
if opt in ["+", "-", "*", "/"]:
    if opt == "+":
        args = input("Type the arguments as '1, 2, 4': ")
        args = args.replace(" ", "").split(",")
        args_lst = [float(arg) for arg in args]

        result = Operations.sum(args_lst)
        print()
        print(f"The sum of the numbers {args_lst} is {result}")

    elif opt == "-":
        args = input("Type the arguments as 'number1, number2': ")
        args = args.replace(" ", "").split(",")
        num1, num2 = tuple(float(arg) for arg in args)

        result = Operations.subtract(num1, num2)
        print()
        print(f"The subtraction of the numbers {num1} and {num2} is {result}")

    elif opt == "*":
        args = input("Type the arguments as '1, 2, 4': ")
        args = args.replace(" ", "").split(",")
        args_lst = [float(arg) for arg in args]

        result = Operations.mult(args_lst)
        print()
        print(f"The multiplication of the numbers {args_lst} is {result}")

    elif opt == "/":
        args = input("Type the arguments as 'number1, number2': ")
        args = args.replace(" ", "").split(",")
        num1, num2 = tuple(float(arg) for arg in args)

        result = Operations.div(num1, num2)
        print()
        print(f"The division of the numbers {num1} and {num2} is {result}")
else:
    print()
    print("Finishing the process.")


    





