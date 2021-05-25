# create a calculator class
# add, subtract, multiply, divide, divisible
# extra Percentage, area of a triangle, inches to cm converter
# Divisible by the method that returns true or false depending on the outcome
# Work out and return the area of a triangle
# print(Nums())

class Calculator:  # define the class method

    def __init__(self):
        super().__init__()
        pass

    def add(Num1, Num2):  # addition function
        return Num1 + Num2

    def subtract(Num1, Num2):  # Subtraction function
        return Num1 - Num2

    def multiply(Num1, Num2):  # Multiply Function
        return Num1 * Num2

    def divide(Num1, Num2):  # Divide Function
        if Num2 == 0:  # error check to make sure the user doesnt enter 0 as you cannot divide by 0
            raise ZeroDivisionError  # this will raise an error in the programme that i will catch on the output of
            # the function
        else:  # if the numbers are valid it will return the answer for the division
            return Num1 / Num2

    def Nums():  # this function controls the users input making sure that the
        Num1 = input("Number 1 = ")  # these two lines control the users input for number 1 and 2
        Num2 = input("Number 2 = ")
        if Num1.isdigit() and Num2.isdigit():  # errors checks to make sure the user only can enter numbers
            Num1 = int(Num1)
            Num2 = int(Num2)
            return Num1, Num2
        else:  # if one or both is not a number it will run the following
            if not Num1.isdigit():  # this will  prints what ever the users entered and tell them it is not a valid
                # input
                print(f"{Num1} isn't a valid number")
            if not Num2.isdigit():  # checks for second number as well
                print(f"{Num2} isn't a valid number")
            print("Try again....\nEnter two valid Numbers")
            raise ValueError  # Raises a value error to be caught at the other end of the function

