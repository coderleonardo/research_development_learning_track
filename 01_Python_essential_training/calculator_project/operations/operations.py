class Operations:

    def sum(args):
        """This function take as argument a tuple of number and sum them all.

        Return the sum."""

        try:
            sum = 0
            for number in args:
                sum += number 

            return sum
        except:
            return "Something goes wrong"

    def subtract(num1, num2):
        """This function take as argument 2 numbers subtract them.

        Return the result of the subtraction."""
        try:
            return num1 - num2
        except:
            return "Something goes wrong"

    def mult(args):
        """This function take as argument a tuple and return the multiplication between all
        of it's elements."""

        try:
            mult_ = 1
            for number in args:
                mult_ *= number

            return mult_
        except:
            return "Something goes wrong"

    def div(number1, number2):
        """This function take as argument two numbers and divide one by another.
        
        Return the division."""
        
        try:
            return round(number1 / number2, 2)
        except:
            return "Something goes wrong"